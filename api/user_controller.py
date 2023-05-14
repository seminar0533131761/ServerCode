from flask import Blueprint, jsonify
from dal.data_objects.services.user_crud import UserCRUD

user_controller = Blueprint('user_controller', __name__)


@user_controller.route("get_by_id/<int:user_id>")
def get_user(user_id):
    user = UserCRUD()
    final = user.get_async(user_id)
    return jsonify({"id": final.id, "permission": final.permission, "name": final.user_name})


@user_controller.route("get_all")
def get_all():
    user = UserCRUD()
    final = user.get_all()
    json_list = list(final)
    return jsonify(json_list)


@user_controller.route("update_permission/<int:_id>")
def update_permission(_id):
    user = UserCRUD()
    final = user.update_permission()
    json_list = list(final)
    return jsonify(json_list)

@user_controller.route("add_user/<int:_id>")
def update_permission(_id):
    user = UserCRUD()
    final = user.update_permission()
    json_list = list(final)
    return jsonify(json_list)
