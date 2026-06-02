import pytest
from sqlmodel import Session
from app.crud import create_reading
from app.database import engine

def test_deduplication():
    """Test that duplicate readings are not stored twice"""
    with Session(engine) as session:
        data = {
            "city": "Ottawa",
            "timestamp": "2026-06-02T12:00:00",
            "temperature_2m": 15.0,
            "apparent_temperature": 14.0,
            "precipitation": 0.0,
            "wind_speed_10m": 10.0,
            "weather_code": 0
        }
        
        result1 = create_reading(session, data)
        assert result1 is not None
        
        result2 = create_reading(session, data)
        assert result2 is None