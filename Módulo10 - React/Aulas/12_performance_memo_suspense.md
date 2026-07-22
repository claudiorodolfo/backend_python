## Aula 12 — Performance: `memo`, `useMemo`, `useCallback` e Suspense

### Objetivos

- Saber **quando** otimizar (medir antes)
- Evitar re-render caro com `React.memo`
- Estabilizar referências com `useMemo` / `useCallback`
- Introdução a `Suspense` com lazy loading

### Regra de ouro

Otimize quando há **prova** de gargalo (React DevTools Profiler, lentidão perceptível).

### `React.memo`

Útil para componentes “puros” que re-renderizam por causa do pai sem mudar props.

```jsx
import { memo } from "react";

export const PessoaRow = memo(function PessoaRow({ pessoa, onDelete }) {
  // ...
});
```

### `useMemo` / `useCallback`

- `useMemo`: valor derivado caro
- `useCallback`: função passada para filhos memoizados

### Lazy + Suspense

```jsx
import { lazy, Suspense } from "react";

const Relatorio = lazy(() => import("./Relatorio"));

export function Pagina() {
  return (
    <Suspense fallback={<p>Carregando módulo…</p>}>
      <Relatorio />
    </Suspense>
  );
}
```

### Exercícios

1. Profile uma lista grande: identifique quem re-renderiza sem necessidade.
2. Extraia linha da lista para `memo` e compare.
3. Lazy-load uma rota pesada.

### Desafio

Compare duas versões no Profiler: com e sem `memo` em um filho “caro”.
