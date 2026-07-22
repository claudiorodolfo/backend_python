## Aula 15 — Autenticação: JWT, armazenamento e rotas protegidas

### Objetivos

- Entender fluxo **login → access token → requests autenticadas**
- Armazenar token com trade-offs (`localStorage` vs `memory` + cookie HttpOnly)
- Proteger rotas no React Router

### Fluxo típico (SPA + FastAPI)

1. `POST /auth/login` com credenciais
2. Resposta: `{ access_token, token_type: "bearer" }`
3. Chamadas subsequentes: header `Authorization: Bearer <token>`

### Armazenamento (trade-offs)

- **`localStorage`**: simples para curso; vulnerável a XSS — não coloque dados sensíveis além do necessário.
- **Cookie HttpOnly** (mais seguro): exige configuração extra no backend/front (CORS, CSRF). Para produção, estude esse modelo.

### Rotas protegidas (padrão)

```tsx
function RequireAuth({ children }) {
  const { token } = useAuth();
  if (!token) return <Navigate to="/login" replace />;
  return children;
}
```

### Exercícios

1. Implemente login que salva token no `localStorage`.
2. Decore `apiFetch` para anexar `Authorization` automaticamente.
3. Trate `401` com logout e redirect.

### Desafio

Implemente **refresh token** (rota `/auth/refresh`) — o `Projeto2` pode ser estendido depois com esse passo.

### Referência de implementação

Veja o **Projeto2** em `Projetos/Projeto2-Fullstack-Pessoas-Auth/`.
