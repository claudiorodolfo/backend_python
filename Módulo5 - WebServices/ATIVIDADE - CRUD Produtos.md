# ATIVIDADE - CRUD Produtos com Web Services

## 📋 Objetivo da Atividade

Desenvolver um sistema completo de CRUD (Create, Read, Update, Delete) para gerenciamento de produtos através de uma API REST implementada em Python, seguindo a mesma arquitetura e padrões utilizados no projeto **WS10 - CRUD Pessoa**.

## 🎯 Objetivos de Aprendizado

Ao final desta atividade, o aluno será capaz de:

- Implementar uma API REST completa com operações CRUD
- Criar uma arquitetura em camadas (Entity, Service, Provider)
- Desenvolver um cliente HTTP para consumir a API
- Implementar tratamento de erros e validações
- Trabalhar com requisições HTTP (GET, POST, PUT, DELETE)
- Manipular dados JSON em requisições e respostas
- Criar uma interface de linha de comando (CLI) interativa

## 📦 Especificações do Projeto

### Estrutura de Diretórios

O projeto deve seguir a seguinte estrutura:

```
WS11 - CRUD Produtos/
├── provider/               # Servidor Web Service
│   ├── ws_provider.py       # Servidor HTTP e handlers das requisições
│   ├── produto_service.py   # Lógica de negócio e gerenciamento de produtos
│   └── produto.py           # Entidade Produto
├── client/                  # Cliente Web Service
│   ├── ws_client_produto.py # Cliente HTTP para comunicação com a API
│   └── run.py               # Interface de linha de comando (CLI)
└── README.md                # Documentação do projeto
```

### Modelo de Dados - Produto

A entidade `Produto` deve possuir os seguintes atributos:

- **codigo** (str, obrigatório): Código único do produto (usado como identificador)
- **nome** (str, opcional): Nome do produto
- **preco** (float, opcional): Preço do produto
- **quantidade** (int, opcional): Quantidade em estoque

**Exemplo de Produto:**
```python
produto = Produto(
    codigo="PROD001",
    nome="Notebook Dell",
    preco=3500.00,
    quantidade=15
)
```

## 🔧 Requisitos Técnicos

### 1. Camada de Entidade (`produto.py`)

Criar a classe `Produto` com:
- Construtor que recebe `codigo` (obrigatório) e `nome`, `preco`, `quantidade` (opcionais)
- Propriedades (properties) para todos os atributos
- Encapsulamento adequado (atributos privados)

### 2. Camada de Serviço (`produto_service.py`)

Implementar a classe `ProdutoService` com os seguintes métodos:

- `criar(produto: Produto) -> Produto`: Cria um novo produto no repositório
- `buscarPorCodigo(produto: Produto) -> Produto`: Busca um produto por código
- `atualizar(produto: Produto) -> Produto`: Atualiza um produto existente
- `apagar(produto: Produto) -> bool`: Remove um produto do repositório
- `listarTodos() -> list`: Retorna lista com todos os produtos

**Observações:**
- Os dados devem ser armazenados em memória (lista)
- A busca por código deve ser case-insensitive
- Retornar `None` quando produto não for encontrado (buscar/atualizar)
- Retornar `False` quando produto não for encontrado (apagar)

### 3. Camada de Apresentação (`ws_provider.py`)

Implementar o servidor HTTP usando `HTTPServer` e `BaseHTTPRequestHandler`:

#### Endpoints a implementar:

**GET /produtos**
- Lista todos os produtos cadastrados
- Resposta 200 OK com JSON: `{"produtos": [...]}`

**GET /produtos?codigo={codigo}**
- Busca um produto específico por código
- Resposta 200 OK se encontrado: `{"produto": {...}}`
- Resposta 404 Not Found se não encontrado: `{"erro": "Produto não encontrado"}`

**POST /produtos**
- Cria um novo produto
- Parâmetros via query string: `codigo` (obrigatório), `nome`, `preco`, `quantidade` (opcionais)
- Resposta 201 Created: `{"produto": {...}}`
- Resposta 400 Bad Request se código não fornecido: `{"erro": "Código é obrigatório"}`

**PUT /produtos**
- Atualiza um produto existente
- Parâmetros via query string: `codigo` (obrigatório), `nome`, `preco`, `quantidade` (opcionais)
- Resposta 200 OK se atualizado: `{"produto": {...}}`
- Resposta 404 Not Found se não encontrado: `{"erro": "Produto não encontrado"}`
- Resposta 400 Bad Request se código não fornecido: `{"erro": "Código é obrigatório"}`

**DELETE /produtos?codigo={codigo}**
- Remove um produto do sistema
- Resposta 200 OK: `{"mensagem": "Produto apagado com sucesso"}`
- Resposta 404 Not Found: `{"erro": "Produto não encontrado"}`
- Resposta 400 Bad Request se código não fornecido: `{"erro": "Código é obrigatório"}`

**Configuração do Servidor:**
- Porta: 8081
- Host: 127.0.0.1
- Content-Type: application/json em todas as respostas

### 4. Cliente HTTP (`ws_client_produto.py`)

Implementar a classe `ProdutoCliente` com os seguintes métodos:

- `__init__(self)`: Inicializa com `base_url = "http://localhost:8081"`
- `buscarPorCodigo(codigo: str) -> dict`: Busca produto por código
- `listarTodos() -> list`: Lista todos os produtos
- `criar(codigo: str, nome: str = None, preco: float = None, quantidade: int = None) -> dict`: Cria novo produto
- `atualizar(codigo: str, nome: str = None, preco: float = None, quantidade: int = None) -> dict`: Atualiza produto
- `apagar(codigo: str) -> bool`: Remove produto

**Observações:**
- Usar a biblioteca `requests` para fazer as requisições HTTP
- Tratar erros apropriadamente (404, 400, etc.)
- Converter tipos numéricos para string nos parâmetros da query string

### 5. Interface CLI (`run.py`)

Criar uma interface de linha de comando interativa com menu:

```
==================================================
MENU - CRUD PRODUTO
==================================================
1. Criar novo produto
2. Buscar produto por código
3. Listar todos os produtos
4. Atualizar produto
5. Apagar produto
0. Sair
==================================================
```

**Funcionalidades do Menu:**

1. **Criar novo produto**: Solicita código (obrigatório), nome, preço e quantidade
2. **Buscar produto por código**: Solicita código e exibe o produto encontrado
3. **Listar todos os produtos**: Exibe todos os produtos cadastrados
4. **Atualizar produto**: Permite atualizar nome, preço e quantidade de um produto existente
5. **Apagar produto**: Remove um produto após confirmação

**Requisitos da CLI:**
- Validação de entrada (código obrigatório)
- Tratamento de erros com mensagens amigáveis
- Formatação adequada da exibição dos dados
- Confirmação antes de apagar
- Pausa após cada operação (input para continuar)

### 6. Documentação (`README.md`)

Criar documentação completa incluindo:

- Descrição do projeto
- Estrutura de diretórios
- Requisitos e instalação
- Como executar (servidor e cliente)
- Documentação de todos os endpoints com exemplos
- Exemplos de uso do cliente
- Modelo de dados
- Arquitetura do projeto
- Exemplos de teste com cURL

## ✅ Critérios de Avaliação

### Funcionalidade (40 pontos)
- [ ] Todos os endpoints CRUD funcionando corretamente
- [ ] Validações implementadas (código obrigatório)
- [ ] Tratamento de erros adequado (404, 400)
- [ ] Cliente HTTP funcionando corretamente
- [ ] Interface CLI completa e funcional

### Código (30 pontos)
- [ ] Arquitetura em camadas bem definida
- [ ] Código limpo e organizado
- [ ] Uso adequado de propriedades e encapsulamento
- [ ] Comentários e documentação no código
- [ ] Tratamento de exceções

### Estrutura e Organização (15 pontos)
- [ ] Estrutura de diretórios correta
- [ ] Nomenclatura consistente
- [ ] Separação adequada de responsabilidades

### Documentação (15 pontos)
- [ ] README.md completo e bem formatado
- [ ] Exemplos de uso claros
- [ ] Documentação dos endpoints detalhada

## 📝 Tarefas Detalhadas

### Fase 1: Entidade e Serviço (2-3 horas)
1. Criar a classe `Produto` com todos os atributos e propriedades
2. Implementar `ProdutoService` com todos os métodos CRUD
3. Testar manualmente a lógica de negócio

### Fase 2: Provider/API (3-4 horas)
1. Implementar o servidor HTTP (`ws_provider.py`)
2. Implementar todos os métodos HTTP (GET, POST, PUT, DELETE)
3. Implementar tratamento de erros e validações
4. Testar endpoints com cURL ou Postman

### Fase 3: Cliente (2-3 horas)
1. Implementar `ProdutoCliente` com todos os métodos
2. Testar comunicação com a API
3. Implementar tratamento de erros no cliente

### Fase 4: Interface CLI (2-3 horas)
1. Criar menu interativo
2. Implementar todas as funções do menu
3. Adicionar validações e tratamento de erros
4. Melhorar formatação e UX

### Fase 5: Documentação (1-2 horas)
1. Criar README.md completo
2. Documentar todos os endpoints
3. Adicionar exemplos de uso
4. Revisar e melhorar documentação

## 🧪 Exemplos de Teste

### Testando com cURL

```bash
# Listar todos os produtos
curl http://localhost:8081/produtos

# Buscar por código
curl "http://localhost:8081/produtos?codigo=PROD001"

# Criar produto
curl -X POST "http://localhost:8081/produtos?codigo=PROD001&nome=Notebook&preco=3500.00&quantidade=10"

# Atualizar produto
curl -X PUT "http://localhost:8081/produtos?codigo=PROD001&nome=Notebook Dell&preco=3800.00&quantidade=15"

# Apagar produto
curl -X DELETE "http://localhost:8081/produtos?codigo=PROD001"
```

### Testando com Python

```python
from ws_client_produto import ProdutoCliente

cliente = ProdutoCliente()

# Criar produto
produto = cliente.criar(
    codigo="PROD001",
    nome="Notebook Dell",
    preco=3500.00,
    quantidade=10
)

# Buscar produto
produto = cliente.buscarPorCodigo("PROD001")

# Listar todos
produtos = cliente.listarTodos()

# Atualizar
produto_atualizado = cliente.atualizar(
    codigo="PROD001",
    preco=3800.00,
    quantidade=15
)

# Apagar
sucesso = cliente.apagar("PROD001")
```

## 💡 Dicas e Observações

1. **Use o projeto WS10 como referência**: Analise a estrutura e padrões utilizados
2. **Teste incrementalmente**: Teste cada camada antes de passar para a próxima
3. **Validações**: Sempre valide dados obrigatórios antes de processar
4. **Tratamento de erros**: Implemente tratamento adequado para todos os casos
5. **Conversão de tipos**: Lembre-se de converter strings para int/float quando necessário
6. **Case-insensitive**: A busca por código deve ignorar maiúsculas/minúsculas
7. **Porta diferente**: Use porta 8081
8. **Documentação**: Documente bem seu código, isso facilita a manutenção

## 🚀 Entrega

O projeto deve ser entregue com:

1. Todos os arquivos do projeto organizados na estrutura correta
2. README.md completo e bem formatado
3. Código funcionando e testado
4. Comentários adequados no código
5. Tratamento de erros implementado

**Formato de entrega**: Pasta compactada (ZIP) ou repositório Git com todos os arquivos.

## 📚 Referências

- Projeto WS10 - CRUD Pessoa (referência principal)
- Documentação Python: `http.server`
- Documentação Requests: `https://requests.readthedocs.io/`
- REST API Design Best Practices

---

**Boa sorte e bom desenvolvimento! 🚀**
