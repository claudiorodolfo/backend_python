"""
04 - Documentação interativa (OpenAPI)
======================================

Ao rodar o servidor, o FastAPI expõe automaticamente:

- GET  /docs     → Swagger UI (interativo)
- GET  /redoc    → ReDoc
- GET  /openapi.json → esquema OpenAPI em JSON

Comando típico (na pasta que contém este arquivo):

    uvicorn 04_documentacao_interativa:app --reload
"""

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="API com documentação automática",
    description="Acesse /docs após subir o Uvicorn.",
    version="1.0.0",
    contact={"name": "Curso", "email": "curso@example.com"},
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/produtos/{produto_id}", tags=["Produtos"])
def detalhe_produto(
    produto_id: Annotated[int, Path(description="Identificador do produto", ge=1)],
    destaque: Annotated[bool, Query(description="Se true, inclui campos extras")] = False,
) -> dict:
    return {"produto_id": produto_id, "destaque": destaque}
