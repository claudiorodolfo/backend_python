from sqlmodel import Session
from app.models import Produto
from app.repositories.categorias_repository import CategoriasRepository
from app.repositories.produtos_repository import ProdutosRepository
from app.schemas.produtos import ProdutoCreate, ProdutoUpdate

class ProdutosService:
    def __init__(self, repository: ProdutosRepository, categorias_repository: CategoriasRepository) -> None:
        self.repository = repository
        self.categorias_repository = categorias_repository

    def list(self, session: Session, nome: str | None, preco_min: float | None, preco_max: float | None) -> list[Produto]:
        return self.repository.list(session, nome=nome, preco_min=preco_min, preco_max=preco_max)

    def get(self, session: Session, produto_id: int) -> Produto | None:
        return self.repository.get(session, produto_id)

    def create(self, session: Session, payload: ProdutoCreate) -> Produto | None:
        if not self.categorias_repository.get(session, payload.categoria_id):
            return None
        return self.repository.create(session, payload)

    def update(self, session: Session, produto: Produto, payload: ProdutoUpdate) -> Produto | None:
        if payload.categoria_id is not None and not self.categorias_repository.get(session, payload.categoria_id):
            return None
        return self.repository.update(session, produto, payload)

    def delete(self, session: Session, produto: Produto) -> None:
        self.repository.delete(session, produto)
