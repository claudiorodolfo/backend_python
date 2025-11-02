# Estratégias para Commits Claros e Históricos Limpos

## Por que Commits Claros Importam?

Commits bem feitos são essenciais para:
- **Rastreabilidade**: Entender o que mudou e por quê
- **Debugging**: Encontrar quando bug foi introduzido
- **Code Review**: Facilitar revisão de código
- **Rollback**: Saber o que reverter
- **Documentação**: Histórico serve como documentação viva
- **Colaboração**: Outros desenvolvedores entendem mudanças

## Princípios de Commits Claros

### 1. Commits Atômicos

Um commit deve representar **uma mudança lógica completa**.

✅ **Bom:**
```bash
git commit -m "feat: Adiciona validação de email"
git commit -m "fix: Corrige cálculo de desconto"
git commit -m "docs: Atualiza instruções de instalação"
```

❌ **Ruim:**
```bash
git commit -m "mudanças"
git commit -m "wip"  # work in progress
git commit -m "fix"
```

### 2. Mensagens Descritivas

A mensagem deve explicar **o que** foi feito e **por quê** (se necessário).

**Formato recomendado:**
```
tipo: Descrição curta (até 50 caracteres)

Corpo detalhado explicando:
- O que foi feito
- Por que foi feito
- Como (se relevante)

Rodapé (opcional):
- Referências a issues: Fixes #123
- Breaking changes
```

**Exemplos:**

✅ **Bom:**
```bash
git commit -m "feat: Adiciona autenticação JWT

Implementa sistema de autenticação usando JSON Web Tokens.
- Gera token após login bem-sucedido
- Valida token em requisições protegidas
- Expira token após 24 horas

Fixes #45"
```

❌ **Ruim:**
```bash
git commit -m "auth"
git commit -m "adiciona jwt"
git commit -m "fix"
```

### 3. Conventional Commits

Padrão amplamente adotado na indústria:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

**Tipos principais:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração de código
- `perf`: Melhoria de performance
- `test`: Testes
- `chore`: Manutenção/tarefas

**Exemplos:**
```bash
git commit -m "feat(auth): Adiciona login com JWT"
git commit -m "fix(validation): Corrige validação de CPF"
git commit -m "docs: Atualiza README com instruções"
git commit -m "refactor(db): Reorganiza estrutura de queries"
```

## Estrutura de Mensagens de Commit

### Mensagem Curta (Assunto)

- **Máximo 50-72 caracteres**
- **Imperativo**: "Adiciona" não "Adicionado"
- **Específico**: O que foi feito
- **Sem ponto final**

### Corpo (Opcional)

Para mudanças complexas:

```bash
git commit -m "feat: Implementa sistema de cache

O sistema de cache melhora performance significativamente para
requisições frequentes. Implementa cache em memória usando Redis
com TTL de 1 hora para dados não críticos.

Benefícios:
- Reduz carga no banco de dados
- Melhora tempo de resposta em 60%
- Configurável via variáveis de ambiente"
```

### Rodapé (Opcional)

```bash
git commit -m "fix: Corrige bug de timeout

Corrige problema onde requisições longas causavam timeout.

Fixes #123
Closes #456
See also: #789"
```

## Histórico Limpo

### O que é Histórico Limpo?

Um histórico onde cada commit:
- Tem propósito claro
- É facilmente compreensível
- Contribui para a história do projeto
- Não contém ruído (typos, tentativas, experimentos)

### Como Manter Histórico Limpo

#### 1. Commits Pequenos e Focados

✅ **Bom:**
```bash
# Commit 1
git commit -m "feat: Adiciona função de soma"

# Commit 2
git commit -m "feat: Adiciona função de subtração"

# Commit 3
git commit -m "test: Adiciona testes para operações"
```

❌ **Ruim:**
```bash
# Um commit gigante
git commit -m "adiciona calculadora completa"
```

#### 2. Não Commitar Debug/Teste

❌ **Ruim:**
```bash
git commit -m "teste"
git commit -m "debug"
git commit -m "tentativa"
```

✅ **Bom:**
Use `git stash` para guardar trabalho em progresso:
```bash
git stash save "WIP: experimentando nova abordagem"
```

#### 3. Separar Mudanças Não Relacionadas

❌ **Ruim:**
```bash
# Tudo em um commit
git commit -m "adiciona feature e corrige bugs e atualiza docs"
```

✅ **Bom:**
```bash
git commit -m "feat: Adiciona nova feature"
git commit -m "fix: Corrige bug X"
git commit -m "docs: Atualiza documentação"
```

### Limpar Histórico com Rebase Interativo

```bash
# Editar últimos 3 commits
git rebase -i HEAD~3

# Opções:
# pick: Manter commit como está
# reword: Manter commit mas mudar mensagem
# edit: Parar para editar commit
# squash: Combinar com commit anterior
# fixup: Como squash mas descartar mensagem
# drop: Remover commit
```

**Exemplo:**

```bash
pick abc1234 feat: Adiciona função X
squash def5678 fix: Corrige typo
reword ghi9012 feat: Adiciona mais coisas

# Resultado: 2 commits, um combinado e um com mensagem reescrita
```

## Padrões de Mensagens por Tipo

### Feature (Nova Funcionalidade)

```bash
git commit -m "feat: Adiciona sistema de notificações

Implementa envio de notificações por email e SMS.
Usuários podem configurar preferências de notificação.

Features:
- Envio de email via SMTP
- Envio de SMS via API
- Preferências por usuário"
```

### Bug Fix

```bash
git commit -m "fix: Corrige validação de data de nascimento

Problema: Validação aceitava datas futuras.
Solução: Adiciona verificação para garantir data <= hoje.

Fixes #78"
```

### Refatoração

```bash
git commit -m "refactor: Reorganiza módulo de autenticação

Separa lógica de autenticação em módulos menores:
- auth/validators.py: Validações
- auth/tokens.py: Geração de tokens
- auth/permissions.py: Sistema de permissões

Melhora organização e testabilidade do código."
```

### Documentação

```bash
git commit -m "docs: Atualiza guia de instalação

Adiciona instruções para:
- Instalação em Windows
- Configuração de variáveis de ambiente
- Troubleshooting comum"
```

### Performance

```bash
git commit -m "perf: Otimiza consultas ao banco de dados

Usa eager loading para reduzir número de queries.
Reduz tempo de resposta de 2s para 0.3s.

Antes: N+1 queries
Depois: 2 queries"
```

## Exemplos de Histórico Limpo

### Histórico Bom

```bash
* a1b2c3d feat: Adiciona autenticação JWT
* d4e5f6g test: Adiciona testes para autenticação
* g7h8i9j docs: Atualiza README com instruções de auth
* j0k1l2m fix: Corrige expiração de token
* m3n4o5p feat: Adiciona refresh token
```

Cada commit tem propósito claro e histórico conta uma história.

### Histórico Ruim

```bash
* a1b2c3d mudanças
* d4e5f6g wip
* g7h8i9j fix
* j0k1l2m mais mudanças
* m3n4o5p commit
```

Histórico confuso, difícil de entender.

## Ferramentas e Automação

### Hooks de Commit

Criar `.git/hooks/commit-msg` para validar mensagens:

```bash
#!/bin/sh
commit_regex='^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,50}'

if ! grep -qE "$commit_regex" "$1"; then
    echo "Erro: Mensagem de commit não segue padrão!"
    echo "Formato: tipo(escopo): descrição"
    exit 1
fi
```

### Templates de Commit

Criar template em `~/.gitmessage`:

```
# <tipo>(<escopo>): <descrição curta>

# <corpo detalhado>

# <rodapé>
# Fixes #123
```

Usar:
```bash
git config --global commit.template ~/.gitmessage
```

### Aliases Úteis

```bash
# Commit com tipo automático
git config --global alias.cf "commit -m 'feat: '"
git config --global alias.cb "commit -m 'fix: '"
git config --global alias.cd "commit -m 'docs: '"

# Log formatado
git config --global alias.lg "log --oneline --graph --decorate --all"
```

## Checklist de Commits

Antes de cada commit, pergunte:

- [ ] Este commit tem um propósito claro?
- [ ] A mensagem descreve o que foi feito?
- [ ] O commit é atômico (uma mudança lógica)?
- [ ] Não há código de debug/teste?
- [ ] Segue padrões da equipe (Conventional Commits)?
- [ ] Mensagem está no imperativo?
- [ ] Mensagem é específica (não vaga)?

## Exemplos Práticos

### Cena 1: Adicionando Feature

```bash
# ❌ Ruim
git add .
git commit -m "adiciona coisas"

# ✅ Bom
git add auth.py
git commit -m "feat: Implementa autenticação básica"

git add test_auth.py
git commit -m "test: Adiciona testes para autenticação"

git add README.md
git commit -m "docs: Documenta sistema de autenticação"
```

### Cena 2: Corrigindo Bug

```bash
# ❌ Ruim
git add .
git commit -m "fix bug"

# ✅ Bom
git add validators.py
git commit -m "fix(validation): Corrige validação de email

Problema: Aceitava emails sem @
Solução: Adiciona validação regex mais rigorosa

Fixes #123"
```

### Cena 3: Refatoração

```bash
# ❌ Ruim
git add .
git commit -m "refatora"

# ✅ Bom
git add database/
git commit -m "refactor(db): Separa queries em módulo dedicado

Reorganiza código de acesso a banco de dados:
- database/queries.py: Queries SQL
- database/models.py: Modelos ORM
- database/connection.py: Gerenciamento de conexão

Melhora organização e facilita manutenção."
```

## Resumo

**Commits claros requerem:**
1. ✅ Commits atômicos (uma mudança lógica)
2. ✅ Mensagens descritivas e específicas
3. ✅ Seguir padrões (Conventional Commits)
4. ✅ Separar mudanças não relacionadas
5. ✅ Não commitar debug/teste temporário

**Histórico limpo é:**
- Fácil de entender
- Útil para debugging
- Documentação viva do projeto
- Profissional e organizado

Lembre-se: **Histórico é para pessoas, não apenas para Git!**
