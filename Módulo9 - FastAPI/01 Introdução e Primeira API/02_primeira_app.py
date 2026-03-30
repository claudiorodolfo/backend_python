"""
02 - Primeira aplicação FastAPI
===============================

API mínima com um endpoint GET.
"""

from fastapi import FastAPI

# Instância principal da aplicação ASGI
app = FastAPI(
    title="Primeira API",
    description="Exemplo didático da unidade 01",
    version="0.1.0",
)


@app.get("/")
def home() -> dict[str, str]:
    """Endpoint raiz: retorna um JSON simples."""
    return {"mensagem": "API no ar"}


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"status": "ok"}
