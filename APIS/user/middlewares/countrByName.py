import requests

def countryByName(name):
    try:
        if name is None:
            return {
                'ok': False,
                'error': 'El nombre del país es requerido.'
            }
        
        url = 'http://localhost:3031/getCountrys'
        response = requests.get(url).json()
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