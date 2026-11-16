
from datetime import datetime, timezone, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from apps.api.app.main import app
from apps.api.app.database import Base, get_db


@pytest.fixture
def client():
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)
    test_engine.dispose()


def event_payload(service="payments-api", environment="test",
                  source="application-log", severity="ERROR",
                  timestamp=None):
    return {
        "source": source,
        "service": service,
        "environment": environment,
        "timestamp": (timestamp or datetime.now(timezone.utc)).isoformat(),
        "severity": severity,
        "message": "Test event message",
        "metadata": {"request_id": "test-123"},
    }


def incident_payload(service="payments-api", environment="test",
                     started_at=None):
    return {
        "title": "Test incident",
        "service": service,
        "environment": environment,
        "started_at": (started_at or datetime.now(timezone.utc)).isoformat(),
    }


def create_incident(client, payload=None):
    response = client.post(
        "/api/v1/incidents",
        json=payload or incident_payload(),
    )
    assert response.status_code == 200
    return response.json()["id"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ingest_event(client):
    response = client.post(
        "/api/v1/events",
        json=event_payload(),
    )
    assert response.status_code == 200
    assert response.json()["service"] == "payments-api"


def test_list_events(client):
    client.post("/api/v1/events", json=event_payload())
    response = client.get("/api/v1/events")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_and_list_incidents(client):
    create_incident(client)
    response = client.get("/api/v1/incidents")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_incident_without_investigation(client):
    incident_id = create_incident(client)
    response = client.get(f"/api/v1/incidents/{incident_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["incident"]["id"] == incident_id
    assert body["evidence"] == []
    assert body["investigation"] is None


def test_get_missing_incident(client):
    response = client.get("/api/v1/incidents/9999")
    assert response.status_code == 404


def test_investigate_without_evidence(client):
    incident_id = create_incident(client)

    response = client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )

    assert response.status_code == 200
    assert response.json()["evidence_count"] == 0
    assert response.json()["confidence"] == 0.25


def test_investigate_error_without_deployment(client):
    now = datetime.now(timezone.utc)
    client.post(
        "/api/v1/events",
        json=event_payload(timestamp=now, severity="ERROR"),
    )
    incident_id = create_incident(
        client,
        incident_payload(started_at=now),
    )

    response = client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )

    assert response.status_code == 200
    assert response.json()["evidence_count"] == 1
    assert response.json()["confidence"] == 0.30


def test_deployment_correlated_with_error(client):
    now = datetime.now(timezone.utc)

    client.post(
        "/api/v1/events",
        json=event_payload(
            source="deployment",
            severity="INFO",
            timestamp=now,
        ),
    )
    client.post(
        "/api/v1/events",
        json=event_payload(
            source="application-log",
            severity="ERROR",
            timestamp=now + timedelta(minutes=1),
        ),
    )

    incident_id = create_incident(
        client,
        incident_payload(started_at=now),
    )

    response = client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )

    assert response.status_code == 200
    result = response.json()
    assert result["evidence_count"] == 2
    assert result["confidence"] == 0.55
    assert "deployment" in result["hypothesis"].lower()


def test_repeated_investigation_updates_existing_record(client):
    now = datetime.now(timezone.utc)
    incident_id = create_incident(
        client,
        incident_payload(started_at=now),
    )

    first = client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )
    second = client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["confidence"] == second.json()["confidence"]
    assert first.json()["evidence_count"] == second.json()["evidence_count"]

    audit = client.get(
        f"/api/v1/incidents/{incident_id}/audit"
    )
    actions = [row["action"] for row in audit.json()]
    assert actions.count("INVESTIGATION_GENERATED") == 2


def test_investigate_missing_incident(client):
    response = client.post("/api/v1/incidents/9999/investigate")
    assert response.status_code == 404


def test_incident_audit_history(client):
    incident_id = create_incident(client)

    client.post(
        f"/api/v1/incidents/{incident_id}/investigate"
    )

    response = client.get(
        f"/api/v1/incidents/{incident_id}/audit"
    )

    assert response.status_code == 200
    actions = [row["action"] for row in response.json()]
    assert "INVESTIGATION_GENERATED" in actions


def test_empty_audit_history(client):
    incident_id = create_incident(client)

    response = client.get(
        f"/api/v1/incidents/{incident_id}/audit"
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["action"] == "INCIDENT_CREATED"


def test_related_events_filter_by_service_and_environment(client):
    now = datetime.now(timezone.utc)

    client.post(
        "/api/v1/events",
        json=event_payload(timestamp=now),
    )
    client.post(
        "/api/v1/events",
        json=event_payload(
            service="different-service",
            timestamp=now,
        ),
    )
    client.post(
        "/api/v1/events",
        json=event_payload(
            environment="staging",
            timestamp=now,
        ),
    )

    incident_id = create_incident(
        client,
        incident_payload(started_at=now),
    )

    response = client.get(
        f"/api/v1/incidents/{incident_id}"
    )

    assert response.status_code == 200
    assert len(response.json()["evidence"]) == 1
def test_get_db_closes_session(monkeypatch):
    from apps.api.app import database

    class FakeSession:
        closed = False

        def close(self):
            self.closed = True

    fake_session = FakeSession()

    monkeypatch.setattr(
        database,
        "SessionLocal",
        lambda: fake_session,
    )

    db_generator = database.get_db()

    assert next(db_generator) is fake_session

    with pytest.raises(StopIteration):
        next(db_generator)

    assert fake_session.closed is True
