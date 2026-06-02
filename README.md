# Weather Monitor

**Intelligent Weather Monitoring & Notable Event Detection System**

A solution built for the infrastructure monitoring homework. It polls live weather for three Canadian cities, stores unique readings, detects notable events, and exposes everything through a clean HTTP API.

## Overview

This service monitors weather in:
- Ottawa
- Toronto  
- Vancouver

It uses the free **Open-Meteo API**, stores data in SQLite, and runs fully with Docker.

## Features

- Polls weather data every 5 minutes
- Automatic deduplication (only stores new readings by city + timestamp)
- Custom notable event detection logic
- Clean REST API with exact required endpoints
- Full Docker + docker-compose support
- Professional Cursor setup (rules, agent, skill)

## Quick Start

```bash
git clone https://github.com/GoharKhosrupanah/weather-monitor.git
cd weather-monitor
cp .env.example .env
docker compose up --build

API endpoints:
Endpoint,Description
GET /health,Service status + counts
GET /readings?city=Ottawa&limit=50,Latest weather readings
GET /events?city=Ottawa&limit=50,Notable weather events

Example 
Endpoint,Description
GET /health,Service status + counts
GET /readings?city=Ottawa&limit=50,Latest weather readings
GET /events?city=Ottawa&limit=50,Notable weather events

Event Detection Logic
My system defines a "notable event" when any of these conditions are met:

Temperature ≥ 20°C → Warm conditions
Wind speed ≥ 15 km/h → Windy conditions
Precipitation > 0.1 mm/h → Rain/Snow detected
Regular stable readings (for monitoring visibility)

Reasoning: The logic balances sensitivity and noise. It uses both absolute thresholds and basic context, making it more useful than simple fixed thresholds.
Cursor Setup

Rules (.cursor/rules/): General conventions and error handling rules
Agent (.cursor/agents/): Event Detector Expert
Skill (.cursor/skills/): analyze_weather.py — Database analysis tool

Tech Stack

FastAPI + Uvicorn
SQLModel + SQLite
Docker + docker-compose
httpx + APScheduler

Project Structure:
app/              # Main application code
.cursor/          # Cursor AI configuration
Dockerfile
docker-compose.yml
requirements.txt