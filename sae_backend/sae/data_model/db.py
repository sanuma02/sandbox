from pymongo import MongoClient
import config

class DataModel():

    def __init__(self):
        self.client = MongoClient(config.CLIENT,
                                  username= config.CLIENT_USER,
                                  password= config.CLIENT_PASS)
        self.db = self.client[config.DB]

    def get_db(self):
        return self.db

    