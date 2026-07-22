# Soluções — Aula 13

## Exercício 1 — Mover lista/form para `features/pessoas/`

Estrutura alvo (exemplo):

```text
src/
  app/
    App.jsx
    routes.jsx
  features/
    pessoas/
      components/
        PessoaForm.jsx
        PessoaList.jsx
      api/
        pessoasApi.js
      pages/
        PessoasPage.jsx
  shared/
    ui/
    lib/
```

Atualize imports relativos (ou configure alias `@/` no Vite se desejar).

## Exercício 2 — `shared/ui/Button.jsx`

```jsx
export default function Button({ children, variant = "primary", ...props }) {
  return (
    <button type="button" className={`btn btn-${variant}`} {...props}>
      {children}
    </button>
  );
}
```

Substitua `<button>` repetidos por `<Button variant="secondary">...</Button>`.

## Exercício 3 — `ARCHITECTURE.md` (uma página)

Conteúdo sugerido:

- **Objetivo:** regras de dependência entre pastas.
- **`app/`:** shell, providers, definição de rotas; pode importar `features` e `shared`.
- **`features/<domínio>/`:** telas, hooks e API do domínio; pode importar `shared` e o próprio feature; **não** importar outro `features/xyz`.
- **`shared/`:** UI genérica e helpers sem regra de negócio; **não** importar `features`.
- **Exceções:** tipos compartilhados podem ir em `shared/types` se forem realmente transversais.

## Desafio — Barrel `index.js`

Use barrel só quando exportar poucos símbolos públicos de um módulo, por exemplo:

`features/pessoas/index.js`:

```js
export { PessoaForm } from "./components/PessoaForm.jsx";
export { PessoaList } from "./components/PessoaList.jsx";
```

Evite barris que reexportam árvores grandes (`export * from "./components"`) — prejudica tree-shaking e rastreio de dependências.
