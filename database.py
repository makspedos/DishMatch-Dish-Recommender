from pymongo import MongoClient, ReturnDocument
from culinary.variables import ENV_VARS


class DatabaseManipulator:
    def __init__(self, test_db=False):
        self.db = self.connect_db(test_db)

    def connect_db(self, test_db=False):
        """
        Connects to a local MongoDB instance and returns the corresponding database object.
        The database name is 'recommendationdb'.
        The connection is configured using the following environment variables:
        - DB_USER: MongoDB username
        - DB_PASS: MongoDB password
        """
        client = MongoClient('localhost', 27017, username=ENV_VARS['DB_USER'], password=ENV_VARS['DB_PASS'])
        if test_db:
            return client.test_recommendationdb
        return client.recommendationdb

    def create_or_update_user(self, session_id, user_data=None, recommended_ingredients=None):
        updated_user = []
        if recommended_ingredients:
            updated_user = self.db.user.find_one_and_update(
                {"session_id": session_id},
                {"$set": {'recommended_ingredients': recommended_ingredients}},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )

        elif user_data:
            self.db.user.update_one(
                {"session_id": session_id},
                {"$push": {"user_dish": user_data}},
                upsert=True,
            )
            updated_user = self.db.user.find_one({"session_id": session_id})
            if len(updated_user['user_dish']) > 5:
                self.delete_ingredients(updated_user)
        return updated_user

    def find_user(self, session_id):
        user_session = self.db.user.find_one({'session_id': session_id})
        created_user = user_session is True
        if created_user:
            if len(user_session['user_dish']) > 5:
                self.delete_ingredients(user_session)
        return user_session

    def delete_ingredients(self, user):
        user_id = user['_id']
        self.db.user.update_one(
            {'_id': user_id},
            {'$pop': {'user_dish': -1}}
        )
