import requests

TOKEN = input('Введите токен')

host = 'https://cloud-api.yandex.net:443/'
def get_headers():
    return {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(name_folder):
    uri = 'v1/disk/resources'
    url = host + uri
    headers = get_headers()
    params = {'path': f'/{name_folder}'}
    response = requests.put(url, headers=headers, params=params)
    return(response.status_code)
