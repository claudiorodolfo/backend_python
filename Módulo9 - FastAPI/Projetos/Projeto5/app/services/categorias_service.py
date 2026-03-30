from sqlmodel import Session
from app.models import Categoria
from app.repositories.categorias_repository import CategoriasRepository
from app.schemas.categorias import CategoriaCreate, CategoriaUpdate

class CategoriasService:
    def __init__(self, repository: CategoriasRepository) -> None:
        self.repository = repository

    def list(self, session: Session) -> list[Categoria]:
        return self.repository.list(session)

    def get(self, session: Session, categoria_id: int) -> Categoria | None:
        return self.repository.get(session, categoria_id)

    def create(self, session: Session, payload: CategoriaCreate) -> Categoria:
        return self.repository.create(session, payload)

    def update(self, session: Session, categoria: Categoria, payload: CategoriaUpdate) -> Categoria:
        return self.repository.update(session, categoria, payload)

    def delete(self, session: Session, categoria: Categoria) -> None:
        self.repository.delete(session, categoria)
