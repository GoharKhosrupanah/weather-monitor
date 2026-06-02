import time
import os
from datetime import datetime
from sqlmodel import Session
from app.database import engine
from app.utils import fetch_weather, CITIES
from app.crud import create_reading, create_event, get_readings
from app.events import detect_notable_events


def poll_weather():
    """Poll weather for all cities and detect events"""
    print(f"🌤️ Polling weather at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    with Session(engine) as session:
        for city in CITIES.keys():
            try:
                reading_data = fetch_weather(city)
                if not reading_data:
                    continue

                # Store only if it's a new reading (deduplication)
                new_reading = create_reading(session, reading_data)
                
                if new_reading:
                    print(f"📊 New reading saved for {city}")
                    
                    # Get recent readings for context
                    recent_readings = get_readings(session, city=city, limit=10)
                    recent_dicts = [r.model_dump() for r in recent_readings[:-1]]  # exclude current
                    
                    # Detect events
                    events = detect_notable_events(reading_data, recent_dicts)
                    
                    for event in events:
                        create_event(session, event)
                        print(f"🚨 {event['severity'].upper()} EVENT in {city}: {event['reason']}")
                else:
                    pass  # duplicate reading, skip quietly
                    
            except Exception as e:
                print(f"❌ Error polling {city}: {e}")


if __name__ == "__main__":
    print("🚀 Weather Poller Started - Press Ctrl+C to stop")
    while True:
        poll_weather()
        interval = int(os.getenv("POLL_INTERVAL", 300))
        print(f"⏳ Sleeping for {interval} seconds...\n")
        time.sleep(interval)