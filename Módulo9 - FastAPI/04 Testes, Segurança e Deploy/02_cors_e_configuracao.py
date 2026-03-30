"""
02 - CORS e configuração
========================

Quando o front-end roda em outro domínio/porta, o navegador aplica CORS.
Para APIs públicas de desenvolvimento, costuma-se liberar origens específicas.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/publico")
def publico() -> dict[str, str]:
    return {"msg": "ok"}


"""
Boas práticas em produção:

- Liste apenas origens confiáveis em `allow_origins` (não use ["*"] com cookies).
- Use variáveis de ambiente para URLs: `os.getenv("FRONTEND_ORIGIN")`.
- Nunca commite segredos (chaves JWT, senhas de banco).

Exemplo de leitura de ambiente:

    import os

    ALLOWED = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
"""
