import os


def get_the_front_img():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'the_school.jpg')
    return path
