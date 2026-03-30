from pydantic import BaseModel, EmailStr

class PessoaBase(BaseModel):
    nome: str
    email: EmailStr

class PessoaCreate(PessoaBase):
    pass

class PessoaUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None

class PessoaOut(PessoaBase):
    id: int
