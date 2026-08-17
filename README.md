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

> ⚠️ Live demo currently unavailable: GCP credentials were overwritten, so the deployed app is down.
>
> For a proof-of-working recording, see this Loom video: https://www.loom.com/share/e45c505525304126a782ce730fa1380e

We are working to restore deployment credentials and bring the live demo back online.
