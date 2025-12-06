# Importa o módulo urllib.request para fazer requisições HTTP
import urllib.request
# Importa o módulo urllib.error para tratar erros de requisições HTTP
import urllib.error
# Importa o módulo json para serializar e deserializar dados JSON
import json

# Seção para testar requisição HTTP POST
# Imprime cabeçalho indicando que será feita uma requisição POST
print("POST:") 
# Tenta executar o código dentro do bloco try
try:
    # Converte o dicionário Python em string JSON e depois em bytes
    # O CPF "11144477735" é um exemplo de CPF válido para teste
    dados = json.dumps({"cpf": "11144477735"}).encode()
    
    # Cria um objeto Request com os detalhes da requisição HTTP POST
    req = urllib.request.Request(
        # URL do endpoint do servidor para validação de CPF
        "http://localhost:8000/cpf",
        # Corpo da requisição (dados JSON em bytes)
        data=dados,
        # Headers HTTP: define Content-Type como application/json
        headers={"Content-Type": "application/json"},
        # Define o método HTTP como POST
        method="POST"
    )
    
    # Abre a conexão HTTP e envia a requisição
    # O contexto manager (with) garante que a conexão seja fechada automaticamente
    with urllib.request.urlopen(req) as resp:
        # Lê a resposta HTTP e converte de JSON para dicionário Python
        resultado = json.load(resp)
        # Converte o dicionário de volta para JSON formatado (indent=2 para legibilidade)
        # ensure_ascii=False permite caracteres especiais (acentos) na saída
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura exceções do tipo URLError (erros de conexão, URL inválida, etc.)
except urllib.error.URLError as e:
    # Imprime mensagem de erro caso não consiga conectar ao servidor
    print(f"Erro ao conectar com o servidor: {e}")

# Seção para testar requisição HTTP GET
# Imprime uma linha em branco e cabeçalho indicando que será feita uma requisição GET
print("\nGET:")
# Tenta executar o código dentro do bloco try
try:
    # Abre a conexão HTTP e envia requisição GET diretamente pela URL
    # O parâmetro "numero" é passado na query string (?numero=11144477735)
    # O contexto manager (with) garante que a conexão seja fechada automaticamente
    with urllib.request.urlopen("http://localhost:8000/cpf?numero=11144477735") as resp:
        # Lê a resposta HTTP e converte de JSON para dicionário Python
        resultado = json.load(resp)
        # Converte o dicionário de volta para JSON formatado (indent=2 para legibilidade)
        # ensure_ascii=False permite caracteres especiais (acentos) na saída
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
# Captura exceções do tipo URLError (erros de conexão, URL inválida, etc.)
except urllib.error.URLError as e:
    # Imprime mensagem de erro caso não consiga conectar ao servidor
    print(f"Erro ao conectar com o servidor: {e}")
