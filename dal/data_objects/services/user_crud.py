from dal.data_objects.services.basemodel import BaseModel
from dal.models.user import User
import csv
import pandas as pd
# import pymongo
# import csv
import os.path


# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class UserCRUD(BaseModel):

    def __init__(self):
        super().__init__()
        self.user = {}
        self.users = []
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.my_path, "../../../api/csvs/users.csv")
        self.df = pd.read_csv(self.path)
        # ls = self.df.T.to_dict().values()
        # for i in ls:
        #     self.users.append(User(i["id"], i["user_name"], i["permission"]))

    def get_async(self, id):
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.user = User(lst[0], lst[1], lst[2])
        return self.user

    def add_user(self, _id, user_name, permission):
        new_row = {'id': int(_id), 'user_name': user_name, 'permission': permission}
        self.df = self.df._append(new_row, ignore_index=True)
        self.df.to_csv(self.path, index=False)
        return {"user added successfully":"the user name is {} and the permission is {}".format(user_name,permission)}

    def get_all(self):
        ls = self.df.T.to_dict().values()
        return ls

    def update_permission(self, _id):
        row_index = self.df.index[self.df['id'] == int(_id)]
        self.df.loc[row_index, 'permission'] = 'super'
        self.df.to_csv(self.path, index=False)
        return "update permission to super for id {}".format(_id)

    def del_user(self, _id):
        row_to_delete = self.df[self.df['id'] == _id].index
        self.df = self.df.drop(row_to_delete)
        self.df.to_csv(self.path, index=False)
        # return {"user deleted successfully": "the id is {}".format(_id)}
        return "user was deleted successfully"
