from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)
    ativo: bool = True
    categoria_id: int
