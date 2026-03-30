from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.models import Pessoa
from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.pessoas import PessoaCreate, PessoaUpdate
from app.services.pessoas_service import PessoasService

router = APIRouter(prefix='/pessoas', tags=['Pessoas'])
service = PessoasService(PessoasRepository())

@router.get('', response_model=list[Pessoa])
def list_pessoas(session: Session = Depends(get_session)) -> list[Pessoa]:
    return service.list(session)

@router.post('', response_model=Pessoa, status_code=201)
def create_pessoa(payload: PessoaCreate, session: Session = Depends(get_session)) -> Pessoa:
    return service.create(session, payload)

@router.patch('/{pessoa_id}', response_model=Pessoa)
def update_pessoa(pessoa_id: int, payload: PessoaUpdate, session: Session = Depends(get_session)) -> Pessoa:
    pessoa = service.get(session, pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
    return service.update(session, pessoa, payload)

@router.delete('/{pessoa_id}', status_code=204)
def delete_pessoa(pessoa_id: int, session: Session = Depends(get_session)) -> None:
    pessoa = service.get(session, pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
    service.delete(session, pessoa)
