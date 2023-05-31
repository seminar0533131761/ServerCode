import os
from http.client import HTTPException
from flask import Blueprint, jsonify, request
from dal.data_objects.services.user_crud import UserCRUD

user_controller = Blueprint('user_controller', __name__)
user = UserCRUD()


@user_controller.route("get_by_id/<user_id>/<user_name>")
def get_user(user_id, user_name):
    try:
        user_id = int(user_id)
    except ValueError as err:
        return jsonify({"message": "id must contains only numbers"}), 500
    final = user.get_async(user_id)
    if "Empty" == final.id or final.user_name != user_name:
        return jsonify({"message": "user does not exits"}), 400
    return jsonify({"id": final.id, "permission": final.permission, "name": final.user_name}), 200


@user_controller.route("get_all")
def get_all():
    try:
        final = user.get_all()
        json_list = list(final)
        return jsonify(json_list)
    except Exception as error:
        return jsonify({"error": error})


@user_controller.route("update_permission/<_id>", methods=["GET", "PUT"])
def update_permission(_id):
    try:
        final = user.update_permission(_id)
        return jsonify({"the server answered": final})
    except Exception as error:
        return jsonify({"error": error})


@user_controller.route("add_user", methods=['POST'])
def add_user():
    try:
        data = request.json
        name = data.get("user_name")
        _id = data.get("user_id")
        permission = data.get('user_permission')
        final = user.add_user(_id, name, permission)
        return jsonify(final)
    except Exception as error:
        return jsonify({"error": error})


@user_controller.route("del_user/<_id>", methods=['DELETE'])
def del_user(_id):
    try:
        final = user.del_user(_id)
        return jsonify({"the server answered ": final})
    except Exception as error:
        return jsonify({"error": error})
