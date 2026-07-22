# Soluções — Aula 04

## Exercício 1 — Form nome + Salvar

```jsx
import { useState } from "react";

export default function NomeForm() {
  const [nome, setNome] = useState("");
  const [salvo, setSalvo] = useState("");

  function salvar() {
    setSalvo(nome);
  }

  return (
    <div>
      <label>
        Nome{" "}
        <input value={nome} onChange={(e) => setNome(e.target.value)} />
      </label>
      <button type="button" onClick={salvar}>
        Salvar
      </button>
      {salvo ? <p>Nome salvo: {salvo}</p> : null}
    </div>
  );
}
```

## Exercício 2 — Lista de tarefas em memória

```jsx
import { useState } from "react";

export default function TodoList() {
  const [texto, setTexto] = useState("");
  const [itens, setItens] = useState([]);

  function adicionar() {
    const t = texto.trim();
    if (!t) return;
    setItens((lista) => [...lista, t]);
    setTexto("");
  }

  return (
    <div>
      <input value={texto} onChange={(e) => setTexto(e.target.value)} />
      <button type="button" onClick={adicionar}>
        Adicionar
      </button>
      <ul>
        {itens.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

> Para listas que reordenam/removam, prefira `key` estável (id) em vez do índice.

## Desafio — Filtro por `query`

```jsx
import { useState } from "react";

const INICIAL = ["react", "vite", "fastapi", "javascript"];

export default function FiltroLista() {
  const [query, setQuery] = useState("");

  const filtrados = INICIAL.filter((s) =>
    s.toLowerCase().includes(query.trim().toLowerCase())
  );

  return (
    <div>
      <input
        placeholder="Filtrar…"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul>
        {filtrados.map((s) => (
          <li key={s}>{s}</li>
        ))}
      </ul>
    </div>
  );
}
```
