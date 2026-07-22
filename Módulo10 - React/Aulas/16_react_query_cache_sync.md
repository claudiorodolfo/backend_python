## Aula 16 — TanStack Query (React Query): cache, sync e estado de servidor

### Objetivos

- Separar **estado de UI** do **estado de servidor**
- Cache, refetch e invalidação após mutações
- Substituir parte do `useEffect + fetch`

### Instalação

```bash
npm i @tanstack/react-query
```

### Provider

```jsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

export function AppProviders({ children }) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
```

### Query + Mutation

```jsx
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

function usePessoas() {
  return useQuery({
    queryKey: ["pessoas"],
    queryFn: () => api.get("/pessoas").then((r) => r.data), // ou sua camada api
  });
}
```

Após `create`, invalide `["pessoas"]` para refletir a lista.

### Exercícios

1. Converta a lista de pessoas do `Projeto1` para `useQuery`.
2. Converta criação para `useMutation` com `onSuccess` invalidando a query.
3. Adicione `retry: 1` e um botão “Refetch”.

### Desafio

Implemente **optimistic update** em `update` (reverte se falhar).
