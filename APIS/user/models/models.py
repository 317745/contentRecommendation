#APIS\user\models\models.py
from middlewares.countrByName import *
from models.connection import *

import requests

from flask import jsonify, request
from datetime import datetime
from psycopg2.extras import RealDictCursor

def countrys():
    url = 'https://country.io/names.json'
    
    try:
        data = requests.get(url).json()
        response = {
            'ok': True,
            'data': data
        }
    except Exception as e:
        response = {
            'ok': False,
            'exception': str(e)
        }

def confirmUserNameEmail():
    try: 
        username = request.json.get('username')
        email = request.json.get('email')
        
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT username, email FROM users WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()
        print(user)
        if user is not None:
            if user['username'] == username:
                return {
                    'ok': False,
                    'data': f"There's another user with the username {username}"
                }
            elif user['email'] == email:
                return {
                    'ok': False,
                    'data': f"There's another user with the email {email}"
                }
        return {
            'ok': True,
            'data': f"The username {username} and email {email} is available"
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }
    
def createUser():
    try:
        first_name = request.json.get('first_name').title()
        last_name = request.json.get('last_name').title()
        date_of_birth = request.json.get('date_of_birth')
        city_of_birth = request.json.get('city_of_birth')
        city_of_residence = request.json.get('city_of_residence')
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        country = request.json.get('country')

        responseCountry = countryByName(country)

        if responseCountry['ok'] == False:
            return responseCountry

        country = responseCountry['country']
        active = False
        created_at = datetime.now()

        requiredValues = ['first_name', 'last_name', 'date_of_birth', 'city_of_birth', 'city_of_residence', 'username', 'email', 'password', 'country']
        missedValues = [i.replace("_", " ").capitalize() for i in requiredValues if not request.json.get(i)]

        if missedValues:
            return {
                'ok': False,
                'data': f'The value/s: {", ".join(missedValues)} are required.'
            }

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('''INSERT INTO users (
        first_name, last_name, date_of_birth, 
        city_of_birth, city_of_residence, username, 
        email, password, country, active, created_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )''', (
            first_name, last_name, date_of_birth, 
            city_of_birth, city_of_residence, username, 
            email, password, country, active, created_at
        ))
        conn.commit()
        return {
            'ok': True,
            'data': f'New user {username} created.'
        }
    
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }


def getUsers():
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('''
        SELECT * FROM users
        ''')
        response = cursor.fetchall()
        return {
            'ok': True,
            'data': response
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }


def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('''
        SELECT username FROM users 
        WHERE email = %s and password = %s
        ''', (email, password))
        response = cursor.fetchone()
        if response == None:
            return {
                'ok': False,
                'data': f"The username or password are incorrect"
            }
        else: 
            return {
                'ok': True,
                'data': f"Welcome user {response['username']}"
            }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }
    

def getUserById(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('''
        SELECT * FROM users 
        WHERE user_id = %s
        ''', (id))
        response = cursor.fetchone()
        return {
            'ok': True,
            'data': response
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }

