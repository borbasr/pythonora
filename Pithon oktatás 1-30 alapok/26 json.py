import json

data = {}
data['users'] = []

data['users'].append({
    'name': 'Mekk Elek',
    'email': 'mekk@elek.hu',
    'address': 'Budapest'
})

data['users'].append({
    'name': 'Gipsz Jakab',
    'email': 'gipsz@jakab.hu',
    'address': 'Debrecen'
})

data['users'].append({
    'name': 'Teszt Elek',
    'email': 'teszt@elek.hu',
    'address': 'Miskolc'
})

with open('data.json', 'w', encoding="utf-8") as file:
    json.dump(data, file)

with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(data)
    for u in data['users']:
        print(u["name"])

