from pymongo import MongoClient
from culinary.variables import ENV_VARS

def connect_db():
    client = MongoClient('localhost', 27017, username=ENV_VARS['DB_USER'], password=ENV_VARS['DB_PASS'])
    db = client.recommendationdb
    return db
