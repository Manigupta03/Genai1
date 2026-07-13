import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))

SYSTEM_PROMPT = """
You are a document analysis assistant.
Return only valid JSON.
"""

response_schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "bullet_points": {
            "type": "array",
            "items": {"type": "string"}
        },
        "key_facts": {
            "type": "array",
            "items": {"type": "string"}
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral", "mixed"]
        }
    },
    "required": [
        "summary",
        "bullet_points",
        "key_facts",
        "sentiment"
    ]
}


def get_structured_summary(document_text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=document_text,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=response_schema,
            temperature=0.3,
        ),
    )

    return json.loads(response.text)


if __name__ == "__main__":
    with open("sample_input.txt", "r") as f:
        text = f.read()

    result = get_structured_summary(text)
    print(json.dumps(result, indent=2))