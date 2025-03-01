import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)   

print(response)   ##3 retorna o status code da solicitacao

if response.status_code == 200:
    data_json = response.json()
    print(data_json)
else:
    print(f'O erro foi {response.status_code}')