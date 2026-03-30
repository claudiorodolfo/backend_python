from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome: str
    ativa: bool = True
