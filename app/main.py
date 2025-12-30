from fastapi import FastAPI
from app.agent import Agent

app = FastAPI(title="Production-Grade Agentic System")

agent = Agent()

@app.post("/run")
def run_agent(prompt: str):
    return {
        "response": agent.run(prompt)
    }
