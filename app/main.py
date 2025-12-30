from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .observability import logger, tracer
from .agent import run_agent
from .config import settings


app = FastAPI(title="Agentic AI - Production Demo")


class RunRequest(BaseModel):
query: str




@app.get("/health")
async def health():
return {"status": "ok", "service": "agentic", "port": settings.port}




@app.post("/run_agent")
async def run_agent_endpoint(req: RunRequest):
if not req.query or len(req.query.strip()) < 3:
raise HTTPException(status_code=400, detail="Query is too short")
with tracer.start_as_current_span("http_run_agent"):
logger.info("Received run_agent request", extra={"query": req.query})
result = run_agent(req.query)
return result
