import urllib.request
import urllib.error
import json

# POST
print("POST:") 
try:
    dados = json.dumps({"cpf": "11144477735"}).encode()
    
    req = urllib.request.Request(
        "http://localhost:8000/cpf",
        data=dados,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req) as resp:
        resultado = json.load(resp)
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
except urllib.error.URLError as e:
    print(f"Erro ao conectar com o servidor: {e}")

# GET
print("\nGET:")
try:
    with urllib.request.urlopen("http://localhost:8000/cpf?cpf=11144477735") as resp:
        resultado = json.load(resp)
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
except urllib.error.URLError as e:
    print(f"Erro ao conectar com o servidor: {e}")
