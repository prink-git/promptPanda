import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


def improve_prompt(prompt):

    system_prompt = f"""
You are a professional prompt engineer.

Rewrite the following prompt to make it clearer and more effective.

Requirements:
- specify the target audience
- specify output format
- add clear instructions
- keep it concise

Return ONLY the improved prompt in plain text.

Prompt: {prompt}
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": system_prompt,
                "stream": False
            }
        )

        data = response.json()

        text = data.get("response", "")

        text = text.replace("Prompt:", "")
        text = text.replace("Output Format:", "")
        text = text.replace("Instructions:", "")

        return text.strip()

    except:
        return "AI improvement unavailable."