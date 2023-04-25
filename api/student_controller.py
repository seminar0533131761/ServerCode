from flask import Blueprint, jsonify
from dal.data_objects.services.student_crud import StudentCrud

student_controller=Blueprint('student_controller',__name__)

@student_controller.route("get_by_id/<int:student_id>")
def get_student(student_id):
    student=StudentCrud()
    final=student.get_async(student_id)
    return jsonify({"first_name":final.first_name,"last_name":final.last_name,"student_id":final.id,"student_phone":final.phone})