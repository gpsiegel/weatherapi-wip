from flask import Flask
from ddb_scan import ddb_return

application = Flask(__name__)

api_result = ddb_return()

@application.route('/')
def index():
    return api_result

if __name__ == '__main__':
    application.run(host="0.0.0.0")