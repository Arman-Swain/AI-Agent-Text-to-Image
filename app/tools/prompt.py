def agent_prompt(user_input):
    return f"""
You are an AI agent.

Your job is to decide what the user wants.

Rules:
- If the user wants an image, respond ONLY in valid JSON:
  {{
    "action": "image",
    "prompt": "<detailed image description>"
  }}

- If the user wants text, respond ONLY in valid JSON:
  {{
    "action": "text",
    "response": "<text answer>"
  }}

Do NOT explain anything.
Do NOT add extra text.

User input: "{user_input}"
"""

