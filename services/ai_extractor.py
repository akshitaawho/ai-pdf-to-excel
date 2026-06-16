import os
import json

from groq import Groq
from dotenv import load_dotenv

# get api key for groq in this case
load_dotenv()

# this opens the connection to groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_structured_data(text):
    prompt = f"""
    You are an expert document analyst.

    Your task is to convert ANY document into structured spreadsheet data.

    The document may be:
    - Invoice
    - Loan application
    - Technical report
    - Research paper
    - Financial statement
    - Medical report
    - Legal agreement
    - Procurement report
    - Resume
    - Survey results
    - Inspection report
    - Any other business or technical document

    Instructions:

    1. Analyze the document structure.
    2. Identify all meaningful entities, records, tables, lists, measurements, observations, metrics, transactions, findings, or structured information.
    3. Determine the most useful spreadsheet representation.
    4. Create one or more logical sheets if needed.
    5. Do NOT summarize the document.
    6. Extract actual data.
    7. Preserve important numeric values.
    8. Preserve dates, names, identifiers, amounts, quantities, measurements, coordinates, ratings, and classifications.
    9. If the document contains multiple sections, create multiple sheets.
    10. Choose column names yourself.
    11. Ignore decorative text, headers, footers, page numbers, and repeated boilerplate.

    Return ONLY valid JSON.

    Schema:

    {{
    "document_type": "string",
    "sheets": [
        {{
        "sheet_name": "string",
        "columns": ["column1", "column2"],
        "rows": [
            ["value1", "value2"]
        ]
        }}
    ]
    }}
    The goal is to create an Excel workbook that preserves the document's useful structured information as accurately as possible.

    Rules:

    1. Analyze the document structure.
    2. Identify all structured information.
    3. Create one or more sheets as needed.
    4. Each sheet should represent one logical category of information.
    5. Extract ALL available records.
    6. Do not limit the number of rows.
    7. Preserve values exactly whenever possible.
    8. Create meaningful sheet names.
    9. Create meaningful column names.
    10. Do not invent data.
    11. Do not summarize data when records can be extracted.
    12. Return the maximum amount of useful spreadsheet data possible.

    Return ONLY valid JSON.

    Document:

    {text}
    """

    # here, wesend the request to AI and wait for an answer
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

    # receiving answer
    result = response.choices[0].message.content

    # cleaning up
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)