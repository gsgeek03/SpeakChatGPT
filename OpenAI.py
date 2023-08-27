import openai
import os
from Listen import *
from Speak import *
from dotenv import load_dotenv


API="---------"
openai.api_key=API
completion=openai.Completion()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt=start()
print(f"YOU: {prompt}")
result=get_completion(f"Give result in 300 words or less {prompt}")
print(result)

if len(result)<3000:
    speak(result)

speak("Have a good day Boss")





