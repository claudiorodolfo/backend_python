# Ficha de exercícios por aula

> Cada bloco pode ser feito em um app Vite novo ou no `Projeto1`, conforme a aula.

## 00 — Ambiente

- [ ] Criar app com Vite React e substituir a home por um layout simples (header/main/footer).
- [ ] Documentar no README do app: instalar, dev, build.

## 01 — Fundamentos web

- [ ] Implementar `getJson(url)` com validação `res.ok`.
- [ ] Escrever o contrato JSON de `Pessoa` alinhado ao FastAPI (`id`, `nome`, `email`).

## 02 — Mental modelo React

- [ ] Componente `Counter` com +1 e -1.

## 03 — JSX e props

- [ ] `Button` reutilizável (`label`, `onClick`).
- [ ] `Card` com `title` + `children`.

## 04 — Estado

- [ ] Form “nome” + exibir valor salvo após submit.
- [ ] Lista de tarefas em memória com filtro por texto.

## 05 — Listas

- [ ] Renderizar `pessoas` com `key={id}`.
- [ ] Empty state quando lista vazia.

## 06 — Forms + API

- [ ] POST `/pessoas` com JSON; tratar 422 exibindo `detail`.
- [ ] Estado `isSubmitting` desabilitando botão.

## 07 — `useEffect`

- [ ] Carregar lista no mount com cleanup (`alive`).
- [ ] Botão “Tentar novamente” após erro.

## 08 — Router

- [ ] Rotas `/`, `/pessoas`, `/pessoas/:id`.
- [ ] Rota `*` para 404.

## 09 — Context

- [ ] `ThemeProvider` claro/escuro.
- [ ] `AuthProvider` com `login`/`logout` (mock).

## 10 — Camada API

- [ ] Centralizar `apiFetch`; implementar `pessoasApi.*`.
- [ ] `AbortController` ao desmontar (desafio).

## 11 — Testes

- [ ] Configurar Vitest + RTL.
- [ ] Teste de botão + mock de `fetch`.

## 12 — Performance

- [ ] Profiling com React DevTools.
- [ ] `React.memo` em linha de lista.

## 13 — Pastas

- [ ] Mover domínio “pessoas” para `features/pessoas/`.

## 14 — TypeScript

- [ ] Tipar `Pessoa` e props dos componentes principais.

## 15 — Auth

- [ ] Login persistindo token; header `Authorization`.
- [ ] Rota protegida + redirect para `/login`.

## 16 — React Query

- [ ] `useQuery` para lista; `useMutation` para create com invalidação.

## 17 — Realtime (opcional)

- [ ] Eco WebSocket no FastAPI + cliente mínimo no React.

## 18 — Deploy

- [ ] `npm run build` + checklist de CORS/HTTPS/variáveis.
