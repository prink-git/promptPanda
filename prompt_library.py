import json

FILE = "prompts.json"


def load_prompts():

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_prompt(prompt):

    prompts = load_prompts()

    prompts.append(prompt)

    with open(FILE, "w") as f:
        json.dump(prompts, f, indent=2)