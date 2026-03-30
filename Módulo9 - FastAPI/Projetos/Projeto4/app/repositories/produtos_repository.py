from sqlmodel import Session, select
from app.models import Produto
from app.schemas.produtos import ProdutoCreate

class ProdutosRepository:
    def list(self, session: Session) -> list[Produto]:
        return list(session.exec(select(Produto)).all())

    def create(self, session: Session, payload: ProdutoCreate) -> Produto:
        produto = Produto(**payload.model_dump())
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto
