from flask import Flask
from models.connection import *

app = Flask(__name__)
app.teardown_appcontext(closeConnection)