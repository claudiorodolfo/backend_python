# Git Flow: Desenvolvimento com Múltiplos Branches

## O que é Git Flow?

**Git Flow** é uma estratégia de branching desenvolvida por Vincent Driessen. É mais estruturada que o fluxo básico e é ideal para projetos com:
- Releases versionadas (v1.0, v1.1, v2.0, etc.)
- Múltiplas versões em produção
- Processo de desenvolvimento e release separados
- Necessidade de hotfixes em produção

## Estrutura de Branches

```
main/master (produção)
  │
  ├── develop (desenvolvimento)
  │     ├── feature/nova-funcionalidade
  │     └── feature/outra-funcionalidade
  │
  ├── release/v1.2.0 (preparação de release)
  │
  └── hotfix/corrigir-bug-critico (correção urgente)
```

### Branches Principais

#### 1. main/master
- **Propósito**: Código em produção
- **Características**:
  - Sempre estável e deployável
  - Cada commit representa uma release
  - Protegida (não commitar diretamente)
  - Tags de versão aqui

#### 2. develop
- **Propósito**: Branch de integração de desenvolvimento
- **Características**:
  - Branch principal de trabalho
  - Features são mergeadas aqui primeiro
  - Sempre atualizada com última versão
  - Base para releases

### Branches de Suporte

#### 3. feature/*
- **Propósito**: Desenvolvimento de novas funcionalidades
- **Criação**: A partir de `develop`
- **Merge**: De volta para `develop`
- **Deletar**: Após merge bem-sucedido

#### 4. release/*
- **Propósito**: Preparar nova release para produção
- **Criação**: A partir de `develop` quando features estão prontas
- **Merge**: Para `main` (com tag) e para `develop`
- **Uso**: Apenas correções de bugs e ajustes finais

#### 5. hotfix/*
- **Propósito**: Correções urgentes em produção
- **Criação**: A partir de `main`
- **Merge**: Para `main` (com tag) e para `develop`
- **Uso**: Apenas quando há bug crítico em produção

## Workflows Detalhados

### Feature Development

```bash
# 1. Criar feature a partir de develop
git switch develop
git pull origin develop
git switch -c feature/nova-funcionalidade

# 2. Desenvolver
# ... trabalhar ...
git add .
git commit -m "feat: Implementa nova funcionalidade"
git push -u origin feature/nova-funcionalidade

# 3. Manter atualizada
git fetch origin
git merge origin/develop  # ou rebase

# 4. Finalizar feature
git switch develop
git merge --no-ff feature/nova-funcionalidade
git push origin develop

# 5. Deletar branch
git branch -d feature/nova-funcionalidade
git push origin --delete feature/nova-funcionalidade
```

**Nota**: `--no-ff` cria commit de merge mesmo em fast-forward, mantendo histórico claro.

### Release Preparation

```bash
# 1. Criar release quando develop está pronto
git switch develop
git pull origin develop
git switch -c release/v1.2.0

# 2. Preparar release
# - Atualizar números de versão
# - Atualizar CHANGELOG
# - Ajustes finais
git add .
git commit -m "chore: Atualiza versão para 1.2.0"
git push -u origin release/v1.2.0

# 3. Correções de bugs (sem novas features!)
# ... corrigir bugs ...
git add .
git commit -m "fix: Corrige bug X"
git push origin release/v1.2.0

# 4. Finalizar release
git switch main
git merge --no-ff release/v1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main
git push origin --tags

# 5. Merge de volta para develop
git switch develop
git merge --no-ff release/v1.2.0
git push origin develop

# 6. Deletar branch de release
git branch -d release/v1.2.0
git push origin --delete release/v1.2.0
```

### Hotfix (Correção Urgente)

```bash
# 1. Criar hotfix a partir de main
git switch main
git pull origin main
git switch -c hotfix/corrigir-bug-critico

# 2. Corrigir bug
# ... corrigir urgentemente ...
git add .
git commit -m "fix: Corrige bug crítico Y"
git push -u origin hotfix/corrigir-bug-critico

# 3. Merge para main (com tag)
git switch main
git merge --no-ff hotfix/corrigir-bug-critico
git tag -a v1.1.1 -m "Hotfix version 1.1.1"
git push origin main
git push origin --tags

# 4. Merge para develop também!
git switch develop
git merge --no-ff hotfix/corrigir-bug-critico
git push origin develop

# 5. Deletar branch
git branch -d hotfix/corrigir-bug-critico
git push origin --delete hotfix/corrigir-bug-critico
```

**Importante**: Hotfixes devem ir para AMBAS main E develop!

## Exemplo Visual do Fluxo

```
main:     A---B-----------------------E---F---G (tags: v1.0, v1.1, v1.1.1)
           \   \                       /   /
develop:   C---D---H---I---J---K---L---M---N
              /           \           /
feature1:     F1---F2       \         /
                              \       /
feature2:                       F3---F4

release:                           R1---R2
                                       /
hotfix:                                H1
```

## Convenções de Versionamento

### Semantic Versioning (SemVer)

Formato: `MAJOR.MINOR.PATCH` (ex: 1.2.3)

- **MAJOR**: Mudanças incompatíveis (1.0.0 → 2.0.0)
- **MINOR**: Novas funcionalidades compatíveis (1.0.0 → 1.1.0)
- **PATCH**: Correções de bugs (1.0.0 → 1.0.1)

### Tags de Versão

```bash
# Criar tag anotada (recomendado)
git tag -a v1.2.0 -m "Release version 1.2.0"

# Criar tag leve
git tag v1.2.0

# Push de tags
git push origin v1.2.0
git push origin --tags  # todas as tags

# Ver tags
git tag
git tag -l "v1.*"  # filtrar

# Ver detalhes
git show v1.2.0
```

## Git Flow com Ferramentas

### Instalação do Git Flow (opcional)

```bash
# macOS
brew install git-flow-avh

# Linux
sudo apt install git-flow
```

### Comandos Git Flow

```bash
# Inicializar Git Flow no repositório
git flow init

# Criar feature
git flow feature start nome-feature
git flow feature finish nome-feature

# Criar release
git flow release start 1.2.0
git flow release finish 1.2.0

# Criar hotfix
git flow hotfix start 1.1.1
git flow hotfix finish 1.1.1
```

**Nota**: Você pode fazer Git Flow manualmente sem a ferramenta!

## Quando Usar Git Flow

### Ideal para:
- ✅ Projetos com releases versionadas
- ✅ Software comercial/empresarial
- ✅ Equipes grandes
- ✅ Necessidade de manter múltiplas versões
- ✅ Processo de QA/testes antes de produção

### Não ideal para:
- ❌ Deploy contínuo (sem releases formais)
- ❌ Projetos pequenos
- ❌ Equipes pequenas (muito overhead)
- ❌ Aplicações web simples

## Comparação: Git Flow vs GitHub Flow

| Aspecto | Git Flow | GitHub Flow |
|---------|----------|-------------|
| Branches | Múltiplas (main, develop, feature, release, hotfix) | Poucas (main, feature) |
| Complexidade | Alta | Baixa |
| Releases | Versionadas e formais | Contínuas |
| Ideal para | Software com versões | Deploy contínuo |
| Overhead | Alto | Baixo |

**Recomendação**: Use GitHub Flow para apps web, Git Flow para software versionado.

## Exemplo Prático Completo

```bash
# === SETUP INICIAL ===
git clone projeto.git
cd projeto
git switch develop

# === DESENVOLVIMENTO DE FEATURE ===
git switch -c feature/sistema-pagamento
# ... desenvolver ...
git commit -m "feat: Implementa pagamento"
git push -u origin feature/sistema-pagamento
# PR para develop → merge
git switch develop
git pull origin develop
git branch -d feature/sistema-pagamento

# === OUTRAS FEATURES ===
# ... mais features são mergeadas em develop ...

# === PREPARAR RELEASE ===
git switch -c release/v2.0.0
# Atualizar versão, changelog, etc.
git commit -m "chore: Atualiza versão para 2.0.0"
# Testes finais, correções de bugs
git commit -m "fix: Corrige bug X"
git push -u origin release/v2.0.0

# === FINALIZAR RELEASE ===
git switch main
git merge --no-ff release/v2.0.0
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin main
git push origin v2.0.0

git switch develop
git merge --no-ff release/v2.0.0
git push origin develop

git branch -d release/v2.0.0
git push origin --delete release/v2.0.0

# === HOTFIX (se necessário) ===
git switch main
git switch -c hotfix/corrigir-bug-critico
# ... corrigir ...
git commit -m "fix: Corrige bug crítico"
git push -u origin hotfix/corrigir-bug-critico

git switch main
git merge --no-ff hotfix/corrigir-bug-critico
git tag -a v2.0.1 -m "Hotfix version 2.0.1"
git push origin main
git push origin v2.0.1

git switch develop
git merge --no-ff hotfix/corrigir-bug-critico
git push origin develop
```

## Resumo

**Git Flow** é um workflow estruturado com:
- **main**: Produção estável
- **develop**: Integração de desenvolvimento
- **feature**: Novas funcionalidades
- **release**: Preparação de versões
- **hotfix**: Correções urgentes

É mais complexo que o fluxo básico, mas necessário para projetos com releases formais e versionadas!

## Próximos Passos

No próximo arquivo, você aprenderá sobre **resolução avançada de conflitos** e **estratégias para commits claros**!
