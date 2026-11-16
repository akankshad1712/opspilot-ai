import time
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from apps.api.app.models import Incident
from apps.api.app.config import settings
from apps.api.app.engine import investigate

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

def run_once():
    with SessionLocal() as db:
        incidents = db.scalars(select(Incident).where(Incident.status == "OPEN").limit(10)).all()
        for incident in incidents:
            investigate(db, incident)

if __name__ == "__main__":
    interval = int(os.getenv("WORKER_INTERVAL", "30"))
    while True:
        run_once()
        time.sleep(interval)
