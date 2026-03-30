"""
02 - Engine SQLite e sessão (dependency injection)
====================================================

Padrão comum no FastAPI: uma função geradora `get_session` injetada nas rotas.
"""

import os
from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

# SQLite local por padrão; em produção use variável de ambiente (ex.: Postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./exemplo_crud.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def create_db_and_tables() -> None:
    # Importe os modelos antes, para registrarem metadados
    # from .01_modelo_sqlmodel import Pessoa  # em pacote real use imports normais
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


"""
Uso típico na rota:

    from fastapi import Depends

    @app.get("/pessoas")
    def listar(session: Session = Depends(get_session)):
        ...
"""
