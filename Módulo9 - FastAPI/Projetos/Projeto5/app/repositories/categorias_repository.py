from sqlmodel import Session, select
from app.models import Categoria
from app.schemas.categorias import CategoriaCreate, CategoriaUpdate

class CategoriasRepository:
    def list(self, session: Session) -> list[Categoria]:
        return list(session.exec(select(Categoria)).all())

    def get(self, session: Session, categoria_id: int) -> Categoria | None:
        return session.get(Categoria, categoria_id)

    def create(self, session: Session, payload: CategoriaCreate) -> Categoria:
        categoria = Categoria(**payload.model_dump())
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        return categoria

    def update(self, session: Session, categoria: Categoria, payload: CategoriaUpdate) -> Categoria:
        for k, v in payload.model_dump().items():
            if v is not None:
                setattr(categoria, k, v)
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        return categoria

    def delete(self, session: Session, categoria: Categoria) -> None:
        session.delete(categoria)
        session.commit()
