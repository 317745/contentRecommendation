from flask import Flask
from flask_cors import CORS

from models.connection import *

app = Flask(__name__)

@app.before_request
def before_request():
    get_connection()

@app.teardown_appcontext
def teardown_appcontext(exception=None):
    close_connection()

CORS(app)