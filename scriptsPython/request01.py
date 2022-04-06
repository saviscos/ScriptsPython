import requests
response = requests.get('https://viacep.com.br/ws/22041001/json')
print(response.status_code)
print(response.json())
print(dados_cep['logradouro'])