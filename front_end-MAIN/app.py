from flask import Flask
from ddb_scan import ddb_return

app = Flask(__name__)

api_result = ddb_return()

@app.route('/')
def index():
    return api_result

if __name__ == '__main__':
    app.run(host="0.0.0.0")