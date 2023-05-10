from dal.data_objects.services.basemodel import BaseModel
from dal.models.user import User


# import pymongo
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class UserCRUD(BaseModel):
    def __init__(self):
        super(UserCRUD, self).__init__()
        self.users = self.my_db["users"]
        if "users" in self.my_db.list_collection_names():
            print("The collection exists.")

    # users = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not isinstance(cls.users, cls):
    #         cls.users = BaseModel.client["users"]
    #     return BaseModel.__new__(cls)

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
        self.user = User("chani", "214088999", "super")
        return self.user

    def get_all_async(self):
        pass

# class A(object):
#     def __new__(cls):
#         print("Creating instance")
#
#
#     def __init__(self):
#         print("Init is called")
#
# class B(A):
#     def __init__(self):
#         super(B, self).__init__()
#         print("Init B is called")
# a = A()