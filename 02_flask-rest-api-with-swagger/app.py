from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/employee')
def get(self):
    result = {'employee': 'shine test'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()