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
