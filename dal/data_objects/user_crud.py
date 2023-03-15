from icrud import ICRUD
from db_manger import DBManger
from dal.data_objects.user import User
import pymongo
import asyncio
# from Idb_manger import IDBManger
mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]
class UserCRUD(ICRUD):
    def UserService(self,users:DBManger):
        self.users=users.get_all_users()
    # async def create_async(self,obj:T):
    #     pass
    # async def delete_async(self,id:int):
    #     pass
    async def update_async(self,id,permmision):
        tmp_user=users.update_one({"_id":id},{"permmision":permmision})
        self.user=User(tmp_user.user_name,tmp_user._id,tmp_user.permmision)
        return self.user
    def get_async(self,_id):
        tmp_user=users.find_one({"_id":_id})
        x=tmp_user
        self.user=User(x["user_name"],x["_id"],x["permission"])
        return self.user
    async def get_all_async(self):
        return self.users
     