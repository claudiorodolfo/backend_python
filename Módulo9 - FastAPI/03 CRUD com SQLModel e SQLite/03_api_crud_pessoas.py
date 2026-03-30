"""
03 - API CRUD mínima com SQLModel
=================================

Exemplo autocontido. Para rodar **a partir desta pasta**:

    pip install fastapi uvicorn sqlmodel
    uvicorn 03_api_crud_pessoas:app --reload

Será criado o arquivo `exemplo_crud.db` no diretório atual.

Veja também `01_modelo_sqlmodel.py` para o mesmo `class Pessoa` isolado.
"""

from collections.abc import Generator

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

DATABASE_URL = "sqlite:///./exemplo_crud.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class Pessoa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    email: str = Field(index=True)
    ativa: bool = Field(default=True)


class PessoaCreate(BaseModel):
    nome: str
    email: str
    ativa: bool = True


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


app = FastAPI(title="CRUD Pessoas (didático)")


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/pessoas", response_model=list[Pessoa])
def listar(session: Session = Depends(get_session)) -> list[Pessoa]:
    return list(session.exec(select(Pessoa)).all())


@app.get("/pessoas/{pessoa_id}", response_model=Pessoa)
def obter(pessoa_id: int, session: Session = Depends(get_session)) -> Pessoa:
    pessoa = session.get(Pessoa, pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return pessoa


@app.post("/pessoas", response_model=Pessoa, status_code=201)
def criar(payload: PessoaCreate, session: Session = Depends(get_session)) -> Pessoa:
    pessoa = Pessoa(**payload.model_dump())
    session.add(pessoa)
    session.commit()
    session.refresh(pessoa)
    return pessoa


@app.delete("/pessoas/{pessoa_id}", status_code=204)
def remover(pessoa_id: int, session: Session = Depends(get_session)) -> None:
    pessoa = session.get(Pessoa, pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Não encontrado")
    session.delete(pessoa)
    session.commit()
