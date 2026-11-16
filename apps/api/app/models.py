from datetime import datetime, timezone
from sqlalchemy import String, Text, DateTime, Integer, JSON, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

def utcnow():
    return datetime.now(timezone.utc)

class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source: Mapped[str] = mapped_column(String(80))
    service: Mapped[str] = mapped_column(String(120))
    environment: Mapped[str] = mapped_column(String(40), default="production")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    severity: Mapped[str] = mapped_column(String(20), default="INFO")
    message: Mapped[str] = mapped_column(Text)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

class Incident(Base):
    __tablename__ = "incidents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(240))
    service: Mapped[str] = mapped_column(String(120))
    environment: Mapped[str] = mapped_column(String(40), default="production")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(String(30), default="OPEN")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    investigation = relationship("Investigation", back_populates="incident", uselist=False)

class Investigation(Base):
    __tablename__ = "investigations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    incident_id: Mapped[int] = mapped_column(ForeignKey("incidents.id"), unique=True)
    summary: Mapped[str] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float, default=0)
    evidence_count: Mapped[int] = mapped_column(Integer, default=0)
    hypothesis: Mapped[str] = mapped_column(Text)
    recommendation: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    incident = relationship("Incident", back_populates="investigation")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    incident_id: Mapped[int | None] = mapped_column(ForeignKey("incidents.id"), nullable=True)
    action: Mapped[str] = mapped_column(String(100))
    actor: Mapped[str] = mapped_column(String(100), default="system")
    detail: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
