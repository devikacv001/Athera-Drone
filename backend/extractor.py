import requests
import json

def extract_items(text):

    prompt = f"""
    Extract all shopping items, products, medicines and quantities from the text.

    Rules:
    1. Include every item mentioned.
    2. If quantity is not mentioned, assume 1.
    3. Preserve medicine names exactly.
    4. Return ONLY valid JSON.
    5. No explanation.
    6. No markdown.

    Text:
    {text}

    Example:

    Input:
    I need 2 paracetamol tablets, one Crocin strip and 3 packets of milk

    Output:
    {{
        "paracetamol tablets": 2,
        "crocin strip": 1,
        "milk": 3
    }}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except Exception:
        return {
            "error": "Invalid JSON returned by Llama3",
            "raw_response": result
        }