import pyttsx3


# username and assistant name init
uname = ''
assname = ''
engine = None
voices = None
#Sound engine initialisation

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(type(engine))
print(type(voices))


