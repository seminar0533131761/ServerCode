import os
from http.client import HTTPException

from flask import Blueprint, jsonify, request
from dal.data_objects.services.user_crud import UserCRUD

user_controller = Blueprint('user_controller', __name__)


@user_controller.route("get_by_id/<user_id>")
def get_user(user_id):
    user = UserCRUD()
    final = user.get_async(user_id)
    return jsonify({"id": final.id, "permission": final.permission, "name": final.user_name})


@user_controller.route("get_all")
def get_all():
    user = UserCRUD()
    final = user.get_all()
    json_list = list(final)
    print(json_list)
    return jsonify(json_list)


@user_controller.route("update_permission/<int:_id>", methods=["GET", "PUT"])
def update_permission(_id):
    user = UserCRUD()
    final = user.update_permission(_id)
    return jsonify({"the server answered":final})


@user_controller.route("add_user", methods=['POST'])
def add_user():
    data = request.json
    name=data.get("user_name")
    print(name)
    _id = data.get("user_id")
    print(_id)
    permission = data.get('user_permission')
    user = UserCRUD()
    final = user.add_user(_id,name,permission)
    # json_list = list(final)
    return jsonify(final)


@user_controller.route("del_user/<int:_id>", methods=['DELETE'])
def del_user(_id):
    try:
        user = UserCRUD()
        final = user.del_user(_id)
        return jsonify({"the server answered ": final})
    except HTTPException as error:
        return error(os.version)



