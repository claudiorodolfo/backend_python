"""
01 - Testes com pytest e TestClient
===================================

O FastAPI expõe uma instância ASGI que o `starlette.testclient` consome.

Instalação:

    pip install fastapi pytest httpx

Rodar testes (na pasta que contém `test_exemplo.py` junto deste arquivo ou do projeto):

    pytest -q
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


client = TestClient(app)


# Rode manualmente no interpretador ou veja `tests/test_exemplo_cliente.py`
# para o mesmo cenário executado com: pytest -q
def _demo_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


"""
Em projetos reais, coloque testes em `tests/` e importe `app` de `app.main`:

    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

Nesta pasta, use `pytest -q` (há um exemplo em `tests/test_exemplo_cliente.py`).
"""
