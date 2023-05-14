from dal.data_objects.services.basemodel import BaseModel
from dal.models.diploma import Diploma
import pandas as pd
import os.path


class DiplomaCRUD(BaseModel):
    def __init__(self):
        # super(DiplomaCRUD,self).__init__()
        # self.diplomas=self.my_db["diploma"]
        # self.diploma={}
        super().__init__()
        self.diploma = {}
        self.diplomas = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../../api/csvs/diploma.csv")
        self.df = pd.read_csv(path)

    def create_async(self, obj):
        pass

    def delete_async(self, id):
        pass

    def update_async(self, obj):
        pass

    def get_all_async(self):
        pass

    def get_async(self, id):
        # tmp_diploma=self.diplomas.find_one({"_id":id})
        # self.diploma=Diploma(tmp_diploma["_id"],tmp_diploma["math"],tmp_diploma["english"],tmp_diploma["torah"],tmp_diploma["sciences"],tmp_diploma["grammar"],tmp_diploma["history"],tmp_diploma["trend"])
        # return self.diploma
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.diploma = Diploma(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7])
        return self.diploma

    def compare_students_grades(self, student1_id, student2_id):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../../api/csvs/diploma.csv")
        g = pd.read_csv(path)
        student1 = g[(g['id'] == student1_id)]
        student2 = g[(g['id'] == student2_id)]
        subjects = list(g.columns)
        # the first col is the idd and the last is the trend
        subjects = subjects[1:-1]
        student1_lst_of_dicts = student1.to_dict().values()
        student2_lst_of_dicts = student2.to_dict().values()
        student1_lst_of_lst = [list(i.values()) for i in student1_lst_of_dicts]
        student2_lst_of_lst = [list(i.values()) for i in student2_lst_of_dicts]
        # slices are for the id and the trend name
        correct_student1_and_id = student1_lst_of_lst[1:-1]
        correct_student2_and_id = student2_lst_of_lst[1:-1]
        student1_grades = [int(i[0]) for i in correct_student1_and_id]
        student2_grades = [int(i[0]) for i in correct_student2_and_id]
        return student1_grades, student2_grades, subjects


a = DiplomaCRUD()
print(a.compare_students_grades(343553777, 558888922))
