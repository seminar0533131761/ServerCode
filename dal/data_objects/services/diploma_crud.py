from dal.data_objects.services.icrud import ICRUD
from dal.models.diploma import Diploma


class DiplomaCRUD(ICRUD):
    def __init__(self):
        super().__init__()
        self.diplomas=self.my_data_base["diploma"]
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
        tmp_diploma=self.diplomas.find_one({"_id":id})
        self.diploma=Diploma(tmp_diploma["_id"],tmp_diploma["math"])
        return self.diploma