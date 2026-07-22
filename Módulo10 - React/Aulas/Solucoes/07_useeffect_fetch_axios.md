# Soluções — Aula 07

## Exercício 1 — `src/api/pessoas.js`

```js
const BASE = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export async function getPessoas() {
  const res = await fetch(`${BASE}/pessoas`);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
```

No Projeto1 em dev com proxy, troque a URL por sua função `path("/pessoas")` ou importe `apiFetch` de `./client.js` e use `apiFetch("/pessoas")`.

## Exercício 2 — Lista com “Tentar novamente”

```jsx
import { useEffect, useState } from "react";
import { getPessoas } from "../api/pessoas.js";

export default function PessoasLoader() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  function load() {
    let alive = true;
    setLoading(true);
    setError("");
    getPessoas()
      .then((rows) => {
        if (alive) setData(rows);
      })
      .catch((e) => {
        if (alive) setError(String(e.message ?? e));
      })
      .finally(() => {
        if (alive) setLoading(false);
      });
    return () => {
      alive = false;
    };
  }

  useEffect(() => {
    const cancel = load();
    return cancel;
  }, []);

  if (loading) return <p>Carregando…</p>;
  if (error) {
    return (
      <div>
        <p>Erro: {error}</p>
        <button type="button" onClick={load}>
          Tentar novamente
        </button>
      </div>
    );
  }

  return (
    <ul>
      {data.map((p) => (
        <li key={p.id}>{p.nome}</li>
      ))}
    </ul>
  );
}
```

> Ajuste: `load` acima retorna cleanup; para “Tentar novamente”, use um `key` ou `useCallback` + estado de “tentativa” para repetir o `useEffect` sem vazar atualizações. Padrão simples: incrementar `retryCount` no clique e colocá-lo nas deps do `useEffect`.

Versão com retry explícito:

```jsx
const [retry, setRetry] = useState(0);

useEffect(() => {
  let alive = true;
  // ... mesma lógica getPessoas
  return () => {
    alive = false;
  };
}, [retry]);

// botão: onClick={() => setRetry((r) => r + 1)}
```

## Exercício 3 (opcional) — Axios

```js
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000",
});

export function getPessoasAxios() {
  return api.get("/pessoas").then((r) => r.data);
}
```

## Desafio — Busca por id (preparação ao Router)

```js
export async function getPessoaById(id) {
  const res = await fetch(`${BASE}/pessoas/${id}`);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
```

Em uma página de detalhe (depois com `useParams`):

```jsx
const { id } = useParams();
useEffect(() => {
  getPessoaById(id).then(setPessoa).catch(setError);
}, [id]);
```
