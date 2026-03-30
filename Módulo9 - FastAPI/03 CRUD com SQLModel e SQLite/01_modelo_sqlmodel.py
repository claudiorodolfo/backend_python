"""
01 - Modelo com SQLModel
========================

SQLModel combina Pydantic + SQLAlchemy: um único modelo pode servir para
persistência e validação.

Dependência:

    pip install sqlmodel
"""

from sqlmodel import Field, SQLModel


class Pessoa(SQLModel, table=True):
    """Tabela `pessoa` no banco (nome da tabela é derivado do nome da classe)."""

    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    email: str = Field(index=True)
    ativa: bool = Field(default=True)


"""
Dicas:

- `Field(index=True)` ajuda em buscas frequentes (cria índice no SQLite/Postgres).
- Relacionamentos usam `Relationship` (ver unidades seguintes nos Projetos).
"""
