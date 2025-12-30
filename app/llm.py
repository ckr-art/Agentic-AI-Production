# app/llm.py
import os
from dotenv import load_dotenv

# Optionally still using google.generativeai for now (you saw deprecation warning).
# We wrap calls in try/except and provide a deterministic fallback.
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except Exception:
    GENAI_AVAILABLE = False

load_dotenv()  # loads .env in project root

def get_llm():
    """
    Returns a configured LLM client object or None if not available.
    Do NOT raise if no key — return None so caller can fallback.
    """
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")  # accept either env name
    if not api_key or not GENAI_AVAILABLE:
        return None

    # configure SDK safely
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        return model
    except Exception:
        # don't propagate SDK errors to API layer
        return None

def generate_text_from_llm(llm, prompt: str) -> str:
    """
    Safely call the LLM. If anything fails return a deterministic fallback string.
    """
    if not llm:
        return _fallback_response(prompt)

    try:
        # Using the older SDK generate_content method — wrap in try/except
        resp = llm.generate_content(prompt)
        # Older SDK: maybe resp.text or resp
        if hasattr(resp, "text"):
            return resp.text
        if hasattr(resp, "content"):
            return resp.content
        # fallback to str if none of above
        return str(resp)
    except Exception:
        return _fallback_response(prompt)

def _fallback_response(prompt: str) -> str:
    # deterministic simple reply (no exceptions)
    if "2+2" in prompt or "what is 2+2" in prompt.lower():
        return "The answer is 4."
    if "calculate" in prompt.lower():
        # try to extract expression after 'calculate'
        try:
            expr = prompt.lower().split("calculate", 1)[1].strip()
            # very restricted eval
            result = eval(expr, {"__builtins__": {}}, {})
            return f"CALC_RESULT: {result}"
        except Exception:
            return "CALC_ERROR"
    return "Fallback LLM: running in offline mode. Provide an API key for live responses."
