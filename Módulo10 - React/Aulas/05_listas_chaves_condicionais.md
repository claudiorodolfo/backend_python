## Aula 05 — Listas, keys e renderização condicional

### Objetivos

- Renderizar listas com `.map()`
- Entender **por que o React exige `key`** estável
- Usar `&&`, ternário e early return para UI condicional

### Listas e `key`

- Cada item da lista deve ter uma **key única** entre irmãos (ideal: `id` do backend).
- Evite usar **índice do array** como key se a lista pode reordenar/remover itens.

```jsx
{pessoas.map((p) => (
  <li key={p.id}>
    {p.nome} — {p.email}
  </li>
))}
```

### Renderização condicional

- **Ternário** quando há dois ramos claros.
- **`&&`** quando o “falso” é não renderizar nada.
- **Early return** no componente quando não há dados mínimos.

```jsx
if (loading) return <p>Carregando…</p>;
if (error) return <p>Erro: {error}</p>;
```

### Exercícios

1. Receba uma lista `pessoas` via props e renderize uma `<ul>`.
2. Se `pessoas.length === 0`, mostre “Nenhuma pessoa cadastrada”.
3. Adicione um botão “Remover” que chama `onDelete(id)` passado por props (sem implementar API ainda).

### Desafio

Extraia um componente `PessoaList` e outro `PessoaItem` (cada item com sua própria key).
