import psycopg2
from flask import g
from config import ConfigDB

def connection():
    if 'db' not in g:
        try: 
            g.db = psycopg2.connect(
                host=ConfigDB.HOST,
                user=ConfigDB.USER,
                password=ConfigDB.PASSWORD,
                database=ConfigDB.NAME,
                port=ConfigDB.PORT
            )
            print('Se establecio la conexion de manera correcta.')
        except Exception as e:
            print('Sucedio un error:', e)
    return g.db

def closeConnection(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()