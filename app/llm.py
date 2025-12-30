import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # <-- THIS loads .env file

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model
