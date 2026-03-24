def score_label(score):

    if score >= 80:
        return "🟢 Excellent Prompt"

    if score >= 60:
        return "🟡 Good Prompt"

    if score >= 40:
        return "🟠 Weak Prompt"

    return "🔴 Poor Prompt"