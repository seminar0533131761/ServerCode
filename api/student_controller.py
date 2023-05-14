from flask import Blueprint, jsonify
from dal.data_objects.services.student_crud import StudentCrud

student_controller = Blueprint('student_controller', __name__)


@student_controller.route("get_by_id/<int:student_id>")
def get_student(student_id):
    student = StudentCrud()
    final = student.get_async(student_id)
    return jsonify(
        {"first_name": final.first_name, "last_name": final.last_name, "student_id": final.id, "phone": final.phone,
         "class": final.class_name})


@student_controller.route("get_by_class_name/<class_name>")
def get_students_by_class(class_name):
    student = StudentCrud()
    final = student.get_student_by_class_name(class_name)
    new_lst = []
    for student in final:
        new_lst.append(
            {"first_name": student.first_name, "last_name": student.last_name, "student_id": student.id,
             "phone": student.phone,
             "class": student.class_name})
    return jsonify(new_lst)




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
    json_list=list(final)
    # return jsonify(json_lst)
    return jsonify(json_list)
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
    json_list=list(final)
    # return jsonify(json_lst)
    return jsonify(json_list)


