# Boas Práticas para Colaboração em Equipe

## Princípios Fundamentais

### 1. Commits Atômicos

Um commit deve representar uma mudança lógica completa e coerente.

✅ **Bom:**
```bash
git commit -m "feat: Adiciona validação de email no formulário"
git commit -m "fix: Corrige cálculo de desconto"
git commit -m "docs: Atualiza README com instruções de instalação"
```

❌ **Ruim:**
```bash
git commit -m "mudanças"
git commit -m "fix"
git commit -m "wip"
```

### 2. Mensagens de Commit Claras

Siga o padrão **Conventional Commits**:

```
tipo(escopo): descrição curta

Corpo detalhado (opcional)

Rodapé (opcional)
```

**Tipos comuns:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção/configuração

**Exemplos:**
```bash
git commit -m "feat(auth): Adiciona login com JWT"
git commit -m "fix(validation): Corrige validação de CPF"
git commit -m "docs: Atualiza instruções de instalação"
```

### 3. Branches Descritivas

Use nomes que indiquem claramente o propósito:

✅ **Bom:**
```bash
feature/adicionar-pagamento
bugfix/corrigir-validacao-email
hotfix/corrigir-falha-login
refactor/reorganizar-estrutura-db
docs/atualizar-api-docs
```

❌ **Ruim:**
```bash
teste
branch1
nova-feature
fix
```

## Workflow de Colaboração

### 1. Antes de Começar

```bash
# Sempre atualizar antes de começar novo trabalho
git switch main
git pull origin main

# Criar branch a partir da main atualizada
git switch -c feature/minha-feature
```

### 2. Durante o Desenvolvimento

```bash
# Commits frequentes e pequenos
git add arquivo.py
git commit -m "feat: Adiciona função X"

# ... mais trabalho ...

git add outro_arquivo.py
git commit -m "test: Adiciona testes para função X"

# Push regular (não precisa esperar terminar)
git push origin feature/minha-feature
```

### 3. Mantendo Branch Atualizada

```bash
# Regularmente, atualizar sua branch com mudanças da main
git switch feature/minha-feature

# Opção 1: Merge
git fetch origin
git merge origin/main

# Opção 2: Rebase (histórico mais limpo, apenas branches locais)
git fetch origin
git rebase origin/main
```

### 4. Antes de Criar PR

```bash
# 1. Garantir que está atualizado
git fetch origin
git rebase origin/main  # ou merge

# 2. Verificar que tudo funciona
# Rodar testes, lint, etc.

# 3. Ver histórico
git log --oneline origin/main..HEAD

# 4. Push
git push origin feature/minha-feature
```

## Convenções de Equipe

### Nomenclatura de Branches

Estabeleça padrão na equipe:

**Exemplo 1: Tipo/Número-Descrição**
```bash
feature/123-adicionar-login
bugfix/456-corrigir-validacao
hotfix/789-corrigir-crash
```

**Exemplo 2: Tipo/Descrição**
```bash
feature/adicionar-login
bugfix/corrigir-validacao
hotfix/corrigir-crash
```

**Exemplo 3: Nome/Tipo-Descrição**
```bash
joao/feature-login
maria/bugfix-validacao
```

### Política de Merge

Defina na equipe:

1. **Quem pode fazer merge?**
   - Apenas mantenedores?
   - Após aprovação de X revisores?
   - Todos após code review?

2. **Quando fazer merge?**
   - Após aprovação de code review?
   - Após testes passarem?
   - Após aprovação de X pessoas?

3. **Como fazer merge?**
   - Merge commit?
   - Squash and merge?
   - Rebase and merge?

## Code Review

### Como Revisar Código

1. **Verifique funcionamento**: O código faz o que deveria?
2. **Verifique qualidade**: Código limpo e bem estruturado?
3. **Verifique testes**: Há testes adequados?
4. **Verifique documentação**: Código está documentado?
5. **Verifique padrões**: Segue padrões da equipe?

### Dar Feedback Construtivo

✅ **Bom:**
```
Ótimo trabalho! A implementação está clara.

Sugestão: Podemos melhorar a função X adicionando validação 
para o caso quando o valor é None. Veja exemplo:

```python
def processar(valor):
    if valor is None:
        raise ValueError("Valor não pode ser None")
    # resto do código
```

Isso evitaria erros em runtime. O que acha?
```

❌ **Ruim:**
```
Está errado.
Refaça.
Não gostei.
```

### Receber Feedback

1. **Seja receptivo**: Feedback é para melhorar, não ataque pessoal
2. **Pergunte se não entender**: Peça esclarecimentos
3. **Discuta alternativas**: Proponha soluções se discordar
4. **Agradeça**: Sempre agradeça o tempo do revisor

## Tratamento de Conflitos

### Prevenindo Conflitos

1. **Trabalhe em arquivos diferentes** quando possível
2. **Atualize frequentemente** sua branch
3. **Comunique mudanças grandes** antes de fazer
4. **Mantenha branches curtas** (integre cedo)

### Resolvendo Conflitos

```bash
# Quando há conflito ao atualizar branch
git fetch origin
git rebase origin/main  # ou merge

# Resolver conflitos manualmente
# ... editar arquivos ...

# Continuar após resolver
git add arquivos_resolvidos.py
git rebase --continue  # se fez rebase
# ou
git commit  # se fez merge

# Push
git push origin feature/minha-feature
```

**Dicas:**
- Resolva conflitos cedo (não deixe acumular)
- Quando em dúvida, pergunte ao autor da outra mudança
- Teste após resolver conflitos

## Pull Requests Efetivos

### Tamanho Ideal

- **Pequeno**: 50-200 linhas (ideal para revisão rápida)
- **Médio**: 200-500 linhas (aceitável, mas pode demorar mais)
- **Grande**: 500-1000 linhas (difícil de revisar)
- **Muito grande**: 1000+ linhas (evitar, dividir em PRs menores)

### Estrutura de PR

```markdown
## Descrição
Breve descrição do que o PR faz e por que é necessário.

## Tipo de Mudança
- [ ] Bug fix
- [x] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Como Testar
Passos para testar as mudanças:
1. Fazer X
2. Fazer Y
3. Verificar que Z acontece

## Screenshots (se aplicável)
[Incluir screenshots se mudanças afetam UI]

## Checklist
- [x] Código segue padrões do projeto
- [x] Testes foram adicionados/atualizados
- [x] Documentação foi atualizada
- [x] Não há conflitos com main
- [x] Build passa localmente
```

### Quando Criar PR?

**PRs pequenos e frequentes:**
- Trabalho em progresso visível
- Feedback cedo
- Menos chance de conflitos grandes

**Ou PR quando completo:**
- Feature completa testada
- Histórico limpo
- Uma revisão completa

Escolha baseado na cultura da equipe!

## Comunicação

### Issues e Discussões

Use GitHub Issues para:
- Planejar features antes de implementar
- Reportar bugs
- Discutir decisões de arquitetura
- Rastrear tarefas

**Link PR com Issues:**
```markdown
# No PR ou commit
Fixes #123
Closes #456
Relates to #789
```

### Mensagens de Commit Referenciando Issues

```bash
git commit -m "fix: Corrige validação de email

Resolve problema onde emails com múltiplos pontos falhavam.
Fixes #123"
```

### Comunicação Assíncrona

- **PRs**: Para discussão de código
- **Issues**: Para planejamento e bugs
- **Comentários inline**: Para feedback específico
- **Slack/Teams/etc**: Para comunicação geral

## Configurações de Projeto

### .gitignore

Mantenha `.gitignore` atualizado:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Secrets
.env
*.key
secrets/
```

### Branch Protection Rules (GitHub)

Configure proteção na branch principal:
- Requer PR antes de merge
- Requer aprovação de reviewers
- Requer que testes passem
- Bloqueia force push
- Bloqueia deleção

### Templates

Use templates para:
- **Pull Requests**: Padronizar descrições
- **Issues**: Facilitar criação de bugs/features
- **Commits**: Padronizar mensagens (via hooks)

## Checklist de Boas Práticas

### Antes de Commitar

- [ ] Código testado localmente
- [ ] Sem código comentado desnecessário
- [ ] Sem arquivos temporários
- [ ] Mensagem de commit clara
- [ ] Commit atômico (uma mudança lógica)

### Antes de Push

- [ ] Commits revisados (git log)
- [ ] Branch atualizada com main
- [ ] Sem conflitos
- [ ] Testes passando

### Antes de Criar PR

- [ ] Branch atualizada
- [ ] Código revisado
- [ ] Testes adicionados
- [ ] Documentação atualizada
- [ ] PR descrito claramente

### Ao Revisar PR

- [ ] Código funciona conforme esperado
- [ ] Segue padrões do projeto
- [ ] Testes adequados
- [ ] Sem introduzir bugs
- [ ] Documentação atualizada
- [ ] Feedback construtivo dado

## Resumo

**Boas práticas essenciais:**
1. ✅ Commits atômicos com mensagens claras
2. ✅ Branches descritivas
3. ✅ Atualização frequente
4. ✅ PRs pequenos e bem descritos
5. ✅ Code review respeitoso
6. ✅ Comunicação clara
7. ✅ Seguir padrões da equipe

**Lembre-se**: Git é uma ferramenta de colaboração. O objetivo é trabalhar bem em equipe, não apenas usar comandos corretos!

## Recursos Adicionais

- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Code Review Guidelines](https://github.com/google/eng-practices/blob/master/review/)
- [Semantic Versioning](https://semver.org/)

Com estas práticas, você e sua equipe terão um workflow Git eficiente e colaborativo!
