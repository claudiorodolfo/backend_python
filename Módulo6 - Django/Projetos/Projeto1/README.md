# Projeto1

Projeto Django introdutório para cadastro de pessoas.

## Objetivo

Praticar estrutura basica de projeto Django com app `pessoas` e operacoes de cadastro.

## Estrutura principal

- `manage.py`: comando principal do Django.
- `setup/`: configuracoes do projeto.
- `pessoas/`: app com models, views, urls e templates.
- `db.sqlite3`: base SQLite local.

## Execucao

```bash
python manage.py migrate
python manage.py runserver
```

## Funcionalidades

- Cadastro de pessoas.
- Listagem e manutencao de registros.

## URLs disponiveis

- `http://127.0.0.1:8000/`: pagina inicial do app `pessoas`.
- `http://127.0.0.1:8000/admin/`: painel administrativo do Django.
