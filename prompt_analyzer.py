def analyze_prompt(prompt):

    issues = []
    score = 100

    words = prompt.split()

    if len(words) < 6:
        issues.append("Prompt is too short")
        score -= 20

    if "for" not in prompt.lower():
        issues.append("No audience specified")
        score -= 15

    if "bullet" not in prompt.lower() and "list" not in prompt.lower():
        issues.append("No output format specified")
        score -= 15

    if "example" not in prompt.lower():
        issues.append("No examples requested")
        score -= 10

    if "step" not in prompt.lower():
        issues.append("No step-by-step instruction")
        score -= 10

    if score < 0:
        score = 0

    return score, issues