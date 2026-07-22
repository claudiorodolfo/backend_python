# Projeto1 — React consumindo FastAPI (CRUD Pessoas)

SPA em **React (Vite)** que consome a API de pessoas do **Módulo9**:

`Módulo9 - FastAPI/Projetos/Projeto1/` (`GET/POST/PUT/DELETE /pessoas`).

## Por que existe proxy no Vite?

O app React roda em outra porta (ex.: `5173`) e o FastAPI em `8000`. O navegador bloqueia respostas **sem CORS** configurado no backend. Em desenvolvimento, o proxy do Vite encaminha `/api/*` para `http://127.0.0.1:8000/*`, evitando CORS.

## Pré-requisitos

- Node.js 18+ (recomendado 20+)
- API FastAPI rodando em **`http://127.0.0.1:8000`**

### Subir o backend (Módulo9)

Em outro terminal:

```bash
cd "Módulo9 - FastAPI/Projetos/Projeto1"
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install "pydantic[email]"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> O `EmailStr` do schema de pessoas costuma exigir `email-validator` (via `pip install "pydantic[email]"`).

## Rodar o frontend

```bash
cd "Módulo10 - React/Projetos/Projeto1-React-Pessoas"
npm install
npm run dev
```

Abra o endereço que o Vite mostrar (geralmente `http://localhost:5173`).

## Build de produção

```bash
npm run build
npm run preview
```

Em produção, defina a URL do backend:

```bash
VITE_API_URL=http://seu-servidor:8000 npm run build
```

Nesse modo o navegador chama o backend diretamente — **é obrigatório** habilitar **CORS** no FastAPI para o domínio do frontend.

## Estrutura (referência pedagógica)

- `src/api/client.js` — URLs (`/api` em dev via proxy) e `apiFetch`
- `src/components/PessoaForm.jsx` — criar/editar
- `src/components/PessoaList.jsx` — listar e excluir

## Saúde da API

`GET http://127.0.0.1:8000/health` → `{ "status": "ok" }`
