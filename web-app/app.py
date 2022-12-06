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
        userDocument = db.sentiment_analyzer.find_one({'user_name':userName})
        if userDocument is None:
            return render_template("displayUserResults.html", nothingFound="Sorry :( no record saved for this user!")
        else:
            transcribedAudio = userDocument.user_name.transcribed_audio
            sentimentObject = userDocument.user_name.sentiment
            if sentimentObject.compound == 0:
                sentiment = "You're feeling pretty neutral--seems like things are neither here nor there for you"
            elif sentimentObject.compound < 0:
                if sentimentObject < -0.5:
                    sentiment = "Uh oh, you're feeling pretty negative today... do you want to talk about it?"
                elif sentimentObject >= -0.5:
                    sentiment = "You're feeling a bit negative today, did something happen?"
            else:
                if sentimentObject > 0.5:
                    sentiment = "Wow, you're feeling so positive today! Or are you just a positive person in general?"
                elif sentimentObject <= 0.5:
                    sentiment = "You're kinda positive right now, so does that mean you're in a good mood today?"
            return render_template("displayUserResults.html", somethingFound=1, userName=userName, transcribedAudio=transcribedAudio, sentiment=sentiment)