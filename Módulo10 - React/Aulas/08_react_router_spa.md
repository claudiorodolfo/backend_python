## Aula 08 — React Router (SPA)

### Objetivos

- Separar telas sem recarregar a página
- Usar rotas dinâmicas (`/pessoas/:id`)
- Navegar com `<Link>` e `useNavigate`

### Instalação

```bash
npm i react-router-dom
```

### Esqueleto

```jsx
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

export function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/pessoas">Pessoas</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pessoas" element={<PessoasPage />} />
        <Route path="/pessoas/:id" element={<PessoaDetalhe />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### Parâmetros

```jsx
import { useParams } from "react-router-dom";

const { id } = useParams();
```

### Exercícios

1. Crie rotas: `/`, `/pessoas`, `/pessoas/:id`.
2. Na lista, cada nome deve ser um `Link` para o detalhe.
3. Na página 404 simples, use `path="*"` com um componente `NotFound`.

### Desafio

Proteja rota (redireciona para `/login` se não houver token) — base para a Aula 15.
