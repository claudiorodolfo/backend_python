import requests
import json

url = "http://localhost:8000"

# Credenciais
usuario = "admin"
senha = "1234"

print("=" * 60)
print("Cliente JWT - Testando Autenticação")
print("=" * 60)

# 1. Fazer login e obter token
print("\n1. Fazendo login...")
login_url = f"{url}/login"
login_data = {
    "usuario": usuario,
    "senha": senha
}

try:
    response = requests.post(login_url, json=login_data)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        print(f"Token recebido: {token[:50]}...")
        
        # 2. Acessar rota protegida com o token
        print("\n2. Acessando rota protegida...")
        protected_url = f"{url}/protegido"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        response = requests.get(protected_url, headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {response.text}")
        
    else:
        print(f"Erro no login: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("Erro: Não foi possível conectar ao servidor.")
    print("Certifique-se de que o servidor está rodando em http://localhost:8000")
except Exception as e:
    print(f"Erro: {e}")

