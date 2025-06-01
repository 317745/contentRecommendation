#API\src\app.py
from flask import Flask
from models.connection import closeConnection

app = Flask(__name__)
app.teardown_appcontext(closeConnection)