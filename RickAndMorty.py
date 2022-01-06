import json
import csv
import requests


#consulta na API
all_characters_request = requests.get(f'https://rickandmortyapi.com/api/character').json()

#transforma o objeto de dict para string
file_characters = json.dumps(all_characters_request)

#cria o arquivo json
f = open("all_characters.json", "w")
f.write(file_characters)
f.close()

#abre e lê o arquivo
f = open("all_characters.json", "r")
print(f.read())
