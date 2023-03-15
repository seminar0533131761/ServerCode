import pymongo
from abc import ABC, abstractmethod
class ICRUD(ABC):
    def __init__(self):
        self.my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
    async def create_async(self,obj):
        pass
    async def delete_async(self,id:int):
        pass
    async def update_async(self,obj):
        pass
    @abstractmethod
    def get_async(self,id):
        pass
    async def get_all_async(self):
        pass
