
# from flask_restful import Resource
class User:
    def __init__(self, user_name,_id, permission):
        self.user_name = user_name
        self._id = _id
        self.permmision=permission
        