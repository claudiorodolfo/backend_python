## Aula 11 — Testes com Vitest e React Testing Library

### Objetivos

- Configurar Vitest no Vite
- Testar comportamento do usuário (não detalhe de implementação)
- Mock de `fetch` para isolar a UI do backend

### Instalação (projeto Vite)

```bash
npm i -D vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event jsdom
```

No `vite.config.js`, adicione:

```js
/// <reference types="vitest" />
export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    setupFiles: "./src/setupTests.js",
  },
});
```

`src/setupTests.js`:

```js
import "@testing-library/jest-dom/vitest";
```

Script no `package.json`:

```json
"test": "vitest"
```

### Exemplo

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi } from "vitest";

describe("Counter", () => {
  it("incrementa", async () => {
    const user = userEvent.setup();
    render(<Counter />);
    await user.click(screen.getByRole("button", { name: /\+1/i }));
    expect(screen.getByText("1")).toBeInTheDocument();
  });
});
```

### Exercícios

1. Teste um botão que alterna tema.
2. Mock `global.fetch` e teste uma tela que lista pessoas.
3. Teste estado de erro quando `fetch` retorna `!res.ok`.

### Desafio

Adote **Testing Library queries** na ordem recomendada: `getByRole` → `getByLabelText` → `getByText`.
