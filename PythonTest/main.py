import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f719e800a235d47bbde957bbc105075'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
