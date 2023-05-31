import pandas as pd
from flask import Blueprint, jsonify, request
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


@student_desires_controller.route("get_final_answer_by_class/<class_name>")
def get_final_answer_by_class(class_name):
    student_desires = StudentsDesiresCrud()
    final = student_desires.get_final_answer_by_class_name(class_name)
    new_lst = []
    for desire in final:
        new_lst.append(
            {"final_answer": desire.final_answer})
    return jsonify(new_lst)


@student_desires_controller.route("get_final_answer_by_training/<training_name>")
def get_final_answer_by_training(training_name):
    student_desires = StudentsDesiresCrud()
    final = student_desires.get_final_answer_by_training(training_name)
    new_lst = []
    for desire in final:
        new_lst.append(
            {"student id": desire.id, "final_answer": desire.final_answer})
    return jsonify(new_lst)
@student_desires_controller.route("add_students_desires", methods=['POST'])
def process_upload():
    file = request.files['students_desires_file']
    # Read the CSV file using pandas
    nw_students_desires = pd.read_csv(file)
    print(nw_students_desires)
    student_desires = StudentsDesiresCrud()
    student_desires.add_students_desires(nw_students_desires)
    response_data = {'message': 'the student desires file was uploaded and processed'}
    return jsonify(response_data)