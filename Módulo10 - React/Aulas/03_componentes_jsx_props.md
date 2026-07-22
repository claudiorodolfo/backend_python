## Aula 03 — Componentes, JSX e Props

### Objetivos

- Entender JSX (sintaxe, expressões, `className`)
- Criar componentes reutilizáveis
- Tipos de props (strings, números, callbacks)

### JSX: regras rápidas

- `className` no lugar de `class`
- Expressões JS dentro de `{ }`
- Eventos são `onClick`, `onChange`, etc.

### Props

Props são a **forma padrão de parametrizar** componentes.

Exemplos:

- `title="..."` (string)
- `count={10}` (number)
- `onSave={(payload) => ...}` (callback)

### Padrões úteis

- **Composição** com `children`
- **Callbacks** para “subir evento”

### Exercícios

1. Crie um componente `Button` que recebe:
   - `label`
   - `onClick`
2. Crie um componente `Card` que recebe:
   - `title`
   - `children`

### Desafio

Crie um componente `PessoaRow` que recebe `pessoa` e exibe:

- nome
- email

