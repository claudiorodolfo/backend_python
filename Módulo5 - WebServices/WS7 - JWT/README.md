# WS7 - JWT (JSON Web Token)

Este projeto demonstra a implementação de autenticação usando JWT (JSON Web Token) em um servidor web simples usando Python.

## 📋 Descrição

O projeto consiste em:
- **ws_provider.py**: Servidor HTTP que implementa autenticação JWT
- **ws_client.py**: Cliente que faz requisições autenticadas ao servidor usando JWT

O servidor implementa autenticação baseada em tokens JWT, onde:
1. O cliente faz login enviando credenciais (POST `/login`)
2. O servidor valida as credenciais e retorna um token JWT
3. O cliente usa o token JWT para acessar rotas protegidas (GET `/protegido`)

## 🔧 Requisitos

- Python 3.6 ou superior
- Biblioteca `PyJWT` (para geração e validação de tokens)
- Biblioteca `requests` (para o cliente)

### Instalação das dependências

```bash
pip install PyJWT requests
```

Ou instale individualmente:

```bash
pip install PyJWT
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
Servidor JWT rodando em http://localhost:8000
```

### 2. Executar o Cliente

Em outro terminal, execute o cliente:

```bash
python ws_client.py
```

O cliente fará:
1. Login no servidor para obter um token JWT
2. Usar o token para acessar a rota protegida `/protegido`
3. Exibir o resultado

## 👤 Usuários Cadastrados

O servidor possui os seguintes usuários pré-configurados:

| Usuário | Senha   |
|---------|---------|
| `admin` | `1234`  |
| `user`  | `senha` |

## 📖 Como Funciona

### Servidor (ws_provider.py)

#### Endpoint POST `/login`
1. Recebe credenciais (usuario e senha) no corpo da requisição (JSON)
2. Valida as credenciais contra o dicionário `USUARIOS`
3. Se válido, cria um token JWT com:
   - `usuario`: Nome do usuário
   - `exp`: Data de expiração (30 minutos a partir de agora)
4. Retorna o token JWT no formato JSON: `{"token": "..."}`
5. Se inválido, retorna status 401 (Unauthorized)

#### Endpoint GET `/protegido`
1. Verifica o header `Authorization` que deve conter `Bearer <token>`
2. Se não houver header ou formato incorreto, retorna 401
3. Valida o token JWT:
   - Verifica a assinatura usando a chave secreta
   - Verifica se o token não expirou
4. Se válido, retorna 200 com mensagem de sucesso
5. Se inválido ou expirado, retorna 401

### Cliente (ws_client.py)

1. Faz uma requisição POST para `/login` com credenciais
2. Recebe o token JWT na resposta
3. Faz uma requisição GET para `/protegido` incluindo o token no header `Authorization: Bearer <token>`
4. Exibe o status code e a resposta do servidor

## 💡 Exemplos de Uso

### Exemplo 1: Login Bem-Sucedido

Com as credenciais corretas (`admin` / `1234`):

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario": "admin", "senha": "1234"}'
```

**Resposta (200):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJleHAiOjE2..."
}
```

### Exemplo 2: Acessar Rota Protegida

Usando o token obtido no login:

```bash
curl -X GET http://localhost:8000/protegido \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta (200):**
```json
{
  "message": "Acesso liberado: admin"
}
```

### Exemplo 3: Login com Credenciais Inválidas

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario": "admin", "senha": "senha_errada"}'
```

**Resposta (401):** Sem corpo de resposta

### Exemplo 4: Acessar Rota Protegida sem Token

```bash
curl -X GET http://localhost:8000/protegido
```

**Resposta (401):** Sem corpo de resposta

### Exemplo 5: Acessar Rota Protegida com Token Inválido

```bash
curl -X GET http://localhost:8000/protegido \
  -H "Authorization: Bearer token_invalido"
```

**Resposta (401):** Sem corpo de resposta

### Exemplo 6: Fluxo Completo (Login + Acesso Protegido)

```bash
# 1. Fazer login e salvar o token
TOKEN=$(curl -s -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"usuario": "admin", "senha": "1234"}' | \
  python3 -c "import sys, json; print(json.load(sys.stdin)['token'])")

# 2. Usar o token para acessar rota protegida
curl -X GET http://localhost:8000/protegido \
  -H "Authorization: Bearer $TOKEN"
```

## 🔍 Testando com Python

### Usando o cliente fornecido

```bash
python ws_client.py
```

### Usando requests diretamente

```python
import requests

url = "http://localhost:8000"

# Login
response = requests.post(
    f"{url}/login",
    json={"usuario": "admin", "senha": "1234"}
)

if response.status_code == 200:
    token = response.json()["token"]
    
    # Acessar rota protegida
    response = requests.get(
        f"{url}/protegido",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.json()}")
```

## 📝 Estrutura do Código

### ws_provider.py

- `SECRET`: Chave secreta usada para assinar e verificar tokens JWT
- `USUARIOS`: Dicionário com usuários e senhas válidos
- `JWTHandler`: Classe que herda de `BaseHTTPRequestHandler` e implementa a lógica JWT
- `do_POST()`: Processa requisições POST (endpoint `/login`)
- `do_GET()`: Processa requisições GET (endpoint `/protegido`)

### ws_client.py

- Faz requisição POST para `/login` com credenciais
- Extrai o token JWT da resposta
- Faz requisição GET para `/protegido` com o token no header `Authorization`
- Exibe os resultados

## 🔐 Segurança

**Nota**: Este é um exemplo educacional. Em produção, considere:

- Usar HTTPS em vez de HTTP
- Armazenar senhas com hash (nunca em texto plano)
- Usar uma chave secreta forte e armazená-la de forma segura (variáveis de ambiente)
- Implementar rate limiting para prevenir ataques de força bruta
- Considerar refresh tokens para renovação de tokens
- Implementar blacklist de tokens revogados
- Adicionar mais claims ao JWT (iat, iss, aud, etc.)
- Validar e sanitizar todas as entradas

## 🛠️ Personalização

### Adicionar novos usuários

Edite o dicionário `USUARIOS` em `ws_provider.py`:

```python
USUARIOS = {
    "admin": "1234",
    "user": "senha",
    "novo_usuario": "nova_senha"  # Adicione aqui
}
```

### Alterar tempo de expiração do token

Modifique a linha 27 em `ws_provider.py`:

```python
"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 1 hora
```

### Alterar a porta do servidor

Modifique a linha 68 em `ws_provider.py`:

```python
server = HTTPServer(("0.0.0.0", 8080), JWTHandler)  # Porta 8080
```

E atualize a URL no cliente:

```python
url = "http://localhost:8080"
```

### Alterar a chave secreta

Modifique a linha 7 em `ws_provider.py`:

```python
SECRET = "sua_chave_secreta_muito_forte_aqui"
```

**Importante**: Use uma chave secreta forte em produção (mínimo 32 caracteres aleatórios).

## 📚 Sobre JWT

### O que é JWT?

JWT (JSON Web Token) é um padrão aberto (RFC 7519) que define uma forma compacta e autocontida de transmitir informações entre partes como um objeto JSON. Essas informações podem ser verificadas e confiáveis porque são assinadas digitalmente.

### Estrutura do JWT

Um JWT consiste em três partes separadas por pontos (`.`):

1. **Header**: Contém o tipo do token e o algoritmo de assinatura
2. **Payload**: Contém as claims (informações sobre o usuário e metadados)
3. **Signature**: Usada para verificar a integridade do token

Formato: `header.payload.signature`

### Vantagens do JWT

- **Stateless**: Não precisa armazenar tokens no servidor
- **Escalável**: Funciona bem em arquiteturas distribuídas
- **Self-contained**: Contém todas as informações necessárias
- **Padrão da indústria**: Amplamente usado e suportado

### Limitações

- **Não pode ser revogado facilmente**: Uma vez emitido, é válido até expirar (a menos que use blacklist)
- **Tamanho**: Maior que tokens simples (pode ser um problema em requisições frequentes)
- **Segurança**: Se comprometido, é válido até expirar

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'jwt'"

Instale a biblioteca PyJWT:
```bash
pip install PyJWT
```

### Erro: "Connection refused"

Certifique-se de que o servidor está rodando antes de executar o cliente.

### Token expirado

Os tokens expiram após 30 minutos. Faça um novo login para obter um novo token.

### Erro 401 ao acessar rota protegida

Verifique se:
- O token está sendo enviado no header `Authorization`
- O formato está correto: `Bearer <token>` (com espaço após "Bearer")
- O token não expirou
- O token foi gerado pelo mesmo servidor (mesma chave secreta)

