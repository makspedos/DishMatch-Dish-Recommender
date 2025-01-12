from pymongo import MongoClient
from culinary.variables import ENV_VARS

class DatabaseManipulator:
    def __init__(self):
        self.db = self.connect_db()

    def connect_db(self):
        """
        Connects to a local MongoDB instance and returns the corresponding database object.
        The database name is 'recommendationdb'.
        The connection is configured using the following environment variables:
        - DB_USER: MongoDB username
        - DB_PASS: MongoDB password
        """
        client = MongoClient('localhost', 27017, username=ENV_VARS['DB_USER'], password=ENV_VARS['DB_PASS'])
        db = client.recommendationdb
        return db

    def create_or_update_user(self, session_id, user_data):
        self.db.user.update_one(
            {'session_id': session_id},
            {'$push': {'user_dish': user_data}}, upsert=True)

    def find_user(self, session_id):
        user_session = self.db.user.find_one({'session_id': session_id})
        return user_session
