from flask import Flask
from flask import request
application = Flask(__name__)

@application.route("/")
def hello():
    response = request.headers
    return response

if __name__ == "__main__":
    application.run()
