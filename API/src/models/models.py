#API\src\models\models.py
from src.models.connection import get_connection

def getMedia():
    result = {}
    try:
        conn = get_connection()
        if conn is None:
            raise Exception('Error al establecer la conexion vv.')
        else: 
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM moviespreference.media')
            result['ok'] = True
            result['data'] = cursor.fetchall()
    except Exception as e:
        result['ok'] = False
        result['exception'] = e
    return result
        
