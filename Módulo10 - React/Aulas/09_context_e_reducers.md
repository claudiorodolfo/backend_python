## Aula 09 — Context API e `useReducer`

### Objetivos

- Evitar “prop drilling”
- Centralizar estado de domínio (tema, usuário, carrinho)
- Quando usar Context vs biblioteca externa

### Context: padrão mínimo

```jsx
import { createContext, useContext, useMemo, useState } from "react";

const TemaCtx = createContext(null);

export function TemaProvider({ children }) {
  const [tema, setTema] = useState("claro");
  const value = useMemo(() => ({ tema, setTema }), [tema]);
  return <TemaCtx.Provider value={value}>{children}</TemaCtx.Provider>;
}

export function useTema() {
  const ctx = useContext(TemaCtx);
  if (!ctx) throw new Error("useTema fora do provider");
  return ctx;
}
```

### `useReducer`

Bom quando o próximo estado depende de **ações nomeadas** (`SET_USER`, `LOGOUT`).

### Exercícios

1. Crie `ThemeProvider` com `tema` `"claro" | "escuro"` e altere uma classe no `<body>`.
2. Crie `AuthProvider` que guarda `{ user, token, login, logout }` em memória (depois ligue ao `localStorage` na Aula 15).

### Desafio

Migre um estado complexo de formulário multi-etapas para `useReducer`.
