import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_with_gpt(prompt,
                  system_role="You are a helpful financial assistant."):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": system_role
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=0.7,
        max_tokens=256,
    )
    return response.choices[0].message.content.strip()
