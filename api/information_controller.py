from flask import Blueprint, jsonify
# from dal.data_objects.services.information_crud import InformationCrud
from dal.data_objects.services.information_crud import InformationCrud
information_controller = Blueprint('information_controller', __name__)



@information_controller.route("get_by_id/<int:user_id>")
def get_information(user_id):
    information = InformationCrud()
    final = information.get_async(user_id)
    return jsonify({"id":final.id,
                    "educator_recommendation": final.educator_recommendation,
                    "pricipal_recommendation": final.pricipal_recommendation,
                    "til_analysis": final.til_analysis,
                    "occupational_counseling": final.occupational_counseling})
