# WS1 - Somar

Este projeto implementa um Web Service simples que realiza operações de soma através de uma API REST.

## Descrição

O projeto consiste em dois componentes principais:
- **ws_provider.py**: Servidor HTTP que fornece o serviço de soma
- **ws_client.py**: Cliente que consome o serviço de soma

## Funcionalidades

- Endpoint `/somar` que recebe dois números via parâmetros GET
- Retorna o resultado da soma em formato JSON
- Cliente que faz requisições ao servidor e exibe o resultado

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

### 2. Executar o Cliente

Em outro terminal, execute o arquivo `ws_client.py`:

```bash
python3 ws_client.py
```

O cliente fará uma requisição ao servidor somando 20 + 10 e exibirá o resultado.

### 3. Usar o Cliente Programaticamente

Você também pode usar a classe `CalculadoraCliente` em seu próprio código:

```python
from ws_client import CalculadoraCliente

cliente = CalculadoraCliente()
cliente.somar(15, 25)  # Resultado: 40
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

## Estrutura do Projeto

```
WS1 - Somar/
├── ws_provider.py    # Servidor HTTP que fornece o serviço
├── ws_client.py      # Cliente que consome o serviço
└── README.md         # Este arquivo
```

## Exemplo de Saída

Ao executar o cliente, você verá:

```
==============================
RESULTADO SOMAR: 30
==============================
```

## Notas

- O servidor roda na porta 8081 por padrão
- Certifique-se de que a porta 8081 está disponível antes de iniciar o servidor
- O servidor precisa estar rodando antes de executar o cliente
