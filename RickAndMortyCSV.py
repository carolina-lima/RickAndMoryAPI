import csv
import json
import requests


all_characters_request = requests.get(f'https://rickandmortyapi.com/api/character').json()

print(all_characters_request['results'][0])

with open("samplecsv.csv", 'w') as f: 
    wr = csv.DictWriter(f, fieldnames = all_characters_request['results'][0].keys()) 
    wr.writeheader() 
    wr.writerow(all_characters_request['results'][0]) 