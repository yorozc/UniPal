from pymongo import MongoClient
from pymongo.errors import ConfigurationError
import certifi
import os

try: 
    def _uri():
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise ConfigurationError("MONGOD_URI not set")
        return uri

    def get_client() -> MongoClient:
        client = MongoClient(_uri(), tls=True, tlscafile=certifi.where())
        return client
    try:
        get_client().admin.command('ping')
        print('Pinged your deployment. Successfull connection to MongoDB!')
    except Exception as e:
        print(e)

    def get_db():
        return get_client()[os.getenv("DB")]
    
    def get_user_collection():
        return get_db()[os.getenv("USER_COLLECTION")]
    
    def get_unipal_posts():
        return get_db()[os.getenv("POST_COLLECTION")]


except Exception as e:
    print('Unable to make connectino to DB')