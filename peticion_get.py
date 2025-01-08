import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    #params en forma de diccionario
    params={"q": "python"}
)

#cuerpo de la respuesta en diccionario
print(response.json())

#primera llave de la respuesta
print(response.json()["current_user_url"])

#codigo de estado de la respuesta
print(response.status_code)

#cuerpo de la respuesta en bytes
print(response.content)

#cuerpo de la respuesta en string
print(response.text)

data = response.json()
print(data.keys())