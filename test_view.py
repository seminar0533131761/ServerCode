from flask_classful import FlaskView,route

class TestView(FlaskView):

    def index(self):
    # http://localhost:5000/
        return "<h1>This is my indexpage</h1>"


    @route('/diffrentname')
    def bsicname(self):
    # customized route
    # http://localhost:5000/diffrentname
        return "<h1>This is my custom route</h1>"
