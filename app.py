import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)   

print(response)   ##3 retorna o status code da solicitacao

if response.status_code == 200:
    data_json = response.json()
    data_restaurante = {}
    for item in data_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in data_restaurante:
            data_restaurante[nome_restaurante] = []

        data_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao" : item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante,dados in data_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as file:
        json.dump(dados,file,indent=4)