# nutrition_analysis.py

def analyze_nutrition(data):
    """
    Takes a dictionary of nutrition values and returns health rating + label.
    Example input:
    {
        "Calories": 250,
        "Sugar": 18,
        "Protein": 5,
        "Fat": 10
    }
    """

    # Simple scoring system based on thresholds
    score = 0

    # Sugar (less is better)
    if data["Sugar"] <= 5:
        score += 2
    elif data["Sugar"] <= 10:
        score += 1
    elif data["Sugar"] <= 20:
        score += 0
    else:
        score -= 1

    # Calories (moderate is good)
    if data["Calories"] <= 150:
        score += 2
    elif data["Calories"] <= 250:
        score += 1
    elif data["Calories"] <= 350:
        score += 0
    else:
        score -= 1

    # Fat (less is better)
    if data["Fat"] <= 5:
        score += 2
    elif data["Fat"] <= 10:
        score += 1
    elif data["Fat"] <= 20:
        score += 0
    else:
        score -= 1

    # Protein (more is better)
    if data["Protein"] >= 15:
        score += 2
    elif data["Protein"] >= 10:
        score += 1
    elif data["Protein"] >= 5:
        score += 0
    else:
        score -= 1

    # Total score range: -4 to +8
    if score >= 6:
        rating = "A – Very Healthy ✅"
    elif score >= 3:
        rating = "B – Healthy 👍"
    elif score >= 0:
        rating = "C – Moderate ⚠️"
    else:
        rating = "D – Unhealthy ❌"

    return rating
