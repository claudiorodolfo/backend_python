# Soluções — Aula 00

## Exercício 1 — App com título e `Hello`

Após `npm create vite@latest` e `npm install`, ajuste `src/App.jsx`:

```jsx
import Hello from "./Hello.jsx";

export default function App() {
  return (
    <>
      <h1>Módulo10 - React</h1>
      <Hello name="Aluno" />
    </>
  );
}
```

`src/Hello.jsx`:

```jsx
export default function Hello({ name }) {
  return <p>Olá, {name}!</p>;
}
```

## Exercício 2 — Script `dev`

O template Vite já inclui em `package.json`:

```json
"scripts": {
  "dev": "vite"
}
```

Rodar: `npm run dev`.

## Desafio — README do app

Exemplo mínimo para colar em `README.md`:

- Título do projeto.
- Seção **Rodar em desenvolvimento**: `npm install` e `npm run dev`.
- Seção **Build**: `npm run build` (saída em `dist/`) e, se quiser, `npm run preview` para testar o build localmente.
