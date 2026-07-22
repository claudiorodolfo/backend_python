## Aula 01 — Fundamentos Web e JavaScript Moderno (para React)

### Objetivos

- Revisar HTTP, JSON e CORS
- Consolidar ES Modules, `async/await`, destructuring
- Entender como o frontend conversa com o backend FastAPI

### Conceitos essenciais

- **HTTP**: métodos (`GET/POST/PUT/DELETE`), status (200, 201, 204, 400, 401, 404, 422, 500)
- **JSON**: formato de troca de dados
- **CORS**: browser bloqueia requisições cross-origin sem permissão do backend

### JavaScript que você vai usar o tempo todo

#### Import/Export (ESM)

```js
export function sum(a, b) {
  return a + b;
}
```

```js
import { sum } from "./math";
```

#### Destructuring

```js
const pessoa = { id: 1, nome: "Ana", email: "ana@email.com" };
const { id, nome } = pessoa;
```

#### Async/Await + Fetch

```js
async function listPessoas() {
  const res = await fetch("http://localhost:8000/pessoas");
  if (!res.ok) throw new Error("Falha ao carregar");
  return await res.json();
}
```

### Exercícios

1. Crie uma função `getJson(url)` que:
   - usa `fetch`
   - lança erro se `res.ok` for falso
   - retorna `res.json()`
2. Faça uma função `sleep(ms)` e teste `await sleep(500)`

### Desafio

Modele (em um arquivo `.md`) o contrato JSON de uma entidade `Pessoa`:

- `id: number`
- `nome: string`
- `email: string`

