# WS2 - Web Service de Validação de CPF

Este projeto implementa um Web Service para validação de CPF (Cadastro de Pessoa Física) com providers em múltiplas linguagens e um cliente em Python.

## Estrutura do Projeto

```
WS2/
├── ws provider/          # Servidores (providers) do Web Service
│   ├── provider.py       # Provider em Python (porta 8000)
│   ├── provider.js       # Provider em Node.js (porta 8081)
│   ├── provider.php      # Provider em PHP (porta 8081)
│   └── Provider.java     # Provider em Java (porta 8082)
└── ws client/            # Cliente para testar o Web Service
    └── client.py         # Cliente em Python
```

## Funcionalidades

O Web Service oferece dois endpoints para validação de CPF:

### GET /cpf?cpf=XXXXXXXXXXX
Valida um CPF via parâmetro de query string.

**Exemplo:**
```bash
curl "http://localhost:8000/cpf?cpf=11144477735"
```

**Resposta:**
```json
{
  "cpf": "11144477735",
  "valid": true
}
```

### POST /cpf
Valida um CPF enviado no corpo da requisição em formato JSON.

**Exemplo:**
```bash
curl -X POST http://localhost:8000/cpf \
  -H "Content-Type: application/json" \
  -d '{"cpf": "11144477735"}'
```

**Resposta:**
```json
{
  "cpf": "11144477735",
  "valid": true
}
```

## Como Executar

### Provider Python (Recomendado)

**Pré-requisitos:** Python 3.x instalado

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS2/ws provider"
```

2. Inicie o servidor:
```bash
python3 provider.py
```

Você verá a mensagem: `Servidor rodando em http://localhost:8000 ...`

3. Em outro terminal, execute o cliente:
```bash
cd "Módulo5 - WebServices/WS2/ws client"
python3 client.py
```

O cliente testará os endpoints GET e POST automaticamente.

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider Node.js

**Pré-requisitos:** Node.js instalado

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS2/ws provider"
```

2. Inicie o servidor:
```bash
node provider.js
```

Você verá a mensagem: `Servidor JS rodando em http://localhost:8081`

3. Para testar, você pode:
   - Usar o cliente Python (após atualizar a porta no código)
   - Usar curl:
     ```bash
     curl "http://localhost:8081/cpf?cpf=11144477735"
     curl -X POST http://localhost:8081/cpf -H "Content-Type: application/json" -d '{"cpf": "11144477735"}'
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider PHP

**Pré-requisitos:** PHP instalado (versão 7.0 ou superior)

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS2/ws provider"
```

2. Inicie o servidor:
```bash
php -S localhost:8081 provider.php
```

Você verá a mensagem indicando que o servidor está rodando.

3. Para testar, você pode:
   - Usar o cliente Python (após atualizar a porta no código)
   - Usar curl:
     ```bash
     curl "http://localhost:8081/cpf?cpf=11144477735"
     curl -X POST http://localhost:8081/cpf -H "Content-Type: application/json" -d '{"cpf": "11144477735"}'
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

---

### Provider Java

**Pré-requisitos:** JDK instalado (Java 8 ou superior)

1. Abra um terminal e navegue até a pasta do provider:
```bash
cd "Módulo5 - WebServices/WS2/ws provider"
```

2. Compile o código:
```bash
javac Provider.java
```

Isso criará o arquivo `Provider.class` na mesma pasta.

3. Execute o servidor:
```bash
java Provider
```

Você verá a mensagem: `Java CPF Provider rodando em http://localhost:8082`

4. Para testar, você pode:
   - Usar o cliente Python (após atualizar a porta no código)
   - Usar curl:
     ```bash
     curl "http://localhost:8082/cpf?cpf=11144477735"
     curl -X POST http://localhost:8082/cpf -H "Content-Type: application/json" -d '{"cpf": "11144477735"}'
     ```

**Para parar o servidor:** Pressione `Ctrl+C` no terminal onde o servidor está rodando.

**Nota:** Se você quiser limpar os arquivos compilados após usar:
```bash
rm Provider.class
```

---

### Testando com o Cliente Python

O cliente padrão (`client.py`) está configurado para usar o provider Python na porta 8000. Para usar outros providers, você precisa editar o arquivo `client.py` e alterar a URL:

- Para Node.js/PHP (porta 8081): `"http://localhost:8081/cpf"`
- Para Java (porta 8082): `"http://localhost:8082/cpf"`

## Algoritmo de Validação de CPF

O algoritmo implementado segue o padrão oficial de validação de CPF brasileiro:

1. Remove caracteres não numéricos
2. Verifica se possui 11 dígitos
3. Verifica se não são todos os dígitos iguais
4. Calcula o primeiro dígito verificador
5. Calcula o segundo dígito verificador
6. Compara com os dígitos informados

## Exemplos de CPF para Teste

- **Válido:** `11144477735`
- **Válido:** `12345678909`
- **Inválido:** `11111111111` (todos os dígitos iguais)
- **Inválido:** `12345678900` (dígitos verificadores incorretos)

## Tecnologias Utilizadas

- **Python:** `http.server` (BaseHTTPRequestHandler) - Porta 8000
- **Node.js:** `http` (módulo nativo) - Porta 8081
- **PHP:** Built-in server (`php -S`) - Porta 8081
- **Java:** `com.sun.net.httpserver` - Porta 8082

## Observações Importantes

- ⚠️ **Portas:** Cada provider usa uma porta diferente. Certifique-se de que apenas um provider esteja rodando por vez em cada porta, ou altere as portas se necessário.
- O cliente padrão (`client.py`) está configurado para usar o provider Python na porta 8000
- Para usar outros providers, altere a URL no arquivo `client.py` (linhas 11 e 26)
- Todos os providers implementam a mesma lógica de validação de CPF
- Todos os providers suportam os mesmos endpoints: `GET /cpf?cpf=XXXXXXXXXXX` e `POST /cpf` com JSON no body
