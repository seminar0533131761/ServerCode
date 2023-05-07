from flask import Blueprint, jsonify

from dal.data_objects.services.student_crud import StudentCrud

class_controller = Blueprint('class_controller', __name__)


@class_controller.route("get_by_class_name/<class_name>")
def get_students_by_class(class_name):
    student = StudentCrud()
    final = student.get_student_by_class_name(class_name)
    return jsonify(final)
