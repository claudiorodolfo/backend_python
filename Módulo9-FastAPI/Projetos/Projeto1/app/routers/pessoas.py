from fastapi import APIRouter, HTTPException
from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.pessoas import PessoaCreate, PessoaOut, PessoaUpdate
from app.services.pessoas_service import PessoasService

router = APIRouter(prefix='/pessoas', tags=['Pessoas'])
service = PessoasService(PessoasRepository())

@router.get('', response_model=list[PessoaOut])
def list_pessoas() -> list[PessoaOut]:
    return service.list()

@router.get('/{pessoa_id}', response_model=PessoaOut)
def get_pessoa(pessoa_id: int) -> PessoaOut:
    pessoa = service.get(pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
    return pessoa

@router.post('', response_model=PessoaOut, status_code=201)
def create_pessoa(payload: PessoaCreate) -> PessoaOut:
    return service.create(payload)

@router.put('/{pessoa_id}', response_model=PessoaOut)
def update_pessoa(pessoa_id: int, payload: PessoaUpdate) -> PessoaOut:
    pessoa = service.update(pessoa_id, payload)
    if not pessoa:
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
    return pessoa

@router.delete('/{pessoa_id}', status_code=204)
def delete_pessoa(pessoa_id: int) -> None:
    if not service.delete(pessoa_id):
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
