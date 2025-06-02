#API\src\controllers\controllers.py
import requests
import base64
import os
from flask import jsonify

from app import app
from models.models import *

@app.route("/getMedia")
def media():
    response = getMedia()
    if response['ok']:
        return jsonify(response), 200
    else:
        return jsonify(response), 500
        

#Va en song Byeeeeeeeeeeee

def token():

    url = "https://accounts.spotify.com/api/token"
    id_client = os.getenv('ID_CLIENT')
    secret_client = os.getenv('SECRET_CLIENT')
    str = f'{id_client}:{secret_client}'
    strToBytes = str.encode('utf-8')
    b64 = base64.b64encode(strToBytes).decode('utf-8')

    headers = {
        "Authorization": f"Basic {b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data).json()
    token = response['access_token']
    return jsonify(token)

@app.route("/artist")
def getArtist():
    url = "https://api.spotify.com/v1/search"
    headers = { 
        "Authorization": f'Bearer {token().get_json()}'
    }
    params = {
        'q':'turizo',
        'type':'artist'
    }
    response = requests.get(url, headers=headers, params=params).json()
    return response