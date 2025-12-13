# WS2 - Calculadora

Este projeto implementa um Web Service simples que realiza operações aritméticas básicas (soma, subtração, multiplicação e divisão) através de uma API REST.

## Descrição

O projeto consiste em dois componentes principais:
- **ws_provider.py**: Servidor HTTP que fornece os serviços de cálculo
- **ws_client.py**: Cliente que consome os serviços de cálculo

## Funcionalidades

O Web Service oferece quatro operações aritméticas:

- **GET /somar**: Soma dois números
- **GET /subtrair**: Subtrai dois números
- **POST /multiplicar**: Multiplica dois números
- **POST /dividir**: Divide dois números

Todas as operações retornam o resultado em formato JSON.

## Requisitos

- Python 3.x
- Biblioteca `requests` (para o cliente)

## Instalação

Instale a biblioteca `requests` se ainda não tiver:

```bash
pip install requests
```

## Como Usar

### 1. Iniciar o Servidor

Execute o arquivo `ws_provider.py`:

```bash
python3 ws_provider.py
```

O servidor será iniciado em `http://127.0.0.1:8081`

Você verá a mensagem:
```
Servidor iniciado em http://127.0.0.1:8081
```

### 2. Executar o Cliente

Em outro terminal, execute o arquivo `ws_client.py`:

```bash
python3 ws_client.py
```

O cliente fará requisições para todas as operações usando os números 20 e 10, e exibirá os resultados.

### 3. Usar o Cliente Programaticamente

Você também pode usar a classe `CalculadoraCliente` em seu próprio código:

```python
from ws_client import CalculadoraCliente

cliente = CalculadoraCliente()
cliente.calcular(15, 25)  # Executa todas as operações com 15 e 25
```

## API

### Endpoint: GET /somar

Realiza a soma de dois números.

**Parâmetros:**
- `numero1` (int): Primeiro número
- `numero2` (int): Segundo número

**Exemplo de requisição:**
```
GET http://127.0.0.1:8081/somar?numero1=20&numero2=10
```

**Resposta:**
```json
{
  "resultado": 30
}
```

### Endpoint: GET /subtrair

Realiza a subtração de dois números.

**Parâmetros:**
- `numero1` (int): Primeiro número
- `numero2` (int): Segundo número

**Exemplo de requisição:**
```
GET http://127.0.0.1:8081/subtrair?numero1=20&numero2=10
```

**Resposta:**
```json
{
  "resultado": 10
}
```

### Endpoint: POST /multiplicar

Realiza a multiplicação de dois números.

**Parâmetros (form data):**
- `numero1` (int): Primeiro número
- `numero2` (int): Segundo número

**Exemplo de requisição:**
```
POST http://127.0.0.1:8081/multiplicar
Content-Type: application/x-www-form-urlencoded

numero1=20&numero2=10
```

**Resposta:**
```json
{
  "resultado": 200
}
```

### Endpoint: POST /dividir

Realiza a divisão de dois números.

**Parâmetros (form data):**
- `numero1` (int): Primeiro número (dividendo)
- `numero2` (int): Segundo número (divisor)

**Exemplo de requisição:**
```
POST http://127.0.0.1:8081/dividir
Content-Type: application/x-www-form-urlencoded

numero1=20&numero2=10
```

**Resposta:**
```json
{
  "resultado": 2.0
}
```

**Nota:** Se `numero2` for 0, a resposta será:
```json
{
  "resultado": "Erro: Divisão por zero"
}
```

## Estrutura do Projeto

```
WS2 - Calculadora/
├── ws_provider.py    # Servidor HTTP que fornece os serviços
├── ws_client.py      # Cliente que consome os serviços
└── README.md         # Este arquivo
```

## Exemplo de Saída

Ao executar o cliente com os números 20 e 10, você verá:

```
==============================
SOMAR: 30
SUBTRAIR: 10
==============================
MULTIPLICAR: 200
DIVIDIR: 2.0
==============================
```

## Notas

- O servidor roda na porta 8081 por padrão
- Certifique-se de que a porta 8081 está disponível antes de iniciar o servidor
- O servidor precisa estar rodando antes de executar o cliente
- As operações GET (somar e subtrair) recebem os parâmetros via query string na URL
- As operações POST (multiplicar e dividir) recebem os parâmetros via form data no corpo da requisição
- A divisão por zero é tratada e retorna uma mensagem de erro apropriada
