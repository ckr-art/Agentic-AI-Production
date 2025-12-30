# Agentic AI — Production-Grade Agentic System


This project is a submission-ready scaffold for the Ready Tensor "Agentic AI In Production" module.


## Goals
- Demonstrate production-readiness for an agentic system
- Provide tests, monitoring, and deployment artifacts
- Be runnable locally with free/open-source tools


## Prerequisites
- Python 3.10+
- Git
- Docker (optional but recommended)
- Optional: OpenAI API key if you want to run with OpenAI models


## Quickstart (local, without Docker)
1. Clone the repo
2. Create virtual env: `python -m venv .venv && source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Copy env file: `cp .env.example .env` and set `OPENAI_API_KEY` if using OpenAI
5. Initialize vector DB (script included) — the app will auto-create collections on first run.
6. Run: `uvicorn app.main:app --reload --port 8080`


Endpoints:
- `GET /health` — basic health + metrics
- `POST /run_agent` — run the demo agent with a JSON payload `{ "query": "..." }`


## Testing
Run tests with:
