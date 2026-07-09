import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API")
)

history = []

print("Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("This chat is closed.")
        break

    history.append(f"User: {user_input}")

    prompt = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text

    print(f"Bot: {reply}\n")

    history.append(f"Bot: {reply}")