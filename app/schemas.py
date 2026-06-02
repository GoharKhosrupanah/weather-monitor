from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ReadingResponse(BaseModel):
    id: int
    city: str
    timestamp: datetime
    temperature_2m: float
    apparent_temperature: float
    precipitation: float
    wind_speed_10m: float
    weather_code: int


class EventResponse(BaseModel):
    id: int
    city: str
    timestamp: datetime
    event_type: str
    value: float
    reason: str
    severity: str


class HealthResponse(BaseModel):
    status: str
    readings_stored: int
    events_stored: int


class ReadingsList(BaseModel):
    readings: List[ReadingResponse]


class EventsList(BaseModel):
    events: List[EventResponse]