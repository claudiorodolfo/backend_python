from sqlmodel import Session, select
from app.models import Produto
from app.schemas.produtos import ProdutoCreate, ProdutoUpdate

class ProdutosRepository:
    def list(self, session: Session, nome: str | None, preco_min: float | None, preco_max: float | None) -> list[Produto]:
        query = select(Produto)
        if nome:
            query = query.where(Produto.nome.contains(nome))
        if preco_min is not None:
            query = query.where(Produto.preco >= preco_min)
        if preco_max is not None:
            query = query.where(Produto.preco <= preco_max)
        return list(session.exec(query).all())

    def get(self, session: Session, produto_id: int) -> Produto | None:
        return session.get(Produto, produto_id)

    def create(self, session: Session, payload: ProdutoCreate) -> Produto:
        produto = Produto(**payload.model_dump())
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto

    def update(self, session: Session, produto: Produto, payload: ProdutoUpdate) -> Produto:
        for k, v in payload.model_dump().items():
            if v is not None:
                setattr(produto, k, v)
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto

    def delete(self, session: Session, produto: Produto) -> None:
        session.delete(produto)
        session.commit()
