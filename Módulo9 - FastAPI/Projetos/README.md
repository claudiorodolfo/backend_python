# Projetos FastAPI

Esta pasta reúne os projetos práticos do módulo de FastAPI.

## Estrutura

- `Projeto1`: CRUD básico de pessoas em memória (camadas).
- `Projeto2`: CRUD de pessoas com filtros e validações (camadas).
- `Projeto3`: CRUD de pessoas com SQLModel (SQLite/PostgreSQL) em camadas.
- `Projeto4`: Catálogo de categorias e produtos em camadas.
- `Projeto5`: Evolução do catálogo com CRUD completo, filtros e testes ampliados.

## Padrão adotado

Todos os projetos usam a mesma organização:

- `app/routers/`: camada HTTP.
- `app/services/`: regras de negócio.
- `app/repositories/`: acesso a dados.
- `app/schemas/`: contratos de entrada e saída.

## Testes

```bash
pytest -q
```

## Docker (projetos com banco)

Os projetos `Projeto3`, `Projeto4` e `Projeto5` possuem `docker-compose.yml` base com API + PostgreSQL.
