import pymongo
from abc import ABC, abstractmethod

import pymongo
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


username = quote_plus('chani')
password = quote_plus('chani113')
uri = f"mongodb+srv://{username}:{password}@cluster0.7v5y8rk.mongodb.net/?retryWrites=true&w=majority"


class BaseModel:

    client = None

    def __init__(self):
        if not isinstance(BaseModel.client, BaseModel) and not BaseModel.client:
            BaseModel.client = MongoClient(uri, server_api=ServerApi('1'))
            # Send a ping to confirm a successful connection
            try:
                BaseModel.client.admin.command('ping')
                print("Pinged your deployment. You successfully connected to MongoDB!")

                self.my_db = BaseModel.client['Cluster0']
            except Exception as e:
                print(e)

    # def __init__(self):
    #     print('init')
    #     # # todo singelton
    #     # uri = f"mongodb+srv://{username}:{password}@cluster0.7v5y8rk.mongodb.net/?retryWrites=true&w=majority"
    #     # # Create a new client and connect to the server
    #     # if not self.client:
    #     #     self.client = MongoClient(uri, server_api=ServerApi('1'))
    #     # # Send a ping to confirm a successful connection
    #     #     try:
    #     #         self.client.admin.command('ping')
    #     #         print("Pinged your deployment. You successfully connected to MongoDB!")
    #     #     except Exception as e:
    #     #         print(e)

    @abstractmethod
    def create_async(self, obj):
        pass

    @abstractmethod
    def delete_async(self, id):
        pass

    @abstractmethod
    def update_async(self, obj):
        pass

    @abstractmethod
    def get_async(self, id):
        pass

    @abstractmethod
    def get_all_async(self):
        pass


