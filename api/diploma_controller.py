import pandas as pd
from flask import Blueprint, jsonify, request

from dal.data_objects.services.diploma_crud import DiplomaCRUD

diploma_controller = Blueprint('diploma_controller', __name__)
diploma = DiplomaCRUD()


@diploma_controller.route("get_by_id/<int:diploma_id>")
def get_diploma(diploma_id):
    final = diploma.get(diploma_id)
    return jsonify({"diploma_id": final.id, "math": final.math, "torah": final.torah, "grammer": final.grammar,
                    "english": final.english, "sciences": final.sciences, "history": final.history,
                    "trend": final.trend})


@diploma_controller.route("add_diploma", methods=['POST'])
def process_upload():
    file = request.files['diploma_file']
    # Read the CSV file using pandas
    nw_students_diploma = pd.read_csv(file)
    if diploma.add_diploma(nw_students_diploma):
        return jsonify({'message': 'the diploma file was uploaded and processed'}), 200
    return jsonify({"message": "wrong details"}), 400
