from dal.data_objects.services.basemodel import BaseModel
from dal.models.user import User
import csv
import pandas as pd


# import pymongo
#import csv
import os.path
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class UserCRUD(BaseModel):
    # def __init__(self):
    #     super(UserCRUD, self).__init__()
    #     # self.users = self.my_db["users"]
    #     self.user = {}
    #     self.users = []
    #     df = pd.read_csv('users.csv')
    #     ls = df.T.to_dict().values()
    #     for i in ls:
    #         self.users.append(User(i["id"], i["user_name"], i["permission"]))
    #
    # def create_async(self, obj):
    #     pass
    #
    # def delete_async(self, id):
    #     pass
    #
    # def update_async(self, id):
    #     tmp_user = self.users.find_one({"_id": id})
    #     if (tmp_user["permission"] == "super"):
    #         tmp_user["permission"] = "regular"
    #     else:
    #         tmp_user["permission"] = "super"
    #     self.users.update_one({"_id": id}, {"permission": tmp_user["permission"]})
    #     self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permmision)
    #     return self.user
    #
    # def get_async(self, _id):
    #     # tmp_user=self.users.find_one({"_id":_id})
    #     # self.user=User(tmp_user["user_name"],tmp_user["_id"],tmp_user["permission"])
    #     for i in self.users:
    #         if i.id == "214088999":
    #             self.user = User(i.id, i.user_name, i.permmision)
    #             return self.user
    #
    # def get_all_async(self):
    #     pass
    def __init__(self):
        super().__init__()
        self.user = {}
        self.users = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../../api/csvs/users.csv")
        self.df = pd.read_csv(path)
        # ls = self.df.T.to_dict().values()
        # for i in ls:
        #     self.users.append(User(i["id"], i["user_name"], i["permission"]))

    # def get_async(self, _id):
    #     pass
        # for i in self.users:
        #     if i.id == int(_id):
        #         self.user = User(i.id, i.user_name, i.permission)
        #         return self.user

    def get_async(self, id):
        # Read the CSV file into a DataFrame
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.user=User(lst[0],lst[1],lst[2])
        return self.user

    def add_user(self, _id, user_name, permission):
        # self.user=User(_id,user_name,permission)
        # df = pd.read_csv('users.csv')
        new_row = {'id': int("111"), 'user_name': 'JohnDoe', 'permission': 'regular'}
        self.df = self.df._append(new_row, ignore_index=True)
        self.df.to_csv('users.csv', index=False)
        return "created successfully"

    def get_all(self):
        # self.df = pd.read_csv('users.csv')
        ls = self.df.T.to_dict().values()
        for i in ls:
            self.users.append(User(i["id"], i["user_name"], i["permission"]))
        return self.users

    def update_permission(self, id):
        row_index = self.df.index[self.df['id'] == 8790]
        # self.df.loc[row_index, 'user_name'] = 'yhuda'
        self.df.loc[row_index, 'permission'] = 'super'
        self.df.to_csv('users.csv', index=False)

    def del_user(self, id):
        row_to_delete = self.df[self.df['id'] == 2134].index
        self.df = self.df.drop(row_to_delete)
        self.df.to_csv('users.csv', index=False)
        print(self.df)


a=UserCRUD()
print(a.get_async("214088999"))
