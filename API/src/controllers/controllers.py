from src.app import app

@app.route("/")
def hola():
    return 'hola mundo'