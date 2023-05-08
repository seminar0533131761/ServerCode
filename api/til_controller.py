from flask import Blueprint, jsonify
from dal.data_objects.services.til_crod import TilCRUD

til_controller = Blueprint('til_controller', __name__)


@til_controller.route("get_by_id/<int:user_id>")
def get_til(user_id):
    til = TilCRUD()
    final = til.get_async(user_id)
    return jsonify({"_id": final._id,
                    "class_name": final.class_name,
                    "verbal_ability": final.verbal_ability,
                    "logical_ability": final.logical_ability,
                    "final_mark": final.final_mark})
