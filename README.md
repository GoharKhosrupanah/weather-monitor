# Weather Monitor

**Intelligent weather monitoring system for Canadian cities**  
Polls live weather data, detects notable events, and exposes results via a clean HTTP API.

## Overview

This service monitors weather conditions in **Ottawa, Toronto, and Vancouver** using the Open-Meteo API. It stores readings, detects notable events based on intelligent logic, and provides a REST API for easy access.

## Features

- Real-time weather polling every 5 minutes
- Automatic deduplication of readings (by city + timestamp)
- Smart event detection logic (absolute thresholds + contextual changes)
- Persistent SQLite database
- Dockerized deployment
- Clean REST API

## Architecture
Poller → Weather API (Open-Meteo) → Database (SQLite)
↓
Event Detector
↓
FastAPI Endpoints
## Quick Start (Docker)

```bash
git clone <your-repo>
cd weather-monitor
cp .env.example .env
docker compose up --build
he API will be available at: http://localhost:8000
API Endpoints






Method,Endpoint,Description
GET,/health,Service status + counts
GET,/readings?city=Ottawa&limit=50,Latest weather readings
GET,/events?city=Ottawa&limit=50,Notable weather events
Example: 
curl http://localhost:8000/health
curl "http://localhost:8000/readings?city=Ottawa"
curl "http://localhost:8000/events"

Event Detection Logic
Notable events are triggered when:

Temperature ≥ 20°C (Warm conditions)
Wind speed ≥ 15 km/h (Windy)
Precipitation > 0.1 mm/h
Stable/normal conditions (for monitoring visibility)

Reasoning: The logic balances sensitivity and noise while being relevant to Canadian weather patterns. It considers both absolute values and trends.
Cursor Setup

Rules: Project conventions and error handling standards
Agent: Event Detector Expert
Skill: analyze_weather.py – Data analysis tool

Tech Stack

FastAPI – Modern Python web framework
SQLModel – ORM + Pydantic
SQLite – Simple persistent storage
Docker – Containerized deployment
Open-Meteo – Free weather API

Repo Structure
app/              # Main application code
.cursor/          # Cursor rules, agents, and skills
tests/            # Unit tests
Dockerfile
docker-compose.yml