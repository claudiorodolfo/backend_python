from sqlmodel import Field, SQLModel

class Pessoa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
    telefone: str
    ativa: bool = True
