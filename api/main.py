from api import create_app
from flask_cors import CORS

app = create_app()
CORS(app)


def check():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
