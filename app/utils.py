import httpx
from datetime import datetime
from typing import Dict, Optional

CITIES = {
    "Ottawa": {"lat": 45.42, "lon": -75.69},
    "Toronto": {"lat": 43.70, "lon": -79.42},
    "Vancouver": {"lat": 49.25, "lon": -123.12}
}

def fetch_weather(city: str) -> Optional[Dict]:
    """Fetch current weather from Open-Meteo API"""
    if city not in CITIES:
        return None
    
    coords = CITIES[city]
    
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={coords['lat']}&longitude={coords['lon']}"
        f"&current=temperature_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code"
        f"&wind_speed_unit=kmh&timezone=auto"
    )
    
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        
        current = data["current"]
        
        return {
            "city": city,
            "timestamp": datetime.fromisoformat(current["time"]),
            "temperature_2m": current["temperature_2m"],
            "apparent_temperature": current["apparent_temperature"],
            "precipitation": current["precipitation"],
            "wind_speed_10m": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
        }
    except Exception as e:
        print(f"❌ Failed to fetch weather for {city}: {e}")
        return None