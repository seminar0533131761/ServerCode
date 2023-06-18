from flask import Blueprint, jsonify, request
from dal.data_objects.services.til_crud import TilCRUD
import pandas as pd

til_controller = Blueprint('til_controller', __name__)
til = TilCRUD()

@til_controller.route("get_by_id/<int:student_id>")
def get_til(student_id):
    final = til.get(student_id)
    print(final.class_name)
    return jsonify({"_id": final._id,
                    "class_name": final.class_name,
                    "verbal_ability": final.verbal_ability,
                    "logical_ability": final.logical_ability,
                    "final_mark": final.final_mark})


@til_controller.route("add_tils_results", methods=['POST'])
def process_upload():
    file = request.files['tils_file']
    # Read the CSV file using pandas
    nw_til_result = pd.read_csv(file)
    print(nw_til_result)
    til.add_students_tiles(nw_til_result)
    response_data = {'message': 'the til file was uploaded and processed'}
    return jsonify(response_data)
