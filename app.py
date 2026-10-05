import os
import ssl

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured")

# Create SSL context with verification disabled

ssl_context = ssl.create_default_context()

ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


# HTTP options

http_options = types.HttpOptions(
    client_args={
        "verify": ssl_context
    },
    async_client_args={
        "verify": ssl_context
    }
)

# Create Gemini client

client = genai.Client(
    api_key=api_key,
    http_options=http_options
)


MODEL = "gemini-3.5-flash-lite"

# Chatbot

print("================================")
print("       Gemini AI Chatbot")
print("================================")
print("Type 'exit' to stop.\n")


while True:

    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not user_prompt.strip():
        continue

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=user_prompt
        )

        print("\nBot:", response.text)
        print()

    except Exception as e:

        print("\nError:", e)
        print()