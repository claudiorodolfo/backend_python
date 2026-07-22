# Soluções — Aula 05

## Exercícios 1–3 + Desafio — `PessoaList` e `PessoaItem`

`PessoaItem.jsx`:

```jsx
export default function PessoaItem({ pessoa, onDelete }) {
  return (
    <li>
      {pessoa.nome} — {pessoa.email}{" "}
      <button type="button" onClick={() => onDelete(pessoa.id)}>
        Remover
      </button>
    </li>
  );
}
```

`PessoaList.jsx`:

```jsx
import PessoaItem from "./PessoaItem.jsx";

export default function PessoaList({ pessoas, onDelete }) {
  if (pessoas.length === 0) {
    return <p>Nenhuma pessoa cadastrada</p>;
  }

  return (
    <ul>
      {pessoas.map((p) => (
        <PessoaItem key={p.id} pessoa={p} onDelete={onDelete} />
      ))}
    </ul>
  );
}
```

Pai (exemplo de estado e callback):

```jsx
import { useState } from "react";
import PessoaList from "./PessoaList.jsx";

export default function App() {
  const [pessoas, setPessoas] = useState([
    { id: 1, nome: "Ana", email: "ana@email.com" },
    { id: 2, nome: "Bruno", email: "bruno@email.com" },
  ]);

  function remover(id) {
    setPessoas((lista) => lista.filter((p) => p.id !== id));
  }

  return <PessoaList pessoas={pessoas} onDelete={remover} />;
}
```
