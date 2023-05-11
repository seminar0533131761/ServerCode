
# from flask_restful import Resource
class User:
    def __init__(self, id,user_name, permission):
        self.user_name = user_name
        self.id = id
        self.permmision=permission
        