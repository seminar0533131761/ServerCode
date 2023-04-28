from api.diploma_controller import diploma_controller
from api.user_controller import user_controller
from api.student_controller import student_controller
from flask import Flask
from api.student_desires_controller import student_desires_controller
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="chani113"
    app.register_blueprint(user_controller, url_prefix='/user_controller/')
    app.register_blueprint(student_controller, url_prefix='/student_controller/')
    app.register_blueprint(student_desires_controller, url_prefix='/student_desires_controller/')
    app.register_blueprint(diploma_controller,url_prefix='/diploma_controller/')
    return app