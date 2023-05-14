from dal.data_objects.services.basemodel import BaseModel
# from dal.data_objects.services.students_desires_crud import StudentsDesiresCrud
# from dal.data_objects.services.student_crud import StudentCrud
from dal.models.student import Student
import os.path
import pandas as pd


class StudentCrud(BaseModel):
    def __init__(self):
        super().__init__()
        # lst of mongo db collection
        # self.students = self.my_db["students"]
        # lst of instances of class student
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../../api/csvs/students.csv")
        self.df = pd.read_csv(path)
        self.obj_students = []
        self.student = {}

    # def __new__(cls, *args, **kwargs):
    #     return BaseModel.__new__(cls)
    def create_async(self, obj):
        # tmp_user = self.users.insert_one(obj)
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permission)
        # return self.user
        pass

    def delete_async(self, id):
        # tmp_user = self.users.delete_one({"_id": id})
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permission)
        # return self.user
        pass

    def update_async(self, id, permmision):
        # tmp_user = self.users.update_one({"_id": id}, {"permission": permission})
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permission)
        # return self.user
        pass

    def get_async(self, id):
        int_id = int(id)
        row = self.df.loc[self.df['id'] == int_id]
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        self.student = Student(lst[0], lst[1], lst[2], lst[3], lst[4])
        return self.student

    def get_all_async(self):
        pass

    def get_student_by_class_name(self, class_name):
        self.obj_students.extend([Student("214088999", "rivi", "dryman", "0369202", "a1"),
                                  Student("214088999", "chani", "chalamish", "054768322", "a1"),
                                  Student("214088999", "chavi", "chif", "0572322", "a1")])
        specified_class = [i for i in self.obj_students if i.class_name == class_name]
        print(list(specified_class[0].class_name))
        return specified_class
    def get_students_and_desires_by_training(self,tranining):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path1 = os.path.join(my_path, "../../../api/csvs/students.csv")
        s=pd.read_csv(path1)
        path2 = os.path.join(my_path, "../../../api/csvs/students_desires.csv")
        d = pd.read_csv(path2)
        merged_df = pd.merge(s, d, on='id')
        filtered_df = merged_df[merged_df['final_answer'] == tranining]
        # filtered_df.to_csv('filtered_data.csv', index=False)
        # f=pd.read_csv('filtered_data.csv')
        return filtered_df.T.to_dict().values()
    def get_students_and_desires_by_class(self,class_name):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path1 = os.path.join(my_path, "../../../api/csvs/students.csv")
        s = pd.read_csv(path1)
        path2 = os.path.join(my_path, "../../../api/csvs/students_desires.csv")
        d = pd.read_csv(path2)
        merged_df = pd.merge(s, d, on='id')
        filtered_df = merged_df[merged_df['class_name'] == class_name]
        return filtered_df.T.to_dict().values()



s=StudentCrud()
print(s.get_students_and_desires_by_training("math"))