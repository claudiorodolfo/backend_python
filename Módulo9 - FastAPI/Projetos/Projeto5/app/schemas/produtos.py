from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)
    ativo: bool = True
    categoria_id: int

class ProdutoUpdate(BaseModel):
    nome: str | None = None
    preco: float | None = Field(default=None, gt=0)
    estoque: int | None = Field(default=None, ge=0)
    ativo: bool | None = None
    categoria_id: int | None = None
