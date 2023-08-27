# speak function
# 1- Windows based speak function - pip install pyttsx3
# 2- chrome based speak function - pip install selenium

#windows based
# adv - Fast, Offline accessable
#disadv - Can't Interrupt it while it is speaking, Less Voices.
import pyttsx3
from Listen import *
def speak(Text):
    #sapi5 is windows api which will help us to connect
    engine=pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    for voice in  voices:
        print(voice)
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',180)
    print(f"You : {Text}")
    engine.say(Text)
    engine.runAndWait()

text=start()
speak(text)


#chrome based
# adv- more voices, more clear, Can interrupt in between
#disadv - word limit