# Projeto4

Projeto Django de catalogo com categorias e produtos.

## Objetivo

Praticar relacionamento entre entidades com `Categoria` e `Produto` (1 categoria para N produtos).

## Estrutura principal

- `manage.py`: comando principal do Django.
- `setup/`: configuracoes do projeto.
- `categoria/`: app para gestao de categorias.
- `produto/`: app para gestao de produtos.
- `db.sqlite3`: base SQLite local.

## Execucao

```bash
python manage.py migrate
python manage.py runserver
```

## Funcionalidades

- CRUD de categorias.
- CRUD de produtos com vinculo obrigatorio a uma categoria.
- Controle de status (ativo/inativo) e dados de estoque/preco.

## URLs disponiveis

- `http://127.0.0.1:8000/`: pagina inicial do catalogo.
- `http://127.0.0.1:8000/categoria/`: lista de categorias.
- `http://127.0.0.1:8000/categoria/criar/`: criar categoria.
- `http://127.0.0.1:8000/categoria/<id>/`: detalhe da categoria.
- `http://127.0.0.1:8000/categoria/<id>/editar/`: editar categoria.
- `http://127.0.0.1:8000/categoria/<id>/deletar/`: remover categoria.
- `http://127.0.0.1:8000/produto/`: lista de produtos.
- `http://127.0.0.1:8000/produto/criar/`: criar produto.
- `http://127.0.0.1:8000/produto/<id>/`: detalhe do produto.
- `http://127.0.0.1:8000/produto/<id>/editar/`: editar produto.
- `http://127.0.0.1:8000/produto/<id>/deletar/`: remover produto.
- `http://127.0.0.1:8000/admin/`: painel administrativo do Django.
