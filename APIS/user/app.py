from flask import Flask
from flask_cors import CORS
from models.connection import *

app = Flask(__name__)
app.teardown_appcontext(closeConnection)
CORS(app)