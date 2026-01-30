import json

def parse_llm_response(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "action": "text",
            "response": "Sorry, I could not understand the request."
        }
