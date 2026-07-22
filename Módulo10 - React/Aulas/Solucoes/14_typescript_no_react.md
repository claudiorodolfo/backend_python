# Soluções — Aula 14

## Exercício 1 — Migração incremental

Ordem sugerida:

1. Renomeie `src/api/client.js` → `client.ts` e tipar retornos onde possível.
2. Renomeie componentes de folha para `.tsx` (ex.: `PessoaRow.tsx`).
3. Ative `strict` no `tsconfig.json` quando a maior parte compilar.

## Exercício 2 — `PessoaCreate`

```ts
type Pessoa = { id: number; nome: string; email: string };
type PessoaCreate = Pick<Pessoa, "nome" | "email">;

async function criarPessoa(body: PessoaCreate): Promise<Pessoa> {
  // fetch tipado…
  return {} as Pessoa;
}
```

## Exercício 3 — Rotas com `satisfies`

```ts
const ROUTES = {
  home: "/",
  pessoas: "/pessoas",
  pessoa: (id: string | number) => `/pessoas/${id}`,
} as const satisfies Record<string, string | ((id: string | number) => string)>;
```

(Ajuste o tipo `satisfies` conforme o que você exportar — o importante é o objeto constante ser verificado sem perder literais.)

## Desafio — `zod` na resposta da API

```ts
import { z } from "zod";

const PessoaSchema = z.object({
  id: z.number(),
  nome: z.string(),
  email: z.string().email(),
});

export type Pessoa = z.infer<typeof PessoaSchema>;

export function parsePessoa(data: unknown): Pessoa {
  return PessoaSchema.parse(data);
}

export async function fetchPessoa(id: number): Promise<Pessoa> {
  const res = await fetch(`/api/pessoas/${id}`);
  const json = await res.json();
  return parsePessoa(json);
}
```

Use `.safeParse` se quiser tratar erro de validação sem lançar.
