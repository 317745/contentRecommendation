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
            data = response['artists']['items']
            artists = []

            for artist in data:
                artists.append({
                    'followers': artist['followers']['total'],
                    'genres': artist['genres'],
                    'spotify': artist['external_urls']['spotify'],
                    'id': artist['id'],
                    'image': artist['images'][0]['url'] if artist['images'] else '',
                    'name': artist['name'],
                    'popularity': artist['popularity']        
                })

            return {
                'ok': True,
                'data': artists
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
            artist = [{
                'followers': response['followers']['total'],
                'genres': response['genres'],
                'spotify': response['external_urls']['spotify'],
                'id': response['id'],
                'image': response['images'][0]['url'] if response['images'] else '',
                'name': response['name'],
                'popularity': response['popularity']        
            }]

            return {
                'ok': True,
                'data': artist
            }
    
        except Exception as e:
            return {
                'ok': False,
                'data': str(e) 
            }
    else:
        return token_response