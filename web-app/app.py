from flask import Flask

app = Flask(__name__)

@app.route("/")
def sentimentGuesser():
    return "<p>Press the microphone button and start speaking!</p>"

