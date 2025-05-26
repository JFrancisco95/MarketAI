import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def chat_with_gpt(prompt, system_role="You are a helpful financial assistant."):
    response = openai.ChatCompletion.create(
        model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt},
    ]
    )
    return response.choices[0].message['content']