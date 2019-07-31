import uuid
from src.common.database import Database
from bson.objectid import ObjectId


class Burger(object):

    def __init__(self, name, eaten=None, description=None, ingredients=None, _id=None):
        self.name = name
        self.eaten = False if eaten is None else eaten
        self.description = "" if description is None else description
        self.ingredients = "" if ingredients is None else ingredients
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_burger(self):
        Database.insert(collection="burgers",
                        data=self.burger_info())

    def burger_info(self):
        return {
            '_id': self._id,
            'name': self.name,
            'eaten': self.eaten,
            'description': self.description,
            'ingredients': self.ingredients,
        }


    @classmethod
    def findAll_mongo(cls):
        burgers = Database.find(collection='burgers', query={})

        return [cls(**burger) for burger in burgers]


    @classmethod
    def from_mongo(cls, id):
        burger_data = Database.find_one(collection='burgers', query={"_id": ObjectId(id)})

        return cls(**burger_data)

    @staticmethod
    def update_burger(id, data):
        print(id, data)
        Database.update_one(collection="burgers", query={"_id": id},
                        data=data)
