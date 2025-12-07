# Importa o módulo requests para fazer requisições HTTP
import requests
# Importa o módulo json para serializar e deserializar dados JSON
import json

# Seção para testar requisição HTTP POST
# Imprime cabeçalho indicando que será feita uma requisição POST
print("POST:") 
# Tenta executar o código dentro do bloco try
try:
    # URL do endpoint do servidor para validação de CPF
    url = "http://localhost:8000/cpf"
    # Dados JSON com o CPF a ser validado
    # O CPF "11144477735" é um exemplo de CPF válido para teste
    dados = {"cpf": "11144477735"}
    
    # Faz uma requisição HTTP POST usando a biblioteca requests
    # json=dados automaticamente serializa o dicionário para JSON e define Content-Type
    response = requests.post(url, json=dados)
    # Converte a resposta JSON para dicionário Python
    resultado = response.json()
    # Converte o dicionário de volta para JSON formatado (indent=2 para legibilidade)
    # ensure_ascii=False permite caracteres especiais (acentos) na saída
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura exceções de requisição (erros de conexão, URL inválida, etc.)
except requests.exceptions.RequestException as e:
    # Imprime mensagem de erro caso não consiga conectar ao servidor
    print(f"Erro ao conectar com o servidor: {e}")

# Seção para testar requisição HTTP GET
# Imprime uma linha em branco e cabeçalho indicando que será feita uma requisição GET
print("\nGET:")
# Tenta executar o código dentro do bloco try
try:
    # URL do endpoint com o parâmetro "numero" na query string (?numero=11144477735)
    url = "http://localhost:8000/cpf?numero=11144477735"
    
    # Faz uma requisição HTTP GET usando a biblioteca requests
    response = requests.get(url)
    # Converte a resposta JSON para dicionário Python
    resultado = response.json()
    # Converte o dicionário de volta para JSON formatado (indent=2 para legibilidade)
    # ensure_ascii=False permite caracteres especiais (acentos) na saída
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura exceções de requisição (erros de conexão, URL inválida, etc.)
except requests.exceptions.RequestException as e:
    # Imprime mensagem de erro caso não consiga conectar ao servidor
    print(f"Erro ao conectar com o servidor: {e}")
