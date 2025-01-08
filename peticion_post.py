import requests

url = "https://webhook.site/"
payload = {"plato": "asado", "cantidad": 2}
#quien hizo la consulta
query_params = {"nombre": "Choni"}
response = requests.post(url, data=payload, params=query_params)
#imprimir el status de la respuesta
print(response.status_code)

#imprimir la respuesta en texto
print(response.text)