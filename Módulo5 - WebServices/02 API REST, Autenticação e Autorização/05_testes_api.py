"""
05 - Testes Básicos com Ferramentas
=====================================
Exemplos de como testar APIs usando curl, requests e Postman
"""

import requests
import json

print("=" * 60)
print("TESTES DE APIs")
print("=" * 60)

# ============================================
# 1. TESTES COM REQUESTS (PYTHON)
# ============================================

base_url = "http://localhost:5000"

def testar_get():
    """Testa requisição GET"""
    print("\n" + "=" * 60)
    print("TESTE 1: GET - Listar Usuários")
    print("=" * 60)
    
    try:
        response = requests.get(f"{base_url}/api/users")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor")
        print("Certifique-se de que a API está rodando em http://localhost:5000")
    except Exception as e:
        print(f"Erro: {e}")


def testar_post():
    """Testa requisição POST"""
    print("\n" + "=" * 60)
    print("TESTE 2: POST - Criar Usuário")
    print("=" * 60)
    
    dados = {
        "nome": "João Silva",
        "email": "joao@example.com",
        "idade": 30
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/users",
            json=dados,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Request Body: {json.dumps(dados, indent=2, ensure_ascii=False)}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro: {e}")


def testar_put():
    """Testa requisição PUT"""
    print("\n" + "=" * 60)
    print("TESTE 3: PUT - Atualizar Usuário")
    print("=" * 60)
    
    dados = {
        "nome": "João Silva Santos",
        "email": "joao.silva@example.com",
        "idade": 31
    }
    
    try:
        response = requests.put(
            f"{base_url}/api/users/1",
            json=dados
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro: {e}")


def testar_delete():
    """Testa requisição DELETE"""
    print("\n" + "=" * 60)
    print("TESTE 4: DELETE - Deletar Usuário")
    print("=" * 60)
    
    try:
        response = requests.delete(f"{base_url}/api/users/1")
        print(f"Status Code: {response.status_code}")
        if response.content:
            print(f"Response:")
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            print("204 No Content - Sem corpo na resposta")
    except Exception as e:
        print(f"Erro: {e}")


def testar_com_query_params():
    """Testa GET com query parameters"""
    print("\n" + "=" * 60)
    print("TESTE 5: GET com Query Parameters")
    print("=" * 60)
    
    params = {
        "page": 1,
        "limit": 5,
        "search": "joão"
    }
    
    try:
        response = requests.get(f"{base_url}/api/users", params=params)
        print(f"URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro: {e}")


def testar_headers():
    """Testa envio de headers customizados"""
    print("\n" + "=" * 60)
    print("TESTE 6: Requisição com Headers Customizados")
    print("=" * 60)
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": "test-key-123",
        "X-Client-Version": "1.0.0"
    }
    
    try:
        response = requests.get(f"{base_url}/api/exemplo/headers", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Headers enviados: {headers}")
        print(f"Response:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro: {e}")


# ============================================
# 2. COMANDOS CURL
# ============================================

print("\n" + "=" * 60)
print("COMANDOS CURL PARA TESTAR")
print("=" * 60)

comandos_curl = {
    "GET - Listar": """
curl -X GET http://localhost:5000/api/users
""",
    "GET - Com Query Parameters": """
curl -X GET "http://localhost:5000/api/users?page=1&limit=10&search=joão"
""",
    "POST - Criar": """
curl -X POST http://localhost:5000/api/users \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "João Silva", "email": "joao@example.com", "idade": 30}'
""",
    "PUT - Atualizar": """
curl -X PUT http://localhost:5000/api/users/1 \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "João Santos", "email": "joao.santos@example.com", "idade": 31}'
""",
    "PATCH - Atualização Parcial": """
curl -X PATCH http://localhost:5000/api/users/1 \\
  -H "Content-Type: application/json" \\
  -d '{"idade": 32}'
""",
    "DELETE - Deletar": """
curl -X DELETE http://localhost:5000/api/users/1
""",
    "GET - Com Headers": """
curl -X GET http://localhost:5000/api/exemplo/headers \\
  -H "X-Custom-Header: valor-customizado"
""",
    "POST - JSON Complexo": """
curl -X POST http://localhost:5000/api/pedidos/criar \\
  -H "Content-Type: application/json" \\
  -d '{
    "cliente": {"nome": "João", "email": "joao@example.com"},
    "itens": [{"produto_id": 1, "quantidade": 2}]
  }'
"""
}

for nome, comando in comandos_curl.items():
    print(f"\n{nome}:")
    print(comando.strip())


# ============================================
# 3. EXEMPLOS DE TESTES AUTOMATIZADOS
# ============================================

class APITester:
    """Classe para testar APIs de forma organizada"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.results = []
    
    def test(self, nome, metodo, endpoint, data=None, headers=None):
        """Executa um teste"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if metodo.upper() == "GET":
                response = requests.get(url, headers=headers)
            elif metodo.upper() == "POST":
                response = requests.post(url, json=data, headers=headers)
            elif metodo.upper() == "PUT":
                response = requests.put(url, json=data, headers=headers)
            elif metodo.upper() == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Método {metodo} não suportado")
            
            resultado = {
                "nome": nome,
                "metodo": metodo,
                "endpoint": endpoint,
                "status_code": response.status_code,
                "sucesso": 200 <= response.status_code < 300,
                "response": response.json() if response.content else None
            }
            
            self.results.append(resultado)
            return resultado
        
        except Exception as e:
            resultado = {
                "nome": nome,
                "metodo": metodo,
                "endpoint": endpoint,
                "erro": str(e),
                "sucesso": False
            }
            self.results.append(resultado)
            return resultado
    
    def imprimir_resultados(self):
        """Imprime resultados dos testes"""
        print("\n" + "=" * 60)
        print("RESULTADOS DOS TESTES")
        print("=" * 60)
        
        for resultado in self.results:
            status = "✓ PASSOU" if resultado.get("sucesso") else "✗ FALHOU"
            print(f"\n{status} - {resultado['nome']}")
            print(f"  Método: {resultado['metodo']}")
            print(f"  Endpoint: {resultado['endpoint']}")
            if 'status_code' in resultado:
                print(f"  Status: {resultado['status_code']}")
            if 'erro' in resultado:
                print(f"  Erro: {resultado['erro']}")
        
        total = len(self.results)
        passou = sum(1 for r in self.results if r.get("sucesso"))
        print(f"\nTotal: {passou}/{total} testes passaram")


# ============================================
# 4. EXEMPLO DE USO DO TESTER
# ============================================

def executar_suite_testes():
    """Executa uma suíte de testes"""
    print("\n" + "=" * 60)
    print("EXECUTANDO SUÍTE DE TESTES")
    print("=" * 60)
    
    tester = APITester(base_url)
    
    # Testes
    tester.test("Listar usuários", "GET", "/api/users")
    tester.test("Criar usuário", "POST", "/api/users", {
        "nome": "Teste",
        "email": "teste@example.com",
        "idade": 25
    })
    tester.test("Obter usuário", "GET", "/api/users/1")
    tester.test("Atualizar usuário", "PUT", "/api/users/1", {
        "nome": "Teste Atualizado",
        "email": "teste.atualizado@example.com"
    })
    tester.test("Deletar usuário", "DELETE", "/api/users/1")
    
    tester.imprimir_resultados()


# ============================================
# 5. TESTES COM POSTMAN (GUIA)
# ============================================

print("\n" + "=" * 60)
print("GUIA: TESTANDO COM POSTMAN")
print("=" * 60)
print("""
1. Criar Nova Requisição:
   - Abrir Postman
   - New → HTTP Request
   - Selecionar método (GET, POST, etc.)

2. Configurar URL:
   - Digite a URL completa
   - Ex: http://localhost:5000/api/users

3. Adicionar Headers:
   - Vá para aba "Headers"
   - Adicione: Content-Type: application/json

4. Adicionar Body (para POST/PUT):
   - Vá para aba "Body"
   - Selecione "raw"
   - Escolha "JSON"
   - Digite o JSON no campo

5. Enviar Requisição:
   - Clique em "Send"
   - Veja a resposta na parte inferior

6. Salvar Coleção:
   - Clique em "Save"
   - Crie uma coleção
   - Organize suas requisições

Exemplo de JSON para Body (POST):
{
  "nome": "João Silva",
  "email": "joao@example.com",
  "idade": 30
}
""")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - TESTES DE APIs")
print("=" * 60)
print("""
Ferramentas para testar APIs:

1. requests (Python):
   - Biblioteca Python para HTTP
   - Fácil de usar em scripts
   - Ideal para testes automatizados

2. curl:
   - Linha de comando
   - Disponível em todos os sistemas
   - Rápido para testes rápidos

3. Postman:
   - Interface gráfica
   - Salvar coleções
   - Testes automatizados
   - Documentação

4. httpie:
   - Alternativa moderna ao curl
   - Sintaxe mais amigável
   - Melhor formatação de output

Boas práticas:
- Teste todos os métodos HTTP
- Teste casos de sucesso e erro
- Valide status codes
- Verifique estrutura de resposta
- Teste com dados inválidos
""")

if __name__ == '__main__':
    print("\nPara executar os testes:")
    print("1. Certifique-se de que a API está rodando")
    print("2. Execute este arquivo: python 05_testes_api.py")
    print("3. Ou execute testes individuais")
    
    # Descomentar para executar testes (se API estiver rodando)
    # executar_suite_testes()

