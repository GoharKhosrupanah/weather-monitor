from app.events import detect_notable_events

def test_event_detection():
    """Test that event detection function works"""
    current = {
        "city": "Ottawa",
        "timestamp": "2026-06-02T12:00:00",
        "temperature_2m": 33.0,
        "wind_speed_10m": 65.0,
        "precipitation": 6.0
    }
    
    events = detect_notable_events(current, [])
    assert len(events) > 0