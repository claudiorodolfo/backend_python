# WS4 - Valida CPF (Vários Clientes)

Este projeto contém um web service que valida CPF e clientes em Python, Java, JavaScript, PHP e C++ para testá-lo.

## 📁 Estrutura do Projeto

```
WS4 -Valida CPF (Varios Clientes)/
├── ws provider/
│   ├── provider.py          # Servidor HTTP (web service)
│   └── matar_servidor.py    # Script utilitário para encerrar processos em uma porta específica
└── ws client/
    ├── client.py            # Cliente Python
    ├── client.js            # Cliente JavaScript (Node.js)
    ├── Client.java          # Cliente Java
    ├── client.php           # Cliente PHP
    └── client.cpp           # Cliente C++
```

## 📋 Pré-requisitos

### Python 3
- **Necessário para:** Servidor e cliente Python
- **Biblioteca adicional:** `requests` (para o cliente Python)

**Instalação do Python:**

**No macOS:**
```bash
# Python geralmente já vem instalado. Verifique com:
python3 --version

# Se não estiver instalado, instale via Homebrew:
brew install python3
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

**No Linux (CentOS/RHEL):**
```bash
sudo yum install python3 python3-pip
```

**Instalação da biblioteca requests:**
```bash
pip3 install requests
```

**Verificar instalação:**
```bash
python3 --version
pip3 show requests
```

---

### Java JDK
- **Necessário para:** Cliente Java
- **Versão mínima:** JDK 8 ou superior

**Instalação do Java:**

**No macOS:**
```bash
# Instale via Homebrew:
brew install openjdk

# Ou baixe do site oficial:
# https://www.oracle.com/java/technologies/downloads/
# https://adoptium.net/
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install default-jdk
```

**No Linux (CentOS/RHEL):**
```bash
sudo yum install java-1.8.0-openjdk-devel
```

**Verificar instalação:**
```bash
java -version
javac -version
```

**Nota:** Certifique-se de que tanto `java` quanto `javac` estão disponíveis. Se apenas `java` estiver instalado, você precisa instalar o JDK (Java Development Kit), não apenas o JRE (Java Runtime Environment).

---

### Node.js
- **Necessário para:** Cliente JavaScript
- **Versão mínima:** Node.js 18.0 ou superior (para suporte nativo ao `fetch`)

**Instalação do Node.js:**

**No macOS:**
```bash
# Instale via Homebrew:
brew install node

# Ou baixe do site oficial:
# https://nodejs.org/
```

**No Linux (Ubuntu/Debian):**
```bash
# Usando NodeSource (recomendado):
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Ou via apt:
sudo apt-get update
sudo apt-get install nodejs npm
```

**No Linux (CentOS/RHEL):**
```bash
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install -y nodejs
```

**Verificar instalação:**
```bash
node --version
```

**Nota:** Se você estiver usando Node.js versão anterior à 18, pode precisar instalar um pacote como `node-fetch` ou atualizar o Node.js.

---

### PHP
- **Necessário para:** Cliente PHP
- **Versão mínima:** PHP 7.0 ou superior
- **Extensão necessária:** `php-json` (geralmente já incluída)

**Instalação do PHP:**

**No macOS:**
```bash
# Instale via Homebrew:
brew install php
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install php php-json
```

**No Linux (CentOS/RHEL):**
```bash
sudo yum install php php-json
```

**Verificar instalação:**
```bash
php --version
```

**Nota:** O PHP não vem pré-instalado no macOS. Se o comando retornar "command not found", siga as instruções de instalação acima.

---

### C++ (g++ ou clang++)
- **Necessário para:** Cliente C++
- **Bibliotecas necessárias:**
  - `libcurl` (para requisições HTTP)
  - `nlohmann/json` (header-only, para parsing JSON)

**Instalação do Compilador C++:**

**No macOS:**
```bash
# Instale as ferramentas de linha de comando do Xcode:
xcode-select --install

# Ou instale via Homebrew:
brew install gcc

# Instale libcurl (geralmente já vem instalado, mas pode precisar):
brew install curl

# Para nlohmann/json:
brew install nlohmann-json
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install build-essential libcurl4-openssl-dev

# Para nlohmann/json, baixe o header de:
# https://github.com/nlohmann/json/releases
# E coloque json.hpp na mesma pasta do client.cpp
```

**No Linux (CentOS/RHEL):**
```bash
sudo yum groupinstall "Development Tools"
sudo yum install libcurl-devel

# Para nlohmann/json, baixe o header de:
# https://github.com/nlohmann/json/releases
```

**Verificar instalação:**
```bash
g++ --version
# ou
clang++ --version
curl-config --version
```

**Nota sobre nlohmann/json:**
- No macOS com Homebrew, você pode usar `brew install nlohmann-json` e incluir com `#include <nlohmann/json.hpp>`
- No Linux, baixe `json.hpp` de https://github.com/nlohmann/json/releases e coloque na mesma pasta do `client.cpp`
- Ou ajuste o `#include` no código para apontar para o caminho correto

---

## 🚀 Como Executar

### 1. Iniciar o Servidor (Provider)

O servidor é um web service HTTP que valida CPF através de endpoints GET e POST.

**Passo a passo:**

1. Abra um terminal e navegue até a pasta do provider:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws provider"
   ```

2. Execute o servidor:
   ```bash
   python3 provider.py
   ```

3. Você verá a mensagem:
   ```
   Servidor iniciado em http://127.0.0.1:8080
   ```

**Importante:** 
- Mantenha este terminal aberto enquanto testa os clientes
- O servidor ficará rodando até você pressionar `Ctrl+C`
- Certifique-se de que a porta 8080 não está em uso por outro processo

**Verificar se o servidor está rodando:**
```bash
curl http://localhost:8080/validar?cpf=11144477735
```

**Se a porta 8080 estiver em uso:**
Use o script `matar_servidor.py` para encerrar processos na porta 8080:
```bash
python3 matar_servidor.py 8080
```

---

### 2. Executar os Clientes

Abra **outro terminal** (deixe o servidor rodando no primeiro terminal) e execute um dos clientes abaixo.

#### 📦 Cliente Python

**Pré-requisitos:**
- Python 3.6 ou superior
- Biblioteca `requests` instalada

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. Execute o cliente:
   ```bash
   python3 client.py
   ```

**O que o programa faz:**
- Faz uma requisição GET com um CPF de exemplo
- Exibe o resultado da validação formatado

**Exemplo de saída:**
```
==============================
RESULTADO VALIDAR CPF: True
==============================
```

---

#### ☕ Cliente Java

**Pré-requisitos:**
- Java JDK 8 ou superior
- Compilador `javac` e runtime `java` no PATH

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
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
- Executa requisição GET
- Exibe a resposta JSON em uma linha

**Exemplo de saída:**
```
GET => {"cpf": "11144477735", "valido": true}
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
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. Execute o script:
   ```bash
   node client.js
   ```

**O que o programa faz:**
- Usa `async/await` para fazer requisições assíncronas
- Faz requisição GET usando a API `fetch`
- Exibe mensagens de progresso e resultados formatados

**Exemplo de saída:**
```
Validando via GET...
[GET] Resposta: { cpf: '11144477735', valido: true }
CPF: 11144477735 | válido: true
```

---

#### 🐘 Cliente PHP

**Pré-requisitos:**
- PHP 7.0 ou superior
- Extensão `php-json` (geralmente já incluída)

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. Execute o script:
   ```bash
   php client.php
   ```

**O que o programa faz:**
- Usa `file_get_contents()` para fazer requisições HTTP
- Executa GET
- Exibe a resposta JSON bruta

**Exemplo de saída:**
```
GET:
{"cpf":"11144477735","valido":true}
```

---

#### ⚙️ Cliente C++

**Pré-requisitos:**
- Compilador C++ (g++ ou clang++)
- Biblioteca libcurl (para requisições HTTP)
- Biblioteca nlohmann/json (header-only, para parsing JSON)

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. **Importante:** Certifique-se de que o arquivo `json.hpp` está disponível:
   - **macOS (Homebrew):** Se instalou via `brew install nlohmann-json`, o header estará em `/opt/homebrew/include/nlohmann/json.hpp` ou similar. Ajuste o `#include` no código se necessário.
   - **Linux:** Baixe `json.hpp` de https://github.com/nlohmann/json/releases e coloque na mesma pasta do `client.cpp`

3. Compile o programa:
   ```bash
   g++ -o client client.cpp -lcurl
   ```
   Ou com clang++:
   ```bash
   clang++ -o client client.cpp -lcurl
   ```
   
   **No macOS com nlohmann/json via Homebrew:**
   ```bash
   g++ -o client client.cpp -lcurl -I/opt/homebrew/include
   ```

4. Execute o programa compilado:
   ```bash
   ./client
   ```

**O que o programa faz:**
- Solicita um CPF ao usuário via entrada padrão
- Faz requisição GET usando libcurl
- Parseia a resposta JSON usando nlohmann/json
- Exibe se o CPF é válido ou não

**Exemplo de saída:**
```
Digite um CPF (somente dígitos): 11144477735
[GET] CPF 11144477735 válido
```

---

## 🔧 Endpoints do Web Service

### GET /validar
Valida CPF via query parameter:
```
http://localhost:8080/validar?cpf=11144477735
```

### Resposta
```json
{
  "cpf": "11144477735",
  "valido": true
}
```

**Nota:** O endpoint POST não está implementado no servidor atual.

---

## ⚠️ Troubleshooting

### Problemas Gerais

**Erro de conexão:**
- Certifique-se de que o servidor está rodando antes de executar os clientes
- Verifique se o servidor está em `http://localhost:8080`
- Teste com: `curl http://localhost:8080/validar?cpf=11144477735`

**Porta 8080 em uso:**
- Use o script utilitário `matar_servidor.py`:
  ```bash
  cd "ws provider"
  python3 matar_servidor.py 8080
  ```
- Ou manualmente:
  - Verifique processos usando a porta: `lsof -ti:8080`
  - Encerre o processo: `kill -9 $(lsof -ti:8080)`
- Ou altere a porta no `provider.py` (linha 63) e atualize os clientes

**Comportamento inesperado:**
- Limpe o cache do Python: `find . -name "__pycache__" -type d -exec rm -rf {} +`
- Reinicie o servidor completamente
- Verifique se não há múltiplas instâncias do servidor rodando

### Problemas Específicos por Cliente

**Python:**
- `python3: command not found`: Instale Python 3 ou use `python` em vez de `python3`
- `ModuleNotFoundError: No module named 'requests'`: Instale com `pip3 install requests`
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
- `php: command not found`: O PHP não vem pré-instalado no macOS
  - **macOS:** Instale via Homebrew: `brew install php`
  - **Linux (Ubuntu/Debian):** `sudo apt-get install php`
  - **Linux (CentOS/RHEL):** `sudo yum install php`
  - Após instalar, verifique com: `php --version`
- Erro de extensão JSON: Geralmente já incluída, mas pode precisar habilitar no `php.ini`

**C++:**
- `g++: command not found`: Instale um compilador C++
  - macOS: `xcode-select --install` ou `brew install gcc`
  - Linux: `sudo apt-get install build-essential`
- Erro `json.hpp: No such file`:
  - macOS: `brew install nlohmann-json` e ajuste o `#include` ou use `-I/opt/homebrew/include`
  - Linux: Baixe de https://github.com/nlohmann/json/releases e coloque na mesma pasta
- Erro `undefined reference to 'curl_*'`:
  - Instale libcurl: `brew install curl` (macOS) ou `sudo apt-get install libcurl4-openssl-dev` (Linux)
  - Certifique-se de usar `-lcurl` na compilação
- Erro de compilação: Verifique se todas as dependências estão instaladas

---

## 🧪 Testando com cURL

Você também pode testar o web service diretamente com cURL:

```bash
# GET
curl "http://localhost:8080/validar?cpf=11144477735"
```

---

## 🛠️ Utilitários

### matar_servidor.py

Script utilitário para encerrar processos que estão usando uma porta específica. Útil quando o servidor não pode ser iniciado porque a porta já está em uso.

**Como usar:**
```bash
cd "ws provider"
python3 matar_servidor.py <porta>
```

**Exemplo:**
```bash
python3 matar_servidor.py 8000
```

**O que o script faz:**
- Recebe a porta como parâmetro na linha de comando
- Encontra todos os processos escutando na porta especificada
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

### Liberar Porta 8080 (se necessário)
```bash
cd "ws provider"
python3 matar_servidor.py 8080
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

**Nota:** Todos os clientes devem ser executados enquanto o servidor está rodando. O servidor atual implementa apenas o método GET no endpoint `/validar`.

---

## 📝 Notas Adicionais

- O servidor valida CPF usando o algoritmo oficial brasileiro
- CPFs com todos os dígitos iguais são considerados inválidos
- O CPF deve ter exatamente 11 dígitos (após remover caracteres não numéricos)
- O cliente Python usa a biblioteca `requests` para facilitar as requisições HTTP
- Todos os clientes fazem requisições tanto GET quanto POST para demonstrar ambos os métodos
