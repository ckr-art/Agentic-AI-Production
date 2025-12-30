# Production-Grade Agentic AI System

This project demonstrates a **production-ready Agentic AI system** using
a modular agent architecture, tool usage, memory, and an LLM backend.

## Features
- Agent orchestration
- Tool calling
- Short-term memory
- FastAPI-based service
- Gemini 2.0 LLM integration (free tier)
- Docker-ready deployment

## Tech Stack
- Python
- FastAPI
- Gemini LLM
- Docker

## Setup

1. Clone the repository
2. Create a `.env` file using `.env.example`
3. Add your Gemini API key

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
