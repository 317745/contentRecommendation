import psycopg2
import os
import time

from dotenv import load_dotenv
from flask import g

load_dotenv()
max_attempts = 5

def get_connection(): 
    if 'db' not in g:
        attempts = 0
        while attempts < max_attempts:
            try:
                g.db = psycopg2.connect(**{
                    'database':os.getenv('DATABASE'),
                    'port':int(os.getenv('PORT')),
                    'user':os.getenv('DBUSER'),
                    'host':os.getenv('HOST'),
                    'password':os.getenv('PASSWORD')
                })
                print('Se establecion la conexion a la DB de manera correcta.')
                break
            except Exception as e:
                attempts += 1
                print(f'''Error al establecer la conexion a la DB.
                Tienes {5 - attempts} intentos mas.''')
                time.sleep(5)
        else:
            raise Exception('Fallo al establecer la conexion a la DB.')
    return g.db

def close_connection():
    db = g.pop('db', None)
    if db is not None:
        print('Cerrando la conexion a la DB.')
        db.close()