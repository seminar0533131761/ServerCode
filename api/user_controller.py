

from flask import Blueprint, jsonify
from dal.data_objects.services.user_crud import UserCRUD

user_controller=Blueprint('user_controller',__name__)

@user_controller.route("get_by_id/<int:user_id>")
def get_user(user_id):
    user=UserCRUD()
    final=user.get_async(user_id)
    return jsonify({"user_name":final.user_name,"user_id":final.id})
