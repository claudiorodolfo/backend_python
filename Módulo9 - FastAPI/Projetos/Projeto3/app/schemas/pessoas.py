from pydantic import BaseModel, EmailStr

class PessoaCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    ativa: bool = True

class PessoaUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    ativa: bool | None = None
