from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import dotenv_values

# set up connection to database & call the database "db"
# connect to the database
config = dotenv_values(".env")

app = Flask(__name__)


# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mode

# # connect to the database
cxn = MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
#     # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
#     # the ping command failed, so the connection is not available.
    #render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug



@app.route("/", methods = ["GET", "POST"])
def displaySavedResults():
    if(request.method == "GET"):
        return render_template("enterUserInfo.html")
    else:
        userName = request.form["userName"]
        userDocuments = db.sentiment_analyzer.find({'user_name':userName})
        if len(list(userDocuments.clone())) == 0:
            return render_template("displayUserResults.html", nothingFound="Sorry :( no record saved for this user!")
        else:
            userDocument = userDocuments[0]
            transcribedAudio = userDocument.transcribed_audio
            sentiment = userDocument.sentiment
            return render_template("displayUserResults.html", somethingFound=1, userName=userName, transcribedAudio=transcribedAudio, sentiment=sentiment)