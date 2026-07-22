# Soluções — Aula 12

## Exercício 1 — Profiler

1. Instale a extensão **React DevTools** no navegador.
2. Abra a aba **Profiler**, clique em gravar, interaja com a lista (scroll, filtro, digitação).
3. Pare a gravação e identifique componentes com alto tempo de render ou muitas renderizações sem mudança de props relevante.

## Exercício 2 — Linha com `memo`

Antes: lista re-renderiza todas as linhas quando o estado do pai muda (ex.: contador no mesmo pai).

```jsx
import { memo } from "react";

export const PessoaRow = memo(function PessoaRow({ pessoa, onDelete }) {
  return (
    <tr>
      <td>{pessoa.nome}</td>
      <td>
        <button type="button" onClick={() => onDelete(pessoa.id)}>
          Remover
        </button>
      </td>
    </tr>
  );
});
```

**Importante:** estabilize `onDelete` com `useCallback` no pai se passar função inline que muda a cada render — caso contrário o `memo` não ajuda.

```jsx
const onDelete = useCallback((id) => {
  setRows((r) => r.filter((x) => x.id !== id));
}, []);
```

## Exercício 3 — Lazy route

```jsx
import { lazy, Suspense } from "react";
import { Route, Routes } from "react-router-dom";

const Relatorio = lazy(() => import("./pages/Relatorio.jsx"));

export function AppRoutes() {
  return (
    <Suspense fallback={<p>Carregando…</p>}>
      <Routes>
        <Route path="/relatorio" element={<Relatorio />} />
      </Routes>
    </Suspense>
  );
}
```

## Desafio — Comparar no Profiler

1. Grave interação com lista **sem** `memo` nas linhas.
2. Adicione `memo` (e `useCallback` no pai) e grave a mesma interação.
3. Compare “ranked” ou “flame graph”: tempo total e quantidade de commits.

Documente em uma linha o ganho (ou ausência de ganho) para o seu caso — listas pequenas muitas vezes não justificam `memo`.
