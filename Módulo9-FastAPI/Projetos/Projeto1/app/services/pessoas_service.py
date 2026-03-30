from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.pessoas import PessoaCreate, PessoaOut, PessoaUpdate

class PessoasService:
    def __init__(self, repository: PessoasRepository) -> None:
        self.repository = repository

    def list(self) -> list[PessoaOut]:
        return self.repository.list()

    def get(self, pessoa_id: int) -> PessoaOut | None:
        return self.repository.get(pessoa_id)

    def create(self, payload: PessoaCreate) -> PessoaOut:
        return self.repository.create(payload)

    def update(self, pessoa_id: int, payload: PessoaUpdate) -> PessoaOut | None:
        return self.repository.update(pessoa_id, payload)

    def delete(self, pessoa_id: int) -> bool:
        return self.repository.delete(pessoa_id)
