from flask import Blueprint, jsonify

# from dal.data_objects.services.students_desires_crud import StudentsDesiresCrud

training_controller = Blueprint('training_controller', __name__)


# @training_controller.route("get_by_training/<training_name>")
# def get_students_by_training(training_name):
#     student = StudentsDesiresCrud()
#     final = student.get_students_by_training(training_name)
#     new_lst=[]
#     for student in final:
#         new_lst.append(
#             {"preference1": student.preference1, "preference2": student.preference2, "recommendation1": student.recommendation1, "recommendation2": student.recommendation2,
#              "final_answer": student.final_answer})
#     return jsonify(new_lst)
