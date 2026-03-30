from fastapi import APIRouter, HTTPException, Query
from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.pessoas import PessoaCreate, PessoaOut, PessoaUpdate
from app.services.pessoas_service import PessoasService

router = APIRouter(prefix='/pessoas', tags=['Pessoas'])
service = PessoasService(PessoasRepository())

@router.get('', response_model=list[PessoaOut])
def list_pessoas(nome: str | None = Query(default=None), email: str | None = Query(default=None), ativa: bool | None = Query(default=None)) -> list[PessoaOut]:
    return service.list(nome=nome, email=email, ativa=ativa)

@router.post('', response_model=PessoaOut, status_code=201)
def create_pessoa(payload: PessoaCreate) -> PessoaOut:
    return service.create(payload)

@router.patch('/{pessoa_id}', response_model=PessoaOut)
def patch_pessoa(pessoa_id: int, payload: PessoaUpdate) -> PessoaOut:
    pessoa = service.update(pessoa_id, payload)
    if not pessoa:
        raise HTTPException(status_code=404, detail='Pessoa não encontrada')
    return pessoa
