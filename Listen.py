#step-1 pip install googletrans
#step-2 
#Three Functions 
#1- Listen
#2- English Translation
#3- Connect
import speech_recognition as sr
from googletrans import Translator

#1- Listen                   
def Listen():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening Sir....")
        r.pause_threshold=1
        audio= r.listen(source,0,8)
    try:
        print("Translating into English sir....")
        query=r.recognize_google(audio,language="hi")
    except:
        return "Error occuring while recognizing"
    query=str(query).lower()
    return query


#hindi to english
def Translation(Text):
    line=str(Text)
    translate = Translator()
    result= translate.translate(line,src='hi',dest='en')
    data=result.text
    return data

def start():
    query=Listen()
    result=Translation(query)
    return result
