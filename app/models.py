from datetime import datetime
from sqlmodel import SQLModel, Field, Index
from typing import Optional


class Reading(SQLModel, table=True):
    __tablename__ = "readings"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    city: str = Field(index=True)
    timestamp: datetime = Field(index=True)
    
    temperature_2m: float
    apparent_temperature: float
    precipitation: float
    wind_speed_10m: float
    weather_code: int
    
    # Unique constraint to prevent storing duplicate readings
    __table_args__ = (
        Index("ix_city_timestamp", "city", "timestamp", unique=True),
    )

    class Config:
        arbitrary_types_allowed = True


class Event(SQLModel, table=True):
    __tablename__ = "events"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    city: str = Field(index=True)
    timestamp: datetime = Field(index=True)
    
    event_type: str          # e.g. "extreme_heat", "rapid_temp_change"
    value: float             # The key value that triggered the event
    reason: str              # Human readable explanation
    severity: str = Field(default="medium")  # low, medium, high

    class Config:
        arbitrary_types_allowed = True