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

**Resposta (Python, Java, PHP, C++):**
```json
{
  "cpf": "11144477735",
  "valido": true
}
```

**Resposta (Node.js):**
```json
{
  "cpf": "11144477735",
  "valid": true
}
```

**Nota:** Este Web Service aceita apenas requisições GET. Requisições POST retornarão erro 405 (Method Not Allowed).

**⚠️ Importante:** O provider Node.js retorna o campo `"valid"` (em inglês), enquanto os demais providers retornam `"valido"` (em português).

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

Você verá a mensagem: `Servidor iniciado em http://127.0.0.1:8080`

5. Para testar, você pode:
   - Usar o cliente Python:
     ```bash
     cd "Módulo5 - WebServices/WS5 - Valida CPF (Varios Provedores)/ws client"
     python3 ws_client.py 8080
     ```
   - Usar curl:
     ```bash
     curl "http://localhost:8080/validar?cpf=11144477735"
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

| Provider | Porta | Endpoint | Campo de Resposta |
|----------|-------|------------|------------|
| Python   | 8080  | `/validar` | `"valido"` |
| Node.js  | 8081  | `/validar` | `"valido"` |
| Java     | 8082  | `/validar` | `"valido"` |
| PHP      | 8083  | `/validar` | `"valido"` |
| C++      | 8084  | `/validar` | `"valido"` |

**⚠️ Atenção:** Os providers Python e Java usam a mesma porta (8080). Certifique-se de executar apenas um por vez, ou altere a porta de um deles se necessário.

## Tecnologias Utilizadas

- **Python:** `http.server` (BaseHTTPRequestHandler) - Porta 8080
- **Node.js:** `http` (módulo nativo) - Porta 8081
- **Java:** `com.sun.net.httpserver` e `org.json` - Porta 8082
- **PHP:** Built-in server (`php -S`) - Porta 8083
- **C++:** `cpp-httplib` (httplib.h) - Porta 8084

## Observações Importantes

- ⚠️ **Portas:** Cada provider usa uma porta diferente (exceto Python e Java que compartilham a porta 8080). Certifique-se de que apenas um provider esteja rodando por vez em cada porta, ou altere as portas se necessário.
- ⚠️ **Método HTTP:** Este Web Service aceita apenas requisições GET. Requisições POST retornarão erro 405 (Method Not Allowed).
- ⚠️ **Formato de Resposta:** O provider Node.js retorna o campo `"valid"` (em inglês), enquanto todos os outros providers retornam `"valido"` (em português). Isso deve ser considerado ao desenvolver clientes que precisem trabalhar com múltiplos providers.
- O cliente Python (`ws_client.py`) aceita a porta como argumento de linha de comando e testa automaticamente dois CPFs: um válido e um inválido.
- Todos os providers implementam a mesma lógica de validação de CPF.
- Todos os providers suportam o mesmo endpoint: `GET /validar?cpf=XXXXXXXXXXX`
- A resposta JSON usa um campo boolean para indicar se o CPF é válido ou não (veja a tabela acima para o nome exato do campo por provider).
