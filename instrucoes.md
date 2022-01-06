# Instruções

## URL's
- personagem_url "https://rickandmortyapi.com/api/character"
- locais_url "https://rickandmortyapi.com/api/location"
- episodios_url = "https://rickandmortyapi.com/api/episode"

## modelo de consulta por variável da resposta:
id_personagem = input("Digite o ID do personagem: ")
resposta = requests.get(f'https://rickandmortyapi.com/api/character/{id_personagem}').json()
print(resposta["name"])
print(resposta["status"])