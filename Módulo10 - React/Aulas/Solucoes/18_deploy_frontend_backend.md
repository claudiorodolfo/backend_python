# Soluções — Aula 18

## Exercício 1 — Build e `vite preview`

No diretório do frontend (ex.: `Projeto1-React-Pessoas`):

```bash
npm install
npm run build
npm run preview
```

Abra a URL exibida no terminal (geralmente `http://localhost:4173`).

## Exercício 2 — Variáveis dev × prod

| Variável / config | Dev | Produção |
|-------------------|-----|----------|
| `VITE_API_URL` | `http://127.0.0.1:8000` ou vazio (proxy) | URL pública HTTPS da API |
| CORS no FastAPI | `localhost` | Domínio do frontend |
| `NODE_ENV` / modo Vite | development | production (automático no build) |

Arquivo `.env.production` (exemplo):

```env
VITE_API_URL=https://api.seudominio.com
```

## Exercício 3 — Checklist de deploy

1. **Build:** `npm run build`; artefatos em `dist/`.
2. **Secrets:** JWT secret, strings de DB, chaves de API só em variáveis de ambiente no servidor.
3. **CORS:** `allow_origins` com o domínio real do SPA.
4. **HTTPS:** terminado no proxy (Nginx/Caddy) ou na plataforma.
5. **SPA fallback:** `try_files … /index.html` ou equivalente.
6. **Healthcheck:** rota `GET /health` no backend para orquestradores.
7. **Logs:** stdout agregado; rotação e nível (INFO) em produção.
8. **Migrações:** se houver DB, comando documentado antes do `uvicorn`.

## Desafio — Docker multi-stage (frontend)

`Dockerfile` (exemplo):

```dockerfile
# build
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# runtime — só estáticos
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

`nginx.conf` mínimo com fallback SPA:

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

Backend: imagem separada com `uvicorn` ou `gunicorn` + `uvicorn.workers`, por trás do mesmo compose ou de um load balancer.
