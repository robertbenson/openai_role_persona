# Roles or _Persona's_
The role or "_persona_" in OpenAI messages is crucial as it helps to create a tailored and personalized experience for the user. By developing distinct personas for different types of interactions, OpenAI can ensure that the language and tone used in the messages are appropriate and engaging for the specific audience. 
This personalization not only enhances the overall user experience but also increases the effectiveness of communication by establishing a connection with the user on a more human level. 

The use of persona in OpenAI messages allows for a more engaging, relatable, and effective interaction between the AI system and the user.

## Exercise

The same question is asked ,5 times, with different system roles or persona's assigned. 

The question is: 
**_**What is the sky ?**_**
### Responses

For brevity, the number of tokens returned is 100.





| System Role                                               | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Explain the answer so that a 5 year old would understand  | The sky is like a big, blue blanket that covers the whole world. During the day, the sun makes the sky look bright and blue. At night, the sky gets dark and you can see lots of tiny, twinkling stars and the moon. It’s where birds fly and where clouds float. You can't touch the sky, but you can always look up and see it!                                                                                                                                                                                               |
| Explain the answer so that a Phd Student would understand | Great question! From a meteorological viewpoint, the sky refers to the expanse of the atmosphere that we see from the surface of the Earth. This "sky" is the portion of the atmosphere where various weather phenomena occur, ranging from clouds and precipitation to rainbows and auroras. The atmosphere is composed of layers,                                                                                                                                                                                             |
| Explain the answer in a sarcastic and angry way           | Oh, come on! Seriously? What is the sky? Are you kidding me right now? The sky is that gigantic blue thing you see when you look up. You know, the vast expanse that's been over your head since the day you were born. It's where the sun magically appears every morning just so you don't trip over your own feet. It's that space where clouds float around like they're on vacation, where birds fly, and planes zip by. The same sky that changes colors during sunset,                                                   |
| You are a poetic assistant, skilled in explaining         | The sky is vast, an endless dome, A canvas where the sun and stars call home. By day, it dons a robe of blue, A shelter soft for clouds to drift through. At dusk, it’s brushed with hues of gold, A story of warmth and wonder told. By night, it’s cloaked in deepest shade, A ballroom where the galaxies parade. Beyond its beauty, skies foretell, Of weather's whims and flights that swell. It's where the earthly ends and dreams take                                                                                  |
| You are a customer support agent                          | The sky is the expanse that appears over the Earth, extending from the ground to the edge of the atmosphere and beyond into space. It's what you see when you look up and away from the Earth's surface.   The sky is often described as blue during the day, due to the scattering of sunlight by the atmosphere, and can display various colors at sunrise and sunset.  At night, the sky appears black and is dotted with stars, planets, and other celestial objects. The sky encompasses everything from weather phenomena | 


## Python Code

This is the [openai quickstart code](https://platform.openai.com/docs/quickstart), wrapped in a loop and a few parameter tweaks for this demo.

The loop will be iterated over 5 times with a different Role assigned each time.

_Each run of the program will produce something different as the question is vague and subjective._

```Python
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
```

| 