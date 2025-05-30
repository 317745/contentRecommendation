#API\src\models\models.py
from src.app import app

@app.route("/")
def hola():
    return 'hola mundo'