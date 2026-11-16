from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from .config import settings
from .database import Base, engine, get_db
from .models import Event, Incident, AuditLog
from .schemas import EventCreate, EventOut, IncidentCreate, IncidentOut, InvestigationOut
from .services import create_event, create_incident
from .engine import investigate, related_events

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OpsPilot AI",
    description="Evidence-first operations intelligence API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in settings.cors_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "opspilot-api"}

@app.post("/api/v1/events", response_model=EventOut)
def ingest_event(payload: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, payload)

@app.get("/api/v1/events", response_model=list[EventOut])
def list_events(limit: int = 100, db: Session = Depends(get_db)):
    return db.scalars(select(Event).order_by(Event.timestamp.desc()).limit(limit)).all()

@app.post("/api/v1/incidents", response_model=IncidentOut)
def create_incident_endpoint(payload: IncidentCreate, db: Session = Depends(get_db)):
    return create_incident(db, payload)

@app.get("/api/v1/incidents", response_model=list[IncidentOut])
def list_incidents(db: Session = Depends(get_db)):
    return db.scalars(select(Incident).order_by(Incident.created_at.desc())).all()

@app.get("/api/v1/incidents/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)
    if not incident:
        raise HTTPException(404, "Incident not found")
    events = related_events(db, incident)
    inv = incident.investigation
    return {
        "incident": IncidentOut.model_validate(incident).model_dump(),
        "evidence": [EventOut.model_validate(e).model_dump() for e in events],
        "investigation": InvestigationOut.model_validate(inv).model_dump() if inv else None,
    }

@app.post("/api/v1/incidents/{incident_id}/investigate", response_model=InvestigationOut)
def investigate_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)
    if not incident:
        raise HTTPException(404, "Incident not found")
    return investigate(db, incident)

@app.get("/api/v1/incidents/{incident_id}/audit")
def audit(incident_id: int, db: Session = Depends(get_db)):
    rows = db.scalars(
        select(AuditLog).where(AuditLog.incident_id == incident_id).order_by(AuditLog.created_at.desc())
    ).all()
    return [{"id": r.id, "action": r.action, "actor": r.actor, "detail": r.detail, "created_at": r.created_at} for r in rows]
