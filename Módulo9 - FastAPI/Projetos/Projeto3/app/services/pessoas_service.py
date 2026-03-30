from sqlmodel import Session
from app.models import Pessoa
from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.pessoas import PessoaCreate, PessoaUpdate

class PessoasService:
    def __init__(self, repository: PessoasRepository) -> None:
        self.repository = repository

    def list(self, session: Session) -> list[Pessoa]:
        return self.repository.list(session)

    def get(self, session: Session, pessoa_id: int) -> Pessoa | None:
        return self.repository.get(session, pessoa_id)

    def create(self, session: Session, payload: PessoaCreate) -> Pessoa:
        return self.repository.create(session, payload)

    def update(self, session: Session, pessoa: Pessoa, payload: PessoaUpdate) -> Pessoa:
        return self.repository.update(session, pessoa, payload)

    def delete(self, session: Session, pessoa: Pessoa) -> None:
        self.repository.delete(session, pessoa)
