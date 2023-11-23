import requests

# response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
#               json=
#                   {
#                     "name": "жора",
#                     "photo": "https://dolnikov.ru/pokemons/albums/141.png"
#                   }, headers={'Content-Type': 'application/json',
#                           'trainer_token': 'token'}, timeout=5)

# print(f'{response.status_code} - {response.reason}. {response.text}')


# response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
#               json=
#                   {
#                     "pokemon_id": "20417",
#                     "name": "борис",
#                     "photo": "https://dolnikov.ru/pokemons/albums/141.png"
#                   }, headers={'Content-Type': 'application/json',
#                           'trainer_token': 'token'}, timeout=5)

# print(f'{response.status_code} - {response.reason}. {response.text}')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json=
                  {
                    "pokemon_id": "20417"
                  }, headers={'Content-Type': 'application/json',
                          'trainer_token': 'token'}, timeout=5)

print(f'{response.status_code} - {response.reason}. {response.text}')