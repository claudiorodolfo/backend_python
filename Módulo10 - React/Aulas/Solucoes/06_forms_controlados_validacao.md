# Soluções — Aula 06

Alinhe `API` ao seu projeto (ex.: `import.meta.env.VITE_API_URL` ou proxy `/api` como no Projeto1).

## Exercícios 1–3 — Criação com validação e `isSubmitting`

```jsx
import { useState } from "react";

const API = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export default function PessoaCreateForm({ onSuccess }) {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [erro, setErro] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function onSubmit(e) {
    e.preventDefault();
    setErro("");

    if (!email.includes("@")) {
      setErro("E-mail deve conter @.");
      return;
    }

    setIsSubmitting(true);
    try {
      const res = await fetch(`${API}/pessoas`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, email }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(
          typeof body.detail === "string"
            ? body.detail
            : JSON.stringify(body.detail ?? res.statusText)
        );
      }
      setNome("");
      setEmail("");
      onSuccess?.();
    } catch (err) {
      setErro(String(err.message ?? err));
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label>
          Nome{" "}
          <input value={nome} onChange={(e) => setNome(e.target.value)} required />
        </label>
      </div>
      <div>
        <label>
          E-mail{" "}
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
      </div>
      {erro ? <p role="alert">{erro}</p> : null}
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Salvando…" : "Salvar"}
      </button>
    </form>
  );
}
```

## Desafio — Edição com `PUT /pessoas/{id}`

Ideia: quando `pessoa` existir, use `PUT`; senão, `POST`. Exemplo enxuto:

```jsx
async function salvar(pessoa, payload) {
  const url = pessoa
    ? `${API}/pessoas/${pessoa.id}`
    : `${API}/pessoas`;
  const method = pessoa ? "PUT" : "POST";
  const res = await fetch(url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(
      typeof body.detail === "string" ? body.detail : "Falha ao salvar"
    );
  }
  return res.json();
}
```

No Projeto1, `PessoaForm.jsx` já cobre esse fluxo com `apiFetch` e prop `editing`.
