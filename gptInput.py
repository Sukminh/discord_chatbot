from dotenv import load_dotenv
import os
load_dotenv()

import openai

openai.api_key = os.getenv("API_KEY")

messages = []

def gptReply(message) -> str:
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    return reply