import pyttsx3
import webbrowser
import datetime
import numpy as np
import cv2 as ec
import os
import shutil
import face_recognition
import face_recognizer as fr
import speech_recognition as sr







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

    assname = ("V 1 point 0")
    speak("I am your Assistant")
    speak(assname)        



def usrname():
    print('...recognizing...')
    uname = fr.find_face()
    if uname != 'unknown':
     speak("welcome back "+uname)
    else:
     confirm=False
     speak("What should i call you, Sir")
     while(confirm!=True):
      uname = takeCommand()
      speak("Is your name")
      speak(uname)
      confirmation=takeCommand()
      if confirmation=='yes':
        confirm=True
        cam = ec.VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        if s:    # frame captured without any errors
            ec.destroyAllWindows()
            storage=os.path.abspath(__file__)
            storagen=storage.replace('V.3.0.py', '')
            storagen=storagen.replace("\\", '/')

            ec.imwrite(os.path.join(storagen+'/face_storage' ,uname+".jpg"),img) #save image
      else:
        speak("can you please repeat your name again")
     speak("Welcome Mister")
     speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("How can i Help you, Sir")

def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=800
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    
    return query