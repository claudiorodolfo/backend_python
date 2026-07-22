# Soluções — Aula 01

## Exercício 1 — `getJson(url)`

```js
export async function getJson(url) {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${res.statusText}`);
  }
  return res.json();
}
```

## Exercício 2 — `sleep(ms)`

```js
export function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Uso:
// await sleep(500);
```

## Desafio — Contrato JSON `Pessoa`

Crie um arquivo `contrato-pessoa.md` com tabela de campos e exemplos.

**Campos:** `id` (number, na leitura), `nome` (string), `email` (string).

**Exemplo de resposta (GET):**

`{ "id": 1, "nome": "Ana Silva", "email": "ana@email.com" }`

**Exemplo de criação (POST, sem `id`):**

`{ "nome": "Ana Silva", "email": "ana@email.com" }`
