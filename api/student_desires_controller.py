from flask import Blueprint, jsonify
from dal.data_objects.services.students_desires_crud import StudentsDesiresCrud

student_desires_controller=Blueprint('student_desires_controller',__name__)

@student_desires_controller.route("get_by_id/<int:student_id>")
def get_user(student_id):
    student_desires=StudentsDesiresCrud()
    final=student_desires.get_async(student_id)
    return jsonify({"student_id":final.id,"final_answer":final.final_answer})