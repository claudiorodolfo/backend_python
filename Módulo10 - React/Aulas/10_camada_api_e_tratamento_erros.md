## Aula 10 — Camada de API e tratamento de erros

### Objetivos

- Isolar URLs, headers e parse de erro
- Padronizar respostas do FastAPI (`HTTPException`, 422 validation)
- Evitar repetir `fetch` espalhado na UI

### Camada `api/client`

Responsabilidades:

- `baseURL` (via `import.meta.env.VITE_API_URL`)
- JSON automático
- Headers comuns (`Content-Type`, `Authorization`)

Exemplo com `fetch` (minimalista):

```js
const BASE = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export async function apiFetch(path, { method = "GET", body, token } = {}) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers.Authorization = `Bearer ${token}`;

  const res = await fetch(`${BASE}${path}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });

  if (res.status === 204) return null;

  const text = await res.text();
  const data = text ? JSON.parse(text) : null;

  if (!res.ok) {
    const msg = data?.detail ?? text ?? res.statusText;
    throw new Error(typeof msg === "string" ? msg : JSON.stringify(msg));
  }

  return data;
}
```

### Erros comuns no SPA + FastAPI

- **CORS**: configure `CORSMiddleware` no backend (vide `Projeto2`).
- **422**: body inválido; mostre `detail` no UI.
- **401/403**: token ausente/expirado/permissão.

### Exercícios

1. Extraia `apiFetch` e substitua chamadas diretas na UI.
2. Crie `pessoasApi.list()`, `.create()`, `.update()`, `.remove()`.
3. Trate `DELETE` retornando 204 sem JSON.

### Desafio

Adicione timeout/abort com `AbortController` e cancele requisições ao desmontar.
