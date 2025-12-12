import requests

url = "http://localhost:8000"

# credenciais
usuario = "admin"
senha = "1234"

res = requests.get(url, auth=(usuario, senha))
print(res.status_code, res.text)
