#API\src\controllers\controllers.py
from app import app
from models.models import getMedia

@app.route("/getMedia")
def media():
    if getMedia()['ok'] == True:
        return getMedia()
    else:
        e = getMedia()['exception']
        raise Exception(f'Ocurrio un error: {e}')
    return 