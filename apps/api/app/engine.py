from datetime import timedelta
from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from .models import Event, Incident, Investigation, AuditLog

def related_events(db: Session, incident: Incident):
    start = incident.started_at - timedelta(minutes=30)
    end = incident.started_at + timedelta(hours=2)
    return db.scalars(
        select(Event).where(
            and_(
                Event.service == incident.service,
                Event.environment == incident.environment,
                Event.timestamp >= start,
                Event.timestamp <= end,
            )
        ).order_by(Event.timestamp.asc())
    ).all()

def investigate(db: Session, incident: Incident):
    events = related_events(db, incident)
    errors = [e for e in events if e.severity.upper() in {"ERROR", "CRITICAL"}]
    deploys = [e for e in events if e.source.lower() in {"deployment", "deploy", "release"}]

    score = 0.25
    hypothesis = "Insufficient evidence to identify a dominant cause."
    recommendation = "Collect additional logs, metrics, deployment context, and dependency health signals."

    if errors:
        score += min(0.30, 0.05 * len(errors))
        hypothesis = f"{len(errors)} error-level signal(s) were observed for {incident.service} in the investigation window."
        recommendation = "Inspect the earliest correlated error and verify the health of the affected dependency."

    if deploys and errors:
        score += 0.25
        hypothesis = "A recent deployment is temporally correlated with error-level signals."
        recommendation = "Compare the deployment change set with the earliest error and consider a controlled rollback only after human review."

    score = min(round(score, 2), 0.95)
    summary = f"Investigation found {len(events)} related evidence item(s), including {len(errors)} error-level signal(s) and {len(deploys)} deployment signal(s)."

    existing = db.scalar(select(Investigation).where(Investigation.incident_id == incident.id))
    if existing:
        existing.summary = summary
        existing.confidence = score
        existing.evidence_count = len(events)
        existing.hypothesis = hypothesis
        existing.recommendation = recommendation
        investigation = existing
    else:
        investigation = Investigation(
            incident_id=incident.id,
            summary=summary,
            confidence=score,
            evidence_count=len(events),
            hypothesis=hypothesis,
            recommendation=recommendation,
        )
        db.add(investigation)

    db.add(AuditLog(
        incident_id=incident.id,
        action="INVESTIGATION_GENERATED",
        detail={"evidence_count": len(events), "confidence": score},
    ))
    db.commit()
    db.refresh(investigation)
    return investigation
