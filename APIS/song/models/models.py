import base64
import os
import requests

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
        #Verifica si es un 200
        response.raise_for_status()
        token = response.json()['access_token']

        return {
            'ok': True, 
            'token': token
        }

    except Exception as e:
        return {
            'ok': False,
            'data': str(e)
        }

def getArtist(name):
    token_response = token()

    if token_response['ok']:
        url = "https://api.spotify.com/v1/search"
        headers = { 
            "Authorization": f"Bearer {token_response['token']}"
        }

        params = {
            'q':name,
            'type':'artist'
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            return {
                'ok': True,
                'data': response.json()
            }

        except Exception as e:
            return {
                'ok': False,
                'data': str(e) 
            }
    else:
        return token_response