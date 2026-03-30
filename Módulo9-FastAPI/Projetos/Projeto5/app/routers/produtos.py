from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.db import get_session
from app.models import Produto
from app.repositories.categorias_repository import CategoriasRepository
from app.repositories.produtos_repository import ProdutosRepository
from app.schemas.produtos import ProdutoCreate, ProdutoUpdate
from app.services.produtos_service import ProdutosService

router = APIRouter(prefix='/produtos', tags=['Produtos'])
service = ProdutosService(ProdutosRepository(), CategoriasRepository())

@router.get('', response_model=list[Produto])
def list_produtos(nome: str | None = Query(default=None), preco_min: float | None = Query(default=None), preco_max: float | None = Query(default=None), session: Session = Depends(get_session)) -> list[Produto]:
    return service.list(session, nome=nome, preco_min=preco_min, preco_max=preco_max)

@router.post('', response_model=Produto, status_code=201)
def create_produto(payload: ProdutoCreate, session: Session = Depends(get_session)) -> Produto:
    produto = service.create(session, payload)
    if not produto:
        raise HTTPException(status_code=400, detail='Categoria inválida')
    return produto

@router.patch('/{produto_id}', response_model=Produto)
def update_produto(produto_id: int, payload: ProdutoUpdate, session: Session = Depends(get_session)) -> Produto:
    produto = service.get(session, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    atualizado = service.update(session, produto, payload)
    if not atualizado:
        raise HTTPException(status_code=400, detail='Categoria inválida')
    return atualizado

@router.delete('/{produto_id}', status_code=204)
def delete_produto(produto_id: int, session: Session = Depends(get_session)) -> None:
    produto = service.get(session, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    service.delete(session, produto)
