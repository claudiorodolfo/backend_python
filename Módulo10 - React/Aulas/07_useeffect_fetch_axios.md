## Aula 07 — `useEffect`, `fetch` e Axios

### Objetivos

- Buscar dados ao montar o componente
- Tratar **loading**, **erro** e **dados**
- Comparar `fetch` × `axios` (quando vale a pena cada um)

### `useEffect` com dependências

```jsx
useEffect(() => {
  let alive = true;

  async function load() {
    try {
      setLoading(true);
      const res = await fetch(`${API}/pessoas`);
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      if (alive) setPessoas(data);
    } catch (e) {
      if (alive) setError(String(e.message ?? e));
    } finally {
      if (alive) setLoading(false);
    }
  }

  load();
  return () => {
    alive = false;
  };
}, []);
```

### Por que o “cleanup” (`alive`)?

Se o usuário sair da tela rápido, evita atualizar state em componente desmontado.

### Axios

- Interceptors (ex.: anexar `Authorization`)
- Erros padronizados (`error.response?.status`)

Instalação: `npm i axios`

### Exercícios

1. Crie `getPessoas()` em `src/api/pessoas.js` e use no `useEffect`.
2. Ao falhar, mostre um botão “Tentar novamente”.
3. (Opcional) Reescreva com `axios.get`.

### Desafio

Implemente busca por `id` com rota `/pessoas/:id` (preparação para React Router).
