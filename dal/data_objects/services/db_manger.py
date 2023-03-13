import pymongo
# from Idb_manger import IDBManger
mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]
class DBManger:
    def DBManger(self):
        self.users=[]
    def get_all_users():
        users=users.find()
        return users