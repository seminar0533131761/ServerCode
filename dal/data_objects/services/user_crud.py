from dal.data_objects.services.basemodel import BaseModel
from dal.models.user import User
import csv
import pandas as pd


# import pymongo
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class UserCRUD(BaseModel):
    def __init__(self):
        super(UserCRUD, self).__init__()
        # self.users = self.my_db["users"]
        self.user = {}
        self.users = []
        df = pd.read_csv('users.csv')
        ls = df.T.to_dict().values()
        for i in ls:
            self.users.append(User(i["id"], i["user_name"], i["permission"]))

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, id):
        tmp_user = self.users.find_one({"_id": id})
        if (tmp_user["permission"] == "super"):
            tmp_user["permission"] = "regular"
        else:
            tmp_user["permission"] = "super"
        self.users.update_one({"_id": id}, {"permission": tmp_user["permission"]})
        self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permmision)
        return self.user

    def get_async(self, _id):
        # tmp_user=self.users.find_one({"_id":_id})
        # self.user=User(tmp_user["user_name"],tmp_user["_id"],tmp_user["permission"])
        for i in self.users:
            if i.id == "214088999":
                self.user = User(i.id, i.user_name, i.permmision)
                return self.user

    def get_all_async(self):
        pass


a = UserCRUD()
print(a.get_async("214088999"))
