"""
03 - Parâmetros de rota (path)
==============================

Path parameters são valores embutidos na URL.
"""

from fastapi import FastAPI

app = FastAPI(title="Parâmetros de rota")


@app.get("/usuarios/{user_id}")
def obter_usuario(user_id: int) -> dict[str, int]:
    """
    FastAPI converte e valida `user_id` como inteiro.

    - /usuarios/abc retorna 422 (validação).
    - /usuarios/1 retorna {"user_id": 1}.
    """
    return {"user_id": user_id}


@app.get("/itens/{nome}")
def obter_item_por_nome(nome: str) -> dict[str, str]:
    """Strings na rota também são validadas como tipo `str`."""
    return {"nome": nome}
