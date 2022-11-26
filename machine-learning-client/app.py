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


#contains the methods to access and update the database based on calls from the frontEnd
def store_sentiment(user_name, phrase, sentiment):
    #store the sentiment associated with a user's phrase along with the rest of their phrases
    return
def calculate_sentiment(phrase):
    #calculate the sentiment associated with a phrase input
    return
def update_summary_stats():
    #create summary stats based off of all the data in the database
    # we can have things like average sentiment, most popular word, etc.
    return