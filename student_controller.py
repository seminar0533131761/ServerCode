from user import User
import pymongo
import flask
from flask_cors import CORS,cross_origin
from flask_restful import Api
from user_actions import UsersActions
import json
from db_manger import DBManger

mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]


app = flask.Flask(__name__)
CORS(app)
# @app.route('/')
def hello():
    response=flask.jsonify()
    response.headers.add("Access-Control-Allow-Origin", "*")
# def is_user_exist(id):
#     return 
# def create_user(name, id):
#     users.insert_many([{"user_name": "chani", "_id": "214088999"}])

# @app.route('/users/<user_id>', methods=['GET'])
# def get_user_by_id(user_id):
#     user=users.find_one({"id":214088999})
#     if user!=None:
#         return flask.jsonify(user)
#     return flask.jsonify({"message": "User not found"}), 404
api=Api(app)
base_url='127.0.0.1'
@app.route("/user_actions/<int:user_id>/<string:user_name>", methods=['GET'])
def get_by_id(user_id,user_name):
    correct_id=users.find_one({"_id":user_id})
    correct_user_name=users.find_one({"user_name":user_name})
    if(correct_id==correct_user_name):
        return flask.jsonify(correct_id)
    return flask.jsonify({"error": "404 user not found"})
@app.route("/user_actions/<string:user_id>", methods=['DELETE'])
def delete_by_id(user_id):
    # try:
        id=users.delete_one({"_id":user_id})
        if(id):
            response= f"User with password={user_id} was removed succesfully" 
            return flask.jsonify({"the server responded":response}), 200
    # response.headers.add("Access-Control-Allow-Origin", "*")
    # except HTTPException as error:
    #     return error(os.version)
@app.route("/user_actions", methods=['POST'])   
def create_user():
    user = flask.request.get_json()
    users.insert_one(user)
    added_user=users.find_one({"_id":user["_id"]})
    response=flask.jsonify(added_user)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    # return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
@app.route("/user_actions/<string:user_id>", methods=['PUT'])
def update_permission(user_id):
    # user_permission=permission["permission"]
    data = flask.request.json
    new_permission=data.get("permission")
    new_query={"$set":{"2":new_permission}}
    user=users.find_one({"_id":user_id})
    if(user!=None):
        users.update_one({"_id":user_id},new_query)
        response=flask.jsonify({f"User with id={user_id} was updated": new_permission})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    return flask.jsonify({"Message": f"User with id={user_id} does not exist!"}), 404
@app.route("/add_students/", methods=['POST'])
def add_students():
    data = flask.request.files
    return flask.jsonify({"hee":"only connection try"})
#api.add_resource(UsersActions,"/users_actions/<string:user_id>/<string:user_name>")
@app.route("/suceess")
def get_one():
    user=UsersActions()
    final=user.get_by_id("1")
    return flask.jsonify({"final":"hrk"})
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)