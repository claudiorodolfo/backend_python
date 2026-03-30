from sqlmodel import Field, SQLModel

class Categoria(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    ativa: bool = True

class Produto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    preco: float
    estoque: int
    ativo: bool = True
    categoria_id: int = Field(foreign_key='categoria.id')
