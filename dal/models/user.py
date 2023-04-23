
# from flask_restful import Resource
class User:
    def __init__(self, user_name,id, permission):
        self.user_name = user_name
        self.id = id
        self.permmision=permission
        