from flask import Flask
from flask import request
from flask import render_template
import os
from dotenv import dotenv_values
import pymongo
from bs4 import BeautifulSoup
import speech_recognition as sr
#from werkzeug import secure_filename
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# # load credentials and configuration options from .env file
# # if you do not yet have a file named .env, make one based on the template in env.example
# config = dotenv_values(".env")

# # turn on debugging if in development mode
# if config['FLASK_ENV'] == 'development':
#     # turn on debugging, if in development
#     app.debug = True # debug mnode

# # connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
#     # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
#     # the ping command failed, so the connection is not available.
    render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST": # time permitting: add logic to acknowledge their previous submission
        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route("/upload", methods = ['POST', 'GET'])
def upload():
    if request.method == "POST":
        if 'audioFile' in request.files:
            f = request.files['audioFile']
            f.save(f.filename)
            #print(request.files)

            recog_text = parse_phrase_from_voice(f.filename) # string translated from the file
            sentiment = calculate_sentiment(recog_text)

            print('file uploaded successfully')
            print(recog_text)
            print(sentiment)
        #print("posting")
        print(request.files)
        return render_template('upload.html')
    else:
        return render_template('index.html')


# phrase can be a list input of space-separated words said by user, parsed by us
# audio can be the audio file recorded by the front end
# sentiment can be a numerical score assigned by our classifier
# user_name can be the user's name, used in the database to map their phrases/sentiments to them
# db structure:
# user_name --> {phrase : sentiment, phrase2 : sentiment2, etc} (dict structure)
# each user will have to be treated as unique or we will have to update their entries

def add_record(user_name, transcribed_audio, sentiment_dict):
    # function to save a user's formatted input and sentiment to the db
    if (check_new_user(user_name)):
        create_data={user_name:{'transcribed_audio': transcribed_audio, 'sentiment': sentiment_dict}}
        db.sentiment_analyzer.insert_one(create_data)
    else:
        #user already exists
        print('user already exists')
    return render_template('homePage.html')

def parse_phrase_from_voice(filename):
    # read the entire audio file
    #takes audio input and generates a phrase list from it using ML
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)  
    return r.recognize_google(audio)
    
def calculate_sentiment(phrase):
    sid_obj = SentimentIntensityAnalyzer()
    #calculate the sentiment associated with a phrase input
    return sid_obj.polarity_scores(phrase)

def check_new_user(user):
    # return a boolean representing whether the user is new or existing, will impact how we update the db
    # returns True if user does not yet exist, False if they do
    docs= db.sentiment_analyzer.find({'user_name':user})
    if len(docs)>=1:
        return False
    return True
