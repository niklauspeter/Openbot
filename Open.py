from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

client = OpenAI(
    api_key = os.getenv("OPENBOT_API_KEY")
    
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","byw"]:
            break
        response = chat_with_gpt(user_input)
        print("chatbot: ", response)