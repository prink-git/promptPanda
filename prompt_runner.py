import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


def run_prompt(prompt):

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data.get("response", "No response generated.")

    except:
        return "LLM execution failed."