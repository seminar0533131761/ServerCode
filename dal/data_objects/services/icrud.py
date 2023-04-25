import pymongo
from abc import ABC, abstractmethod
class ICRUD(ABC):
    def __init__(self):
        self.my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
        self.my_data_base=self.my_client["Registration"]
    @abstractmethod
    def create_async(self,obj):
        pass
    @abstractmethod
    def delete_async(self,id):
        pass
    @abstractmethod
    def update_async(self,obj):
        pass
    @abstractmethod
    def get_async(self,id):
        pass
    @abstractmethod
    def get_all_async(self):
        pass
