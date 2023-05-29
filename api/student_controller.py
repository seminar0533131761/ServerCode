import os

from flask import Blueprint, jsonify, request
from dal.data_objects.services.student_crud import StudentCrud
import pandas as pd

student_controller = Blueprint('student_controller', __name__)


@student_controller.route("get_by_id/<student_id>")
def get_student(student_id):
    try:
        student_id = int(student_id)
    except Exception as err:
        return jsonify({"message": "id must contains only numbers"}), 400
    student = StudentCrud()
    final = student.get_async(student_id)
    print(final)
    print(final.id)
    if "Empty" == final.id:
        return jsonify({"message": "student does not exits"}), 400
    return jsonify(
        {"first_name": final.first_name, "last_name": final.last_name, "student_id": final.id, "phone": final.phone,
         "class": final.class_name}), 200

#
# @student_controller.route("get_by_class_name/<class_name>")
# def get_students_by_class(class_name):
#     student = StudentCrud()
#     final = student.get_student_by_class_name(class_name)
#     new_lst = []
#     for student in final:
#         new_lst.append(
#             {"first_name": student.first_name, "last_name": student.last_name, "student_id": student.id,
#              "phone": student.phone,
#              "class": student.class_name})
#     print(new_lst)
#     # if new_lst.:
#     #     print("ghj")
#     #     return jsonify({"message": "class does not exits"}), 400
#     return jsonify(new_lst), 200


@student_controller.route("get_by_training/<training_name>")
def get_student_by_training(training_name):
    student = StudentCrud()
    final = student.get_students_and_desires_by_training(training_name)
    # json_lst=[]
    # for student in final:
    #     json_lst.append(
    #         {"first_name": student.first_name, "last_name": student.last_name, "student_id": student.id,
    #          "phone": student.phone,
    #          "class": student.class_name})
    json_list = list(final)
    if not json_list:
        return jsonify({"message": "class does not exits"}), 400
    return jsonify(json_list), 200


@student_controller.route("get_by_class/<class_name>")
def get_student_by_class(class_name):
    student = StudentCrud()
    final = student.get_students_and_desires_by_class(class_name)
    # json_lst=[]
    # for student in final:
    #     json_lst.append(
    #         {"first_name": student.first_name, "last_name": student.last_name, "student_id": student.id,
    #          "phone": student.phone,
    #          "class": student.class_name})
    json_list = list(final)
    if not json_list:
        return jsonify({"message": "class does not exits"}), 400
    # return jsonify(json_lst)
    return jsonify(json_list)


@student_controller.route("/add_students", methods=['POST'])
def process_upload():
    print("fghjk")
    file = request.files['file']
    # Read the CSV file using pandas
    nw_students = pd.read_csv(file)
    student = StudentCrud()
    student.create_async(nw_students)

    # Return a response (optional)
    response_data = {'message': 'File uploaded and processed'}
    return jsonify(response_data)
