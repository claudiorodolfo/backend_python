from app.core.security import create_access_token, hash_password, verify_password
from app.repositories.users_repository import UsersRepository
from app.schemas.auth import UserOut


class AuthService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def register(self, username: str, password: str) -> UserOut:
        if self.repository.get_by_username(username):
            raise ValueError("Usuário já existe")
        self.repository.create(username, hash_password(password))
        return UserOut(username=username)

    def login(self, username: str, password: str) -> str | None:
        user = self.repository.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user["password_hash"]):
            return None
        return create_access_token(username)
