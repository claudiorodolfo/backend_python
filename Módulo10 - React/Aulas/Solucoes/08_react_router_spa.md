# Soluções — Aula 08

## Exercícios 1–3 — Rotas e 404

`App.jsx` (esqueleto completo):

```jsx
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home.jsx";
import PessoasPage from "./pages/PessoasPage.jsx";
import PessoaDetalhe from "./pages/PessoaDetalhe.jsx";
import NotFound from "./pages/NotFound.jsx";

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/pessoas">Pessoas</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pessoas" element={<PessoasPage />} />
        <Route path="/pessoas/:id" element={<PessoaDetalhe />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

`PessoasPage.jsx` — cada nome como `Link`:

```jsx
import { Link } from "react-router-dom";

export default function PessoasPage({ pessoas /* ou fetch interno */ }) {
  const lista = pessoas ?? [];
  return (
    <ul>
      {lista.map((p) => (
        <li key={p.id}>
          <Link to={`/pessoas/${p.id}`}>{p.nome}</Link>
        </li>
      ))}
    </ul>
  );
}
```

`NotFound.jsx`:

```jsx
import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <div>
      <h1>404</h1>
      <p>Página não encontrada.</p>
      <Link to="/">Voltar ao início</Link>
    </div>
  );
}
```

## Desafio — Rota protegida (base Aula 15)

```jsx
import { Navigate } from "react-router-dom";

function readToken() {
  return localStorage.getItem("token");
}

export default function RequireAuth({ children }) {
  if (!readToken()) {
    return <Navigate to="/login" replace />;
  }
  return children;
}
```

Uso:

```jsx
<Route
  path="/pessoas"
  element={
    <RequireAuth>
      <PessoasPage />
    </RequireAuth>
  }
/>
```

Na Aula 15, substitua `readToken()` por `useAuth().token`.
