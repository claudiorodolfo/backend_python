## Aula 18 — Deploy (frontend e backend)

### Objetivos

- Build de produção do React (`npm run build`)
- Servir SPA e configurar **fallback** para `index.html`
- Rodar FastAPI atrás de um process manager (visão geral)

### Frontend (Vite)

```bash
npm run build
```

Saída em `dist/`. Em produção, arquivos estáticos costumam ir para:

- CDN + storage (S3, GCS, etc.) **ou**
- Nginx/Apache servindo `dist/` **ou**
- Plataforma (Vercel/Netlify) com redirects SPA

### SPA routing

Para React Router `BrowserRouter`, o servidor precisa devolver `index.html` para rotas desconhecidas (evita 404 ao dar F5 em `/pessoas`).

Exemplo Nginx:

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

### Backend (FastAPI)

Normalmente:

- `uvicorn app.main:app --host 0.0.0.0 --port 8000` atrás de **reverse proxy** (Nginx/Caddy)
- HTTPS no proxy
- Variáveis sensíveis via ambiente (`SECRET_KEY`, CORS origins)

### CORS em produção

Configure `allow_origins` com o domínio do frontend (não use `*` se houver credenciais/cookies).

### Exercícios

1. Gere build do `Projeto1` e sirva localmente com `vite preview`.
2. Liste variáveis que devem mudar entre dev e prod (`VITE_API_URL`).
3. Escreva um checklist de deploy (build, secrets, healthcheck, logs).

### Desafio

Containerize backend e frontend com **Docker** (multi-stage no frontend).
