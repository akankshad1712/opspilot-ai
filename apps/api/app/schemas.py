from datetime import datetime
from pydantic import BaseModel, Field

class EventCreate(BaseModel):
    source: str = Field(min_length=1, max_length=80)
    service: str = Field(min_length=1, max_length=120)
    environment: str = "production"
    timestamp: datetime
    severity: str = "INFO"
    message: str = Field(min_length=1)
    metadata: dict = Field(default_factory=dict)

class EventOut(BaseModel):
    id: int
    source: str
    service: str
    environment: str
    timestamp: datetime
    severity: str
    message: str
    metadata: dict = Field(validation_alias="metadata_json")

    class Config:
        from_attributes = True

class IncidentCreate(BaseModel):
    title: str
    service: str
    environment: str = "production"
    started_at: datetime

class IncidentOut(BaseModel):
    id: int
    title: str
    service: str
    environment: str
    started_at: datetime
    status: str

    class Config:
        from_attributes = True

class InvestigationOut(BaseModel):
    summary: str
    confidence: float
    evidence_count: int
    hypothesis: str
    recommendation: str

    class Config:
        from_attributes = True
