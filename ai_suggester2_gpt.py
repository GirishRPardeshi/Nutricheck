# ai_suggester.py (GPT version)

import openai

def get_ai_suggestion(data):
    prompt = f"""
    Give a short 2-line health suggestion for a food product with the following nutrition:
    Calories: {data['Calories']} kcal,
    Sugar: {data['Sugar']}g,
    Protein: {data['Protein']}g,
    Fat: {data['Fat']}g.
    """

    openai.api_key = "your-api-key-here"  # Replace with env var ideally

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "Error fetching AI suggestion: " + str(e)
'''input:{ "Calories": 420, "Sugar": 26, "Protein": 3, "Fat": 18 }
'''
'''Sugar is quite high, consider low-sugar alternatives. Fat content is high, consider baked or grilled options. Very high calorie – avoid frequent consumption. Low protein – consider adding protein-rich foods.
'''