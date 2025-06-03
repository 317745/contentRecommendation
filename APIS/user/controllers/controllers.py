#APIS\user\controllers\controllers.py
from app import app
from models.models import *

from flask import jsonify

@app.route('/getCountrys')
def getCountrys():
    data = countrys()
    if data['ok'] == True:
        return jsonify(data), 200
    else: 
        return jsonify(data), 500

@app.route('/countryById/<string:name>')
def getCountryById(name):
    data = countryByName(name)
    if data['ok'] == True:
        return jsonify(data), 200
    else: 
        return jsonify(data), 500

@app.route('/createUser', methods=['POST'])
def postUser():
    data = createUser()
    if data['ok'] == True:
        return jsonify(data), 200
    else:
        return jsonify(data), 500