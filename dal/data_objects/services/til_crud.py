from dal.data_objects.services.basemodel import BaseModel
from dal.models.til import Til
import pandas as pd
import os.path


# import pymongo
# my_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
# my_data_base=my_client["Registration"]
# users=my_data_base["users"]
class TilCRUD(BaseModel):
    def __init__(self):
        super().__init__()
        # super(TilCRUD,self).__init__()
        # self.tiles = self.my_db["til"]
        self.til = {}
        self.tils = []
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.my_path, "../../../api/csvs/til.csv")
        self.df = pd.read_csv(self.path)

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, id):
        pass

    def get(self, _id):
        # tmp_til = self.tiles.find_one({"_id": _id})
        # self.til = Til(tmp_til["class_name"], tmp_til["_id"], tmp_til["verbal_ability"], tmp_til["logical_ability"])
        # return self.til
        int_id = int(_id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.til = Til(lst[0], lst[1], lst[2], lst[3], lst[4])
        print(self.til._id)
        return self.til

    def get_all_async(self):
        pass

    def add_students_tiles(self, nw_students):
        tiles = []
        for index, row in nw_students.iterrows():
            til = Til(row["id"], row["class_name"], row["verbal_ability"], row["logical_ability"], row["final_mark"])
            tiles.append(til)
            print(str(til))
        for row in tiles:
            new_til = {"id": int(row._id), "class_name": row.class_name, "verbal_ability": row.verbal_ability,
                       "logical_ability": row.logical_ability, "final_mark": row.final_mark}
            print(str(new_til))
            self.df = self.df._append(new_til, ignore_index=True)
            print("fghjk", self.df)
        self.df.to_csv(self.path, index=False)
        print(self.df)
