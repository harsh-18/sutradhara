# Sūtradhāra
### Multi-Agent AI Productivity Assistant
#### Google GenAI APAC Academy Cohort 1

A Google-native multi-agent AI productivity assistant built using Google ADK, Gemini 2.5 Flash on Vertex AI, MCP Toolbox for Databases, BigQuery, and deployed on Cloud Run.

## Architecture
- **Root Agent**: productivity_coordinator (routes all requests)
- **Task Agent**: manages tasks via BigQuery
- **Schedule Agent**: manages calendar events via BigQuery  
- **Notes Agent**: searches and creates notes via BigQuery
- **Workflow Team**: SequentialAgent for daily briefing workflow

## Stack
- Google ADK
- Vertex AI (Gemini 2.5 Flash)
- MCP Toolbox for Databases v0.31.0
- BigQuery
- Cloud Run

## Live Demo
https://productivity-assistant-785984389524.asia-south1.run.app
