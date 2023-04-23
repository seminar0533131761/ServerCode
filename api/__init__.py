from user_controller import user_controller
from flask import Flask
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="chani113"
    app.register_blueprint(user_controller, url_prefix='/')
    return app