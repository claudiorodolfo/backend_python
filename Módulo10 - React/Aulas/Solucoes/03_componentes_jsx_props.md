# Soluções — Aula 03

## Exercício 1 — `Button`

```jsx
export default function Button({ label, onClick }) {
  return (
    <button type="button" onClick={onClick}>
      {label}
    </button>
  );
}
```

## Exercício 2 — `Card`

```jsx
export default function Card({ title, children }) {
  return (
    <section className="card">
      <h2>{title}</h2>
      {children}
    </section>
  );
}
```

Uso:

```jsx
<Card title="Resumo">
  <p>Texto interno.</p>
</Card>
```

## Desafio — `PessoaRow`

```jsx
export default function PessoaRow({ pessoa }) {
  return (
    <div>
      <strong>{pessoa.nome}</strong>
      <span> — {pessoa.email}</span>
    </div>
  );
}
```
