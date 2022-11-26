from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def sentimentGuesser():
    return render_template("homePage.html")

