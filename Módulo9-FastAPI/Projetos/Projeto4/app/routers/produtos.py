from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.models import Produto
from app.repositories.categorias_repository import CategoriasRepository
from app.repositories.produtos_repository import ProdutosRepository
from app.schemas.produtos import ProdutoCreate
from app.services.produtos_service import ProdutosService

router = APIRouter(prefix='/produtos', tags=['Produtos'])
service = ProdutosService(ProdutosRepository(), CategoriasRepository())

@router.get('', response_model=list[Produto])
def list_produtos(session: Session = Depends(get_session)) -> list[Produto]:
    return service.list(session)

@router.post('', response_model=Produto, status_code=201)
def create_produto(payload: ProdutoCreate, session: Session = Depends(get_session)) -> Produto:
    produto = service.create(session, payload)
    if not produto:
        raise HTTPException(status_code=400, detail='Categoria inválida')
    return produto
