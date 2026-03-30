"""
03 - response_model e filtro de resposta
========================================

`response_model` define o formato **de saída** (e pode ocultar campos internos).
"""

from datetime import datetime
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field

from fastapi import FastAPI, Query

app = FastAPI()


class UsuarioDB(BaseModel):
    """Modelo “interno” (ex.: como viria do banco)."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    hash_senha: str
    criado_em: datetime


class UsuarioPublico(BaseModel):
    """O que a API expõe — sem `hash_senha`."""

    id: int
    email: str
    criado_em: datetime


@app.get("/usuarios/{user_id}", response_model=UsuarioPublico)
def get_usuario(user_id: int) -> Any:
    fake_db = UsuarioDB(
        id=user_id,
        email="ana@example.com",
        hash_senha="nao_expor_isso",
        criado_em=datetime.now(),
    )
    # FastAPI serializa usando UsuarioPublico — campos extras são descartados
    return fake_db


class Pagina(BaseModel):
    pagina: int = Field(ge=1)
    tamanho: int = Field(ge=1, le=100)


@app.get("/lista", response_model=list[UsuarioPublico])
def listar_usuarios(p: Annotated[Pagina, Query()]) -> list[UsuarioPublico]:
    _ = p  # em um projeto real: offset/limit na query
    return [
        UsuarioPublico(id=1, email="a@example.com", criado_em=datetime.now()),
    ]
