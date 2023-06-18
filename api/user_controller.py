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
        return jsonify({err: "id must contains only numbers"}), 500
    final = user.get_async(user_id)
    if "Empty" == final.id or final.user_name != user_name:
        return jsonify({"message": "user does not exits"}), 400
    return jsonify({"id": final.id, "permission": final.permission, "name": final.user_name}), 200


@user_controller.route("get_all")
def get_all():
    try:
        final = user.get_all()
        json_list = list(final)
        return jsonify(json_list), 200
    except Exception as error:
        return jsonify({"error": error}), 400


@user_controller.route("update_permission/<_id>", methods=["GET", "PUT"])
def update_permission(_id):
    try:
        answer, is_exit = user.update_permission(_id)
        print(answer, is_exit, "hjkl")
        if is_exit:
            return jsonify({"the server answered": answer}), 200
        return jsonify({"error": answer}), 400
    except Exception as error:
        return jsonify({"error": error}), 400


@user_controller.route("add_user", methods=['POST'])
def add_user():
    try:
        data = request.json
        name = data.get("user_name")
        _id = data.get("user_id")
        if _id.isnumeric() and len(_id) == 9 and name:
            permission = data.get('user_permission')
            if permission == "super" or "regular":
                final = user.add_user(_id, name, permission)
                return jsonify(final), 200
            return jsonify({"error": "not valid permission"}), 400
        return jsonify({"error": "not valid id or name"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400


@user_controller.route("del_user/<_id>", methods=['DELETE'])
def del_user(_id):
    try:
        if _id.isnumeric() and len(_id) == 9:
            final = user.del_user(_id)
            return jsonify({"the server answered ": final}), 200
        else:
            return ({"message": "id is not valid"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400
