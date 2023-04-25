# from icrud import ICRUD
# from dal.models.student import Student
# class StudentCrud(ICRUD):
#     def __init__(self):
#         super().__init__()
#         self.students_information = self.my_data_base["information"]
#         self.student_information = {}
#     def create_async(self, obj):
#         pass
#
#     def delete_async(self, id):
#         pass
#
#     def update_async(self, id):
#         pass
#
#     def get_async(self, _id):
#         # id,educator_recommendation,pricipal_recommendation,til_analysis,occupational_counseling
#         tmp_student_information = self.students_information.find_one({"_id": _id})
#         self.student_information = Student(tmp_student_information["_id"], tmp_student_information["first_name"], tmp_student_information["last_name"],tmp_student_information["phone"])
#         return self.student_information
#     #
#     async def get_all_async(self):
#         pass