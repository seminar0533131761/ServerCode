from dal.data_objects.student import Student
from icrud import ICRUD
from db_manger import DBManger
from dal.data_objects.user import User
import pymongo
import asyncio
# from Idb_manger import IDBManger
mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]
# global users
class StudentCRUD(ICRUD):
    #,users:DBManger
    def __init(self):
        super.__init__()
        self.student=self.my_data_base["students"]
        self.student={}
    def create_async(self,obj):
        tmp_user=users.insert_one(obj)
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def delete_async(self,id):
        tmp_user=users.delete_one({"_id":id})
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def update_async(self,id,permmision):
        tmp_user=users.update_one({"_id":id},{"permmision":permmision})
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def get_async(self,_id):
        tmp_user=self.students.find_one({"_id":_id})
        self.user=User(tmp_user["user_name"],tmp_user["_id"],tmp_user["permission"])
        return self.user
    async def get_all_async(self):
        return self.users
     