from dotenv import dotenv_values
import pymongo

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
config = dotenv_values(".env")

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    # render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug



# phrase can be a list input of space-separated words said by user, parsed by us
# audio can be the audio file recorded by the front end
# sentiment can be a numerical score assigned by our classifier
# user_name can be the user's name, used in the database to map their phrases/sentiments to them
# db structure:
# user_name --> {phrase : sentiment, phrase2 : sentiment2, etc} (dict structure)
# each user will have to be treated as unique or we will have to update their entries


def getForm(form):
    # overall function to parse entries by the user
    # uses parse_phrase_from_voice() and check_new_user()
    return
def post_add_record():
    # function to save a user's formatted input and sentiment to the db
    return
def post_delete_record():
    # function to delete a record from the db
    # form = request.form
    # print(form)
    # db.songs.delete_one({
    #     '_id': ObjectId(form['mongoId'])
    # })
    return

def parse_phrase_from_voice(audio):
    #takes audio input and generates a phrase list from it using ML
    return
def calculate_sentiment(phrase):
    #calculate the sentiment associated with a phrase input
    return
def update_summary_stats():
    #create summary stats based off of all the data in the database
    # we can have things like average sentiment, most popular word, etc.
    return
def check_new_user(user_name):
    # return a boolean representing whether the user is new or existing, will impact how we update the db
    return
