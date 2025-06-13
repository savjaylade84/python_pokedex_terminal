

import requests
import json

def runStats(response) -> None:
    pokedex = response.json()
    
    print("="*30)
    
    print(f"ID: {pokedex['id']}")
    print(f"ORDER: {pokedex['order']}")
    print(f"BASE EXPERIENCE: {pokedex['base_experience']}")
    
    print("="*30)
    
    print('NAME: ' + f"{pokedex['name']}".capitalize())
    print('SPECIES: ' + f"{pokedex['species']['name']}".capitalize())

    print("TYPES: ")
    for ptype in pokedex['types']:
        print(f"{ptype['type']['name']}".capitalize())

    print("="*30)
    
    print(f"HEIGHT: {pokedex['height']}")
    print(f"WEIGHT: {pokedex['weight']}")

    print("="*30)
    print("ABILITIES:")
    for ability in pokedex['abilities']:
        print(f"{ability['ability']['name']} ".capitalize())

    print("="*30)
    print("MOVES:")
    count = 0
    for move in pokedex['moves']:
        if count > 10:
            break
        print(f"{move['move']['name']} ".capitalize())
        count += 1


print("="*30)
print("AUTHOR: JOHN JAYSON B. DE LEON")
print("GITHUB: SAVJAYLADE84")
print("EMAIL: SAVJAYLADE84@GMAIL.COM")
answer = 'y'
while answer != 'n':
    print("="*30)
    answer = input('Search For Pokemon Yes[y] or No[n]: ')
    answer.lower()

    if answer == 'n': break
    
    pokemon = input('Enter Pokemon Name: ')
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/".lower()
    response = requests.get(url)

    if response.status_code != 200:
        print("Sorry try Again!!!")
    else:
        runStats(response)
