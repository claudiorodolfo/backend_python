from fastapi import APIRouter, Depends, HTTPException

from app.deps import get_current_user
from app.repositories.pessoas_repository import PessoasRepository
from app.schemas.auth import UserOut
from app.schemas.pessoas import PessoaCreate, PessoaOut, PessoaUpdate
from app.services.pessoas_service import PessoasService

router = APIRouter()
service = PessoasService(PessoasRepository())


@router.get("", response_model=list[PessoaOut])
def list_pessoas(_user: UserOut = Depends(get_current_user)) -> list[PessoaOut]:
    return service.list()


@router.get("/{pessoa_id}", response_model=PessoaOut)
def get_pessoa(pessoa_id: int, _user: UserOut = Depends(get_current_user)) -> PessoaOut:
    pessoa = service.get(pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa


@router.post("", response_model=PessoaOut, status_code=201)
def create_pessoa(
    payload: PessoaCreate,
    _user: UserOut = Depends(get_current_user),
) -> PessoaOut:
    return service.create(payload)


@router.put("/{pessoa_id}", response_model=PessoaOut)
def update_pessoa(
    pessoa_id: int,
    payload: PessoaUpdate,
    _user: UserOut = Depends(get_current_user),
) -> PessoaOut:
    pessoa = service.update(pessoa_id, payload)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa


@router.delete("/{pessoa_id}", status_code=204)
def delete_pessoa(pessoa_id: int, _user: UserOut = Depends(get_current_user)) -> None:
    if not service.delete(pessoa_id):
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
