# Pull Requests e Colaboração em Equipe

## O que é Pull Request?

Um **Pull Request (PR)** ou **Merge Request (MR)** é uma solicitação para integrar mudanças de uma branch em outra. É como dizer: "Ei, olha essas mudanças que fiz, pode integrar?"

### Por que Usar Pull Requests?

1. **Code Review**: Outros desenvolvedores revisam seu código
2. **Discussão**: Debater mudanças antes de integrar
3. **Testes**: CI/CD pode rodar testes automaticamente
4. **Documentação**: Histórico de decisões e discussões
5. **Qualidade**: Garante que código seja revisado antes de entrar na main

## Fluxo de Pull Request

### Passo a Passo Básico

```
1. Criar branch de feature
   ↓
2. Fazer mudanças e commits
   ↓
3. Push da branch para GitHub
   ↓
4. Criar Pull Request no GitHub
   ↓
5. Code Review (outros desenvolvedores)
   ↓
6. Fazer ajustes se necessário
   ↓
7. Aprovação e Merge
   ↓
8. Deletar branch
```

## Criando um Pull Request

### 1. Preparar Branch

```bash
# Garantir que está atualizado
git switch main
git pull origin main

# Criar branch de feature
git switch -c feature/nova-funcionalidade

# Fazer mudanças
# ... trabalhar no código ...

# Commitar
git add .
git commit -m "feat: Implementa nova funcionalidade"

# Push da branch
git push -u origin feature/nova-funcionalidade
```

### 2. Criar PR no GitHub

1. **Ir para GitHub** após fazer push
2. **GitHub mostra banner** sugerindo criar PR (clique em "Compare & pull request")
3. **Ou manualmente:**
   - Ir em "Pull requests" > "New pull request"
   - Selecionar branch base (geralmente `main`) e branch de origem (sua feature)
4. **Preencher informações:**
   - **Título**: Descreva claramente o que o PR faz
   - **Descrição**: Detalhes sobre mudanças
   - **Reviewers**: Pessoas para revisar código
   - **Labels**: Categorizar (bug, feature, etc.)

### 3. Template de PR Bom

```markdown
## Descrição
Implementa sistema de autenticação com JWT.

## Tipo de Mudança
- [ ] Bug fix
- [x] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Como Testar
1. Executar testes: `pytest tests/test_auth.py`
2. Testar login manualmente na aplicação

## Checklist
- [x] Código testado
- [x] Documentação atualizada
- [x] Sem conflitos com main
- [x] Aprovado em code review
```

## Code Review

### Como Revisar um PR

1. **Ler descrição e contexto**
2. **Revisar código mudado:**
   - Clique em "Files changed" no PR
   - Veja linhas adicionadas (verde) e removidas (vermelho)
3. **Deixar comentários:**
   - Comentários gerais: Na aba "Conversation"
   - Comentários em código: Clique no número da linha
4. **Aprovar ou solicitar mudanças:**
   - "Approve": Código está bom
   - "Request changes": Precisa ajustes
   - "Comment": Apenas comentários, sem aprovação

### Tipos de Comentários

**Construtivos:**
```
✅ "Ótima implementação! Sugestão: considerar adicionar validação aqui."
✅ "Essa função está muito grande, podemos refatorar?"
✅ "Pode adicionar testes para este caso edge?"
```

**Não-construtivos:**
```
❌ "Isso está errado."
❌ "Refaça tudo."
❌ "Não gostei."
```

### Respondendo a Comentários

```markdown
Agradeço o feedback! Vou ajustar conforme sugerido.

- ✅ Feito: Adicionei validação conforme solicitado
- ✅ Feito: Refatorei função em funções menores
- 📝 Pergunta: Sobre o ponto X, qual abordagem prefere?
```

## Fazendo Ajustes em um PR

### Atualizar Branch do PR

```bash
# Fazer mudanças baseadas em feedback
# ... editar código ...

# Adicionar e commitar
git add .
git commit -m "fix: Corrige validação conforme feedback do review"

# Push (PR é atualizado automaticamente)
git push origin feature/nova-funcionalidade
```

**O PR é atualizado automaticamente** quando você faz push na branch!

### Adicionar Mais Commits

Você pode adicionar quantos commits quiser na branch do PR:

```bash
git add arquivo.py
git commit -m "docs: Adiciona comentários na função X"
git push origin feature/nova-funcionalidade
```

## Merge do Pull Request

### Opções de Merge no GitHub

1. **Create a merge commit**
   - Cria commit de merge
   - Preserva histórico completo
   - Recomendado para branches compartilhadas

2. **Squash and merge**
   - Combina todos os commits em um só
   - Histórico mais limpo
   - Perde histórico detalhado da feature

3. **Rebase and merge**
   - Aplica commits linearmente
   - Histórico linear sem commit de merge
   - Requer histórico limpo

### Processo de Merge

1. **Aguardar aprovações** necessárias
2. **Garantir que testes passem** (se houver CI/CD)
3. **Resolver conflitos** se houver
4. **Clicar em "Merge pull request"**
5. **Confirmar merge**
6. **Deletar branch** (GitHub oferece opção)

## Boas Práticas para PRs

### Tamanho do PR

✅ **Bom:**
- PRs pequenos e focados
- Uma funcionalidade por PR
- Fácil de revisar (100-300 linhas)

❌ **Ruim:**
- PRs gigantes (1000+ linhas)
- Múltiplas funcionalidades não relacionadas
- Difícil de revisar

### Commits no PR

✅ **Bom:**
- Commits pequenos e lógicos
- Mensagens descritivas
- Fácil de entender histórico

❌ **Ruim:**
- Um commit gigante
- Mensagens vagas
- Histórico confuso

### Descrição do PR

✅ **Bom:**
```markdown
## O que faz
Adiciona autenticação de usuários via JWT.

## Por que
Necessário para proteger rotas da API.

## Como testar
1. POST /auth/login com credenciais válidas
2. Verificar token JWT na resposta
```

❌ **Ruim:**
```markdown
PR
```

## Resolvendo Conflitos em PRs

Se a branch principal mudou desde que o PR foi criado:

```bash
# 1. Atualizar branch base localmente
git switch main
git pull origin main

# 2. Voltar para branch do PR
git switch feature/nova-funcionalidade

# 3. Fazer merge ou rebase da main
git merge main
# ou
git rebase main

# 4. Resolver conflitos se houver
# ... resolver conflitos ...

# 5. Push atualizado
git push origin feature/nova-funcionalidade
# Se fez rebase, pode precisar force push:
# git push --force-with-lease origin feature/nova-funcionalidade
```

**GitHub também oferece** botão para resolver conflitos via interface web.

## Exemplo Completo: PR do Início ao Fim

```bash
# === 1. Preparar ===
git switch main
git pull origin main

# === 2. Criar feature ===
git switch -c feature/adicionar-login

# === 3. Desenvolver ===
cat > auth.py << 'EOF'
def login(username, password):
    # Implementação de login
    if username == "admin" and password == "senha123":
        return {"token": "jwt_token_here"}
    return None
EOF

# === 4. Commitar ===
git add auth.py
git commit -m "feat: Implementa função de login"

# === 5. Criar testes ===
cat > test_auth.py << 'EOF'
def test_login_success():
    from auth import login
    result = login("admin", "senha123")
    assert result is not None
    assert "token" in result

def test_login_failure():
    from auth import login
    result = login("admin", "wrong")
    assert result is None
EOF

git add test_auth.py
git commit -m "test: Adiciona testes para login"

# === 6. Push ===
git push -u origin feature/adicionar-login

# === 7. Criar PR no GitHub ===
# Via interface web: New Pull Request

# === 8. Aguardar review ===
# Outro desenvolvedor revisa e sugere mudanças

# === 9. Fazer ajustes ===
# ... editar código conforme feedback ...

git add auth.py
git commit -m "fix: Melhora validação de credenciais"
git push origin feature/adicionar-login

# === 10. Após aprovação, merge ===
# Via interface web: Merge pull request

# === 11. Limpar ===
git switch main
git pull origin main
git branch -d feature/adicionar-login
```

## Colaboração em Equipe

### Workflow de Equipe

1. **Cada desenvolvedor trabalha em sua branch**
2. **Commits frequentes** na branch de feature
3. **PR quando feature está pronta** (ou em progresso para feedback)
4. **Code review obrigatório** antes de merge
5. **Testes devem passar** antes de merge
6. **Merge na main** após aprovação
7. **Deletar branch** após merge

### Boas Práticas de Colaboração

1. **Comunicação**: Discutir mudanças grandes antes de implementar
2. **Atualização frequente**: Fazer pull da main regularmente
3. **Branches curtas**: Integrar mudanças cedo
4. **Code review respeitoso**: Seja construtivo e educado
5. **Testes**: Sempre testar antes de criar PR
6. **Documentação**: Documentar mudanças importantes

### Problemas Comuns

**Conflitos frequentes:**
- Solução: Atualizar branch mais frequentemente
- Fazer pull/merge da main diariamente

**PRs esquecidos:**
- Solução: Revisar PRs abertos regularmente
- Notificações do GitHub ajudam

**Review lento:**
- Solução: Designar reviewers
- Comunicar urgência quando necessário

## Comandos Úteis

```bash
# Workflow de PR
git switch -c feature/nome
# ... trabalhar ...
git push -u origin feature/nome
# Criar PR no GitHub

# Atualizar PR
git add .
git commit -m "mensagem"
git push origin feature/nome

# Resolver conflitos
git switch main
git pull origin main
git switch feature/nome
git merge main
# ... resolver conflitos ...
git push origin feature/nome
```

## Resumo

- **Pull Request**: Solicitação para integrar código
- **Code Review**: Revisão de código por outros desenvolvedores
- **Workflow**: Branch → Desenvolver → PR → Review → Merge
- **Boas práticas**: PRs pequenos, descrições claras, código testado
- **Colaboração**: Comunicação e respeito são essenciais

## Próximos Passos

Agora você sabe:
- ✅ Criar e gerenciar Pull Requests
- ✅ Fazer code review
- ✅ Colaborar efetivamente em equipe

Você completou o módulo de Branches e GitHub! Continue para o próximo módulo sobre **Fluxos de Trabalho Avançados**!
