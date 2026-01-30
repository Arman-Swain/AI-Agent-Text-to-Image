import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def extract_json(text: str) -> dict:
    """
    Safely extract JSON object from LLM output.
    """
    try:
        # Try direct parse first
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to extract JSON using regex
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    # Final fallback
    return {
        "action": "text",
        "response": text.strip()
    }

def agent_decide(user_input: str) -> dict:
    prompt = f"""
You are an AI agent.

Respond ONLY with JSON.

If the user wants an image, respond:
{{
  "action": "image",
  "prompt": "<image description>"
}}

If the user wants text, respond:
{{
  "action": "text",
  "response": "<answer>"
}}

User input: "{user_input}"
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    raw_output = response.json().get("response", "").strip()

    # DEBUG (very useful)
    print("\n🧠 Raw LLM output:\n", raw_output, "\n")

    return extract_json(raw_output)
