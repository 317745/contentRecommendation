#API\src\models\connection.py
import psycopg2
import os
from flask import g

def get_connection():
    if 'db' not in g:
        try: 
            g.db = psycopg2.connect(
                host = os.getenv('HOST'),
                user = os.getenv('USER'),
                password = os.getenv('DBPASSWORD'),
                database = os.getenv('DBNAME'),
                port = os.getenv('PORT')
            )
            print('Se establecio la conexion de manera correcta.')
        except Exception as e:
            print('Sucedio un error:', e)
            g.db = None
    return g.db

def closeConnection(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()