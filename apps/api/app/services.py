from sqlalchemy.orm import Session
from .models import Event, Incident, AuditLog
from .schemas import EventCreate, IncidentCreate

def create_event(db: Session, payload: EventCreate):
    event = Event(
        source=payload.source,
        service=payload.service,
        environment=payload.environment,
        timestamp=payload.timestamp,
        severity=payload.severity,
        message=payload.message,
        metadata_json=payload.metadata,
    )
    db.add(event)
    db.add(AuditLog(action="EVENT_INGESTED", detail={"service": payload.service, "source": payload.source}))
    db.commit()
    db.refresh(event)
    return event

def create_incident(db: Session, payload: IncidentCreate):
    incident = Incident(**payload.model_dump())
    db.add(incident)
    db.flush()
    db.add(AuditLog(incident_id=incident.id, action="INCIDENT_CREATED", detail={"title": incident.title}))
    db.commit()
    db.refresh(incident)
    return incident
