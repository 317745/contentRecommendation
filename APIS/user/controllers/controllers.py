#APIS\user\controllers\controllers.py
from app import app
from models.models import *

from flask import jsonify

@app.route('/getCountrys')
def getCountrys():
    data = countrys()
    if data['ok']:
        return jsonify(data), 200
    else: 
        return jsonify(data), 500
    
@app.route('/usernameEmailConfirmation', methods=['POST'])
def usernameEmailCode():
    data = confirmUserNameEmail()
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500
    
@app.route('/createUser', methods=['POST'])
def postUser():
    data = createUser()
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500

@app.route('/getUsers', methods=['GET'])
def getAllUsers():
    data = getUsers()
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500

@app.route('/getUserId/<string:id>', methods=['GET'])
def getUserID(id):
    try:
        int(id)
    except ValueError:
        return jsonify({
            'ok': False,
            'data': 'Invalid ID: Must be a number.',
        }), 400

    data = getUserById(id)
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500

@app.route('/login', methods=['POST'])
def loginControllers():
    data = login()
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500