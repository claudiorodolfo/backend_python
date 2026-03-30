from sqlmodel import Session
from app.models import Produto
from app.repositories.categorias_repository import CategoriasRepository
from app.repositories.produtos_repository import ProdutosRepository
from app.schemas.produtos import ProdutoCreate

class ProdutosService:
    def __init__(self, repository: ProdutosRepository, categorias_repository: CategoriasRepository) -> None:
        self.repository = repository
        self.categorias_repository = categorias_repository

    def list(self, session: Session) -> list[Produto]:
        return self.repository.list(session)

    def create(self, session: Session, payload: ProdutoCreate) -> Produto | None:
        if not self.categorias_repository.get(session, payload.categoria_id):
            return None
        return self.repository.create(session, payload)
