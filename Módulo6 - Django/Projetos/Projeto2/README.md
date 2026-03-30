# Projeto2

Projeto Django de cadastro de pessoas, evoluindo a base do Projeto1.

## Objetivo

Consolidar CRUD de pessoas com organizacao de app e modelagem mais completa.

## Estrutura principal

- `manage.py`: comando principal do Django.
- `setup/`: configuracoes do projeto.
- `pessoas/`: app principal do dominio.
- `db.sqlite3`: base SQLite local.

## Execucao

```bash
python manage.py migrate
python manage.py runserver
```

## Funcionalidades

- Cadastro de pessoas com campos como nome, email, telefone, CPF e status.
- Consulta e manutencao dos registros.
- Busca de pessoas por nome, email ou CPF na listagem.

## URLs disponiveis

- `http://127.0.0.1:8000/`: lista de pessoas.
- `http://127.0.0.1:8000/criar/`: criar nova pessoa.
- `http://127.0.0.1:8000/<id>/`: detalhe da pessoa.
- `http://127.0.0.1:8000/<id>/editar/`: editar pessoa.
- `http://127.0.0.1:8000/<id>/deletar/`: remover pessoa.
- `http://127.0.0.1:8000/admin/`: painel administrativo do Django.
