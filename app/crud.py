from sqlmodel import Session, select, desc, func
from datetime import datetime
from app.models import Reading, Event
from typing import List, Optional


def create_reading(session: Session, reading_data: dict) -> Optional[Reading]:
    """Create reading only if timestamp is new for that city"""
    reading = Reading(**reading_data)
    
    try:
        session.add(reading)
        session.commit()
        session.refresh(reading)
        return reading
    except Exception:  # Unique constraint violation = duplicate
        session.rollback()
        return None


def get_readings(session: Session, city: Optional[str] = None, limit: int = 50) -> List[Reading]:
    statement = select(Reading).order_by(desc(Reading.timestamp))
    
    if city:
        statement = statement.where(Reading.city == city)
    
    statement = statement.limit(limit)
    return session.exec(statement).all()


def create_event(session: Session, event_data: dict) -> Event:
    event = Event(**event_data)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


def get_events(session: Session, city: Optional[str] = None, limit: int = 50) -> List[Event]:
    statement = select(Event).order_by(desc(Event.timestamp))
    
    if city:
        statement = statement.where(Event.city == city)
    
    statement = statement.limit(limit)
    return session.exec(statement).all()


def get_stats(session: Session):
    readings_count = session.exec(select(func.count(Reading.id))).one()
    events_count = session.exec(select(func.count(Event.id))).one()
    return readings_count, events_count