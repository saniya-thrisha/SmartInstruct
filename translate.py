#pip install googletrans==4.0.0-rc1
#https://cloud.google.com/translate/docs/languages

from googletrans import Translator
import pyttsx3

def translate(my_input):
    
    
    translator= Translator()
    translated= translator.translate(my_input, dest='hi').text
    trans=translator.translate(translated, dest='hi').pronunciation
    print(trans)
    return trans

engine = pyttsx3.init()
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say("Okay")    
    engine.say(text)
    engine.runAndWait()

if __name__=='__main__':
    text=translate("how is the tyre")
    talk(text)