# WS4 - Valida CPF (Vários Clientes)

Este projeto contém um web service que valida CPF e múltiplos clientes em diferentes linguagens (Python, Java, JavaScript, PHP e C++) para demonstrar a integração com o serviço.

## 📁 Estrutura do Projeto

```
WS4 -Valida CPF (Varios Clientes)/
├── ws provider/
│   ├── provider.py          # Servidor HTTP (web service)
│   └── matar_servidor.py    # Script utilitário para encerrar processos em uma porta específica
└── ws client/
    ├── client.py            # Cliente Python
    ├── client.js            # Cliente JavaScript (Node.js)
    ├── CPFCliente.java      # Cliente Java
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
- **Biblioteca adicional:** `org.json` (JSONObject) - pode ser necessário adicionar ao classpath

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

**Biblioteca JSON para Java:**
O cliente Java usa `org.json.JSONObject`. Você pode baixar o JAR de:
- https://mvnrepository.com/artifact/org.json/json
- Ou incluir no classpath ao compilar: `javac -cp ".:json.jar" CPFCliente.java`

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
- **Versão mínima:** C++11
- **Bibliotecas necessárias:**
  - `libcurl` (para requisições HTTP)
  - `nlohmann-json` (biblioteca JSON para C++)

**Instalação das dependências:**

**No macOS (usando Homebrew):**
```bash
# Instale as ferramentas de linha de comando do Xcode (se necessário):
xcode-select --install

# Instale as dependências:
brew install nlohmann-json curl

# Verifique se o compilador está instalado:
g++ --version
# ou
clang++ --version
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install libcurl4-openssl-dev nlohmann-json3-dev g++
```

**No Linux (Fedora/RHEL):**
```bash
sudo dnf install libcurl-devel json-devel gcc-c++
```

**No Windows (usando vcpkg ou MSYS2/MinGW):**
```bash
# Com vcpkg:
vcpkg install curl nlohmann-json

# Ou com MSYS2/MinGW:
pacman -S mingw-w64-x86_64-curl mingw-w64-x86_64-nlohmann-json
```

**Verificar instalação:**
```bash
g++ --version
# ou
clang++ --version
curl-config --version
```

**Nota sobre nlohmann/json:**
- No macOS com Homebrew: `brew install nlohmann-json` e use `#include <nlohmann/json.hpp>`
- No Linux (Ubuntu/Debian): `sudo apt-get install nlohmann-json3-dev` (instalação via pacote)
- No Linux (Fedora/RHEL): `sudo dnf install json-devel` (instalação via pacote)
- O código usa C++11 (`-std=c++11` na compilação)

---

## 🚀 Como Executar

### 1. Iniciar o Servidor (Provider)

O servidor é um web service HTTP que valida CPF através do endpoint GET.

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
- Faz uma requisição GET com um CPF de exemplo (`11144477735`)
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
- Biblioteca `org.json` (JSONObject) - pode precisar adicionar ao classpath

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. Compile o arquivo Java:
   ```bash
   javac CPFCliente.java
   ```
   Se precisar da biblioteca JSON:
   ```bash
   javac -cp ".:json.jar" CPFCliente.java
   ```
   Isso gerará o arquivo `CPFCliente.class` (bytecode Java).

3. Execute o programa compilado:
   ```bash
   java CPFCliente
   ```
   Se precisar da biblioteca JSON:
   ```bash
   java -cp ".:json.jar" CPFCliente
   ```

**O que o programa faz:**
- Conecta ao servidor via HTTP
- Executa requisição GET com CPF `11144477735`
- Exibe a resposta JSON e o resultado da validação

**Exemplo de saída:**
```
GET => {"cpf":"11144477735","valido":true}
RESULTADO VALIDAR CPF: true
```

**Nota:** Se você já compilou anteriormente e o arquivo `CPFCliente.class` existe, pode executar diretamente com `java CPFCliente` sem precisar recompilar.

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
- Valida o CPF `11144477735`
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
- Executa GET com CPF `11144477735`
- Exibe o resultado formatado

**Exemplo de saída:**
```
GET:
==============================
RESULTADO VALIDAR CPF: true
==============================
```

---

#### ⚙️ Cliente C++

**Pré-requisitos:**
- Compilador C++11 (g++ ou clang++)
- Biblioteca libcurl (para requisições HTTP)
- Biblioteca nlohmann-json (header-only, para parsing JSON)

**Instalação das dependências:**

**No macOS (usando Homebrew):**
```bash
brew install nlohmann-json curl
```

**No Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install libcurl4-openssl-dev nlohmann-json3-dev g++
```

**No Linux (Fedora/RHEL):**
```bash
sudo dnf install libcurl-devel json-devel gcc-c++
```

**No Windows (usando vcpkg ou MSYS2/MinGW):**
```bash
vcpkg install curl nlohmann-json
```

**Passo a passo:**

1. Navegue até a pasta do cliente:
   ```bash
   cd "Módulo5 - WebServices/WS4 -Valida CPF (Varios Clientes)/ws client"
   ```

2. Compile o programa:
   ```bash
   g++ -std=c++11 -o client client.cpp -lcurl
   ```
   
   Ou com clang++:
   ```bash
   clang++ -std=c++11 -o client client.cpp -lcurl
   ```
   
   **No Windows:**
   ```bash
   g++ -std=c++11 -o client.exe client.cpp -lcurl
   ```

3. Execute o programa compilado:
   ```bash
   ./client
   ```
   
   **No Windows:**
   ```bash
   client.exe
   ```

**O que o programa faz:**
- Valida os CPFs `11144477735` e `11111111111` (hardcoded no código)
- Faz requisição GET usando libcurl
- Parseia a resposta JSON usando nlohmann/json
- Exibe se cada CPF é válido ou não

**Exemplo de saída:**
```
CPF 11144477735 válido
CPF 11111111111 inválido
```

**Nota:** O código inclui comentários detalhados no início do arquivo `client.cpp` com todas as instruções de instalação e compilação para diferentes sistemas operacionais.

---

## 🔧 Endpoints do Web Service

### GET /validar
Valida CPF via query parameter:
```
http://localhost:8080/validar?cpf=11144477735
```

**Resposta:**
```json
{
  "cpf": "11144477735",
  "valido": true
}
```

**Nota:** O servidor implementa apenas o método GET. Requisições POST retornam erro 405 (Method Not Allowed).

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
- Ou altere a porta no `provider.py` (linha 69) e atualize os clientes

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
- `package org.json does not exist`: Baixe o JAR de https://mvnrepository.com/artifact/org.json/json e inclua no classpath
- Erro de compilação: Verifique se está no diretório correto com `CPFCliente.java`

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
  - Linux (Ubuntu/Debian): `sudo apt-get install g++`
  - Linux (Fedora/RHEL): `sudo dnf install gcc-c++`
- Erro `json.hpp: No such file` ou `nlohmann/json.hpp: No such file`:
  - macOS: `brew install nlohmann-json`
  - Linux (Ubuntu/Debian): `sudo apt-get install nlohmann-json3-dev`
  - Linux (Fedora/RHEL): `sudo dnf install json-devel`
  - Certifique-se de usar `-std=c++11` na compilação
- Erro `undefined reference to 'curl_*'`:
  - macOS: `brew install curl` e use `-lcurl` na compilação
  - Linux (Ubuntu/Debian): `sudo apt-get install libcurl4-openssl-dev` e use `-lcurl` na compilação
  - Linux (Fedora/RHEL): `sudo dnf install libcurl-devel` e use `-lcurl` na compilação
- Erro de compilação: Verifique se todas as dependências estão instaladas e use `-std=c++11`
- Comando de compilação completo: `g++ -std=c++11 -o client client.cpp -lcurl`

---

## 🧪 Testando com cURL

Você também pode testar o web service diretamente com cURL:

```bash
# GET
curl "http://localhost:8080/validar?cpf=11144477735"
```

**Resposta esperada:**
```json
{"cpf": "11144477735", "valido": true}
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
python3 matar_servidor.py 8080
```

**O que o script faz:**
- Recebe a porta como parâmetro na linha de comando
- Encontra todos os processos escutando na porta especificada
- Encerra esses processos usando `kill -9`
- Exibe mensagens informativas sobre o processo

**Exemplo de saída:**
```
Processos encontrados na porta 8080: 12345
Processo 12345 encerrado com sucesso.
Porta 8080 liberada.
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
cd "ws client" && javac CPFCliente.java && java CPFCliente
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
cd "ws client" && g++ -std=c++11 -o client client.cpp -lcurl && ./client
```

**Nota:** Todos os clientes devem ser executados enquanto o servidor está rodando. O servidor atual implementa apenas o método GET no endpoint `/validar`.

---

## 📝 Notas Adicionais

- O servidor valida CPF usando o algoritmo oficial brasileiro
- CPFs com todos os dígitos iguais são considerados inválidos
- O CPF deve ter exatamente 11 dígitos (após remover caracteres não numéricos como pontos e traços)
- O servidor aceita CPF com ou sem formatação (pontos e traços são removidos automaticamente)
- O cliente Python usa a biblioteca `requests` para facilitar as requisições HTTP
- Todos os clientes fazem requisições GET para demonstrar a integração com o web service
- O servidor retorna erro 405 (Method Not Allowed) para requisições POST

---

## 🔍 Algoritmo de Validação de CPF

O servidor implementa o algoritmo oficial de validação de CPF brasileiro:

1. Remove caracteres não numéricos (pontos e traços)
2. Verifica se o CPF tem exatamente 11 dígitos
3. Verifica se todos os dígitos são iguais (CPFs como 111.111.111-11 são inválidos)
4. Calcula o primeiro dígito verificador
5. Calcula o segundo dígito verificador
6. Compara os dígitos calculados com os dois últimos dígitos do CPF

**Exemplos de CPFs válidos:**
- `11144477735`
- `123.456.789-09`

**Exemplos de CPFs inválidos:**
- `11111111111` (todos os dígitos iguais)
- `12345678901` (dígitos verificadores incorretos)
- `123` (menos de 11 dígitos)
