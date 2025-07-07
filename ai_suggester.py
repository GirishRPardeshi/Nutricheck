# ai_suggester.py

def get_ai_suggestion(data):
    """
    Returns basic AI-style suggestion based on nutrition values.
    """
    suggestions = []

    if data["Sugar"] > 20:
        suggestions.append("Sugar is quite high, consider low-sugar alternatives.")
    elif data["Sugar"] > 10:
        suggestions.append("Try to reduce sugar intake to avoid energy crashes.")

    if data["Fat"] > 15:
        suggestions.append("Fat content is high, consider baked or grilled options.")

    if data["Calories"] > 350:
        suggestions.append("Very high calorie – avoid frequent consumption.")

    if data["Protein"] < 5:
        suggestions.append("Low protein – consider adding protein-rich foods.")

    if not suggestions:
        return "Looks good! This product seems balanced and healthy."

    return " ".join(suggestions)
