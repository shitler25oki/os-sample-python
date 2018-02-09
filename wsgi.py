from flask import Flask
from flask import request
application = Flask(__name__)

@application.route("/")
def hello():
    return 'headers: %s' % request.headers

if __name__ == "__main__":
    application.run()
