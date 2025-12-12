# WS6 - Autenticação

Este projeto demonstra a implementação de autenticação HTTP Basic Authentication em um servidor web simples usando Python.

## 📋 Descrição

O projeto consiste em:
- **ws_provider.py**: Servidor HTTP que implementa autenticação Basic Auth
- **ws_client.py**: Cliente que faz requisições autenticadas ao servidor

O servidor valida credenciais usando o método HTTP Basic Authentication, onde as credenciais são enviadas no header `Authorization` codificadas em Base64.

## 🔧 Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (para o cliente)

### Instalação das dependências

```bash
pip install requests
```

## 🚀 Como Executar

### 1. Iniciar o Servidor

Execute o servidor em um terminal:

```bash
python ws_provider.py
```

O servidor será iniciado em `http://localhost:8000` e ficará aguardando requisições.

Você verá a mensagem:
```
Servidor HTTP com Basic Auth em http://localhost:8000
```

### 2. Executar o Cliente

Em outro terminal, execute o cliente:

```bash
python ws_client.py
```

O cliente fará uma requisição autenticada ao servidor e exibirá o resultado.

## 👤 Usuários Cadastrados

O servidor possui os seguintes usuários pré-configurados:

| Usuário | Senha   |
|---------|---------|
| `admin` | `1234`  |
| `user`  | `senha` |

## 📖 Como Funciona

### Servidor (ws_provider.py)

1. O servidor escuta requisições HTTP na porta 8000
2. Para cada requisição GET, verifica o header `Authorization`
3. Se não houver header de autenticação, retorna status 401 (Unauthorized)
4. Se houver, decodifica as credenciais Base64
5. Valida usuário e senha contra o dicionário `USUARIOS`
6. Se válido, retorna status 200 com mensagem de sucesso
7. Se inválido, retorna status 401

### Cliente (ws_client.py)

1. Faz uma requisição GET para `http://localhost:8000`
2. Usa a biblioteca `requests` com o parâmetro `auth=(usuario, senha)`
3. A biblioteca automaticamente codifica as credenciais em Base64 e adiciona ao header `Authorization`
4. Exibe o status code e a resposta do servidor

## 💡 Exemplos de Uso

### Exemplo 1: Requisição Bem-Sucedida

Com as credenciais corretas (`admin` / `1234`):

```python
res = requests.get(url, auth=("admin", "1234"))
# Status: 200
# Resposta: "Autenticado com sucesso!"
```

### Exemplo 2: Requisição sem Autenticação

Se você tentar acessar sem credenciais:

```python
res = requests.get(url)
# Status: 401
# Resposta: "Autenticacao necessaria"
```

### Exemplo 3: Credenciais Inválidas

Com credenciais incorretas:

```python
res = requests.get(url, auth=("admin", "senha_errada"))
# Status: 401
# Resposta: "Autenticacao necessaria"
```

## 🔍 Testando Manualmente

Você também pode testar usando `curl`:

```bash
# Requisição autenticada (sucesso)
curl -u admin:1234 http://localhost:8000

# Requisição sem autenticação (erro)
curl http://localhost:8000

# Requisição com credenciais inválidas (erro)
curl -u admin:senha_errada http://localhost:8000
```

## 📝 Estrutura do Código

### ws_provider.py

- `USUARIOS`: Dicionário com usuários e senhas válidos
- `SimpleAuthHandler`: Classe que herda de `BaseHTTPRequestHandler` e implementa a lógica de autenticação
- `do_GET()`: Método que processa requisições GET
- `send_auth_request()`: Método auxiliar que envia resposta 401 com header `WWW-Authenticate`

### ws_client.py

- Faz requisição HTTP GET usando a biblioteca `requests`
- Usa autenticação Basic Auth através do parâmetro `auth`
- Exibe o status code e o conteúdo da resposta

## 🔐 Segurança

**Nota**: Este é um exemplo educacional. Em produção, considere:

- Usar HTTPS em vez de HTTP
- Armazenar senhas com hash (nunca em texto plano)
- Implementar rate limiting
- Usar tokens JWT para autenticação stateless
- Implementar logout e expiração de sessões

## 🛠️ Personalização

Para adicionar novos usuários, edite o dicionário `USUARIOS` em `ws_provider.py`:

```python
USUARIOS = {
    "admin": "1234",
    "user": "senha",
    "novo_usuario": "nova_senha"  # Adicione aqui
}
```

Para alterar a porta do servidor, modifique a linha 47 em `ws_provider.py`:

```python
server = HTTPServer(("localhost", 8080), SimpleAuthHandler)  # Porta 8080
```

E atualize a URL no cliente:

```python
url = "http://localhost:8080"
```

