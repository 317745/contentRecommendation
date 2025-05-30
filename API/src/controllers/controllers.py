from src.app import app
from flask import render_template

@app.route("/")
def hola():
    return render_template('index.html')