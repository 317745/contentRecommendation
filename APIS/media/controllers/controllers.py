#API\src\controllers\controllers.py
from app import app
from models.models import getMedia

@app.route("/getMedia")
def media():
    result = getMedia()
    if result['ok']:
        return result
    else:
        e = result['exception']
        raise Exception(f'Ocurrio un error: {e}')