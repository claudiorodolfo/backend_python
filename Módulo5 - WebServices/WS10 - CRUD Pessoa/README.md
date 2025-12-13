# WS10 - CRUD Pessoa

Sistema completo de CRUD (Create, Read, Update, Delete) para gerenciamento de pessoas através de uma API REST implementada em Python.

## 📋 Descrição

Este projeto implementa um Web Service RESTful para operações CRUD de pessoas. O sistema é composto por duas partes principais:

- **Provider (Servidor)**: API REST que expõe endpoints HTTP para gerenciar pessoas
- **Client (Cliente)**: Cliente Python e interface de linha de comando para interagir com a API

## 🏗️ Estrutura do Projeto

```
WS10 - CRUD Pessoa/
├── provider/              # Servidor Web Service
│   ├── ws_provider.py    # Servidor HTTP e handlers das requisições
│   ├── pessoa_service.py # Lógica de negócio e gerenciamento de pessoas
│   └── pessoa.py         # Entidade Pessoa
├── client/               # Cliente Web Service
│   ├── ws_client_pessoa.py # Cliente HTTP para comunicação com a API
│   └── run.py           # Interface de linha de comando (CLI)
└── README.md            # Este arquivo
```

## 📦 Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (para o cliente)

### Instalação de Dependências

```bash
pip install requests
```

## 🚀 Como Executar

### 1. Iniciar o Servidor (Provider)

Abra um terminal e execute:

```bash
cd "Módulo5 - WebServices/WS10 - CRUD Pessoa/provider"
python ws_provider.py
```

O servidor será iniciado em `http://127.0.0.1:8080`

Você verá a mensagem:
```
Servidor iniciado em http://127.0.0.1:8080
```

### 2. Executar o Cliente (Interface CLI)

Em outro terminal, execute:

```bash
cd "Módulo5 - WebServices/WS10 - CRUD Pessoa/client"
python run.py
```

Uma interface de menu interativa será exibida para gerenciar as pessoas.

## 🔌 Endpoints da API

A API expõe os seguintes endpoints:

### GET /pessoas
Lista todas as pessoas cadastradas.

**Exemplo:**
```
GET http://localhost:8080/pessoas
```

**Resposta (200 OK):**
```json
{
  "pessoas": [
    {
      "email": "joao@gmail.com",
      "nome": "João",
      "idade": 30,
      "altura": 1.75
    }
  ]
}
```

### GET /pessoas?email={email}
Busca uma pessoa específica por email.

**Exemplo:**
```
GET http://localhost:8080/pessoas?email=joao@gmail.com
```

**Resposta (200 OK):**
```json
{
  "pessoa": {
    "email": "joao@gmail.com",
    "nome": "João",
    "idade": 30,
    "altura": 1.75
  }
}
```

**Resposta (404 Not Found):**
```json
{
  "erro": "Pessoa não encontrada"
}
```

### POST /pessoas
Cria uma nova pessoa.

**Parâmetros (Query String):**
- `email` (obrigatório): Email da pessoa
- `nome` (opcional): Nome da pessoa
- `idade` (opcional): Idade da pessoa
- `altura` (opcional): Altura da pessoa

**Exemplo:**
```
POST http://localhost:8080/pessoas?email=joao@gmail.com&nome=João&idade=30&altura=1.75
```

**Resposta (201 Created):**
```json
{
  "pessoa": {
    "email": "joao@gmail.com",
    "nome": "João",
    "idade": 30,
    "altura": 1.75
  }
}
```

**Resposta (400 Bad Request):**
```json
{
  "erro": "Email é obrigatório"
}
```

### PUT /pessoas
Atualiza uma pessoa existente.

**Parâmetros (Query String):**
- `email` (obrigatório): Email da pessoa a ser atualizada
- `nome` (opcional): Novo nome
- `idade` (opcional): Nova idade
- `altura` (opcional): Nova altura

**Exemplo:**
```
PUT http://localhost:8080/pessoas?email=joao@gmail.com&nome=João Silva&idade=31&altura=1.76
```

**Resposta (200 OK):**
```json
{
  "pessoa": {
    "email": "joao@gmail.com",
    "nome": "João Silva",
    "idade": 31,
    "altura": 1.76
  }
}
```

**Resposta (404 Not Found):**
```json
{
  "erro": "Pessoa não encontrada"
}
```

### DELETE /pessoas?email={email}
Remove uma pessoa do sistema.

**Exemplo:**
```
DELETE http://localhost:8080/pessoas?email=joao@gmail.com
```

**Resposta (200 OK):**
```json
{
  "mensagem": "Pessoa apagada com sucesso"
}
```

**Resposta (404 Not Found):**
```json
{
  "erro": "Pessoa não encontrada"
}
```

## 💻 Uso do Cliente Python

### Usando a Interface CLI

Execute `python run.py` e use o menu interativo:

```
==================================================
MENU - CRUD PESSOA
==================================================
1. Criar nova pessoa
2. Buscar pessoa por email
3. Listar todas as pessoas
4. Atualizar pessoa
5. Apagar pessoa
0. Sair
==================================================
```

### Usando a Classe PessoaCliente Programaticamente

```python
from ws_client_pessoa import PessoaCliente

# Criar instância do cliente
cliente = PessoaCliente()

# Criar uma nova pessoa
pessoa = cliente.criar(
    email="maria@gmail.com",
    nome="Maria",
    idade=25,
    altura=1.65
)

# Buscar pessoa por email
pessoa = cliente.buscarPorEmail("maria@gmail.com")

# Listar todas as pessoas
pessoas = cliente.listarTodas()

# Atualizar pessoa
pessoa_atualizada = cliente.atualizar(
    email="maria@gmail.com",
    nome="Maria Silva",
    idade=26
)

# Apagar pessoa
sucesso = cliente.apagar("maria@gmail.com")
```

## 📝 Modelo de Dados

### Entidade Pessoa

A entidade `Pessoa` possui os seguintes atributos:

- **email** (str, obrigatório): Email único da pessoa (usado como identificador)
- **nome** (str, opcional): Nome da pessoa
- **idade** (int, opcional): Idade da pessoa
- **altura** (float, opcional): Altura da pessoa em metros

## 🔧 Arquitetura

O projeto segue uma arquitetura em camadas:

1. **Camada de Entidade** (`pessoa.py`): Define a estrutura de dados da entidade Pessoa
2. **Camada de Serviço** (`pessoa_service.py`): Contém a lógica de negócio e gerenciamento em memória
3. **Camada de Apresentação** (`ws_provider.py`): Implementa o servidor HTTP e trata as requisições REST
4. **Cliente** (`ws_client_pessoa.py`, `run.py`): Interface para consumir a API

## ⚠️ Observações Importantes

- Os dados são armazenados **em memória**, ou seja, serão perdidos quando o servidor for reiniciado
- O email é usado como identificador único para as operações de busca, atualização e exclusão
- A comparação de emails é case-insensitive (não diferencia maiúsculas de minúsculas)
- O servidor deve estar rodando antes de executar o cliente

## 🧪 Testando com cURL

Você também pode testar a API usando cURL:

```bash
# Listar todas as pessoas
curl http://localhost:8080/pessoas

# Buscar por email
curl "http://localhost:8080/pessoas?email=joao@gmail.com"

# Criar pessoa
curl -X POST "http://localhost:8080/pessoas?email=joao@gmail.com&nome=João&idade=30&altura=1.75"

# Atualizar pessoa
curl -X PUT "http://localhost:8080/pessoas?email=joao@gmail.com&nome=João Silva&idade=31"

# Apagar pessoa
curl -X DELETE "http://localhost:8080/pessoas?email=joao@gmail.com"
```

## 📄 Licença

Este projeto é parte de um curso de desenvolvimento backend em Python.

## 👨‍💻 Autor

Desenvolvido como parte do Módulo 5 - WebServices do curso de Backend Python.

