import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
r= sr.Recognizer()
mic= sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something:")
    audio = r.listen(source)


print("Google thinks you said", r.recognize_google(audio))
