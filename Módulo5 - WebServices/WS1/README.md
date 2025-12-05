# Web Service de Validação de CPF

Este projeto contém um web service que valida CPF e clientes em Python, Java, JavaScript, PHP e C++ para testá-lo.

## 📁 Estrutura do Projeto

```
WS1/
├── ws provider/
│   ├── provider.py          # Servidor HTTP (web service)
│   └── matar_servidor.py    # Script utilitário para encerrar processos na porta 8000
└── ws client/
    ├── client.py            # Cliente Python
    ├── client.js            # Cliente JavaScript (Node.js)
    ├── Client.java          # Cliente Java
    ├── client.php           # Cliente PHP
    └── client.cpp           # Cliente C++
```

## 📋 Pré-requisitos

- **Python 3** (para o servidor e cliente Python)
- **Java JDK** (para o cliente Java)
- **Node.js** (opcional, para o cliente JavaScript)
- **PHP** (opcional, para o cliente PHP)
- **C++** com libcurl e nlohmann/json (opcional, para o cliente C++)

## 🚀 Como Executar

### 1. Iniciar o Servidor (Provider)

O servidor é um web service HTTP que valida CPF através de endpoints GET e POST.

**Passo a passo:**

1. Abra um terminal e navegue até a pasta do provider:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws provider"
   ```

2. Execute o servidor:
   ```bash
   python3 provider.py
   ```

3. Você verá a mensagem:
   ```
   Servidor rodando em http://localhost:8000 ...
   ```

**Importante:** 
- Mantenha este terminal aberto enquanto testa os clientes
- O servidor ficará rodando até você pressionar `Ctrl+C`
- Certifique-se de que a porta 8000 não está em uso por outro processo

**Verificar se o servidor está rodando:**
```bash
curl http://localhost:8000/cpf?numero=11144477735
```

**Se a porta 8000 estiver em uso:**
Use o script `matar_servidor.py` para encerrar processos na porta 8000:
```bash
python3 matar_servidor.py
```

---

### 2. Executar os Clientes

Abra **outro terminal** (deixe o servidor rodando no primeiro terminal) e execute um dos clientes abaixo.

#### 📦 Cliente Python

**Pré-requisitos:**
- Python 3.6 ou superior
- Bibliotecas padrão (urllib, json) - já incluídas no Python

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws client"
   ```

2. Execute o cliente:
   ```bash
   python3 client.py
   ```

**O que o programa faz:**
- Faz uma requisição POST com um CPF de exemplo
- Faz uma requisição GET com o mesmo CPF
- Exibe as respostas formatadas em JSON

**Verificar instalação do Python:**
```bash
python3 --version
```

---

#### ☕ Cliente Java

**Pré-requisitos:**
- Java JDK 8 ou superior
- Compilador `javac` e runtime `java` no PATH

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws client"
   ```

2. Compile o arquivo Java:
   ```bash
   javac Client.java
   ```
   Isso gerará o arquivo `Client.class` (bytecode Java).

3. Execute o programa compilado:
   ```bash
   java Client
   ```

**O que o programa faz:**
- Conecta ao servidor via HTTP
- Executa requisições GET e POST
- Exibe as respostas JSON em uma linha

**Verificar instalação do Java:**
```bash
java -version
javac -version
```

**Nota:** Se você já compilou anteriormente e o arquivo `Client.class` existe, pode executar diretamente com `java Client` sem precisar recompilar.

---

#### 🟢 Cliente JavaScript (Node.js)

**Pré-requisitos:**
- Node.js 18.0 ou superior (para suporte nativo ao `fetch`)
- NPM não é necessário (usa apenas APIs nativas do Node.js)

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws client"
   ```

2. Execute o script:
   ```bash
   node client.js
   ```

**O que o programa faz:**
- Usa `async/await` para fazer requisições assíncronas
- Faz requisições GET e POST usando a API `fetch`
- Exibe mensagens de progresso e resultados formatados

**Verificar instalação do Node.js:**
```bash
node --version
```

**Nota:** Se você estiver usando Node.js versão anterior à 18, pode precisar instalar um pacote como `node-fetch` ou atualizar o Node.js.

---

#### 🐘 Cliente PHP

**Pré-requisitos:**
- PHP 7.0 ou superior
- Extensão `php-json` (geralmente já incluída)

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws client"
   ```

2. Execute o script:
   ```bash
   php client.php
   ```

**O que o programa faz:**
- Usa `file_get_contents()` para fazer requisições HTTP
- Executa GET e POST sequencialmente
- Exibe as respostas JSON brutas

**Verificar instalação do PHP:**
```bash
php --version
```

**Nota:** No macOS, o PHP pode precisar ser instalado via Homebrew:
```bash
brew install php
```

---

#### ⚙️ Cliente C++

**Pré-requisitos:**
- Compilador C++ (g++ ou clang++)
- Biblioteca libcurl (para requisições HTTP)
- Biblioteca nlohmann/json (header-only, para parsing JSON)

**Instalação das dependências:**

**No macOS (via Homebrew):**
```bash
brew install curl
# Para nlohmann/json, baixe o header de: https://github.com/nlohmann/json/releases
# Ou use: brew install nlohmann-json
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get install libcurl4-openssl-dev
# Baixe json.hpp de: https://github.com/nlohmann/json/releases
```

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS1/ws client"
   ```

2. **Importante:** Certifique-se de que o arquivo `json.hpp` está no mesmo diretório ou ajuste o `#include` no código.

3. Compile o programa:
   ```bash
   g++ -o client client.cpp -lcurl
   ```
   Ou com clang++:
   ```bash
   clang++ -o client client.cpp -lcurl
   ```

4. Execute o programa compilado:
   ```bash
   ./client
   ```

**O que o programa faz:**
- Solicita um CPF ao usuário via entrada padrão
- Faz requisições GET e POST usando libcurl
- Parseia a resposta JSON usando nlohmann/json
- Exibe se o CPF é válido ou não

**Verificar instalação:**
```bash
g++ --version
curl-config --version
```

**Nota:** Se você encontrar erros de compilação relacionados ao `json.hpp`, baixe o arquivo de https://github.com/nlohmann/json/releases e coloque-o na mesma pasta do `client.cpp`.

---

## 📝 Exemplo de Saída

### Servidor (Provider)
```
Servidor rodando em http://localhost:8000 ...
```

### Cliente Python
```
POST:
{
  "cpf": "11144477735",
  "valido": true
}

GET:
{
  "cpf": "11144477735",
  "valido": true
}
```

### Cliente Java
```
GET => {"cpf": "11144477735", "valido": true}
POST => {"cpf": "11144477735", "valido": true}
```

### Cliente JavaScript (Node.js)
```
Validando via GET...
[GET] Resposta: { cpf: '11144477735', valido: true }
CPF: 11144477735 | válido: true
Validando via POST...
[POST] Resposta: { cpf: '11144477735', valido: true }
CPF: 11144477735 | válido: true
```

### Cliente PHP
```
GET:
{"cpf":"11144477735","valido":true}

POST:
{"cpf":"11144477735","valido":true}
```

### Cliente C++
```
Digite um CPF (somente dígitos): 11144477735
[GET] CPF 11144477735 válido
[POST] CPF 11144477735 válido
```

---

## 🔧 Endpoints do Web Service

### GET /cpf
Valida CPF via query parameter:
```
http://localhost:8000/cpf?numero=11144477735
```

### POST /cpf
Valida CPF via JSON no body:
```json
{
  "cpf": "11144477735"
}
```

### Resposta
```json
{
  "cpf": "11144477735",
  "valido": true
}
```

---

## ⚠️ Troubleshooting

### Problemas Gerais

**Erro de conexão:**
- Certifique-se de que o servidor está rodando antes de executar os clientes
- Verifique se o servidor está em `http://localhost:8000`
- Teste com: `curl http://localhost:8000/cpf?numero=11144477735`

**Porta 8000 em uso:**
- Use o script utilitário `matar_servidor.py`:
  ```bash
  cd "ws provider"
  python3 matar_servidor.py
  ```
- Ou manualmente:
  - Verifique processos usando a porta: `lsof -ti:8000`
  - Encerre o processo: `kill -9 $(lsof -ti:8000)`
- Ou altere a porta no `provider.py` (linha 77) e atualize os clientes

**Comportamento inesperado:**
- Limpe o cache do Python: `find . -name "__pycache__" -type d -exec rm -rf {} +`
- Reinicie o servidor completamente
- Verifique se não há múltiplas instâncias do servidor rodando

### Problemas Específicos por Cliente

**Python:**
- `python3: command not found`: Instale Python 3 ou use `python` em vez de `python3`
- Erro de módulo: Certifique-se de estar usando Python 3.6+

**Java:**
- `javac: command not found`: Instale o JDK (não apenas JRE)
- `java: command not found`: Adicione Java ao PATH ou instale o JDK
- Aviso de deprecação: É apenas informativo e não afeta a funcionalidade
- Erro de compilação: Verifique se está no diretório correto com `Client.java`

**JavaScript (Node.js):**
- `node: command not found`: Instale Node.js (https://nodejs.org/)
- `fetch is not defined`: Atualize para Node.js 18+ ou instale `node-fetch`
- Erro de módulo: Este cliente não usa npm, apenas APIs nativas

**PHP:**
- `php: command not found`: 
  - macOS: `brew install php`
  - Linux: `sudo apt-get install php` ou `sudo yum install php`
- Erro de extensão JSON: Geralmente já incluída, mas pode precisar habilitar no `php.ini`

**C++:**
- `g++: command not found`: Instale um compilador C++
  - macOS: `xcode-select --install` ou `brew install gcc`
  - Linux: `sudo apt-get install build-essential`
- Erro `json.hpp: No such file`:
  - Baixe de: https://github.com/nlohmann/json/releases
  - Coloque `json.hpp` na mesma pasta do `client.cpp`
- Erro `undefined reference to 'curl_*'`:
  - Instale libcurl: `brew install curl` (macOS) ou `sudo apt-get install libcurl4-openssl-dev` (Linux)
  - Certifique-se de usar `-lcurl` na compilação
- Erro de compilação: Verifique se todas as dependências estão instaladas

## 🧪 Testando com cURL

Você também pode testar o web service diretamente com cURL:

```bash
# GET
curl "http://localhost:8000/cpf?numero=11144477735"

# POST
curl -X POST "http://localhost:8000/cpf" \
  -H "Content-Type: application/json" \
  -d '{"cpf":"11144477735"}'
```

---

## 🛠️ Utilitários

### matar_servidor.py

Script utilitário para encerrar processos que estão usando a porta 8000. Útil quando o servidor não pode ser iniciado porque a porta já está em uso.

**Como usar:**
```bash
cd "ws provider"
python3 matar_servidor.py
```

**O que o script faz:**
- Encontra todos os processos escutando na porta 8000
- Encerra esses processos usando `kill -9`
- Exibe mensagens informativas sobre o processo

**Exemplo de saída:**
```
Processos encontrados na porta 8000: 12345
Processo 12345 encerrado com sucesso.
Porta 8000 liberada.
```

**Nota:** Este script funciona no macOS e Linux. No Windows, pode ser necessário usar comandos diferentes.

---

## ⚡ Resumo Rápido

### Iniciar Servidor
```bash
cd "ws provider"
python3 provider.py
```

### Liberar Porta 8000 (se necessário)
```bash
cd "ws provider"
python3 matar_servidor.py
```

### Executar Clientes (em outro terminal)

**Python:**
```bash
cd "ws client" && python3 client.py
```

**Java:**
```bash
cd "ws client" && javac Client.java && java Client
```

**JavaScript:**
```bash
cd "ws client" && node client.js
```

**PHP:**
```bash
cd "ws client" && php client.php
```

**C++:**
```bash
cd "ws client" && g++ -o client client.cpp -lcurl && ./client
```

**Nota:** Todos os clientes devem ser executados enquanto o servidor está rodando.
