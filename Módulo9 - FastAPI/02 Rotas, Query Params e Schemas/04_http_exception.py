"""
04 - Erros HTTP com HTTPException
=================================

Use `HTTPException` para retornar status e mensagens consistentes.
"""

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Simula “banco”
_ITENS = {1: "Caneta", 2: "Caderno"}


@app.get("/itens/{item_id}")
def obter_item(item_id: int) -> dict[str, int | str]:
    nome = _ITENS.get(item_id)
    if nome is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado",
        )
    return {"item_id": item_id, "nome": nome}


@app.post("/itens/{item_id}/reservar")
def reservar(item_id: int) -> dict[str, str]:
    if item_id not in _ITENS:
        raise HTTPException(status_code=404, detail="Item inexistente")
    # Exemplo de regra de negócio
    if item_id == 1:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item já reservado",
        )
    return {"mensagem": "Reservado com sucesso"}
