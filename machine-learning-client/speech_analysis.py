import requests
import json
import speech_recognition as sr
r= sr.Recognizer()
mic= sr.Microphone()


with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something:")
    audio = r.listen(source)


def getSentiment(text):
    endpoint = "https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/c816632f-8712-4009-88e2-be8c01be24a3"


    username = "apikey"
    password = "dAXHKT2HRw6hFm0WqNT8KeuRNgkhPMBXYlXBE8PX0N7K"
    parameters = {
        'features': 'emotion,sentiment',
        'version' : '2019-07-12',
        'text': text,
        'language' : 'en',
    }

    resp = requests.get(endpoint, params=parameters, auth=(username, password))
    
    return resp.json()

##audio_text= "" + r.recognize_google(audio)
sentiment= getSentiment("Hi how are you!")


##print("We think you said", audio_text)
print("Sentiment Analysis:")
print(sentiment)
##sentiment['sentiment']
##sentiment['emotion']
