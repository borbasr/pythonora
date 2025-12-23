import requests

def get_data(param):
    response = requests.get(f"https://teszt.valami/{param}")
    if response.status_code != 200:
        raise ValueError('Hiba tortent!')
    return response.json()

