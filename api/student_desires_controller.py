from flask import Blueprint, jsonify
from dal.data_objects.services.students_desires_crud import StudentsDesiresCrud

student_desires_controller = Blueprint('student_desires_controller', __name__)


@student_desires_controller.route("get_by_id/<int:student_id>")
def get_user(student_id):
    student_desires = StudentsDesiresCrud()
    final = student_desires.get_async(student_id)
    return jsonify(
        {"student_id": final.id, "student_preference1": final.preference1, "student_preference2": final.preference2,
         "recommendation_on_option_1": final.recommendation1, "recommendation_on_option_2": final.recommendation2,
         "final_answer": final.final_answer})


@student_desires_controller.route("get_final_answer/<class_name>")
def get_final_answer(class_name):
    student_desires = StudentsDesiresCrud()
    final = student_desires.get_final_answer_by_class_name(class_name)
    new_lst = []
    for desire in final:
        new_lst.append(
            {"final_answer": desire.final_answer})
    return jsonify(new_lst)
    # return jsonify({"hi":"there"})
