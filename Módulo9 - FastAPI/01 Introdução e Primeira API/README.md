# 01 - Introdução e Primeira API

## Objetivo

Criar e executar uma API mínima com FastAPI, entendendo o ciclo requisição-resposta.

## Conteúdo

- Instalação do FastAPI e Uvicorn.
- Criação do arquivo `main.py`.
- Endpoint `GET /`.
- Endpoint com parâmetro de rota.
- Documentação interativa (`/docs`).

## Arquivos

- `01_instalacao_ambientacao.py` — ambiente virtual, instalação e visão geral do FastAPI.
- `02_primeira_app.py` — app mínima com `GET /` e `GET /ping`.
- `03_parametros_rota.py` — parâmetros de path e validação de tipos.
- `04_documentacao_interativa.py` — metadados da API, `/docs` e anotações em parâmetros.

## Exemplo rápido

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'mensagem': 'API no ar'}
```

## Execução

Na pasta desta unidade, apontando o Uvicorn para um dos módulos:

```bash
pip install fastapi uvicorn
uvicorn 02_primeira_app:app --reload
```

Abra em seguida `http://127.0.0.1:8000/docs`.
