import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_structured_data(text):
    prompt = f"""
    You are an expert document extraction engine.

    Extract the following fields if present:

    - invoice_number
    - customer
    - date
    - total_amount
    - items

    Return ONLY valid JSON.

    Example:

    {{
    "invoice_number": "INV-1001",
    "customer": "ABC Corporation",
    "date": "2025-06-16",
    "total_amount": 1020,
    "items": [
        {{
        "name": "Laptop",
        "quantity": 2,
        "unit_price": 500
        }}
    ]
    }}

    Document:

    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)