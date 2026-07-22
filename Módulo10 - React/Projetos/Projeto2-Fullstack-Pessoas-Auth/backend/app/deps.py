from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.core import security
from app.repositories.users_repository import UsersRepository
from app.schemas.auth import UserOut
from app.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

_users_repo = UsersRepository()


def get_users_repo() -> UsersRepository:
    return _users_repo


def get_auth_service(users: UsersRepository = Depends(get_users_repo)) -> AuthService:
    return AuthService(users)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users: UsersRepository = Depends(get_users_repo),
) -> UserOut:
    try:
        username = security.decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )
    user = users.get_by_username(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
        )
    return UserOut(username=user["username"])
