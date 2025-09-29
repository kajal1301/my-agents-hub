from openai import OpenAI
import os

# Groq is OpenAI-compatible; just set base URL and use your GROQ_API_KEY.
# Docs: https://console.groq.com/docs/responses-api
def groq_client() -> OpenAI:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set. Put it in .env.")
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

MODEL_NAME = "openai/gpt-oss-120b"
