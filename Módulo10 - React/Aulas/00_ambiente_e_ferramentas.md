## Aula 00 — Ambiente e Ferramentas (Node, Vite, VSCode, Git)

### Objetivos

- Instalar e validar Node e Python
- Criar um projeto React com Vite
- Entender scripts comuns (`dev`, `build`, `preview`, `test`, `lint`)
- Padronizar formatação e organização

### Checklist rápido

- **Node**:
  - `node -v` (recomendado 20+)
  - `npm -v`
- **Python**:
  - `python3 --version` (recomendado 3.11+)
- **Git**:
  - `git --version`

### Criando um projeto React com Vite

No diretório do projeto (fora de `node_modules` etc.):

```bash
npm create vite@latest meu-app -- --template react
cd meu-app
npm install
npm run dev
```

> Se você for usar TypeScript desde o início:
>
> ```bash
> npm create vite@latest meu-app -- --template react-ts
> ```

### Estrutura mínima recomendada (frontend)

- `src/`
  - `app/` (composição do app: rotas/layout/providers)
  - `features/` (domínios: pessoas, auth, etc.)
  - `shared/` (componentes e utilitários reutilizáveis)
  - `services/` (API client, storage, etc.)

### Padrões (práticos)

- **Componentes**: PascalCase (`PessoaForm.tsx`)
- **Hooks**: prefixo `use` (`usePessoas.ts`)
- **Arquivos**: kebab-case ou camelCase, mas seja consistente

### Exercícios

1. Crie um app Vite React e troque o conteúdo padrão por:
   - Um título “Módulo10 - React”
   - Um componente `Hello` que recebe `name` via props
2. Adicione um script `dev` e rode localmente

### Desafio

Crie um `README.md` no seu app React com:

- Como rodar (`npm i`, `npm run dev`)
- Como buildar (`npm run build`)

