"""
02 - Schemas com Pydantic (corpo da requisição)
===============================================

Use modelos Pydantic para validar JSON enviado no body (POST, PUT, PATCH).
"""

from pydantic import BaseModel, EmailStr, Field

from fastapi import FastAPI

app = FastAPI()


class ItemCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco: float = Field(gt=0, description="Preço deve ser positivo")
    em_estoque: bool = True


class ItemOut(BaseModel):
    id: int
    nome: str
    preco: float
    em_estoque: bool


# Simula “banco” em memória para o exemplo
_proximo_id = 1
_itens: dict[int, ItemOut] = {}


@app.post("/itens", response_model=ItemOut)
def criar_item(payload: ItemCreate) -> ItemOut:
    global _proximo_id
    novo = ItemOut(id=_proximo_id, **payload.model_dump())
    _itens[_proximo_id] = novo
    _proximo_id += 1
    return novo


"""
Observação: `EmailStr` exige o pacote `email-validator`:

    pip install email-validator

Se preferir evitar dependência extra, use `str` com validação manual.
"""
