from icrud import ICRUD
from dal.models.student import Student
class StudentCrud(ICRUD):
    def __init__(self):
        super().__init__()
        self.students = self.my_data_base["students"]
        self.student = {}
    def create_async(self, obj):
        # tmp_user = self.users.insert_one(obj)
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permmision)
        # return self.user
        pass

    def delete_async(self, id):
        # tmp_user = self.users.delete_one({"_id": id})
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permmision)
        # return self.user
        pass

    def update_async(self, id, permmision):
        # tmp_user = self.users.update_one({"_id": id}, {"permmision": permmision})
        # self.user = User(tmp_user.user_name, tmp_user._id, tmp_user.permmision)
        # return self.user
        pass

    def get_async(self, _id):
        tmp_student = self.students.find_one({"_id": _id})
        self.student = Student(tmp_student["_id"], tmp_student["first_name"], tmp_student["last_name"],tmp_student["phone"])
        return self.student
    #
    async def get_all_async(self):
        # return self.users
        pass