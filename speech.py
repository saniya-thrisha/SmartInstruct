import speech_recognition as sr
import pyaudio
import pyttsx3
from database import retrieve_question, insert_val, set_good, set_okay, set_bad, set_additional

listener= sr.Recognizer()

value=0
engine = pyttsx3.init()
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def listen():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            return command
            
            #value=int(command)
            #print(value)
            
    except Exception as e:
        print(str(e))

def talk(text):
    engine.say("Okay")    
    engine.say(text)
    engine.runAndWait()
    
def good(response, q):
    if('good' in response):
        print('setting good')
        set_good(q)
        return
    
def ok(response, q):
    if('okay' in response or 'ok' in response):
        set_okay(q)
        talk("Please provide additional details.")
        details=listen()
        set_additional(details, q)
        
def bad(response, q):
    if('bad' in response):
        print('setting bad')
        set_bad(q)
        talk("Please provide additional details")
        details=listen()
        set_additional(details, q)  
        

questions= retrieve_question()
for q in questions:
    talk(q[0])
    ans=listen()
    
        
    good(ans,q[0])
    ok(ans,q[0])
    bad(ans,q[0])
    
    if(q[-1]==1):
        insert_val(ans,q[0])
    
    

