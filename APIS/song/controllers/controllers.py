from app import app
from models.models import *

from flask import jsonify

@app.route('/artist/<string:name>')
def artistByName(name):
    data = getArtist(name)
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500
