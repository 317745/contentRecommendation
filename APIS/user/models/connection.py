import os
import time
import psycopg2

from flask import g
from dotenv import load_dotenv

load_dotenv()

max_attempts = 5

def get_connection():
    if 'db' not in g:
        attempts = 0
        while attempts < max_attempts:
            try: 
                g.db = psycopg2.connect(**{
                    'database':os.getenv('DATABASE'),
                    'user':os.getenv('DBUSER'),
                    'password':os.getenv('PASSWORD'),
                    'host':os.getenv('HOST'),
                    'port':int(os.getenv('PORT'))
                })
                print('Se establecio la conexion a la DB de manera correcta.')
                break
            except Exception as e:
                attempts += 1
                print(f'''Error al establecer las conexion a la DB.
                Tienes {5 - attempts} intentos mas.''')
                time.sleep(5)
        else:
            raise Exception('Fallo al establecer la conexion a la DB.')
    return g.db

def closeConnection(e=None):
    db = g.pop('db', None)
    if db is not None:
        print('Cerrando la conexion a la DB.')
        db.close()