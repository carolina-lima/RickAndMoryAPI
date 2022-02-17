import csv
import requests


all_characters_request = requests.get(f'https://rickandmortyapi.com/api/character').json()


with open("character.csv", 'w') as f: 
    wr = csv.DictWriter(f, fieldnames = all_characters_request['results'][0].keys()) 
    wr.writeheader() 
    for i in range(20):
        wr.writerow(all_characters_request['results'][i]) 