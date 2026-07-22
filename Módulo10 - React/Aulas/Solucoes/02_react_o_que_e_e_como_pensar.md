# Soluções — Aula 02

## Exercício 1 e 2 — Layout com `appName` no `Header`

`src/App.jsx`:

```jsx
import Header from "./Header.jsx";
import Main from "./Main.jsx";
import Footer from "./Footer.jsx";

export default function App() {
  return (
    <>
      <Header appName="Módulo10 - React" />
      <Main />
      <Footer />
    </>
  );
}
```

`src/Header.jsx`:

```jsx
export default function Header({ appName }) {
  return <header><h1>{appName}</h1></header>;
}
```

`src/Main.jsx`:

```jsx
export default function Main() {
  return <main><p>Conteúdo principal.</p></main>;
}
```

`src/Footer.jsx`:

```jsx
export default function Footer() {
  return <footer><small>Rodapé</small></footer>;
}
```

## Desafio — `Counter`

```jsx
import { useState } from "react";

export default function Counter() {
  const [n, setN] = useState(0);

  return (
    <div>
      <p>Valor: {n}</p>
      <button type="button" onClick={() => setN((c) => c + 1)}>+1</button>
      <button type="button" onClick={() => setN((c) => c - 1)}>-1</button>
    </div>
  );
}
```
