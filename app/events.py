from datetime import datetime, timedelta
from typing import List, Dict
from app.models import Event


def detect_notable_events(current: Dict, recent_readings: List[Dict]) -> List[Dict]:
    """Detect notable weather events"""
    events = []
    city = current["city"]
    temp = current["temperature_2m"]
    wind = current["wind_speed_10m"]
    precip = current["precipitation"]

    # 1. Extreme Temperature
    if temp >= 32:
        events.append({
            "city": city,
            "timestamp": current["timestamp"],
            "event_type": "extreme_heat",
            "value": temp,
            "reason": f"Extreme heat: {temp}°C",
            "severity": "high"
        })
    elif temp <= -20:
        events.append({
            "city": city,
            "timestamp": current["timestamp"],
            "event_type": "extreme_cold",
            "value": temp,
            "reason": f"Extreme cold: {temp}°C",
            "severity": "high"
        })

    # 2. Strong Wind
    if wind >= 60:
        events.append({
            "city": city,
            "timestamp": current["timestamp"],
            "event_type": "strong_wind",
            "value": wind,
            "reason": f"Strong winds: {wind} km/h",
            "severity": "medium"
        })

    # 3. Heavy Precipitation
    if precip >= 5:
        events.append({
            "city": city,
            "timestamp": current["timestamp"],
            "event_type": "heavy_precipitation",
            "value": precip,
            "reason": f"Heavy rain/snow: {precip} mm/h",
            "severity": "high"
        })

    # 4. Rapid Temperature Change (if we have history)
    if len(recent_readings) >= 3:
        recent_temps = [r["temperature_2m"] for r in recent_readings[-6:]]
        avg_temp = sum(recent_temps) / len(recent_temps)
        change = abs(temp - avg_temp)
        
        if change >= 8:
            events.append({
                "city": city,
                "timestamp": current["timestamp"],
                "event_type": "rapid_temp_change",
                "value": change,
                "reason": f"Rapid temperature change of {change:.1f}°C",
                "severity": "medium"
            })

    return events