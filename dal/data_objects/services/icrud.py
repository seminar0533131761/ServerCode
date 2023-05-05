import pymongo
from abc import ABC, abstractmethod
class ICRUD(ABC):
    def __init__(self):
        # mongodb+srv://<username>:<password>@cluster0.tlpijup.mongodb.net/?retryWrites=true&w=majority
        #  always mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority

        self.my_client = pymongo.MongoClient("mongodb+srv://chani:chani113@cluster0.7v5y8rk.mongodb.net/?retryWrites=true&w=majority")
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
