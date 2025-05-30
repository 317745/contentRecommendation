#API\src\controllers\controllers.py
from src.app import app
from src.models.models import getMedia

@app.route("/")
def media():
    return getMedia()