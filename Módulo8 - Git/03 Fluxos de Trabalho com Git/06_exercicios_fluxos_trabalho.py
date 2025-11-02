"""
Exercícios Práticos - Fluxos de Trabalho com Git

Estes exercícios práticos devem ser realizados no terminal usando comandos Git.
Cada exercício tem instruções específicas. Siga os passos e execute os comandos Git necessários.

IMPORTANTE: 
- Execute estes exercícios em diretórios de prática separados
- Alguns exercícios requerem planejamento e estruturação antes de começar
- Foque em criar histórico limpo e commits bem estruturados
"""

# ============================================================================
# EXERCÍCIO 1: Fluxo Básico Completo (Feature Branch)
# ============================================================================

"""
Objetivo: Praticar fluxo básico do início ao fim.

Tarefas:
1. Criar repositório: 'exercicio-fluxo-basico'
2. Fazer commit inicial na main
3. Criar branch feature/calculadora
4. Desenvolver calculadora completa com commits atômicos:
   - commit 1: "feat: Cria classe Calculadora base"
   - commit 2: "feat: Implementa função de soma"
   - commit 3: "feat: Implementa função de subtração"
   - commit 4: "feat: Implementa função de multiplicação"
   - commit 5: "feat: Implementa função de divisão"
   - commit 6: "test: Adiciona testes para todas operações"
   - commit 7: "docs: Documenta classe Calculadora"
5. Push da branch
6. Simular PR (fazer merge na main)
7. Verificar histórico limpo
8. Deletar branch

Comandos úteis:
- git switch -c feature/calculadora
- git commit -m "tipo: mensagem"
- git push -u origin feature/calculadora
- git log --oneline --graph
"""

# ============================================================================
# EXERCÍCIO 2: Git Flow - Feature Development
# ============================================================================

"""
Objetivo: Praticar Git Flow com branch develop.

Tarefas:
1. Criar repositório com estrutura Git Flow:
   - Branch main (produção)
   - Branch develop (desenvolvimento)
2. Criar feature feature/sistema-usuarios a partir de develop
3. Desenvolver com commits atômicos:
   - Modelo User
   - CRUD de usuários
   - Validações
   - Testes
4. Fazer merge na develop (--no-ff)
5. Verificar histórico mantém referência à feature
6. Criar outra feature a partir de develop atualizada
7. Repetir processo

Comandos úteis:
- git switch -c develop
- git switch -c feature/nome develop
- git merge --no-ff feature/nome
"""

# ============================================================================
# EXERCÍCIO 3: Git Flow - Release
# ============================================================================

"""
Objetivo: Praticar processo de release no Git Flow.

Tarefas:
1. Continuando do exercício anterior (ou criar novo)
2. Ter develop com várias features mergeadas
3. Criar branch release/v1.0.0 a partir de develop
4. Na release:
   - Atualizar número de versão no código
   - Criar/atualizar CHANGELOG.md
   - commit: "chore: Prepara release v1.0.0"
5. Fazer merge na main com tag:
   - git merge --no-ff release/v1.0.0
   - git tag -a v1.0.0 -m "Release version 1.0.0"
6. Merge de volta para develop
7. Deletar branch de release
8. Verificar tags: git tag

Comandos úteis:
- git tag -a v1.0.0 -m "mensagem"
- git push origin --tags
- git tag (listar tags)
"""

# ============================================================================
# EXERCÍCIO 4: Git Flow - Hotfix
# ============================================================================

"""
Objetivo: Praticar correção urgente (hotfix).

Tarefas:
1. Criar situação: main tem bug crítico
2. Criar hotfix a partir de main:
   git switch main
   git switch -c hotfix/corrigir-bug-critico
3. Corrigir bug:
   commit: "fix: Corrige bug crítico de segurança"
4. Merge para main com tag:
   git switch main
   git merge --no-ff hotfix/corrigir-bug-critico
   git tag -a v1.0.1 -m "Hotfix version 1.0.1"
5. IMPORTANTE: Merge também para develop!
   git switch develop
   git merge --no-ff hotfix/corrigir-bug-critico
6. Deletar branch hotfix
7. Verificar que bug está corrigido em ambas as branches

Comandos úteis:
- git switch -c hotfix/nome main
- Lembre-se: hotfix vai para main E develop!
"""

# ============================================================================
# EXERCÍCIO 5: Resolução Avançada de Conflitos
# ============================================================================

"""
Objetivo: Praticar resolução de conflitos complexos.

Tarefas:
1. Criar repositório com arquivo config.py complexo
2. Branch main: modificar várias seções
3. Branch feature: modificar outras seções do mesmo arquivo
4. Tentar merge: haverá múltiplos conflitos
5. Resolver estratégias diferentes:
   - Alguns: manter versão da main
   - Alguns: manter versão da feature
   - Alguns: combinar ambas
6. Finalizar merge
7. Verificar que resultado está correto
8. Testar funcionalidade

Comandos úteis:
- git merge feature/nome
- Editar arquivo manualmente
- git mergetool (ferramenta visual)
"""

# ============================================================================
# EXERCÍCIO 6: Commits Claros e Histórico Limpo
# ============================================================================

"""
Objetivo: Praticar criar commits bem estruturados.

Tarefas:
Criar projeto seguindo Conventional Commits:

1. feat: Implementa sistema de autenticação
   - Corpo: Detalhes da implementação
   - Rodapé: Relates to #1

2. test: Adiciona testes para autenticação
   - Corpo: Lista de casos de teste cobertos

3. docs: Documenta API de autenticação
   - Corpo: Instruções de uso

4. fix(auth): Corrige validação de token
   - Corpo: Explicação do bug e solução
   - Rodapé: Fixes #2

5. refactor(auth): Reorganiza estrutura de módulos
   - Corpo: Motivação e mudanças

6. Ver histórico: git log --oneline
7. Verificar que cada commit é claro e descritivo

Comandos úteis:
- git commit -m "tipo: assunto" -m "corpo"
- git log --format=fuller
"""

# ============================================================================
# EXERCÍCIO 7: Rebase Interativo para Limpar Histórico
# ============================================================================

"""
Objetivo: Praticar rebase interativo para histórico limpo.

Tarefas:
1. Criar branch com vários commits "sujos":
   - "wip"
   - "fix"
   - "teste"
   - "mais mudanças"
2. Usar rebase interativo para limpar:
   git rebase -i HEAD~4
3. Ações:
   - reword: Reescrever mensagens vagas
   - squash: Combinar commits relacionados
   - fixup: Combinar descartando mensagem
   - drop: Remover commits desnecessários
4. Verificar histórico final limpo
5. Comparar com histórico original

Comandos úteis:
- git rebase -i HEAD~n
- pick, reword, edit, squash, fixup, drop
"""

# ============================================================================
# EXERCÍCIO 8: Planejamento com Brainstorming
# ============================================================================

"""
Objetivo: Praticar planejamento antes de codificar.

Tarefas:
1. Escolher projeto (ex: Sistema de Biblioteca)
2. Fazer brainstorming:
   - Listar todas as features necessárias
   - Identificar dependências
   - Priorizar features
3. Criar mind map (texto ou desenho):
   - Estrutura do projeto
   - Relações entre features
4. Planejar branches:
   - Quais branches criar
   - Ordem de desenvolvimento
   - Commits planejados
5. Documentar plano em MARKDOWN.md
6. Seguir plano ao desenvolver (exercício seguinte)

Este exercício é teórico mas essencial!
"""

# ============================================================================
# EXERCÍCIO 9: Projeto Completo com Planejamento
# ============================================================================

"""
Objetivo: Aplicar todo aprendizado em projeto completo.

Tarefas:
Projeto: Sistema de Gerenciamento de Tarefas

FASE 1: Planejamento
1. Brainstorm: Listar todas features
2. Mind map: Estruturar projeto
3. Planejar branches e ordem

FASE 2: Desenvolvimento (Git Flow)
1. Setup: main e develop
2. Feature 1: feature/auth (autenticação)
   - Commits atômicos e claros
3. Feature 2: feature/tasks-model (modelo de tarefa)
4. Feature 3: feature/tasks-crud (CRUD)
5. Feature 4: feature/tasks-api (API endpoints)

FASE 3: Release
1. Criar release/v1.0.0
2. Preparar documentação
3. Tag e merge

FASE 4: Manutenção
1. Criar hotfix se necessário
2. Continuar desenvolvimento em develop

Este exercício integra TODOS os conceitos!
"""

# ============================================================================
# EXERCÍCIO 10: Resolução de Conflitos em Rebase
# ============================================================================

"""
Objetivo: Praticar resolução de conflitos durante rebase.

Tarefas:
1. Criar branch feature a partir de commit antigo da main
2. Desenvolver na feature (vários commits)
3. Enquanto isso, main recebe mudanças
4. Tentar rebase da feature na main:
   git rebase main
5. Haverá conflitos (um por commit se necessário)
6. Resolver cada conflito:
   - Editar arquivo
   - git add arquivo.py
   - git rebase --continue
7. Repetir até todos commits rebased
8. Verificar histórico linear limpo

Comandos úteis:
- git rebase main
- git rebase --continue
- git rebase --abort
"""

# ============================================================================
# EXERCÍCIO 11: Múltiplas Features em Paralelo
# ============================================================================

"""
Objetivo: Gerenciar múltiplas features simultaneamente.

Tarefas:
1. Repositório com develop
2. Criar 3 features em paralelo:
   - feature/auth
   - feature/database
   - feature/api
3. Desenvolver cada uma (commits pequenos)
4. Fazer merge de feature/auth na develop
5. Atualizar outras features:
   git switch feature/database
   git rebase develop  # ou merge
6. Continuar desenvolvimento
7. Merge feature/database
8. Repetir para feature/api
9. Ver histórico final: git log --oneline --graph --all

Este exercício simula trabalho em equipe.
"""

# ============================================================================
# EXERCÍCIO 12: Tags e Versionamento
# ============================================================================

"""
Objetivo: Praticar versionamento semântico com tags.

Tarefas:
1. Repositório com histórico de commits
2. Identificar releases baseado em commits:
   - v1.0.0: Primeira release
   - v1.1.0: Novas features
   - v1.1.1: Hotfix
   - v2.0.0: Breaking changes
3. Criar tags anotadas:
   git tag -a v1.0.0 -m "Release version 1.0.0"
4. Listar tags: git tag
5. Ver detalhes: git show v1.0.0
6. Ver histórico entre tags:
   git log v1.0.0..v1.1.0
7. Criar release notes baseado em commits entre tags

Comandos úteis:
- git tag -a v1.0.0 -m "mensagem"
- git tag (listar)
- git show v1.0.0
- git log v1.0..v2.0
"""

# ============================================================================
# EXERCÍCIO 13: Histórico Limpo com Squash
# ============================================================================

"""
Objetivo: Combinar múltiplos commits em um.

Tarefas:
1. Criar branch com muitos commits pequenos:
   - "feat: adiciona função A"
   - "fix: corrige typo em A"
   - "feat: adiciona função B"
   - "fix: corrige bug em B"
   - "test: adiciona teste para A"
   - "test: adiciona teste para B"
2. Usar rebase interativo para combinar:
   - Combinar fixes com commits relacionados
   - Manter estrutura lógica
3. Resultado ideal:
   - "feat: Implementa funcionalidade A com testes"
   - "feat: Implementa funcionalidade B com testes"
4. Verificar histórico mais limpo

Comandos úteis:
- git rebase -i HEAD~n
- squash ou fixup para combinar
"""

# ============================================================================
# EXERCÍCIO 14: Workflow Completo: Desenvolvimento → Release
# ============================================================================

"""
Objetivo: Praticar workflow completo do início ao fim.

Tarefas:
SIMULAR desenvolvimento real de software:

1. SETUP
   - Criar repositório
   - Inicializar Git Flow (main, develop)

2. DESENVOLVIMENTO (várias semanas simuladas)
   - Feature 1: Sistema base
   - Feature 2: Autenticação
   - Feature 3: CRUD principal
   - Hotfix: Bug crítico descoberto

3. RELEASE
   - Preparar v1.0.0
   - Documentação
   - Tag e deploy

4. DESENVOLVIMENTO CONTÍNUO
   - Feature 4: Melhorias
   - Feature 5: Novas funcionalidades
   - Preparar v1.1.0

5. HISTÓRICO FINAL
   - Verificar que está organizado
   - Tags corretas
   - Branches limpas
   - Commits claros

Este exercício consolida TODO o aprendizado!
"""

# ============================================================================
# EXERCÍCIO 15: Colaboração com Git Flow
# ============================================================================

"""
Objetivo: Simular trabalho colaborativo com Git Flow.

Tarefas:
Usar 2 diretórios para simular 2 desenvolvedores:

DESENVOLVEDOR 1:
1. Clonar repositório
2. Criar feature/auth
3. Desenvolver e push

DESENVOLVEDOR 2:
1. Clonar repositório
2. Criar feature/database
3. Desenvolver e push
4. Fazer merge de feature/auth na develop local
5. Atualizar feature/database com develop
6. Continuar desenvolvimento

COORDENADOR (você):
1. Fazer merge de features na develop
2. Criar release
3. Fazer merge na main
4. Criar tags

Este exercício mostra Git Flow em equipe!
"""

# ============================================================================
# DICAS GERAIS
# ============================================================================

"""
1. SEMPRE planeje antes de começar a codificar
   - Brainstorm features
   - Mind map da estrutura
   - Planejar branches

2. Mantenha commits atômicos e descritivos
   - Uma mudança lógica por commit
   - Mensagens claras
   - Seguir Conventional Commits

3. Use Git Flow apropriadamente
   - Fluxo básico para projetos simples
   - Git Flow completo para releases versionadas

4. Mantenha histórico limpo
   - Rebase interativo quando necessário
   - Remover commits de teste/debug
   - Combinar commits relacionados

5. Pratique resolução de conflitos
   - Entenda mudanças de ambas as versões
   - Escolha estratégia apropriada
   - Teste após resolver

6. Documente seu trabalho
   - Commits bem escritos são documentação
   - README atualizado
   - CHANGELOG para releases

7. Colabore efetivamente
   - Atualize branches frequentemente
   - Comunique mudanças grandes
   - Respeite code review
"""

# ============================================================================
# CHECKLIST DE CONCLUSÃO
# ============================================================================

"""
Após completar os exercícios, você deve ser capaz de:

[ ] Executar fluxo básico (feature branch → PR → merge)
[ ] Usar Git Flow completo (develop, feature, release, hotfix)
[ ] Resolver conflitos complexos de forma eficiente
[ ] Criar commits claros seguindo Conventional Commits
[ ] Limpar histórico com rebase interativo
[ ] Planejar estrutura de branches antes de começar
[ ] Criar e gerenciar tags de versão
[ ] Trabalhar colaborativamente com Git Flow
[ ] Manter histórico limpo e organizado
[ ] Aplicar estratégias apropriadas para cada situação

Se conseguiu completar todos, você domina workflows profissionais com Git!
"""
