from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import dotenv_values

# set up connection to database & call the database "db"
# # connect to the database
config = dotenv_values(".env")

cxn = MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug

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