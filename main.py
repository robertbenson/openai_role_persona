from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI()

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")


def run_chat_for_temperature(persona_req: str):
    print(f"\n\nRunning chat completion with a persona of: {persona_req}")
    completion = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=100,
        temperature=1,
        messages=[
            {"role": "system",
             "content": persona_req},
            {"role": "user",
             "content": "What is the sky ?"}
        ]
    )
    print(completion.choices[0].message.content)


if __name__ == '__main__':
    for persona in [
            "Explain the answer so that a 5 year old would understand",
            "Explain the answer so that a Phd Student would understand",
            "Explain the answer in a sarcastic and angry way",
            "You are a poetic assistant, skilled in explaining ",
            "You are a customer support agent"
    ]:
        run_chat_for_temperature(persona)
