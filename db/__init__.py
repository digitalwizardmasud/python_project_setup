from pymongo import MongoClient
from config import mongo_uri


uri = mongo_uri
client = MongoClient(uri)
database = client.get_database("wesualy")

def connectDb():
    return database
