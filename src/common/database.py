import pymongo
from bson.objectid import ObjectId

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
         client = pymongo.MongoClient(Database.URI)
         Database.DATABASE = client['pyburger']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_one(collection, query, data):
        return Database.DATABASE[collection].find_one_and_update(query, {"$set": data})
