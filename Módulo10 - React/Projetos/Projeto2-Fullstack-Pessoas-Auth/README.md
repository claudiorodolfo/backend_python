# Projeto2 — Fullstack React + FastAPI (JWT)

Aplicação de referência com:

- **Backend**: FastAPI, CRUD de pessoas em memória, **JWT** (login/registro), **CORS** para o Vite
- **Frontend**: React (Vite), login, token em `localStorage`, CRUD de pessoas

## Estrutura

- `backend/` — API
- `frontend/` — SPA

## Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Documentação interativa: `http://127.0.0.1:8000/docs`

### Rotas principais

| Método | Rota | Auth | Descrição |
|--------|------|------|-----------|
| POST | `/auth/register` | Não | Cria usuário |
| POST | `/auth/login` | Não | Retorna `access_token` |
| GET | `/auth/me` | Sim | Usuário do token |
| CRUD | `/pessoas` | Sim | Igual ao Projeto1 do Módulo9 |

> **Produção**: altere `SECRET_KEY` via variável de ambiente e restrinja `allow_origins` no CORS.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Abra `http://localhost:5173`. Em desenvolvimento o Vite faz proxy de `/api` para o backend (mesma lógica do Projeto1).

### Produção

```bash
VITE_API_URL=https://seu-api.exemplo.com npm run build
```

O backend precisa permitir CORS para o domínio do frontend.

## Fluxo de autenticação

1. Registre um usuário em `/register` (tela no frontend) ou `POST /auth/register`
2. Faça login — o frontend guarda `access_token` e envia `Authorization: Bearer ...` nas chamadas a `/pessoas`

## Saúde

`GET /health` → `{ "status": "ok" }`
