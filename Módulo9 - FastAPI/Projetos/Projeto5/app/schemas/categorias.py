from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome: str
    ativa: bool = True

class CategoriaUpdate(BaseModel):
    nome: str | None = None
    ativa: bool | None = None
