# Criando o Primeiro Repositório Local

## Inicializando um Repositório

Há duas formas principais de começar um repositório Git:

### 1. Inicializar Repositório Novo

Quando você quer versionar um projeto existente ou criar um novo:

```bash
# Navegar para o diretório do projeto
cd meu-projeto

# Inicializar repositório Git
git init
```

Isso cria uma pasta oculta `.git` que contém todo o histórico do Git.

### 2. Clonar Repositório Existente

Quando você quer trabalhar com um projeto que já está versionado:

```bash
# Clonar repositório remoto
git clone https://github.com/usuario/repositorio.git

# Ou com SSH
git clone git@github.com:usuario/repositorio.git
```

## Estrutura de um Repositório Git

Após `git init`, você verá:

```
meu-projeto/
├── .git/              # Diretório Git (histórico)
│   ├── HEAD           # Referência ao branch atual
│   ├── config         # Configurações do repositório
│   ├── objects/       # Objetos Git (commits, arquivos)
│   └── refs/          # Referências (branches, tags)
└── [seus arquivos]    # Seus arquivos do projeto
```

**⚠️ Importante**: Nunca edite manualmente arquivos dentro de `.git/`!

## Primeiro Repositório Passo a Passo

Vamos criar um repositório simples para aprender:

```bash
# 1. Criar diretório do projeto
mkdir primeiro-projeto-git
cd primeiro-projeto-git

# 2. Inicializar repositório Git
git init

# 3. Criar um arquivo
echo "# Meu Primeiro Projeto Git" > README.md

# 4. Verificar status
git status
# Você verá: README.md está "untracked"
```

## Verificando o Status

O comando `git status` mostra o estado atual do repositório:

```bash
git status
```

**Possíveis estados de arquivos:**

1. **Untracked** (não rastreado): Arquivo novo que o Git ainda não conhece
2. **Modified** (modificado): Arquivo que foi alterado
3. **Staged** (preparado): Arquivo adicionado ao staging area
4. **Unmodified**: Arquivo sem mudanças desde último commit

### Exemplo de Output:

```bash
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

## Adicionando Arquivos ao Staging

Antes de fazer commit, você precisa adicionar arquivos ao **staging area**:

```bash
# Adicionar arquivo específico
git add README.md

# Adicionar todos os arquivos modificados
git add .

# Adicionar todos os arquivos de um tipo
git add *.py

# Adicionar arquivo em diretório específico
git add src/main.py
```

### Verificar após git add:

```bash
git status
```

Agora você verá:
```bash
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

## Criando o Primeiro Commit

Um **commit** salva as mudanças no histórico do repositório:

```bash
# Commit com mensagem inline
git commit -m "Primeiro commit: adiciona README"

# Commit abrindo editor
git commit
```

### Boas Práticas para Mensagens de Commit

- **Seja descritivo**: Explique o que foi feito
- **Use imperativo**: "Adiciona README" e não "Adicionado README"
- **Seja específico**: "Corrige bug de login" e não "Fix bug"
- **Mantenha curto**: Primeira linha até 50 caracteres (ideal)
- **Adicione detalhes**: Se necessário, use corpo da mensagem

### Exemplo de Commit Bom:

```bash
git commit -m "Adiciona sistema de autenticação de usuários

- Implementa login com email e senha
- Adiciona validação de credenciais
- Cria sessão de usuário após login bem-sucedido"
```

### Verificar o Commit:

```bash
# Ver histórico
git log

# Ver histórico mais compacto
git log --oneline

# Ver detalhes do último commit
git show
```

## Fluxo Completo: Trabalho Diário

Agora que você tem um repositório, aqui está o fluxo básico:

```bash
# 1. Verificar status
git status

# 2. Fazer mudanças nos arquivos
# (editar arquivos normalmente)

# 3. Ver quais arquivos mudaram
git status
# ou ver diferenças
git diff

# 4. Adicionar ao staging
git add arquivo_modificado.py

# 5. Verificar novamente
git status

# 6. Fazer commit
git commit -m "Descrição clara das mudanças"

# 7. Ver histórico
git log --oneline
```

## Removendo Arquivos do Staging

Se você adicionou um arquivo por engano ao staging:

```bash
# Remover do staging (arquivo permanece no disco)
git reset HEAD arquivo.py

# Ou (versão mais nova do Git)
git restore --staged arquivo.py
```

## Descartando Mudanças (Cuidado!)

⚠️ **Atenção**: Estes comandos descartam mudanças permanentemente!

```bash
# Descartar mudanças em arquivo (que não foi commitado)
git restore arquivo.py

# Ou (versão antiga do Git)
git checkout -- arquivo.py
```

## Exemplo Prático Completo

Vamos criar um pequeno projeto Python versionado:

```bash
# 1. Criar estrutura do projeto
mkdir calculadora
cd calculadora
git init

# 2. Criar arquivos
cat > calculadora.py << 'EOF'
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

if __name__ == "__main__":
    print(somar(5, 3))
    print(subtrair(10, 4))
EOF

cat > README.md << 'EOF'
# Calculadora Simples

Uma calculadora básica com operações de soma e subtração.

## Uso

```python
python calculadora.py
```
EOF

# 3. Ver status
git status

# 4. Adicionar arquivos
git add .

# 5. Ver status novamente
git status

# 6. Fazer commit
git commit -m "Implementa calculadora básica com soma e subtração"

# 7. Ver histórico
git log --oneline
```

## Comandos Essenciais Resumidos

```bash
# Inicializar repositório
git init

# Ver status
git status

# Adicionar arquivos
git add arquivo.py
git add .

# Fazer commit
git commit -m "Mensagem descritiva"

# Ver histórico
git log
git log --oneline

# Ver diferenças
git diff

# Ver detalhes do último commit
git show
```

## Próximos Passos

Agora você sabe:
- ✅ Como criar um repositório
- ✅ Como adicionar arquivos ao staging
- ✅ Como fazer commits
- ✅ Como verificar status e histórico

No próximo arquivo, você aprenderá sobre o **fluxo básico de trabalho com commits** de forma mais detalhada!
