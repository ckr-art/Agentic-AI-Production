from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import Agent

app = FastAPI()
agent = Agent()

class Prompt(BaseModel):
    prompt: str

@app.post("/run")
def run_agent(data: Prompt):
    response = agent.run(data.prompt)
    return {"response": response}
