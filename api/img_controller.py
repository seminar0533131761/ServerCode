from flask import Flask, send_file, make_response, Blueprint
from imgs import get_imgs

img_controller = Blueprint('img_controller', __name__)


@img_controller.route('/school')
def display_picture():
    picture_path = get_imgs.get_the_front_img()
    response = make_response(send_file(picture_path, mimetype='image/jpeg', as_attachment=True))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
