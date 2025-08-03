# insight_generator.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_insight(summary_text):
    prompt = f"Based on the following text, provide insights and a short summary:\n\n{summary_text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content
