# Soluções — Aula 11

## Exercício 1 — Alternar tema

`ThemeToggle.jsx`:

```jsx
import { useState } from "react";

export default function ThemeToggle() {
  const [tema, setTema] = useState("claro");
  return (
    <button type="button" onClick={() => setTema((t) => (t === "claro" ? "escuro" : "claro"))}>
      Tema: {tema}
    </button>
  );
}
```

`ThemeToggle.test.jsx`:

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect } from "vitest";
import ThemeToggle from "./ThemeToggle.jsx";

describe("ThemeToggle", () => {
  it("alterna entre claro e escuro", async () => {
    const user = userEvent.setup();
    render(<ThemeToggle />);
    const btn = screen.getByRole("button", { name: /tema:/i });
    expect(btn).toHaveTextContent("claro");
    await user.click(btn);
    expect(btn).toHaveTextContent("escuro");
  });
});
```

## Exercício 2 — Mock `fetch` e lista de pessoas

```jsx
import { render, screen, waitFor } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import PessoasPage from "./PessoasPage.jsx";

describe("PessoasPage", () => {
  beforeEach(() => {
    vi.stubGlobal(
      "fetch",
      vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () =>
            Promise.resolve([
              { id: 1, nome: "Ana", email: "a@a.com" },
            ]),
        })
      )
    );
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("lista nomes", async () => {
    render(<PessoasPage />);
    await waitFor(() => {
      expect(screen.getByText("Ana")).toBeInTheDocument();
    });
  });
});
```

(`PessoasPage` deve chamar `fetch` no `useEffect` e renderizar os nomes.)

## Exercício 3 — Erro quando `!res.ok`

```jsx
it("mostra erro quando fetch falha", async () => {
  vi.stubGlobal(
    "fetch",
    vi.fn(() =>
      Promise.resolve({
        ok: false,
        status: 500,
        text: () => Promise.resolve("falha"),
      })
    )
  );
  render(<PessoasPage />);
  await waitFor(() => {
    expect(screen.getByRole("alert")).toBeInTheDocument();
  });
});
```

## Desafio — Ordem de queries

Prefira nesta ordem ao escrever testes:

1. `getByRole` (ex.: `getByRole("button", { name: /salvar/i })`)
2. `getByLabelText` para inputs com `<label>`
3. `getByText` para mensagens visíveis

Evite `getByTestId` salvo em casos difíceis de acessibilidade.
