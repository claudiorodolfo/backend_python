## Aula 14 — TypeScript no React (opcional, recomendado)

### Objetivos

- Tipar props e estado
- Tipar respostas de API com interfaces
- Integrar Vite + React TS

### Criar projeto

```bash
npm create vite@latest meu-app -- --template react-ts
```

### Tipando props

```tsx
type Pessoa = { id: number; nome: string; email: string };

export function PessoaRow({ pessoa }: { pessoa: Pessoa }) {
  return (
    <div>
      {pessoa.nome} — {pessoa.email}
    </div>
  );
}
```

### Tipando eventos

```tsx
function onChange(e: React.ChangeEvent<HTMLInputElement>) {
  setNome(e.target.value);
}
```

### Tipos do FastAPI

Gere tipos a partir do OpenAPI (avançado) ou mantenha interfaces manuais espelhando `schemas` Pydantic.

### Exercícios

1. Converta `Projeto1` para TS (`.tsx`) incrementalmente: comece por `api/` e props.
2. Crie tipo `PessoaCreate = Pick<Pessoa, "nome" | "email">`.
3. Use `satisfies` (TS 4.9+) para validar objetos constantes de rotas.

### Desafio

Experimente `zod` para validar JSON da API em runtime (útil quando o backend ainda muda).
