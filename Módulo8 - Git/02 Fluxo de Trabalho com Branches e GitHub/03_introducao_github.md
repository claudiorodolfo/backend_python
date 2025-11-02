# Introdução ao GitHub e Repositórios Remotos

## O que é GitHub?

**GitHub** é uma plataforma de hospedagem de código baseada em Git. É como um "Google Drive" para código, mas muito mais poderoso.

### Principais Características

- **Hospedagem de repositórios**: Armazena seu código na nuvem
- **Colaboração**: Permite trabalhar com equipes
- **Pull Requests**: Sistema de revisão de código
- **Issues**: Rastreamento de bugs e features
- **GitHub Actions**: Automação e CI/CD
- **GitHub Pages**: Hospedagem de sites estáticos

### GitHub vs Git

- **Git**: Ferramenta de controle de versão (local)
- **GitHub**: Plataforma web que usa Git (remoto)
- **Outras alternativas**: GitLab, Bitbucket, Azure DevOps

## Criando Conta no GitHub

### Passo a Passo

1. Acesse: https://github.com
2. Clique em "Sign up"
3. Escolha plano gratuito (suficiente para começar)
4. Complete cadastro
5. Verifique email

### Recomendações Iniciais

- Adicione foto de perfil
- Configure nome de usuário (será parte da URL do seu repositório)
- Complete perfil básico

## Repositórios Remotos

### Conceito

Um **repositório remoto** é uma versão do seu projeto hospedada em um servidor (como GitHub). Permite:
- Backup do código
- Colaboração com outros desenvolvedores
- Acesso de qualquer lugar
- Histórico compartilhado

### Adicionar Remoto Local

Quando você cria um repositório no GitHub, precisa conectá-lo ao seu repositório local:

```bash
# Adicionar repositório remoto
git remote add origin https://github.com/usuario/repositorio.git

# Ou com SSH (recomendado, mais seguro)
git remote add origin git@github.com:usuario/repositorio.git
```

### Ver Remotos Configurados

```bash
# Listar remotos
git remote

# Listar remotos com URLs
git remote -v

# Ver detalhes de um remoto
git remote show origin
```

### Remover Remoto

```bash
git remote remove origin
```

### Alterar URL do Remoto

```bash
# Mudar URL do remoto
git remote set-url origin nova-url.git

# Verificar
git remote -v
```

## Criando Repositório no GitHub

### Via Interface Web

1. **Acesse GitHub** e clique no botão "+" (canto superior direito)
2. **Selecione "New repository"**
3. **Configure o repositório:**
   - Nome: `meu-projeto`
   - Descrição: (opcional)
   - Visibilidade: Public ou Private
   - **NÃO** marque "Add a README file" (se já tem repositório local)
   - **NÃO** adicione .gitignore ou license (se já tem)
4. **Clique em "Create repository"**
5. **Siga instruções** para conectar repositório local

### Via Interface: Conectar Repositório Local

GitHub mostra comandos após criar repositório:

```bash
# Se você JÁ TEM um repositório local
git remote add origin https://github.com/usuario/repositorio.git
git branch -M main
git push -u origin main

# Se você NÃO TEM repositório local ainda
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/usuario/repositorio.git
git push -u origin main
```

## Push: Enviando para o Remoto

### Primeiro Push

```bash
# Enviar branch main para remoto e configurar tracking
git push -u origin main

# -u (--set-upstream) configura relação entre branch local e remota
```

### Pushs Subsequentes

Após configurar upstream, você pode usar:

```bash
# Push simples (já sabe para onde enviar)
git push

# Ou especificar remoto e branch
git push origin main
```

### Push de Outras Branches

```bash
# Enviar branch específica
git push origin nome-da-branch

# Enviar e configurar upstream
git push -u origin nome-da-branch

# Enviar todas as branches
git push --all origin
```

### Push de Tags

```bash
# Enviar uma tag
git push origin v1.0.0

# Enviar todas as tags
git push --tags
```

## Pull: Buscando do Remoto

### Pull (Fetch + Merge)

```bash
# Buscar e integrar mudanças do remoto
git pull

# Ou especificar remoto e branch
git pull origin main
```

**O que `git pull` faz:**
1. `git fetch`: Busca mudanças do remoto
2. `git merge`: Integra mudanças automaticamente

### Fetch (Apenas Buscar)

```bash
# Buscar mudanças SEM integrar
git fetch origin

# Ver mudanças antes de integrar
git log HEAD..origin/main

# Integrar depois
git merge origin/main
```

**Por que usar `fetch`?**
- Ver mudanças antes de integrar
- Mais controle sobre quando fazer merge
- Evitar merges inesperados

## Clone: Baixar Repositório

### Clonar Repositório Existente

```bash
# Clonar via HTTPS
git clone https://github.com/usuario/repositorio.git

# Clonar via SSH (recomendado)
git clone git@github.com:usuario/repositorio.git

# Clonar para diretório específico
git clone https://github.com/usuario/repositorio.git meu-projeto

# Clonar branch específica
git clone -b nome-branch https://github.com/usuario/repositorio.git
```

### O que Clone Faz?

```bash
git clone URL
```

Isto:
1. Cria diretório com nome do repositório
2. Inicializa repositório Git
3. Baixa todo o histórico
4. Faz checkout da branch padrão
5. Configura `origin` como remoto

## HTTPS vs SSH

### HTTPS

**Vantagens:**
- Mais simples de configurar
- Funciona através de firewalls
- Não precisa gerar chaves

**Desvantagens:**
- Pede senha/token a cada push
- Menos seguro para scripts

**Uso:**
```bash
git remote add origin https://github.com/usuario/repo.git
```

### SSH

**Vantagens:**
- Mais seguro
- Não pede senha após configurado
- Melhor para automação

**Desvantagens:**
- Requer configuração de chaves
- Pode ter problemas em alguns firewalls

**Configuração:**
```bash
# 1. Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@example.com"

# 2. Adicionar ao ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 3. Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# 4. Adicionar no GitHub: Settings > SSH and GPG keys > New SSH key

# 5. Usar SSH
git remote add origin git@github.com:usuario/repo.git
```

## Personal Access Token (HTTPS)

Se usar HTTPS, GitHub requer token ao invés de senha:

1. **GitHub**: Settings > Developer settings > Personal access tokens > Tokens (classic)
2. **Generate new token**
3. **Escolher escopos**: `repo` (acesso completo a repositórios)
4. **Copiar token** (mostrado apenas uma vez!)
5. **Usar token como senha** ao fazer push/pull

## Exemplo Completo: Projeto Local → GitHub

```bash
# === 1. Criar projeto local ===
mkdir meu-projeto
cd meu-projeto
git init

# === 2. Criar arquivos ===
echo "# Meu Projeto" > README.md
cat > app.py << 'EOF'
def hello():
    print("Hello, World!")
EOF

# === 3. Primeiro commit local ===
git add .
git commit -m "docs: Adiciona README e app inicial"

# === 4. Criar repositório no GitHub (via web) ===
# Ir em github.com > New repository > criar "meu-projeto"

# === 5. Conectar local com remoto ===
git remote add origin https://github.com/seu-usuario/meu-projeto.git

# === 6. Renomear branch para main (se necessário) ===
git branch -M main

# === 7. Primeiro push ===
git push -u origin main

# === 8. Verificar no GitHub ===
# Acesse github.com/seu-usuario/meu-projeto
# Deve ver seus arquivos!
```

## Verificando Estado do Remoto

```bash
# Ver informações do remoto
git remote show origin

# Ver branches remotas
git branch -r

# Ver todas as branches (local + remota)
git branch -a

# Ver diferença entre local e remoto
git log origin/main..main  # Commits locais não enviados
git log main..origin/main  # Commits remotos não baixados
```

## Forçar Push (Cuidado!)

⚠️ **PERIGO**: Force push reescreve histórico no remoto!

```bash
# ⚠️ NUNCA force push na branch principal compartilhada!
git push --force origin nome-branch

# Ou versão mais segura (só força se não perder commits)
git push --force-with-lease origin nome-branch
```

**Quando usar:**
- Apenas em suas próprias branches
- Nunca em branches compartilhadas
- Após reescrever histórico local (rebase)

## Comandos Úteis

```bash
# Gerenciar remotos
git remote add origin URL
git remote -v
git remote remove origin

# Enviar código
git push -u origin main
git push

# Buscar código
git pull
git fetch
git fetch origin

# Clonar
git clone URL

# Verificar estado
git remote show origin
git branch -a
```

## Resumo

- **GitHub**: Plataforma de hospedagem de código
- **Remoto**: Repositório na nuvem (GitHub, GitLab, etc.)
- **Push**: Enviar código local → remoto
- **Pull**: Buscar código remoto → local
- **Clone**: Baixar repositório completo
- **HTTPS vs SSH**: Dois métodos de autenticação

## Próximos Passos

Agora você sabe:
- ✅ Criar repositórios no GitHub
- ✅ Conectar repositório local com remoto
- ✅ Enviar e buscar código

No próximo arquivo, você aprenderá sobre **Pull Requests** e **colaboração em equipe**!
