from pydantic import BaseModel, EmailStr, Field

class PessoaBase(BaseModel):
    nome: str = Field(min_length=3, max_length=120)
    email: EmailStr
    telefone: str = Field(min_length=10, max_length=15)
    ativa: bool = True

class PessoaCreate(PessoaBase):
    pass

class PessoaUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=120)
    email: EmailStr | None = None
    telefone: str | None = Field(default=None, min_length=10, max_length=15)
    ativa: bool | None = None

class PessoaOut(PessoaBase):
    id: int
