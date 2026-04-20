from pymongo import MongoClient
from pymongo.errors import ConfigurationError
import certifi
import os
from dotenv import load_dotenv

try: 
    load_dotenv()
    DB_NAME = os.getenv("DB")
    USER_COLL = os.getenv("USER_COLLECTION")
    PALPOST_COLL = os.getenv("POST_COLLECTION")
    def _uri():
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise ConfigurationError("MONGODB_URI not set")
        return uri

    def get_client() -> MongoClient:
        client = MongoClient(_uri(), tls=True, tlscafile=certifi.where())
        return client
    try:
        get_client().admin.command('ping')
        print('Pinged your deployment. Successfull connection to MongoDB!')
    except Exception as e:
        print(e)
    
    db = get_client()[DB_NAME]
    user_coll = db[USER_COLL]
    palpost_coll = db[PALPOST_COLL]

    def get_palpost_coll():
        return palpost_coll


except Exception as e:
    print('Unable to make connectino to DB', e)