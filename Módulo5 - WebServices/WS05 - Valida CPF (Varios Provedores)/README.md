# WS5 - Web Service de Validação de CPF (Vários Provedores)

Este projeto implementa um Web Service para validação de CPF (Cadastro de Pessoa Física) com providers em múltiplas linguagens (Python, Node.js, Java, PHP e C++) e um cliente em Python.

## Estrutura do Projeto

```
WS5 - Valida CPF (Varios Provedores)/
├── ws provider/          # Servidores (providers) do Web Service
│   ├── provider.py       # Provider em Python (porta 8080)
│   ├── provider.js       # Provider em Node.js (porta 8081)
│   ├── Provider.java     # Provider em Java (porta 8082)
│   ├── provider.php      # Provider em PHP (porta 8083)
│   ├── provider.cpp      # Provider em C++ (porta 8084)
│   └── httplib.h         # Biblioteca HTTP para C++ (cpp-httplib)
└── ws client/            # Clientes para testar o Web Service
    └── ws_client.py      # Cliente em Python
```

## Funcionalidades

O Web Service oferece um endpoint para validação de CPF:

### GET /validar?cpf=XXXXXXXXXXX
Valida um CPF via parâmetro de query string.

**Exemplo:**
```bash
curl "http://localhost:8080/validar?cpf=11144477735"
```

**Resposta (todos os providers):**
```json
{
  "cpf": "11144477735",
  "valido": true
}
```

**Resposta de erro (quando parâmetro cpf não é fornecido):**
Todos os providers retornam erro 400 (Bad Request) com mensagem JSON. A estrutura da mensagem pode variar ligeiramente entre providers:

**Python, Node.js, Java, PHP e C++:**
```json
{
  "error": "Parâmetro 'cpf' não fornecido"
}
```

**Nota:** Todos os providers usam o campo `"error"` (em inglês) para este tipo de erro, mantendo consistência entre as linguagens.

**Resposta de erro (quando método HTTP não é permitido):**
Este Web Service aceita apenas requisições GET. Todos os providers retornam erro 405 (Method Not Allowed) para métodos não permitidos (POST, PUT, DELETE, etc.) com mensagem JSON. A estrutura da mensagem pode variar ligeiramente entre providers:

**Python, Java e C++:**
```json
{
  "error": "Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint."
}
```

**Node.js:**
```json
{
  "erro": "Method Not Allowed",
  "mensagem": "Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint.",
  "metodo_solicitado": "POST",
  "metodo_permitido": "GET"
}
```

**PHP:**
```json
{
  "erro": "Method Not Allowed",
  "mensagem": "Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint.",
  "metodo_permitido": "GET"
}
```

**Nota:** Python, Java e C++ usam o campo `"error"` com mensagem descritiva, enquanto Node.js e PHP usam os campos `"erro"`, `"mensagem"` e `"metodo_permitido"` (Node.js também inclui `"metodo_solicitado"`).

**Resposta de erro (quando endpoint não é encontrado):**
Todos os providers retornam erro 404 (Not Found) com mensagem JSON. Todos os providers usam o campo `"error"` de forma consistente:

**Todos os providers (Python, Node.js, Java, PHP e C++):**
```json
{
  "error": "Endpoint não encontrado"
}
```

**⚠️ Importante:** Todos os providers retornam o campo `"valido"` (em português) de forma consistente.

## Como Executar

### Provider Python

**Pré-requisitos:** Python 3.x instalado

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws provider"
```

2. Inicie o servidor:
```bash
python3 provider.py
```

Você verá a mensagem: `Servidor iniciado em http://127.0.0.1:8080`

3. Em outro terminal, execute o cliente:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
python3 ws_client.py 8080
```

O cliente testará o endpoint GET automaticamente.

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider Node.js

**Pré-requisitos:** Node.js instalado

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws provider"
```

2. Inicie o servidor:
```bash
node provider.js
```

Você verá a mensagem: `Servidor JS rodando em http://localhost:8081`

3. Para testar, você pode:
   - Usar o cliente Python:
     ```bash
     cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
     python3 ws_client.py 8081
     ```
   - Usar curl:
     ```bash
     curl "http://localhost:8081/validar?cpf=11144477735"
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider PHP

**Pré-requisitos:** PHP instalado (versão 7.0 ou superior)

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws provider"
```

2. Inicie o servidor:
```bash
php -S 127.0.0.1:8083 provider.php
```

Você verá a mensagem indicando que o servidor está rodando.

3. Para testar, você pode:
   - Usar o cliente Python:
     ```bash
     cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
     python3 ws_client.py 8083
     ```
   - Usar curl:
     ```bash
     curl "http://localhost:8083/validar?cpf=11144477735"
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider Java

**Pré-requisitos:** JDK instalado (Java 8 ou superior) e biblioteca JSON

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws provider"
```

2. Baixe a biblioteca JSON (se ainda não tiver):
```bash
curl -L -o json.jar https://repo1.maven.org/maven2/org/json/json/20250517/json-20250517.jar
```

3. Compile o código:
```bash
javac -cp ".:json.jar" Provider.java
```

Isso criará o arquivo `Provider.class` na mesma pasta.

4. Execute o servidor:
```bash
java -cp ".:json.jar" Provider
```

Você verá a mensagem: `Servidor iniciado em http://127.0.0.1:8082`

5. Para testar, você pode:
   - Usar o cliente Python:
     ```bash
     cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
     python3 ws_client.py 8082
     ```
   - Usar curl:
     ```bash
     curl "http://localhost:8082/validar?cpf=11144477735"
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

**Nota:** Se você quiser limpar os arquivos compilados após usar:
```bash
rm Provider.class
```

---

### Provider C++

**Pré-requisitos:** Compilador C++ (g++) e biblioteca httplib.h

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws provider"
```

2. Baixe a biblioteca httplib.h (se ainda não tiver):
```bash
curl -L -o httplib.h https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h
```

3. Compile o código:
```bash
g++ -std=c++11 -o provider provider.cpp -pthread
```

Isso criará o executável `provider` na mesma pasta.

4. Execute o servidor:
```bash
./provider
```

Você verá a mensagem: `Servidor iniciado em http://127.0.0.1:8084`

5. Para testar, você pode:
   - Usar o cliente Python:
     ```bash
     cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
     python3 ws_client.py 8084
     ```
   - Usar curl:
     ```bash
     curl "http://localhost:8084/validar?cpf=11144477735"
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

**Nota:** Se você quiser limpar o executável após usar:
```bash
rm provider
```

---

## Testando com os Clientes

### Cliente Python

O cliente Python (`ws_client.py`) aceita a porta do provider como argumento de linha de comando.

**Uso:**
```bash
cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
python3 ws_client.py <porta>
```

**Exemplos:**
- Para testar o provider Python (porta 8080): `python3 ws_client.py 8080`
- Para testar o provider Node.js (porta 8081): `python3 ws_client.py 8081`
- Para testar o provider Java (porta 8082): `python3 ws_client.py 8082`
- Para testar o provider PHP (porta 8083): `python3 ws_client.py 8083`
- Para testar o provider C++ (porta 8084): `python3 ws_client.py 8084`

O cliente testará automaticamente dois CPFs: um válido (`11144477735`) e um inválido (`11111111111`).

**Pré-requisitos:** Python 3.x e biblioteca `requests` instalada:
```bash
pip3 install requests
```

## Algoritmo de Validação de CPF

O algoritmo implementado segue o padrão oficial de validação de CPF brasileiro:

1. Remove caracteres não numéricos (pontos e traços)
2. Verifica se possui 11 dígitos
3. Verifica se não são todos os dígitos iguais
4. Calcula o primeiro dígito verificador (usando os 9 primeiros dígitos)
5. Calcula o segundo dígito verificador (usando os 10 primeiros dígitos)
6. Compara com os dígitos informados

## Exemplos de CPF para Teste

- **Válido:** `11144477735`
- **Válido:** `12345678909`
- **Inválido:** `11111111111` (todos os dígitos iguais)
- **Inválido:** `12345678900` (dígitos verificadores incorretos)

## Portas dos Providers

Cada provider usa uma porta específica:

| Provider | Porta |  Endpoint  | Resposta   |
|----------|-------|------------|------------|
| Python   | 8080  | `/validar` | `"valido"` |
| Node.js  | 8081  | `/validar` | `"valido"` |
| Java     | 8082  | `/validar` | `"valido"` |
| PHP      | 8083  | `/validar` | `"valido"` |
| C++      | 8084  | `/validar` | `"valido"` |

**⚠️ Atenção:** Cada provider usa uma porta única, permitindo que todos sejam executados simultaneamente para testes comparativos.

## Tecnologias Utilizadas

- **Python:** `http.server` (BaseHTTPRequestHandler) - Porta 8080
- **Node.js:** `http` (módulo nativo) - Porta 8081
- **Java:** `com.sun.net.httpserver` e `org.json` - Porta 8082
- **PHP:** Built-in server (`php -S`) - Porta 8083
- **C++:** `cpp-httplib` (httplib.h) - Porta 8084

## Observações Importantes

- ⚠️ **Portas:** Cada provider usa uma porta única (8080, 8081, 8082, 8083, 8084), permitindo que todos sejam executados simultaneamente para testes comparativos.
- ⚠️ **Método HTTP:** Este Web Service aceita apenas requisições GET. Todos os providers retornam erro 405 (Method Not Allowed) com mensagem JSON explicativa para métodos não permitidos (POST, PUT, DELETE, etc.).
- ⚠️ **Tratamento de Erros:** 
  - **Métodos HTTP não permitidos (POST, PUT, DELETE, etc.):**
    - Todos os providers (Python, Node.js, Java, PHP e C++) retornam erro 405 (Method Not Allowed) com mensagem JSON explicativa
    - A estrutura da mensagem de erro pode variar ligeiramente entre providers, mas todos incluem informações sobre o método permitido
    - Python, Java e C++ usam o campo `"error"` com mensagem descritiva: "Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint."
    - Node.js e PHP usam os campos `"erro"`, `"mensagem"` e `"metodo_permitido"` (Node.js também inclui `"metodo_solicitado"`)
  - **Parâmetro `cpf` ausente:**
    - Todos os providers retornam erro 400 (Bad Request) com mensagem JSON quando o parâmetro `cpf` não é fornecido
    - Todos os providers (Python, Node.js, Java, PHP e C++) usam o campo `"error"` com mensagem: "Parâmetro 'cpf' não fornecido"
  - **Endpoints não encontrados:**
    - Todos os providers retornam erro 404 (Not Found) para endpoints não encontrados
    - Todos os providers (Python, Node.js, Java, PHP e C++) usam o campo `"error"` com mensagem: "Endpoint não encontrado"
- ⚠️ **Formato de Resposta:** Todos os providers retornam o campo `"valido"` (em português) de forma consistente, facilitando a integração com múltiplos providers.
- O cliente Python (`ws_client.py`) aceita a porta como argumento de linha de comando e testa automaticamente dois CPFs: um válido (`11144477735`) e um inválido (`11111111111`).
- Todos os providers implementam a mesma lógica de validação de CPF, seguindo o algoritmo oficial brasileiro.
- Todos os providers suportam o mesmo endpoint: `GET /validar?cpf=XXXXXXXXXXX`
- A resposta JSON usa o campo `"valido"` (boolean) para indicar se o CPF é válido ou não, de forma consistente em todos os providers.
