# Criação e Troca de Branches

## O que são Branches?

Uma **branch** (ramificação) é uma linha independente de desenvolvimento. Permite que você trabalhe em diferentes funcionalidades sem afetar o código principal.

### Analogia

Imagine branches como linhas do tempo alternativas:
- Branch principal (main/master): A linha do tempo "oficial"
- Outras branches: Linhas do tempo alternativas onde você pode experimentar

Se algo der errado em uma branch alternativa, você pode simplesmente voltar para a linha do tempo principal sem afetá-la.

## Por que Usar Branches?

1. **Isolamento**: Trabalhar em features sem afetar código estável
2. **Experimentos**: Testar ideias sem risco
3. **Colaboração**: Múltiplos desenvolvedores podem trabalhar simultaneamente
4. **Organização**: Manter histórico limpo e organizado
5. **Revisão**: Fazer code review antes de integrar ao código principal

## Criando Branches

### Ver Branches Existentes

```bash
# Listar todas as branches locais
git branch

# Listar todas as branches (locais e remotas)
git branch -a

# Listar apenas branches remotas
git branch -r
```

**Output típico:**
```bash
* main
  feature/login
  bugfix/validation
```

O asterisco (*) indica a branch atual.

### Criar Nova Branch

```bash
# Criar branch sem trocar para ela
git branch nome-da-branch

# Criar e trocar para a branch
git checkout -b nome-da-branch

# Ou (Git 2.23+)
git switch -c nome-da-branch
```

**Exemplo:**
```bash
# Criar branch para nova feature
git branch feature/autenticacao

# Criar branch a partir de outra branch
git checkout -b feature/autenticacao main
```

### Convenções de Nomenclatura

**Boas práticas para nomes de branches:**

✅ **Bom:**
```bash
feature/adicionar-login
bugfix/corrigir-validacao
hotfix/erro-critico
refactor/reorganizar-estrutura
docs/atualizar-readme
```

❌ **Ruim:**
```bash
nova-feature
teste
branch1
fix
```

**Padrões comuns:**
- `feature/nome`: Nova funcionalidade
- `bugfix/nome` ou `fix/nome`: Correção de bug
- `hotfix/nome`: Correção urgente
- `refactor/nome`: Refatoração
- `docs/nome`: Documentação
- `test/nome`: Testes

## Trocando Entre Branches

### Usando checkout (método tradicional)

```bash
# Trocar para branch existente
git checkout nome-da-branch

# Criar e trocar em um comando
git checkout -b nova-branch
```

### Usando switch (método moderno, Git 2.23+)

```bash
# Trocar para branch existente
git switch nome-da-branch

# Criar e trocar em um comando
git switch -c nova-branch

# Criar branch a partir de outra
git switch -c nova-branch branch-origem
```

**Por que usar `switch`?**
- Mais intuitivo e específico
- Não pode ser confundido com outros usos do `checkout`
- Comando mais moderno e recomendado

### Verificar Branch Atual

```bash
# Ver branch atual
git branch

# Ou
git status

# Ou ver nome apenas
git rev-parse --abbrev-ref HEAD
```

## Trabalhando em Branches

### Fluxo Básico

```bash
# 1. Criar ou trocar para branch de feature
git switch -c feature/minha-feature

# 2. Trabalhar normalmente (editar arquivos)
# ... fazer mudanças ...

# 3. Adicionar e commitar
git add .
git commit -m "feat: Implementa funcionalidade X"

# 4. Continuar trabalhando na branch
# ... mais mudanças ...

git add .
git commit -m "feat: Adiciona testes para funcionalidade X"
```

### Exemplo Prático

```bash
# Situação: Você está na branch main e quer adicionar login

# 1. Criar branch
git switch -c feature/login

# 2. Criar arquivo de autenticação
cat > auth.py << 'EOF'
def login(username, password):
    # Lógica de login
    return True
EOF

# 3. Adicionar e commitar
git add auth.py
git commit -m "feat: Implementa função de login"

# 4. Continuar desenvolvendo
# ... mais código ...

git add .
git commit -m "feat: Adiciona validação de credenciais"

# Agora você tem commits na branch feature/login
# A branch main permanece intacta!
```

## Comparando Branches

### Ver Diferenças Entre Branches

```bash
# Diferenças entre branch atual e outra branch
git diff branch-outra

# Diferenças entre duas branches específicas
git diff branch1 branch2

# Ver commits em uma branch que não estão na outra
git log branch1..branch2

# Ver commits que estão em branch2 mas não em branch1
git log branch1..branch2 --oneline
```

### Ver Quais Arquivos Diferem

```bash
# Listar arquivos diferentes entre branches
git diff --name-only branch1 branch2

# Ver estatísticas de diferenças
git diff --stat branch1 branch2
```

## Deletando Branches

### Deletar Branch Local

```bash
# Deletar branch (apenas se já foi mergeada)
git branch -d nome-branch

# Forçar deleção (mesmo sem merge)
git branch -D nome-branch
```

⚠️ **Importante**: Você não pode deletar a branch em que está atualmente!

### Deletar Branch Remota

```bash
# Deletar branch no repositório remoto
git push origin --delete nome-branch

# Ou (sintaxe alternativa)
git push origin :nome-branch
```

## Renomeando Branches

### Renomear Branch Local

```bash
# Renomear branch atual
git branch -m novo-nome

# Renomear outra branch
git branch -m nome-antigo novo-nome
```

### Renomear Branch Remota

```bash
# 1. Renomear localmente
git branch -m nome-antigo novo-nome

# 2. Deletar branch antiga no remoto
git push origin --delete nome-antigo

# 3. Enviar branch nova
git push origin novo-nome

# 4. Configurar upstream
git push -u origin novo-nome
```

## Situações Comuns

### Branch com Mudanças Não Commitadas

Se você tentar trocar de branch com mudanças não commitadas:

```bash
# Git vai avisar:
# error: Your local changes to the following files would be overwritten...
```

**Soluções:**

1. **Comitar as mudanças primeiro:**
```bash
git add .
git commit -m "WIP: Trabalho em progresso"
git switch outra-branch
```

2. **Guardar temporariamente (stash):**
```bash
git stash
git switch outra-branch
# ... trabalhar ...
git switch branch-anterior
git stash pop  # Restaurar mudanças
```

3. **Descartar mudanças** (se não precisa delas):
```bash
git restore .  # ou git checkout -- .
git switch outra-branch
```

### Criar Branch a Partir de Commit Específico

```bash
# Criar branch a partir de um commit
git switch -c nova-branch abc1234

# Criar branch a partir de outra branch em commit específico
git switch -c nova-branch branch-origem abc1234
```

### Ver Histórico de Uma Branch

```bash
# Histórico da branch atual
git log --oneline

# Histórico de branch específica
git log --oneline nome-branch

# Histórico com gráfico mostrando branches
git log --oneline --graph --all
```

## Exercício Prático

```bash
# 1. Criar projeto
mkdir exemplo-branches
cd exemplo-branches
git init

# 2. Commit inicial na main
echo "# Projeto" > README.md
git add README.md
git commit -m "docs: Adiciona README"

# 3. Criar branch feature
git switch -c feature/calculadora

# 4. Trabalhar na feature
cat > calc.py << 'EOF'
def somar(a, b):
    return a + b
EOF
git add calc.py
git commit -m "feat: Adiciona função somar"

# 5. Ver que estamos na branch feature
git branch
git log --oneline --graph

# 6. Voltar para main
git switch main

# 7. Ver que calc.py não existe aqui!
ls
git log --oneline

# 8. Voltar para feature
git switch feature/calculadora
ls  # calc.py existe aqui!
```

## Resumo dos Comandos

```bash
# Criar branches
git branch nome                    # Criar
git switch -c nome                 # Criar e trocar

# Trocar branches
git switch nome                    # Moderno
git checkout nome                  # Tradicional

# Listar branches
git branch                         # Locais
git branch -a                      # Todas

# Deletar branches
git branch -d nome                 # Seguro
git branch -D nome                 # Forçar

# Comparar branches
git diff branch1 branch2
git log branch1..branch2
```

## Próximos Passos

Agora você sabe:
- ✅ Criar e trocar entre branches
- ✅ Trabalhar em branches isoladas
- ✅ Comparar e gerenciar branches

No próximo arquivo, você aprenderá sobre **merge** e **resolução de conflitos**!
