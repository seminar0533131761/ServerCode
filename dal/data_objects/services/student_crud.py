from dal.data_objects.services.icrud import ICRUD
from dal.models.student import Student


class StudentCrud(ICRUD):
    def __init__(self):
        super().__init__()
        # lst of mongo db collection
        self.students = self.my_data_base["students"]
        # lst of instances of class student
        self.obj_students = []
        self.student = {}

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

    def get_async(self, _id):
        # tmp_student = self.students.find_one({"_id": 214088999})
        # self.student = Student(tmp_student["_id"], tmp_student["first_name"], tmp_student["last_name"],tmp_student["phone"])
        self.student = Student("21", "chani", "orthal", "054648", "a1")
        return self.student

    def get_all_async(self):
        pass

    def get_student_by_class_name(self, class_name):
        self.obj_students.extend([Student("1", "rivi", "dryman", "0369202", "a1"),
                                  Student("2", "chani", "chalamish", "054768322", "a1"),
                                  Student("3", "chavi", "chif", "0572322", "a2")])
        filtered = filter(lambda class_n: class_n == class_name, self.obj_students)
        return list(filtered)