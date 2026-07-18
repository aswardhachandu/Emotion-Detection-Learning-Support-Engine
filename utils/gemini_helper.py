import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def generate_ai_response(emotion, user_text):

    prompt = f"""
You are an AI Learning Assistant.

Student Emotion: {emotion}

Student Text:
{user_text}

Provide:

1. A supportive response.
2. A study recommendation.
3. A short motivational message.

Keep the response under 120 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"