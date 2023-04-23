from icrud import ICRUD
from dal.models.user import User
# import pymongo
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class UserCRUD(ICRUD):
    def __init__(self):
        super().__init__()
        self.users=self.my_data_base["users"]
        self.user={}
    def create_async(self,obj):
        tmp_user=self.users.insert_one(obj)
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def delete_async(self,id):
        tmp_user=self.users.delete_one({"_id":id})
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def update_async(self,id):
        tmp_user=self.users.find_one({"_id":id})
        if(tmp_user["permission"]=="super"):
            tmp_user["permission"]="regular"
        else:
            tmp_user["permission"] = "super"
        self.users.update_one({"_id":id},{"permission":tmp_user["permission"]})
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def get_async(self,_id):
        tmp_user=self.users.find_one({"_id":_id})
        self.user=User(tmp_user["user_name"],tmp_user["_id"],tmp_user["permission"])
        return self.user
    def get_all_async(self):
        pass

     