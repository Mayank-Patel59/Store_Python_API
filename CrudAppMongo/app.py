"""
Created on Thursday Sep 17 00:06:08 2020

@author: Mayank patel
"""

# Get Libraries Import here
import json
from bson import ObjectId
from bson.json_util import dumps
from pymongo import MongoClient             # Pymongo API of Mongodb
from flask import Flask, request, jsonify

app = Flask(__name__)

mongo = MongoClient("mongodb://localhost:27017/Movies")  # MongoDb Connection / Database Name


# Get_Movies Json Data From Mongodb
@app.route('/Get_Movies')       # Get DB Data through End Point route
def users():
    users = mongo.Movies.MovieInformation.find()
    response = dumps(users)
    return response


# Exception Handling for Errors
@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': "Not Found" + request.url}

    response = jsonify(message)
    response.status_code = 404

    return response


"""Main Function,
    Port and host details set here"""
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
