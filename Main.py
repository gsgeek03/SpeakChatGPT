from OpenAI import *
from Listen import *
from Speak import *

prompt=start()
print(f"YOU: {prompt}")
result=get_completion(f"Give result in 300 words or less {prompt}")
print(result)

if len(result)<3000:
    speak(result)

speak("Have a good day Boss")
