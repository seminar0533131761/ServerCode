
import pymongo
import flask
from flask_cors import CORS,cross_origin
from flask_restful import Api
# from user_actions import UsersActions
import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager 
from test_view import TestView
from dal.data_objects.user_crud import UserCRUD
import asyncio
mongo_client = pymongo.MongoClient("mongodb+srv://chani:registration@database.ukagb6v.mongodb.net/?retryWrites=true&w=majority")
my_data_base = mongo_client["Registration"]
users = my_data_base["users"]


app = flask.Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)
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
    data = flask.request.files['file']
    # data.save(secure_filename(data.filename))
    return flask.jsonify({"hee":"only connection try"})
#api.add_resource(UsersActions,"/users_actions/<string:user_id>/<string:user_name>")

@app.route("/get_all_users")
def get_all():
    user=UserCRUD()
    # asyncio.run(user.get_async("1"))
    # loop = asyncio.get_event_loop()
    # res=loop.run_until_complete(user.get_async("1"))
    # loop.close()
    # user_dict = {k: getattr(user, k) for k in ['_id', 'user_name', 'permission']}
    # # print(json.dumps(user_dict, indent=2))
    final=user.get_async("1")
    return flask.jsonify({"user name":final.user_name})
# @app.route("del/<string:user_id>",method=['DELETE'])
# def delet():
#     user=UserCRUD()
    # final=user.
    
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@app.route('/token', methods=["POST"])
def create_token():
    user_name=request.json.get("user_name",None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test" or user_name!="test":
        return {"message": "Wrong email or password or user name"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response
    # return jsonify({"hi":"success"})

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body
TestView.register(app,route_base = '/')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)