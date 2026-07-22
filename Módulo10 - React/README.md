## Módulo10 - React (Básico ao Avançado) + FastAPI

Curso completo de React, do básico ao avançado, **integrado com back-end em FastAPI (Python)**.

### Pré-requisitos

- **Node.js LTS** (recomendado 20+)
- **Python 3.11+**
- Git

### Como usar este módulo

- **Aulas** ficam em `Aulas/` (cada aula tem objetivos, conteúdo e exercícios).
- **Exercícios** ficam em `Exercicios/` (listas incrementais + desafios).
- **Projetos** ficam em `Projetos/` (guias e código base).

### Trilhas

#### Trilha A — Fundamentos (React do zero)

1. `Aulas/00_ambiente_e_ferramentas.md`
2. `Aulas/01_fundamentos_web_e_js_moderno.md`
3. `Aulas/02_react_o_que_e_e_como_pensar.md`
4. `Aulas/03_componentes_jsx_props.md`
5. `Aulas/04_state_eventos_renderizacao.md`
6. `Aulas/05_listas_chaves_condicionais.md`
7. `Aulas/06_forms_controlados_validacao.md`

#### Trilha B — SPA e Integração com API

8. `Aulas/07_useeffect_fetch_axios.md`
9. `Aulas/08_react_router_spa.md`
10. `Aulas/09_context_e_reducers.md`
11. `Aulas/10_camada_api_e_tratamento_erros.md`

#### Trilha C — Qualidade, Performance e Arquitetura

12. `Aulas/11_testes_com_vitest_rtl.md`
13. `Aulas/12_performance_memo_suspense.md`
14. `Aulas/13_padrao_projeto_pastas.md`
15. `Aulas/14_typescript_no_react.md` (opcional, mas recomendado)

#### Trilha D — Avançado (Auth, cache, realtime e deploy)

16. `Aulas/15_auth_jwt_refresh_tokens.md`
17. `Aulas/16_react_query_cache_sync.md`
18. `Aulas/17_websockets_sse.md` (opcional)
19. `Aulas/18_deploy_frontend_backend.md`

### Projetos

- **Projeto1 (Frontend React consumindo API pronta)**: `Projetos/Projeto1-React-Pessoas/`
- **Projeto2 (Fullstack React + FastAPI)**: `Projetos/Projeto2-Fullstack-Pessoas-Auth/`

### Relação com o Módulo9 (FastAPI)

Você já tem um exemplo de arquitetura FastAPI em `Módulo9 - FastAPI/Projetos/Projeto1/` com:

- `routers/` (rotas)
- `services/` (regras de negócio)
- `repositories/` (persistência)
- `schemas/` (Pydantic)

Neste módulo vamos reutilizar esse padrão para o back-end do Projeto2.

