from flask import Blueprint, jsonify, request
from dal.data_objects.services.student_crud import StudentCrud
import pandas as pd

student_controller = Blueprint('student_controller', __name__)
student = StudentCrud()


@student_controller.route("get_by_id/<student_id>")
def get_student(student_id):
    try:
        student_id = int(student_id)
    except Exception as err:
        return jsonify({"message": "id must contains only numbers"}), 400
    final = student.get(student_id)
    if "Empty" == final.id:
        return jsonify({"message": "student does not exits"}), 400
    return jsonify(
        {"first_name": final.first_name, "last_name": final.last_name, "student_id": final.id, "phone": final.phone,
         "class": final.class_name}), 200


@student_controller.route("get_all_students")
def get_all_students():
    """the students will be given only by class or training"""
    training_name = request.args.get('training_name')
    class_name = request.args.get('class_name')
    if training_name:
        final = student.get_students_and_desires_by_training(training_name)
        json_list = list(final)
        if not json_list:
            return jsonify({"message": "the wanted training does not exits"}), 400
        return jsonify(json_list), 200
    if class_name:
        final = student.get_students_and_desires_by_class(class_name)
        json_list = list(final)
        if not json_list:
            return jsonify({"message": "class does not exits"}), 400
        return jsonify(json_list), 200
    return jsonify({"message": "not correct class name or training name"}), 400


# not in use to del
@student_controller.route("get_by_training/<training_name>")
def get_student_by_training(training_name):
    final = student.get_students_and_desires_by_training(training_name)
    json_list = list(final)
    if not json_list:
        return jsonify({"message": "class does not exits"}), 400
    return jsonify(json_list), 200


#  not in use to del
@student_controller.route("get_by_class/<class_name>")
def get_student_by_class(class_name):
    final = student.get_students_and_desires_by_class(class_name)
    json_list = list(final)
    if not json_list:
        return jsonify({"message": "class does not exits"}), 40
    return jsonify(json_list)


@student_controller.route("add_students", methods=['POST'])
def process_upload():
    print(request.files)
    file = request.files['students_file']
    print(file)
    # Read the CSV file using pandas
    nw_students = pd.read_csv(file)
    if student.add_students(nw_students):
        return jsonify({'message': 'the student file was uploaded and processed'}), 200
    return jsonify({"message": "wrong details"}), 400
