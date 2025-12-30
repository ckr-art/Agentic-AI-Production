# Production-Grade Agentic AI System

## Overview
This project demonstrates a **production-grade Agentic AI system** designed to run reliably in real-world environments.  
The system follows a modular agent architecture with clear separation of concerns, tool usage, memory handling, and LLM abstraction.

The agent is exposed via a FastAPI service and is fully containerized, making it suitable for deployment in production environments.

---

## Problem Statement
Most agentic AI demos focus only on prompting and lack production readiness.  
This project addresses that gap by implementing:
- Structured agent orchestration
- Tool execution logic
- Memory management
- Secure configuration handling
- Deployment-ready setup

---

## Solution Architecture
The system consists of:
- **Agent Core**: Controls reasoning flow and decision-making
- **LLM Layer**: Abstracted Gemini LLM integration
- **Tools Layer**: Deterministic function execution (calculator)
- **Memory Layer**: Short-term conversational memory
- **API Layer**: FastAPI-based service interface

---

## Key Features
- Modular and extensible agent design
- Tool calling capability
- Short-term memory for contextual reasoning
- Environment-based secret management
- Dockerized for production deployment
- Uses free-tier LLM for easy reproducibility

---

## Technologies Used
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **LLM**: Gemini 2.0 (Free Tier)
- **Containerization**: Docker
- **Testing**: Pytest

---

## LLM Choice
Gemini 2.0 free-tier API is used to ensure:
- No paid dependency
- Easy reproducibility for reviewers
- Secure API key management via environment variables

---

## How to Run

1. Clone the repository
2. Create a `.env` file using `.env.example`
3. Add your Gemini API key
4. Run locally or via Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
