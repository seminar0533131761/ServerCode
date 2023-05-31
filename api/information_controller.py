import pandas as pd
from flask import Blueprint, jsonify, request
from dal.data_objects.services.information_crud import InformationCrud

information_controller = Blueprint('information_controller', __name__)


@information_controller.route("get_by_id/<int:user_id>")
def get_information(user_id):
    information = InformationCrud()
    final = information.get_async(user_id)
    return jsonify({"id": final.id,
                    "educator_recommendation": final.educator_recommendation,
                    "principal_recommendation": final.pricipal_recommendation,
                    "til_analysis": final.til_analysis,
                    "occupational_counseling": final.occupational})


# @information_controller.route("add_user_information", methods=['POST'])
# def add_user_information():
#     data = request.json
#     name = data.get("information_file")
#     print(name)
#     _id = data.get("user_id")
#     print(_id)
#     permission = data.get('user_permission')
#     information = InformationCrud()
#     final = information.add_user_information(_id, name, permission)
#     # json_list = list(final)
#     return jsonify(final)
@information_controller.route("add_students_information", methods=['POST'])
def process_upload():
    file = request.files['information_file']
    # Read the CSV file using pandas
    nw_students_information = pd.read_csv(file)
    information = InformationCrud()
    success=information.add_students_information(nw_students_information)
    if success:
        return jsonify({'message': 'the information file was uploaded and processed'}), 200
    return jsonify({"message": "wrong details"}),400
