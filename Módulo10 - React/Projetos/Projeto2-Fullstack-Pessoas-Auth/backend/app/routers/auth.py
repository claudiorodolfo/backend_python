from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.deps import get_auth_service, get_current_user
from app.schemas.auth import Token, UserOut
from app.services.auth_service import AuthService

router = APIRouter()


class RegisterBody(BaseModel):
    username: str
    password: str


class LoginBody(BaseModel):
    username: str
    password: str


@router.post("/register", response_model=UserOut)
def register(body: RegisterBody, auth: AuthService = Depends(get_auth_service)) -> UserOut:
    try:
        return auth.register(body.username.strip(), body.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
def login(body: LoginBody, auth: AuthService = Depends(get_auth_service)) -> Token:
    token = auth.login(body.username.strip(), body.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return Token(access_token=token, token_type="bearer")


@router.get("/me", response_model=UserOut)
def me(user: UserOut = Depends(get_current_user)) -> UserOut:
    return user
