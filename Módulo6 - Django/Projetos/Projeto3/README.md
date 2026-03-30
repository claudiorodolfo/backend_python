# Projeto3

Projeto Django de cadastro de pessoas com foco em melhoria de interface (front-end) usando Bootstrap.

## Objetivo

Manter o mesmo CRUD do `Projeto2`, mas com uma camada de apresentacao mais trabalhada:

- layout responsivo com Bootstrap;
- componentes visuais para navegação e acoes;
- melhor experiencia de uso nas telas de lista, formulario, detalhe e exclusao.

## Estrutura principal

- `manage.py`: comando principal do Django.
- `setup/`: configuracoes do projeto.
- `pessoas/`: app principal.
- `db.sqlite3`: base SQLite local.

## Execucao

```bash
python manage.py migrate
python manage.py runserver
```

## Funcionalidades

- Mesmo fluxo funcional do `Projeto2`:
  - cadastro, listagem, detalhe, edicao e exclusao de pessoas;
  - controle de status dos registros.
- Diferencial do `Projeto3`:
  - interface modernizada com Bootstrap;
  - barra de navegacao, cards, alertas e botoes com icones;
  - melhor organizacao visual das telas para uso no dia a dia.

## URLs disponiveis

- `http://127.0.0.1:8000/`: lista de pessoas.
- `http://127.0.0.1:8000/criar/`: criar nova pessoa.
- `http://127.0.0.1:8000/<id>/`: detalhe da pessoa.
- `http://127.0.0.1:8000/<id>/editar/`: editar pessoa.
- `http://127.0.0.1:8000/<id>/deletar/`: remover pessoa.
- `http://127.0.0.1:8000/admin/`: painel administrativo do Django.
