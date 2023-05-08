from flask import Blueprint, jsonify

from dal.data_objects.services.student_crud import StudentCrud

class_controller = Blueprint('class_controller', __name__)


@class_controller.route("get_by_class_name/<class_name>")
def get_students_by_class(class_name):
    student = StudentCrud()
    final = student.get_student_by_class_name(class_name)
    new_lst=[]
    for student in final:
        new_lst.append(
            {"first_name": student.first_name, "last_name": student.last_name, "student_id": student.id, "phone": student.phone,
             "class": student.class_name})
    return jsonify(new_lst)
