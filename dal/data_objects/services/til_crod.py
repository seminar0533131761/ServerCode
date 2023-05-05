from dal.data_objects.services.icrud import ICRUD
from dal.models.til import Til


# import pymongo
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class TilCRUD(ICRUD):
    def __init__(self):
        super().__init__()
        self.tiles = self.my_data_base["til"]
        self.til = {}

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, id):
       pass
    def get_async(self, _id):
        # tmp_til = self.tiles.find_one({"_id": _id})
        # self.til = Til(tmp_til["class_name"], tmp_til["_id"], tmp_til["verbal_ability"], tmp_til["logical_ability"])
        self.til = Til("214088999", "a", "good", "good")
        return self.til

    def get_all_async(self):
        pass

