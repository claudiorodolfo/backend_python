# Soluções — Aula 15

## Exercícios 1–3 — Login, header e 401

### Salvar token após login

```js
async function login(email, password) {
  const res = await fetch(`${API}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error("Login falhou");
  const data = await res.json();
  localStorage.setItem("token", data.access_token);
  return data;
}
```

### `apiFetch` com `Authorization`

```js
export async function apiFetch(path, opts = {}) {
  const token = localStorage.getItem("token");
  const headers = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...opts.headers,
  };
  const res = await fetch(`${BASE}${path}`, { ...opts, headers });
  if (res.status === 401) {
    localStorage.removeItem("token");
    window.location.assign("/login");
    throw new Error("Não autorizado");
  }
  // … resto do parse
}
```

### Referência no repositório

O **Projeto2** em `Projetos/Projeto2-Fullstack-Pessoas-Auth/` já implementa fluxo semelhante (`frontend/src/context/AuthContext.jsx`, `frontend/src/api/client.js`).

## Desafio — Refresh token (visão geral)

1. No login, além do `access_token`, guarde `refresh_token` (ex.: `localStorage` ou cookie HttpOnly via backend).
2. Em `apiFetch`, se receber `401` e houver refresh, chame `POST /auth/refresh` com o refresh, atualize o access token e **repita** a requisição original uma vez.
3. Se o refresh falhar, faça logout completo.

Pseudo-código:

```js
let refreshing = null;

async function refreshAccess() {
  const r = localStorage.getItem("refresh_token");
  const res = await fetch(`${API}/auth/refresh`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh_token: r }),
  });
  if (!res.ok) throw new Error("refresh failed");
  const data = await res.json();
  localStorage.setItem("token", data.access_token);
  return data.access_token;
}
```

No tratamento de `401` da primeira tentativa, aguarde `refreshing ??= refreshAccess()` antes de repetir o `fetch`.
