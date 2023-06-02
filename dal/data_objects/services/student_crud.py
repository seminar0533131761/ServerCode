from dal.data_objects.services.basemodel import BaseModel
from dal.models.student import Student
import os.path
import pandas as pd


class StudentCrud(BaseModel):
    def __init__(self):
        super().__init__()
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.my_path, "../../../api/csvs/students.csv")
        self.df = pd.read_csv(self.path)
        self.obj_students = []
        self.student = {}

    def get(self, _id):
        int_id = int(_id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.student = Student(lst[0], lst[1], lst[2], lst[3], lst[4])
        return self.student

    def get_student_by_class_name(self, class_name):
        self.obj_students.extend([Student("214088999", "rivi", "dryman", "0369202", "a1"),
                                  Student("214088999", "chani", "chalamish", "054768322", "a1"),
                                  Student("214088999", "chavi", "chif", "0572322", "a1")])
        specified_class = [i for i in self.obj_students if i.class_name == class_name]
        return specified_class

    def get_students_and_desires_by_training(self, training):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path1 = os.path.join(my_path, "../../../api/csvs/students.csv")
        s = pd.read_csv(path1)
        path2 = os.path.join(my_path, "../../../api/csvs/students_desires.csv")
        d = pd.read_csv(path2)
        merged_df = pd.merge(s, d, on='id')
        filtered_df = merged_df[merged_df['final_answer'] == training]
        return filtered_df.T.to_dict().values()

    def get_students_and_desires_by_class(self, class_name):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path1 = os.path.join(my_path, "../../../api/csvs/students.csv")
        s = pd.read_csv(path1)
        path2 = os.path.join(my_path, "../../../api/csvs/students_desires.csv")
        d = pd.read_csv(path2)
        merged_df = pd.merge(s, d, on='id')
        filtered_df = merged_df[merged_df['class_name'] == class_name]
        return filtered_df.T.to_dict().values()

    def add_students(self, nw_students):
        try:
            students = []
            for index, row in nw_students.iterrows():
                student = Student(row["id"], row["first_name"], row["last_name"], row["phone"], row["class_name"])
                students.append(student)
            for row in students:
                new_student = {"id": int(row.id), "first_name": row.first_name, "last_name": row.last_name,
                               "phone": row.phone, "class_name": row.class_name}
                self.df = self.df._append(new_student, ignore_index=True)
            self.df.to_csv(self.path, index=False)
            return True
        except Exception as err:
            return False