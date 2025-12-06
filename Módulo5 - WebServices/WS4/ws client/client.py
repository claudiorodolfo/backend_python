# client.py - Cliente Python para testar o Web Service de validação de CPF
# Importa o módulo urllib.request para fazer requisições HTTP
import urllib.request
# Importa o módulo urllib.error para tratar erros de requisições HTTP
import urllib.error
# Importa o módulo json para trabalhar com dados JSON
import json

# Seção para testar requisição POST
# POST
# Imprime um cabeçalho indicando que será feita uma requisição POST
print("POST:") 
# Inicia um bloco try-except para capturar erros de conexão
try:
    # Converte um dicionário Python em string JSON e depois em bytes (encode)
    dados = json.dumps({"cpf": "11144477735"}).encode()
    
    # Cria um objeto Request com os dados da requisição POST
    # Request encapsula todas as informações necessárias para fazer a requisição HTTP
    req = urllib.request.Request(
        # URL do endpoint do servidor que valida CPF
        "http://localhost:8000/cpf",
        # Dados do corpo da requisição (em bytes)
        data=dados,
        # Define o header Content-Type como application/json para indicar formato dos dados
        headers={"Content-Type": "application/json"},
        # Define o método HTTP como POST
        method="POST"
    )
    
    # Abre a conexão HTTP e envia a requisição (context manager fecha automaticamente)
    # urlopen() envia a requisição e retorna um objeto de resposta
    # with garante que a conexão será fechada automaticamente após o bloco
    with urllib.request.urlopen(req) as resp:
        # Lê a resposta e converte de JSON para dicionário Python
        # json.load() lê de um arquivo-like object e faz parse do JSON
        resultado = json.load(resp)
        # Imprime o resultado formatado com indentação de 2 espaços e caracteres especiais preservados
        # indent=2 formata com 2 espaços de indentação, ensure_ascii=False preserva caracteres UTF-8
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura erros de URL (conexão, timeout, etc.)
except urllib.error.URLError as e:
    # Imprime mensagem de erro formatada
    print(f"Erro ao conectar com o servidor: {e}")

# Seção para testar requisição GET
# GET
# Imprime um cabeçalho indicando que será feita uma requisição GET (com quebra de linha antes)
print("\nGET:")
# Inicia um bloco try-except para capturar erros de conexão
try:
    # Abre a conexão HTTP com uma URL que contém o parâmetro CPF na query string
    # O parâmetro cpf=11144477735 é passado diretamente na URL após o "?"
    # with garante que a conexão será fechada automaticamente após o uso
    with urllib.request.urlopen("http://localhost:8000/cpf?cpf=11144477735") as resp:
        # Lê a resposta e converte de JSON para dicionário Python
        # json.load() lê de um arquivo-like object e faz parse do JSON
        resultado = json.load(resp)
        # Imprime o resultado formatado com indentação de 2 espaços e caracteres especiais preservados
        # indent=2 formata com 2 espaços de indentação, ensure_ascii=False preserva caracteres UTF-8
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura erros de URL (conexão, timeout, etc.)
# URLError é a exceção base para erros relacionados a URLs
except urllib.error.URLError as e:
    # Imprime mensagem de erro formatada usando f-string
    # f-string permite interpolação de variáveis com {e}
    print(f"Erro ao conectar com o servidor: {e}")
