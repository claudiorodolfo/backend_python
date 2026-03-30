# 03 - CRUD com SQLModel e SQLite

## Objetivo

Persistir dados em banco SQLite e organizar a aplicação por domínio.

## Conteúdo

- Modelos com SQLModel.
- Sessão de banco e dependência de conexão.
- CRUD completo.
- Separação entre modelos de tabela, schemas de API e rotas (e, nos projetos, camadas).

## Arquivos

- `01_modelo_sqlmodel.py` — definição de tabela com `SQLModel`.
- `02_engine_e_sessao.py` — engine, `create_db_and_tables` e `get_session`.
- `03_api_crud_pessoas.py` — API CRUD autocontida (SQLite local).
- `04_camadas_e_projetos.py` — texto-guia sobre routers / services / repositories.

## Resultado esperado

API persistente com operações de criar, listar, consultar e remover registros.

## Execução (exemplo integrado)

```bash
pip install fastapi uvicorn sqlmodel
uvicorn 03_api_crud_pessoas:app --reload
```

Para PostgreSQL em Docker, use os `docker-compose.yml` dos projetos em `Projetos/`.
