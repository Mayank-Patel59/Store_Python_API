import json
from bson import ObjectId
from bson.json_util import dumps
from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

mongo = MongoClient("mongodb://localhost:27017/Movies")


@app.route('/Get_Movies')
def users():
    users = mongo.Movies.MovieInformation.find()
    response = dumps(users)
    # return render_template('Movies Information.html', response = response)
    return response


@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': "Not Found" + request.url}

    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
