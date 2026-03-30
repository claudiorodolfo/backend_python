# Projetos Django

Esta pasta reune os projetos práticos do modulo de Django.

## Estrutura

- `Projeto1`: CRUD básico de pessoas.
- `Projeto2`: CRUD de pessoas com evoluções em modelagem e organizacao.
- `Projeto3`: CRUD de pessoas com foco no front-end.
- `Projeto4`: Catalogo com `Categoria` e `Produto` (relacionamento 1:N).

## URLs por projeto

- `Projeto1`
  - `/`
  - `/admin/`
- `Projeto2`
  - `/`
  - `/criar/`
  - `/<id>/`
  - `/<id>/editar/`
  - `/<id>/deletar/`
  - `/admin/`
- `Projeto3`
  - `/`
  - `/criar/`
  - `/<id>/`
  - `/<id>/editar/`
  - `/<id>/deletar/`
  - `/admin/`
- `Projeto4`
  - `/`
  - `/categoria/`, 
  `/categoria/criar/`, 
  `/categoria/<id>/`, 
  `/categoria/<id>/editar/`, 
  `/categoria/<id>/deletar/`
  - `/produto/`, 
  `/produto/criar/`, 
  `/produto/<id>/`, 
  `/produto/<id>/editar/`, 
  `/produto/<id>/deletar/`
  - `/admin/`


## Como executar qualquer projeto

1. Acesse a pasta do projeto desejado:
   - `cd "Módulo6 - Django/Projetos/ProjetoX"`
2. Crie e ative um ambiente virtual (opcional, mas recomendado).
3. Instale o Django:
   - `pip install django`
4. Rode as migracoes:
   - `python manage.py migrate`
5. Inicie o servidor:
   - `python manage.py runserver`

