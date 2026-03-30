from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.models import Categoria
from app.repositories.categorias_repository import CategoriasRepository
from app.schemas.categorias import CategoriaCreate, CategoriaUpdate
from app.services.categorias_service import CategoriasService

router = APIRouter(prefix='/categorias', tags=['Categorias'])
service = CategoriasService(CategoriasRepository())

@router.get('', response_model=list[Categoria])
def list_categorias(session: Session = Depends(get_session)) -> list[Categoria]:
    return service.list(session)

@router.post('', response_model=Categoria, status_code=201)
def create_categoria(payload: CategoriaCreate, session: Session = Depends(get_session)) -> Categoria:
    return service.create(session, payload)

@router.patch('/{categoria_id}', response_model=Categoria)
def update_categoria(categoria_id: int, payload: CategoriaUpdate, session: Session = Depends(get_session)) -> Categoria:
    categoria = service.get(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail='Categoria não encontrada')
    return service.update(session, categoria, payload)

@router.delete('/{categoria_id}', status_code=204)
def delete_categoria(categoria_id: int, session: Session = Depends(get_session)) -> None:
    categoria = service.get(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail='Categoria não encontrada')
    service.delete(session, categoria)
