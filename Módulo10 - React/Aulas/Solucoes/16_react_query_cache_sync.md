# Soluções — Aula 16

## Exercício 1 — Lista com `useQuery`

```jsx
import { useQuery } from "@tanstack/react-query";
import { pessoasApi } from "../api/pessoas";

export function usePessoasQuery() {
  return useQuery({
    queryKey: ["pessoas"],
    queryFn: () => pessoasApi.list(),
  });
}

export default function PessoasList() {
  const { data, isLoading, error, refetch } = usePessoasQuery();

  if (isLoading) return <p>Carregando…</p>;
  if (error) return <p>Erro: {String(error.message)}</p>;

  return (
    <ul>
      {data.map((p) => (
        <li key={p.id}>{p.nome}</li>
      ))}
    </ul>
  );
}
```

## Exercício 2 — Criação com `useMutation` + invalidação

```jsx
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { pessoasApi } from "../api/pessoas";

export function useCreatePessoa() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (body) => pessoasApi.create(body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["pessoas"] });
    },
  });
}
```

## Exercício 3 — `retry: 1` e “Refetch”

```jsx
const q = useQuery({
  queryKey: ["pessoas"],
  queryFn: () => pessoasApi.list(),
  retry: 1,
});

// …
<button type="button" onClick={() => q.refetch()}>
  Refetch
</button>
```

## Desafio — Optimistic update no `update`

```jsx
useMutation({
  mutationFn: ({ id, body }) => pessoasApi.update(id, body),
  onMutate: async ({ id, body }) => {
    await qc.cancelQueries({ queryKey: ["pessoas"] });
    const previous = qc.getQueryData(["pessoas"]);
    qc.setQueryData(["pessoas"], (old) =>
      old.map((p) => (p.id === id ? { ...p, ...body } : p))
    );
    return { previous };
  },
  onError: (_err, _vars, ctx) => {
    qc.setQueryData(["pessoas"], ctx.previous);
  },
  onSettled: () => {
    qc.invalidateQueries({ queryKey: ["pessoas"] });
  },
});
```
