# Calculadora REST Web Service

Projeto simples de uma calculadora REST. O servidor usa apenas a biblioteca padrão do Python, enquanto o cliente utiliza a biblioteca `requests` para fazer requisições HTTP.

## Arquivos

- `ws_provider.py`: Servidor REST que fornece as operações da calculadora
- `ws_cliente.py`: Cliente que consome o serviço REST

## Operações Disponíveis

- **soma**: Adição de dois números
- **subtracao**: Subtração de dois números
- **multiplicacao**: Multiplicação de dois números
- **divisao**: Divisão de dois números

## Como Usar

### 1. Iniciar o Servidor

```bash
python3 ws_provider.py
```

O servidor será iniciado em `http://localhost:8000`

### 2. Executar o Cliente

Em outro terminal:

```bash
python3 ws_cliente.py
```

O cliente irá testar todas as operações automaticamente.

## Endpoint da API

### POST /calcular
Realiza um cálculo

**Requisição:**
```json
{
  "operacao": "soma",
  "numero1": 10,
  "numero2": 5
}
```

**Resposta de Sucesso (200):**
```json
{
  "operacao": "soma",
  "numero1": 10,
  "numero2": 5,
  "resultado": 15
}
```

**Resposta de Erro (400):**
```json
{
  "erro": "Operação 'xyz' não suportada"
}
```

## Exemplo de Uso

```python
from ws_cliente import CalculadoraCliente

cliente = CalculadoraCliente()
resposta, codigo = cliente.calcular('soma', 10, 5)

if codigo == 200:
    print(f"Resultado: {resposta['resultado']}")
```

## Testando com cURL

```bash
curl -X POST http://localhost:8000/calcular \
  -H "Content-Type: application/json" \
  -d '{"operacao": "soma", "numero1": 10, "numero2": 5}'
```

## Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (para o cliente)

### Instalação das Dependências

```bash
pip install requests
```

Ou usando `pip3`:

```bash
pip3 install requests
```
