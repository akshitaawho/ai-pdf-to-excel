# test_ai.py

from services.ai_extractor import extract_structured_data

with open("crazy_test.txt", "r", encoding="utf-8") as f:
    text = f.read()

result = extract_structured_data(text)

print(result)