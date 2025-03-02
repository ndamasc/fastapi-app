from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello():
    return {'Hello': 'world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None) ):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)   

    if response.status_code == 200:
        data_json = response.json()
        if restaurante is None:
            return {'Dados' : data_json}

        data_restaurante = []
        for item in data_json:
            if item['Company'] == restaurante:
                data_restaurante.append({
                    "item": item['Item'],
                    "preco": item['price'],
                    "descricao" : item['description']
                })
        return {'Restaurante' : restaurante, 'Cardapio': data_restaurante}
    else:
        print(f'O erro foi {response.status_code} - {response.text}')