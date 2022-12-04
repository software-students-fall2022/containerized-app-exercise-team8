from flask import Flask, render_template, request
import pymongo

# set up connection to database & call the database "db"

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def displaySavedResults():
    if(request.method == "GET"):
        return render_template("enterUserInfo.html")
    else:
        userName = request.args.userName
        userDocument = db.sentiment_analyzer.find({'user_name':userName})[0]
        transcribedAudio = userDocument.transcribed_audio
        sentiment = userDocument.sentiment
        return render_template("displayUserResults.html", userName=userName, transcribedAudio=transcribedAudio, sentiment=sentiment)