from api import training_controller
from api.diploma_controller import diploma_controller
# from api.information_controller import information_controller
from api.class_controller import class_controller
from api.information_controller import information_controller
from api.til_controller import til_controller
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
    app.register_blueprint(information_controller,url_prefix='/information_controller/')
    app.register_blueprint(til_controller,url_prefix='/til_controller/')
    app.register_blueprint(class_controller, url_prefix='/class_controller/')
    app.register_blueprint(training_controller,url_prefix='/training_controller')
    return app