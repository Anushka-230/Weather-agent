import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../.env")

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def extract_weather_query(user_query: str):
    prompt = f"""
Extract the weather request from the user's message.

Return ONLY valid JSON.

Example:

{{
  "city":"Puri",
  "year":2027,
  "month":7,
  "day":15
}}

If the day is not mentioned, use 15.
If the year is not mentioned, assume 2026.

User:
{user_query}
"""

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)


def generate_weather_response(city, year, month, day, temperature):
    prompt = f"""
You are a helpful weather assistant.

The machine learning model predicted the following:

City: {city}
Date: {day}/{month}/{year}
Predicted Temperature: {temperature:.2f}°C

Generate a friendly response in 2-3 sentences.
Do not mention AI or machine learning.
"""

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()