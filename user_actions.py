from flask import jsonify
import pymongo
from complete_rest_actions import CompleteRestAction
mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]
from flask_restful import Resource,Api
# api=Api(app)
# app = flask.Flask(__name__)
class UsersActions(Resource):
    # @app.route('/',methods =  ['GET'])
    def get_by_id(self,user_id):
        user=users.find_one({"_id":user_id})
        return user
        # return jsonify({"name":g})
    def post_user(self):
        pass
    def delete_by_id(self):
        pass
    def put_by_id(self):
        pass