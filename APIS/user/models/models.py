#APIS\user\models\models.py
from flask import jsonify
import requests

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
        