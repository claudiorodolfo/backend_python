from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session
from app.models import Categoria
from app.repositories.categorias_repository import CategoriasRepository
from app.schemas.categorias import CategoriaCreate
from app.services.categorias_service import CategoriasService

router = APIRouter(prefix='/categorias', tags=['Categorias'])
service = CategoriasService(CategoriasRepository())

@router.get('', response_model=list[Categoria])
def list_categorias(session: Session = Depends(get_session)) -> list[Categoria]:
    return service.list(session)

@router.post('', response_model=Categoria, status_code=201)
def create_categoria(payload: CategoriaCreate, session: Session = Depends(get_session)) -> Categoria:
    return service.create(session, payload)
