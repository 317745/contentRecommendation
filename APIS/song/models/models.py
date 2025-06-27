import base64
import os
import requests
import json

def token():
    url = "https://accounts.spotify.com/api/token"
    id_client = os.getenv('ID_CLIENT')
    secret_client = os.getenv('SECRET_CLIENT')
    credentials = f'{id_client}:{secret_client}'.encode('utf-8')
    b64 = base64.b64encode(credentials).decode('utf-8')

    headers = {
        "Authorization": f"Basic {b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        token = response.json()['access_token']

        return {
            'ok': True, 
            'data': token
        }

    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }
    
def getArtistByName(name):
    token_response = token()

    if token_response['ok']:
        url = 'https://api.spotify.com/v1/search'

        headers = {
            "Authorization": f"Bearer {token_response['data']}"
        }

        params = {
            'q': name,
            'type': 'artist',
            'limit': 5
        }

        try:
            response = requests.get(url, params=params, headers=headers).json()

            return {
                'ok': True,
                'data': response
            }
        
        except Exception as e:
            return {
                'ok': False,
                'data': str(e)
            }
    else:
        return token_response

def getArtistByID(id):
    token_response = token()

    if token_response['ok']:
        url = f'https://api.spotify.com/v1/artists/{id}'

        headers = { 
            "Authorization": f"Bearer {token_response['data']}"
        }

        try:
            response = requests.get(url, headers=headers).json()
            #data = []

            #for name in response['artists']['items']:
            #    data.append(name['name'])

            return {
                'ok': True,
                'data': response
            }
    
        except Exception as e:
            return {
                'ok': False,
                'data': str(e) 
            }
    else:
        return token_response