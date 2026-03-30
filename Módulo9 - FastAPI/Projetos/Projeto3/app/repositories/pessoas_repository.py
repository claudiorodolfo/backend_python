from sqlmodel import Session, select
from app.models import Pessoa
from app.schemas.pessoas import PessoaCreate, PessoaUpdate

class PessoasRepository:
    def list(self, session: Session) -> list[Pessoa]:
        return list(session.exec(select(Pessoa)).all())

    def get(self, session: Session, pessoa_id: int) -> Pessoa | None:
        return session.get(Pessoa, pessoa_id)

    def create(self, session: Session, payload: PessoaCreate) -> Pessoa:
        pessoa = Pessoa(**payload.model_dump())
        session.add(pessoa)
        session.commit()
        session.refresh(pessoa)
        return pessoa

    def update(self, session: Session, pessoa: Pessoa, payload: PessoaUpdate) -> Pessoa:
        for k, v in payload.model_dump().items():
            if v is not None:
                setattr(pessoa, k, v)
        session.add(pessoa)
        session.commit()
        session.refresh(pessoa)
        return pessoa

    def delete(self, session: Session, pessoa: Pessoa) -> None:
        session.delete(pessoa)
        session.commit()
