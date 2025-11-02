# Instalação e Configuração Inicial do Git

## Instalação do Git

### macOS

**Opção 1: Usando Homebrew (Recomendado)**
```bash
# Instalar Homebrew (se ainda não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Git
brew install git
```

**Opção 2: Download Direto**
- Acesse: https://git-scm.com/download/mac
- Baixe o instalador e siga as instruções

**Opção 3: Xcode Command Line Tools**
```bash
# Git já vem instalado com Xcode CLI Tools
xcode-select --install
```

### Linux (Ubuntu/Debian)

```bash
# Atualizar lista de pacotes
sudo apt update

# Instalar Git
sudo apt install git

# Verificar instalação
git --version
```

### Linux (CentOS/RHEL/Fedora)

```bash
# Fedora
sudo dnf install git

# CentOS/RHEL
sudo yum install git
```

### Windows

**Opção 1: Git para Windows (Recomendado)**
- Acesse: https://git-scm.com/download/win
- Baixe e execute o instalador
- **Importante**: Durante instalação, escolha "Git from the command line and also from 3rd-party software"

**Opção 2: GitHub Desktop**
- Inclui Git e interface gráfica
- Disponível em: https://desktop.github.com/

**Opção 3: Winget (Windows Package Manager)**
```bash
winget install Git.Git
```

### Verificar Instalação

Após instalar, verifique se está funcionando:

```bash
git --version
# Deve mostrar algo como: git version 2.39.0
```

## Configuração Inicial

### Configuração Global (Obrigatória)

Configure seu nome e email. Esta informação aparecerá em todos os seus commits.

```bash
# Configurar nome de usuário
git config --global user.name "Seu Nome Completo"

# Configurar email
git config --global user.email "seu.email@example.com"
```

**⚠️ Importante**: 
- Use o email associado à sua conta GitHub/GitLab (se for usar)
- O nome aparecerá nos commits - use algo profissional

### Outras Configurações Úteis

#### Configurar Branch Padrão

```bash
# Usar 'main' como nome padrão (mais moderno que 'master')
git config --global init.defaultBranch main
```

#### Configurar Editor Padrão

```bash
# VS Code
git config --global core.editor "code --wait"

# Nano (mais simples)
git config --global core.editor "nano"

# Vim
git config --global core.editor "vim"

# Para Windows (Notepad)
git config --global core.editor "notepad"
```

#### Configurações de Formatação

```bash
# Configurar quebra de linha (Windows: true, Unix: input)
# macOS/Linux
git config --global core.autocrlf input

# Windows
git config --global core.autocrlf true
```

#### Habilitar Cores

```bash
# Habilitar output colorido (já vem habilitado por padrão)
git config --global color.ui auto
```

#### Configurações de Alias (Opcional)

Criar atalhos para comandos comuns:

```bash
# Status mais curto
git config --global alias.st status

# Checkout mais curto
git config --global alias.co checkout

# Log mais bonito
git config --global alias.lg "log --oneline --graph --decorate --all"
```

Agora você pode usar `git st` ao invés de `git status`!

### Verificar Configurações

```bash
# Ver todas as configurações globais
git config --list --global

# Ver configuração específica
git config --global user.name
git config --global user.email
```

### Configurações por Repositório (Opcional)

Você pode sobrescrever configurações globais para um repositório específico:

```bash
# Dentro de um repositório específico
cd meu-projeto
git config user.name "Nome Diferente"
git config user.email "email.diferente@example.com"
```

## Configurações de Segurança

### .gitignore Global

Crie um arquivo `.gitignore` global para evitar commitar arquivos sensíveis:

```bash
# Criar diretório se não existir
mkdir -p ~/.config/git

# Criar arquivo .gitignore global
touch ~/.config/git/ignore

# Configurar Git para usar este arquivo
git config --global core.excludesfile ~/.config/git/ignore
```

Adicione ao arquivo `~/.config/git/ignore`:
```
# Arquivos sensíveis
*.env
*.key
*.pem
secrets/
*.log
.DS_Store
```

### SSH Keys (Para GitHub/GitLab)

Se você planeja usar SSH (recomendado):

```bash
# Gerar chave SSH (se ainda não tiver)
ssh-keygen -t ed25519 -C "seu.email@example.com"

# Verificar se o ssh-agent está rodando
eval "$(ssh-agent -s)"

# Adicionar chave ao ssh-agent
ssh-add ~/.ssh/id_ed25519

# Copiar chave pública para adicionar ao GitHub/GitLab
cat ~/.ssh/id_ed25519.pub
```

Depois, adicione a chave pública no GitHub/GitLab nas configurações SSH.

## Testando a Configuração

Crie um repositório de teste para verificar se tudo está funcionando:

```bash
# Criar diretório de teste
mkdir git-test
cd git-test

# Inicializar repositório
git init

# Criar arquivo de teste
echo "# Meu Primeiro Repositório" > README.md

# Adicionar ao staging
git add README.md

# Fazer commit
git commit -m "Primeiro commit: adiciona README"

# Ver histórico
git log

# Limpar (opcional)
cd ..
rm -rf git-test
```

## Resumo dos Comandos de Configuração

```bash
# Configuração básica obrigatória
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
git config --global init.defaultBranch main

# Configurações úteis
git config --global core.editor "code --wait"
git config --global color.ui auto

# Verificar configurações
git config --list --global
git --version
```

## Próximos Passos

Agora que o Git está instalado e configurado, você está pronto para:
1. Criar seu primeiro repositório local
2. Fazer seus primeiros commits
3. Entender o fluxo básico de trabalho

Continue com os próximos arquivos para aprender a usar Git na prática!
