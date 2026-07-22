from __future__ import annotations


class UsersRepository:
    def __init__(self) -> None:
        self._users: dict[str, dict[str, str]] = {}

    def get_by_username(self, username: str) -> dict[str, str] | None:
        return self._users.get(username)

    def create(self, username: str, password_hash: str) -> None:
        self._users[username] = {"username": username, "password_hash": password_hash}
