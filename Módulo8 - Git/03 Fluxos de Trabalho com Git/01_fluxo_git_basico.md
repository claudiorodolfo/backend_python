# Fluxo Git Básico: Feature Branch, Merge e Pull Request

## Visão Geral do Fluxo Básico

O **Git Flow básico** (também chamado de **GitHub Flow**) é um dos workflows mais simples e eficazes para desenvolvimento. É ideal para:
- Projetos pequenos e médios
- Equipes que fazem deploy frequente
- Projetos que não precisam de releases complexas

## Estrutura do Fluxo

```
main (produção)
  ↑
  │ merge via PR
  │
feature/nova-funcionalidade (desenvolvimento)
```

### Características

- **main/master**: Branch principal, sempre deployável
- **feature branches**: Branches temporárias para cada funcionalidade
- **Pull Requests**: Revisão antes de integrar
- **Merge direto**: Feature → main (sem branch intermediária)

## Fluxo Completo Passo a Passo

### 1. Iniciar Nova Feature

```bash
# Garantir que main está atualizada
git switch main
git pull origin main

# Criar branch de feature
git switch -c feature/adicionar-login

# Nome descritivo e claro
```

**Boas práticas:**
- Sempre partir da main atualizada
- Usar nomes descritivos: `feature/`, `bugfix/`, `hotfix/`
- Um desenvolvedor por feature (geralmente)

### 2. Desenvolver na Feature Branch

```bash
# Trabalhar normalmente
# ... editar arquivos ...

# Commits frequentes e pequenos
git add arquivo.py
git commit -m "feat: Implementa função de autenticação"

# ... mais trabalho ...

git add test_auth.py
git commit -m "test: Adiciona testes para autenticação"

# Push regular (permite backup e colaboração)
git push -u origin feature/adicionar-login
```

**Boas práticas:**
- Commits pequenos e atômicos
- Mensagens descritivas
- Push regular para backup

### 3. Manter Feature Atualizada

```bash
# Periodicamente, atualizar com mudanças da main
git fetch origin
git merge origin/main
# ou (para histórico mais limpo)
git rebase origin/main

# Resolver conflitos se houver
# ... resolver ...

# Push atualizado
git push origin feature/adicionar-login
```

**Quando atualizar:**
- Antes de criar PR
- Quando main recebe muitas mudanças
- Diariamente (se trabalho em paralelo)

### 4. Criar Pull Request

```bash
# Após feature completa e testada
git push origin feature/adicionar-login

# Criar PR no GitHub/GitLab via interface web
```

**Informações do PR:**
- Título claro: "feat: Adiciona sistema de login"
- Descrição detalhada
- Reviewers apropriados
- Labels (feature, bugfix, etc.)

### 5. Code Review

Outros desenvolvedores revisam:
- Funcionalidade está correta?
- Código segue padrões?
- Testes adequados?
- Sem bugs óbvios?

### 6. Fazer Ajustes

```bash
# Com base no feedback do review
# ... fazer mudanças ...

git add arquivo.py
git commit -m "fix: Corrige validação conforme feedback"
git push origin feature/adicionar-login

# PR é atualizado automaticamente!
```

### 7. Merge na Main

Após aprovação:
1. Merge via interface web (GitHub/GitLab)
2. Ou localmente:
   ```bash
   git switch main
   git merge feature/adicionar-login
   git push origin main
   ```

### 8. Limpeza

```bash
# Deletar branch local
git branch -d feature/adicionar-login

# Deletar branch remota (se não foi deletada automaticamente)
git push origin --delete feature/adicionar-login
```

## Exemplo Prático Completo

```bash
# === SETUP INICIAL ===
# Repositório já existe no GitHub

# === 1. PREPARAR ===
git switch main
git pull origin main

# === 2. CRIAR FEATURE ===
git switch -c feature/sistema-notificacoes

# === 3. DESENVOLVER ===
# Criar arquivo notificacoes.py
cat > notificacoes.py << 'EOF'
class Notificacao:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem
    
    def enviar_email(self):
        # Lógica de envio
        return True
EOF

git add notificacoes.py
git commit -m "feat: Cria classe Notificacao base"

# Adicionar mais funcionalidade
cat >> notificacoes.py << 'EOF'
    
    def enviar_sms(self):
        # Lógica de SMS
        return True
EOF

git add notificacoes.py
git commit -m "feat: Adiciona método para envio de SMS"

# === 4. PUSH ===
git push -u origin feature/sistema-notificacoes

# === 5. CRIAR PR (via GitHub web) ===
# Título: "feat: Implementa sistema de notificações"
# Descrição: Detalhes da implementação

# === 6. CODE REVIEW (outro dev revisa) ===
# Feedback: "Adicionar tratamento de erros"

# === 7. AJUSTES ===
# Adicionar tratamento de erros
git add notificacoes.py
git commit -m "fix: Adiciona tratamento de erros"
git push origin feature/sistema-notificacoes

# === 8. APROVAÇÃO E MERGE ===
# Via GitHub: Merge pull request

# === 9. ATUALIZAR LOCAL ===
git switch main
git pull origin main

# === 10. LIMPAR ===
git branch -d feature/sistema-notificacoes
```

## Vantagens do Fluxo Básico

✅ **Simplicidade**: Fácil de entender e seguir
✅ **Flexibilidade**: Adapta-se a diferentes projetos
✅ **Histórico limpo**: Mantém histórico organizado
✅ **Code review**: Garante qualidade via PRs
✅ **Rollback fácil**: Pode reverter merges se necessário

## Quando Usar Este Fluxo

**Ideal para:**
- Aplicações web com deploy contínuo
- Projetos com releases frequentes
- Equipes pequenas a médias
- Projetos que não precisam de releases complexas

**Não ideal para:**
- Projetos com releases versionadas complexas
- Projetos que precisam manter múltiplas versões em produção
- Equipes muito grandes com processos rígidos

## Comparação: Merge vs Rebase

### Merge (padrão deste fluxo)

```bash
git switch main
git merge feature/nova-feature
```

**Vantagens:**
- Preserva histórico completo
- Não reescreve histórico
- Seguro para branches compartilhadas

**Desvantagens:**
- Cria commits de merge
- Histórico pode ficar "poluído"

### Rebase (alternativa avançada)

```bash
git switch feature/nova-feature
git rebase main
git switch main
git merge feature/nova-feature
```

**Vantagens:**
- Histórico linear e limpo
- Sem commits de merge

**Desvantagens:**
- Reescreve histórico (cuidado!)
- Não usar em branches compartilhadas

**Recomendação**: Use merge neste fluxo básico. Rebase é para workflows avançados.

## Troubleshooting

### Conflitos Frequentes

**Problema**: Conflitos toda vez que atualiza branch

**Solução:**
- Atualizar mais frequentemente
- Comunicar com equipe sobre mudanças grandes
- Dividir features menores

### PR muito grande

**Problema**: PR tem 1000+ linhas, difícil de revisar

**Solução:**
- Dividir em PRs menores
- Uma feature por PR
- Criar PRs incrementais (WIP - Work In Progress)

### Branch desatualizada

**Problema**: Feature branch muito atrás da main

**Solução:**
```bash
git fetch origin
git rebase origin/main  # ou merge
# Resolver conflitos
git push --force-with-lease origin feature/nome
```

## Comandos Essenciais do Fluxo

```bash
# Preparar
git switch main
git pull origin main

# Criar feature
git switch -c feature/nome

# Desenvolver
git add .
git commit -m "mensagem"
git push -u origin feature/nome

# Atualizar
git fetch origin
git merge origin/main

# Após merge na main
git switch main
git pull origin main
git branch -d feature/nome
```

## Checklist do Fluxo

- [ ] Main atualizada antes de criar branch
- [ ] Branch com nome descritivo
- [ ] Commits pequenos e frequentes
- [ ] Feature testada antes de PR
- [ ] PR bem descrito
- [ ] Code review feito
- [ ] Conflitos resolvidos
- [ ] Branch deletada após merge

## Resumo

O **fluxo básico** é simples e eficaz:
1. Criar branch de feature a partir da main
2. Desenvolver com commits frequentes
3. Criar Pull Request quando pronto
4. Revisar e ajustar
5. Merge na main
6. Deletar branch

Este é o fluxo mais usado na indústria e perfeito para começar!

## Próximos Passos

No próximo arquivo, você aprenderá sobre **Git Flow** - um workflow mais complexo para projetos maiores com releases versionadas!
