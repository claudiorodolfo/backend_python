# Soluções — Aula 10

## Exercício 1 — `apiFetch` centralizado

Use o padrão da própria aula (ou o `apiFetch` já existente em `Projeto1` em `src/api/client.js`). Garanta:

- `baseURL` via `import.meta.env.VITE_API_URL`
- `Content-Type: application/json`
- `Authorization` opcional

## Exercício 2 — `pessoasApi`

```js
import { apiFetch } from "./client.js";

export const pessoasApi = {
  list: () => apiFetch("/pessoas"),
  create: (body) => apiFetch("/pessoas", { method: "POST", body }),
  update: (id, body) => apiFetch(`/pessoas/${id}`, { method: "PUT", body }),
  remove: (id) => apiFetch(`/pessoas/${id}`, { method: "DELETE" }),
};
```

Ajuste `apiFetch` para aceitar `{ token }` se usar auth.

## Exercício 3 — `DELETE` 204

No `apiFetch`, após ler o status:

```js
if (res.status === 204) return null;
```

Não chame `JSON.parse` no corpo vazio (o exemplo da aula já trata isso com `text` vazio).

## Desafio — Timeout + cancelar ao desmontar

```js
export async function apiFetch(
  path,
  { method = "GET", body, token, signal, timeoutMs = 15_000 } = {}
) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);
  const mergedSignal = signal
    ? AbortSignal.any([signal, controller.signal])
    : controller.signal;

  try {
    const res = await fetch(`${BASE}${path}`, {
      method,
      headers: {
        "Content-Type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: body ? JSON.stringify(body) : undefined,
      signal: mergedSignal,
    });
    // ... mesmo parse da aula
  } finally {
    clearTimeout(timeout);
  }
}
```

No componente:

```jsx
useEffect(() => {
  const ac = new AbortController();
  apiFetch("/pessoas", { signal: ac.signal }).then(setData).catch(setError);
  return () => ac.abort();
}, []);
```

> `AbortSignal.any` é recente; em ambientes antigos, use só `ac.signal` e um `alive` boolean como na Aula 07.
