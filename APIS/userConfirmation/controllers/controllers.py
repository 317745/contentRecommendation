from models.models import *
from app import app

from flask import jsonify

@app.route('/senCode', methods=['POST'])
def verifySendCodePost():
    response = verifySendCode()
    return response