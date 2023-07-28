import pyttsx3
import webbrowser
import datetime
import numpy as np



# username and assistant name init
uname = ''
assname = ''
engine = None
voices = None
#Sound engine initialisation

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#voices[1] for female [0] for male
print(type(engine))
print(type(voices))


def browser_init():  # To initialize browser("Chrome")
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    

def speak(audio):  # Speak function that speaks out string in 'audio'
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning Sir !")
        print("Good Morning Sir !")
    elif hour >= 0 and hour < 5:
        speak("Good Morning Sir! Maybe you should be sleeping?")
        print("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
        print("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
        print("Good Evening Sir !")
