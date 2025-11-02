# Fluxo Básico de Trabalho com Commits

## O Fluxo de Trabalho do Git

O Git trabalha com três áreas principais:

```
┌─────────────────┐    git add    ┌──────────────┐    git commit    ┌─────────────┐
│ Working         │ ────────────> │ Staging      │ ───────────────> │ Repository  │
│ Directory       │               │ Area         │                  │ (History)   │
│ (Working Tree)  │               │ (Index)      │                  │             │
└─────────────────┘               └──────────────┘                  └─────────────┘
     ↓                                   ↓                                  ↓
  Modificar                          Preparar                           Salvar
  arquivos                           mudanças                           histórico
```

### 1. Working Directory (Diretório de Trabalho)

- Onde você trabalha normalmente
- Arquivos que você edita e cria
- Estado: `modified` ou `untracked`

### 2. Staging Area (Área de Preparação)

- Também chamada de "Index"
- Área intermediária antes do commit
- Você decide o que vai no próximo commit
- Estado: `staged`

### 3. Repository (Repositório)

- Onde os commits são armazenados permanentemente
- Histórico completo do projeto
- Estado: `committed`

## Comandos do Fluxo Básico

### Verificar Status

```bash
git status
```

**Output típico:**
```bash
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   arquivo.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        novo_arquivo.py

no changes added to commit (use "git add" to commit)
```

### Ver Diferenças

Antes de adicionar ao staging, você pode ver o que mudou:

```bash
# Ver diferenças no working directory
git diff

# Ver diferenças de arquivo específico
git diff arquivo.py

# Ver diferenças no staging area
git diff --staged
# ou
git diff --cached
```

**Exemplo de output do git diff:**
```diff
diff --git a/arquivo.py b/arquivo.py
index 1234567..abcdefg 100644
--- a/arquivo.py
+++ b/arquivo.py
@@ -1,3 +1,5 @@
 def hello():
-    print("Hello")
+    print("Hello")
+    print("World")
     return True
```

### Adicionar ao Staging

```bash
# Arquivo específico
git add arquivo.py

# Todos os arquivos modificados
git add .

# Múltiplos arquivos
git add arquivo1.py arquivo2.py

# Todos arquivos de um tipo
git add *.py

# Todos arquivos de um diretório
git add src/

# Modo interativo (escolher partes do arquivo)
git add -p arquivo.py
```

**Após git add, o status muda:**
```bash
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   arquivo.py
        new file:   novo_arquivo.py
```

### Criar Commit

```bash
# Commit com mensagem inline (recomendado para mensagens curtas)
git commit -m "Adiciona função de cálculo"

# Commit abrindo editor para mensagem longa
git commit

# Commit adicionando e committando em um passo (pula staging)
git commit -am "Mensagem"
# ⚠️ Só funciona para arquivos já rastreados, não adiciona arquivos novos!
```

### Ver Histórico

```bash
# Histórico completo
git log

# Histórico compacto (uma linha por commit)
git log --oneline

# Histórico com gráfico visual
git log --oneline --graph

# Últimos N commits
git log -5

# Histórico com estatísticas
git log --stat

# Histórico mostrando diferenças
git log -p
```

## Padrão de Trabalho Diário

### Cenário 1: Adicionando Nova Funcionalidade

```bash
# 1. Verificar status inicial
git status

# 2. Criar/editar arquivos
# ... fazer seu trabalho ...

# 3. Ver o que mudou
git status
git diff

# 4. Adicionar arquivos relevantes
git add arquivos_modificados.py

# 5. Verificar o que será commitado
git status
git diff --staged

# 6. Fazer commit
git commit -m "Implementa nova funcionalidade X"

# 7. Verificar histórico
git log --oneline -3
```

### Cenário 2: Corrigindo Bug

```bash
# 1. Identificar e corrigir bug
# ... editar código para corrigir bug ...

# 2. Verificar mudanças
git diff arquivo_com_bug.py

# 3. Adicionar correção
git add arquivo_com_bug.py

# 4. Commit com mensagem descritiva
git commit -m "Corrige bug de validação de email"

# 5. Verificar
git show
```

### Cenário 3: Trabalho em Múltiplos Arquivos

```bash
# 1. Fazer mudanças em vários arquivos
# ... editar arquivo1.py, arquivo2.py, arquivo3.py ...

# 2. Ver status
git status

# 3. Adicionar arquivos relacionados à mesma mudança
git add arquivo1.py arquivo2.py
git commit -m "Atualiza sistema de autenticação"

# 4. Adicionar outro grupo de mudanças
git add arquivo3.py
git commit -m "Melhora tratamento de erros"
```

**Dica**: Faça commits separados para mudanças logicamente diferentes!

## Mensagens de Commit Eficazes

### Formato Recomendado

```
Tipo: Descrição curta (até 50 caracteres)

Corpo mais detalhado (se necessário), explicando:
- O que foi feito
- Por que foi feito
- Como foi feito (se relevante)

Pode incluir múltiplas linhas.
```

### Exemplos de Boas Mensagens

**✅ Bom:**
```bash
git commit -m "feat: Adiciona autenticação por JWT"
```

**✅ Melhor:**
```bash
git commit -m "feat: Adiciona autenticação por JWT

Implementa sistema de autenticação usando JSON Web Tokens.
- Gera token após login bem-sucedido
- Valida token em requisições protegidas
- Expira token após 24 horas"
```

**✅ Usando Conventional Commits:**
```bash
# Tipos comuns:
feat: Nova funcionalidade
fix: Correção de bug
docs: Documentação
style: Formatação (não afeta código)
refactor: Refatoração
test: Testes
chore: Manutenção

# Exemplos:
git commit -m "feat: Adiciona endpoint de listagem de usuários"
git commit -m "fix: Corrige validação de CPF"
git commit -m "docs: Atualiza README com instruções de instalação"
```

### Exemplos de Mensagens Ruins

**❌ Ruim:**
```bash
git commit -m "fix"
git commit -m "mudanças"
git commit -m "wip"  # work in progress
git commit -m "ajustes"
```

## Trabalhando com o Histórico

### Ver Detalhes de um Commit

```bash
# Último commit
git show

# Commit específico
git show abc1234

# Commit específico mostrando apenas arquivos
git show --name-only abc1234
```

### Comparar Commits

```bash
# Diferença entre dois commits
git diff commit1 commit2

# Diferença entre commit e working directory
git diff abc1234

# Diferença entre dois commits de arquivo específico
git diff commit1 commit2 -- arquivo.py
```

### Navegar no Histórico

```bash
# Ver commit anterior
git show HEAD~1

# Ver commit 3 commits atrás
git show HEAD~3

# Ver último commit de arquivo específico
git log -1 arquivo.py
```

## Fluxo Completo: Exemplo Prático

Vamos criar um exemplo prático completo:

```bash
# 1. Inicializar projeto
mkdir exemplo-fluxo
cd exemplo-fluxo
git init

# 2. Criar primeiro arquivo
echo "# Exemplo de Fluxo Git" > README.md
git add README.md
git commit -m "docs: Adiciona README inicial"

# 3. Criar código Python
cat > app.py << 'EOF'
def saudacao():
    print("Olá!")
EOF

git add app.py
git commit -m "feat: Adiciona função de saudação"

# 4. Modificar código
cat > app.py << 'EOF'
def saudacao(nome):
    print(f"Olá, {nome}!")

def despedida(nome):
    print(f"Tchau, {nome}!")
EOF

git add app.py
git commit -m "feat: Adiciona parâmetro nome e função despedida"

# 5. Ver histórico
git log --oneline --graph

# 6. Ver diferenças entre commits
git diff HEAD~2 HEAD
```

## Comandos Úteis do Fluxo

```bash
# Status resumido (uma linha por arquivo)
git status -s

# Ver apenas arquivos modificados
git diff --name-only

# Ver apenas arquivos no staging
git diff --staged --name-only

# Adicionar e commitar em um comando (arquivos rastreados)
git commit -am "Mensagem"

# Modificar último commit (adicionar arquivos esquecidos)
git add arquivo_esquecido.py
git commit --amend -m "Mensagem corrigida"

# Ver resumo de mudanças
git diff --stat
```

## Checklist do Fluxo Diário

Antes de cada commit, pergunte-se:

- [ ] Fiz `git status` para ver o estado?
- [ ] Revisei as mudanças com `git diff`?
- [ ] Adicionei apenas arquivos relacionados à mesma mudança?
- [ ] A mensagem de commit é clara e descritiva?
- [ ] O commit é atômico (uma mudança lógica)?
- [ ] Testei as mudanças antes de commitar?

## Resumo dos Comandos do Fluxo

```bash
# Verificar e inspecionar
git status              # Estado atual
git diff                # Mudanças não staged
git diff --staged       # Mudanças staged
git log                 # Histórico

# Adicionar ao staging
git add arquivo.py      # Arquivo específico
git add .               # Todos os arquivos

# Criar commit
git commit -m "msg"     # Commit com mensagem

# Ver histórico
git log --oneline       # Histórico compacto
git show                # Detalhes do último commit
```

## Próximos Passos

Agora você domina o fluxo básico:
- ✅ Entende os três estados do Git
- ✅ Sabe adicionar arquivos ao staging
- ✅ Sabe criar commits descritivos
- ✅ Sabe inspecionar histórico e mudanças

No próximo módulo, você aprenderá sobre **branches** e **trabalho colaborativo**!
