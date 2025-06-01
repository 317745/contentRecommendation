#API\src\models\models.py
from models.connection import get_connection
from flask import jsonify

def getMedia():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM moviespreference.media')
        result = {
            'ok': True,
            'data': cursor.fetchall()[0]
        }
    except Exception as e:
        result = {
            'ok': False,
            'exception': e
        }
    return result
        
