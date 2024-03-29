from dal.data_objects.services.basemodel import BaseModel
from dal.models.diploma import Diploma
import pandas as pd
import os.path


class DiplomaCRUD(BaseModel):
    def __init__(self):
        super().__init__()
        self.diploma = {}
        self.diplomas = []
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.my_path, "../../../api/csvs/diploma.csv")
        self.df = pd.read_csv(self.path)

    def get(self, id):
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.diploma = Diploma(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7])
        return self.diploma

    def compare_students_grades(self, student1_id, student2_id):
        student1 = self.df[(self.df['id'] == int(student1_id))]
        student2 = self.df[(self.df['id'] == int(student2_id))]
        subjects = list(self.df.columns)
        # the first col is the id and the last are the trend
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

    def add_diploma(self, nw_students):
        try:
            diplomas = []
            for index, row in nw_students.iterrows():
                student_diploma = Diploma(row["id"], row["math"], row["english"], row["torah"], row["sciences"],
                                          row["grammar"], row["history"], row["trend"])
                diplomas.append(student_diploma)
            print(diplomas)
            for row in diplomas:
                new_student = {"id": int(row.id), "math": row.math, "english": row.english,
                               "torah": row.torah, "sciences": row.sciences, "grammar": row.grammar,
                               "history": row.history, "trend": row.trend}
                self.df = self.df._append(new_student, ignore_index=True)

            self.df.to_csv(self.path, index=False)
            return True
        except Exception as err:
            print(err)
            return False
