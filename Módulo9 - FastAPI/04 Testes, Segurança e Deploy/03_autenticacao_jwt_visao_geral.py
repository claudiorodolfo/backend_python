"""
03 - Autenticação JWT (visão geral)
===================================

Este arquivo é um **guia conceitual**. Implementação completa costuma usar:

- `OAuth2PasswordBearer` ou OAuth2PasswordRequestForm (fluxo password).
- Biblioteca para JWT, por exemplo `python-jose` (com `cryptography`).
- Hash de senhas: `passlib[bcrypt]` ou similar.
- Armazenamento de usuários no banco.

Fluxo típico (login):

1. Cliente envia `username` + `password` (idealmente via HTTPS).
2. API valida credenciais e devolve um **access token** JWT.
3. Nas rotas protegidas, o cliente envia `Authorization: Bearer <token>`.
4. API valida assinatura, expiração e escopos do token.

No FastAPI, veja o tutorial oficial:
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

Dependências comuns (exemplo):

    pip install "python-jose[cryptography]" passlib[bcrypt]

Esboço de dependência (não executável sem configuração real):

    from fastapi import Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        # decodificar JWT, buscar usuário, etc.
        ...
"""
