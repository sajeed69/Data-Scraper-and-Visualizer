# insight_generator.py

import os
from openai import OpenAI

client = OpenAI(api_key="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")

def get_insight(summary_text):
    prompt = f"Based on the following text, provide insights and a short summary:\n\n{summary_text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content
