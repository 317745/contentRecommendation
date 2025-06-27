from app import app
from models.models import *

from flask import jsonify

@app.route('/artist/<string:id>')
def artistByID(id):
    data = getArtistByID(id)
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500
    
@app.route('/artistName/<string:name>')
def artistByName(name):
    data = getArtistByName(name)
    if data['ok']:
        return jsonify(data), 200
    else:
        return jsonify(data), 500