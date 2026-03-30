# 01 - Introdução e Primeira API

## Objetivo

Criar e executar uma API mínima com FastAPI, entendendo o ciclo requisição-resposta.

## Conteúdo

- Instalação do FastAPI e Uvicorn.
- Criação do arquivo `main.py`.
- Endpoint `GET /`.
- Endpoint com parâmetro de rota.

## Exemplo

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'mensagem': 'API no ar'}
```

## Execução

```bash
uvicorn main:app --reload
```
