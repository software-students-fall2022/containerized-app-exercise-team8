from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def sentimentGuesser():
    #file = request.files["file"]
    # recognizer = sr.Recognizer()

    # with sr.Microphone() as source:
    #     print("Listening!")
    #     audio = recognizer.listen(source)
    #     try:
    #         transcript = recognizer.recognize_google(audio, key = None)
    #     except:
    #         transcript = None
    #         print("Could not transcribe")

    # return render_template("homePage.html", transcript = transcript)
    return render_template("homePage.html")

