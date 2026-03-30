"""
04 - Camadas (routers / services / repositories)
==============================================

Nos projetos da pasta `Projetos/`, a estrutura recomendada separa:

1. **routers** — apenas HTTP: parâmetros, status codes, `Depends`.
2. **services** — regras de negócio (validações que não são só de formato).
3. **repositories** — consultas e persistência (SQLModel / SQLAlchemy).
4. **schemas** — Pydantic para entrada/saída quando diferente do modelo de tabela.

Fluxo típico:

    Request → Router → Service → Repository → Banco
                  ↑______________|
                    response_model / schemas

Por que usar camadas?

- Testes mais simples (mock do repositório no service).
- Troca de banco ou ORM sem reescrever rotas.
- Menos “lógica espalhada” nos endpoints.

Próximo passo: abra `Projetos/Projeto3` ou `Projetos/Projeto4` no repositório do curso.
"""
