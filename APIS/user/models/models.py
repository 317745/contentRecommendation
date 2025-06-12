#APIS\user\models\models.py
from flask import jsonify, request
import requests
from datetime import datetime
from models.connection import *

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
    return response

def countryByName(name):
    try:

        if name is None:
            return {
                'ok': False,
                'error': 'El nombre del país es requerido.'
            }
        response = countrys()
        if response['ok'] == True:
            for key, value in response['data'].items():
                if value.lower() == name.lower():
                    return {
                        'ok': True,
                        'country': value
                    }
            return {
                'ok': False,
                'error': 'Pais no encontrado'
            }
    except Exception as e:
        return {
                'ok': False,
                'error': str(e)
            }

def confirmUserNameEmail(username, email):
    try: 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, email FROM users WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()
        if user[0] == username:
            return {
                'ok': True,
                'data': f"There's another user with the username: {username}"
            }
        elif user[1] == email:
            return {
                'ok': True,
                'data': f"There's another user with the email: {email}"
            }
        return {
            'ok': False,
            'data': f"The username: {username} and email {email} is available"
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
        responseUsername = confirmUserNameEmail(username, email)
        if responseUsername['ok']:
            return responseUsername

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
        cursor = conn.cursor()
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
        cursor = conn.cursor()
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

def getUserById(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
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

def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT username FROM users 
        WHERE email = %s and password = %s
        ''', (email, password))
        response = cursor.fetchone()[0]
        if len(response) > 0:
            return {
            'ok': True,
            'data': f'Welcome user: {response}'
        }
    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }