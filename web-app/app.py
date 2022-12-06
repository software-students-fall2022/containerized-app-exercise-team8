from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import dotenv_values

# set up connection to database & call the database "db"
# # connect to the database
config = dotenv_values(".env")

app = Flask(__name__)

MONGO_URI = "mongodb://mongo:27017"
COLLECTION_NAME = 'sentiment_analyzer'

try:
    client = MongoClient(
        MONGO_URI, serverSelectionTimeoutMS=30000, username="root", password="example")
    db = client[config['MONGO_DBNAME']]
    collection = client[config['MONGO_DBNAME']][COLLECTION_NAME]
    # if we get here, the connection worked!
    print(' *', 'Connected to MongoDB!')
except Exception as e:
    # the ping command failed, so the connection is not available.
    render_template('error.html', error=e)  # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e)  # debug


@app.route("/", methods=["GET", "POST"])
def displaySavedResults():
    if request.method == "GET":
        return render_template("enterUserInfo.html")
    else:
        userName = request.form["userName"]
        userDocument = db.COLLECTION_NAME.find_one({'user_name': userName})
        if userDocument is None:
            return render_template("displayUserResults.html", nothingFound="Sorry :( no record saved for this user!")
        else:
            transcribedAudio = userDocument["transcribed_audio"]
            sentiment = userDocument["sentiment"]
            return render_template("displayUserResults.html", somethingFound=1, userName=userName, transcribedAudio=transcribedAudio, sentiment=sentiment)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2001, debug=True)
