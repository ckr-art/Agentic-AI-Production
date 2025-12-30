# app/main.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.llm import get_llm, generate_text_from_llm
from app.agent import Agent  # if you have Agent class, else we'll call LLM directly
from app.observability import logger

app = FastAPI(title="Agentic AI - Production Demo")

class PromptIn(BaseModel):
    prompt: str

# initialize llm and/or agent
_llm = get_llm()

# If you have Agent class that uses llm, keep and use it. Otherwise we call llm directly.
try:
    agent = Agent()
except Exception:
    agent = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
async def run(request: Request):
    """
    Accepts either:
      - JSON body: { "prompt": "..." }
      - or query param: /run?prompt=...
    Returns structured JSON and never throws an uncaught 500 (we catch errors).
    """
    try:
        # Try to read JSON body first
        try:
            payload = await request.json()
        except Exception:
            payload = {}

        prompt = None
        if isinstance(payload, dict) and "prompt" in payload:
            prompt = str(payload.get("prompt") or "")
        else:
            # fallback to query param
            prompt = request.query_params.get("prompt", "")

        if not prompt or len(prompt.strip()) < 1:
            raise HTTPException(status_code=400, detail="prompt is required")

        # If you have an Agent that expects to run using llm inside, prefer it
        if agent:
            try:
                result = agent.run(prompt)
                return {"response": result}
            except Exception as e:
                # if agent fails, fallback to direct llm call
                logger.exception("Agent.run failed, falling back to LLM: %s", e)

        # Direct LLM call (safe)
        text = generate_text_from_llm(_llm, prompt)
        return {"response": text}

    except HTTPException:
        # re-raise FastAPI validation HTTP errors
        raise
    except Exception as e:
        # catch-all: return 500 with a helpful message (no sensitive secrets)
        logger.exception("Unhandled error in /run: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error - check server logs")
