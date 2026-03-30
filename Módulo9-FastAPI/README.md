# Módulo 9 - FastAPI

Este módulo apresenta o FastAPI, um framework moderno para criação de APIs com Python, focado em performance, tipagem forte e produtividade.

## Conteúdo do Módulo

Você aprenderá a construir APIs REST completas com validação automática, documentação interativa e boas práticas de arquitetura.

### 1. Fundamentos do FastAPI

- O que é FastAPI e quando usar.
- Diferença entre FastAPI, Flask e Django.
- ASGI, Uvicorn e arquitetura assíncrona.
- Estrutura inicial de um projeto FastAPI.

### 2. Rotas e Validação

- Path params e query params.
- Request body com Pydantic.
- Respostas tipadas e `response_model`.
- Tratamento de erros com `HTTPException`.

### 3. CRUD e Banco de Dados

- Organização em camadas (routers, services, schemas).
- Integração com SQLite usando SQLModel.
- Relacionamentos entre entidades.
- Migração da API em memória para persistência real.

### 4. Testes, Segurança e Deploy

- Testes com `pytest` e `TestClient`.
- CORS, variáveis de ambiente e configuração.
- Autenticação com OAuth2/JWT (introdução).
- Deploy com Uvicorn/Gunicorn + Docker.

## Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:

- Criar APIs REST com FastAPI usando tipagem Python.
- Validar entrada e saída com Pydantic.
- Organizar projetos em arquitetura limpa para APIs.
- Implementar CRUD com persistência em banco de dados.
- Testar endpoints automaticamente.
- Publicar APIs em ambiente de produção.

## Pré-requisitos

- Python intermediário (funções, classes, tipagem).
- Conceitos de HTTP e JSON.
- Noções de banco de dados relacional.
- Conhecimento de Git.

## Stack sugerida

- FastAPI
- Uvicorn
- Pydantic
- SQLModel
- Pytest

## Estrutura sugerida de projeto FastAPI

```text
projeto_fastapi/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── schemas/
│   ├── models/
│   └── services/
├── tests/
├── requirements.txt
└── README.md
```

## Comandos essenciais

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
uvicorn app.main:app --reload

# Executar testes
pytest -q
```

## Projetos práticos

Os projetos deste módulo estão na pasta `Projetos/`:

- `Projeto1`: API de pessoas em memória com arquitetura em camadas.
- `Projeto2`: API de pessoas com filtros e validações em camadas.
- `Projeto3`: API de pessoas com SQLModel e suporte a SQLite/PostgreSQL.
- `Projeto4`: API de catálogo com categorias e produtos (1:N) em camadas.
- `Projeto5`: evolução do catálogo com CRUD completo, filtros e testes ampliados.
