"""
01 - Path params e query params
===============================

- Path: parte fixa da URL (/itens/{id})
- Query: após ? (/busca?q=mouse&limite=10)
"""

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/itens/{item_id}")
def ler_item(
    item_id: Annotated[int, Path(ge=1)],
    busca: Annotated[str | None, Query(max_length=50)] = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 10,
) -> dict:
    return {"item_id": item_id, "busca": busca, "limite": limite}
