from dal.data_objects.services.basemodel import BaseModel
from dal.models.diploma import Diploma


class DiplomaCRUD(BaseModel):
    def __init__(self):
        super().__init__()
        self.diplomas=self.my_db["diploma"]
        self.diploma={}
    def create_async(self,obj):
        pass
    def delete_async(self,id):
        pass
    def update_async(self,obj):
        pass
    def get_all_async(self):
        pass
    def get_async(self,id):
        # tmp_diploma=self.diplomas.find_one({"_id":id})
        # self.diploma=Diploma(tmp_diploma["_id"],tmp_diploma["math"],tmp_diploma["english"],tmp_diploma["torah"],tmp_diploma["sciences"],tmp_diploma["grammar"],tmp_diploma["history"],tmp_diploma["trend"])
        self.diploma=Diploma("214088999", 9, 5, 8, 9, 10, 7, "math")
        return self.diploma