## Aula 13 — Padrão de pastas e limites de módulo

### Objetivos

- Organizar código para crescer sem virar “pasta única gigante”
- Separar **feature** × **shared** × **app**
- Manter o acoplamento baixo entre domínios

### Estrutura sugerida (SPA média)

- `src/app/` — `AppProviders`, rotas, layout global
- `src/features/pessoas/` — telas, hooks e serviços do domínio “pessoas”
- `src/shared/ui/` — botões, inputs, modal
- `src/shared/lib/` — helpers puros

### Regras práticas

- Imports “para dentro” do feature são livres; **evite** importar um feature de outro diretamente.
- API types/contratos podem ficar em `features/pessoas/api.js` ou `types.ts`.

### Exercícios

1. Reorganize `Projeto1` movendo lista/form para `features/pessoas/`.
2. Crie `shared/ui/Button.jsx` e substitua botões repetidos.
3. Documente no arquivo `ARCHITECTURE.md` (uma página) os limites entre pastas.

### Desafio

Defina um “barrel export” opcional (`index.js`) só onde realmente reduz ruído — evite barrels que pioram tree-shaking sem necessidade.
