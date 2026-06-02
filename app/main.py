from fastapi import FastAPI, Depends, Query
from sqlmodel import Session
from app.database import create_db_and_tables, get_session
from app.crud import get_readings, get_events, get_stats
from app.schemas import ReadingsList, EventsList, HealthResponse
from typing import Optional

app = FastAPI(title="Weather Monitor")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health")
def health(session: Session = Depends(get_session)):
    readings_count, events_count = get_stats(session)
    return HealthResponse(
        status="ok",
        readings_stored=readings_count,
        events_stored=events_count
    )

@app.get("/readings", response_model=ReadingsList)
def readings(
    city: Optional[str] = None,
    limit: int = Query(50, gt=0, le=100),
    session: Session = Depends(get_session)
):
    readings_data = get_readings(session, city, limit)
    return {"readings": readings_data}

@app.get("/events", response_model=EventsList)
def events(
    city: Optional[str] = None,
    limit: int = Query(50, gt=0, le=100),
    session: Session = Depends(get_session)
):
    events_data = get_events(session, city, limit)
    return {"events": events_data}