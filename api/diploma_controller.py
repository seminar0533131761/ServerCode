
from flask import Blueprint, jsonify

from dal.data_objects.services.diploma_crud import DiplomaCRUD

diploma_controller=Blueprint('diploma_controller', __name__)

@diploma_controller.route("get_by_id/<int:diploma_id>")
def get_diploma(diploma_id):
    diploma = DiplomaCRUD()
    final = diploma.get_async(diploma_id)
    return jsonify({"diploma_id":final.id,"math":final.math, "torah":final.torah, "grammer":final.grammar,"english":final.english,"sciences":final.sciences,"history":final.history,"trend":final.trend})