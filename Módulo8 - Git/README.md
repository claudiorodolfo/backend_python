# Módulo 8 - Git

Este módulo apresenta o Git, sistema de controle de versão distribuído essencial para o desenvolvimento de software profissional, especialmente no contexto de desenvolvimento backend. Git é a ferramenta padrão da indústria para gerenciamento de código e colaboração em equipe, e seu domínio é fundamental para qualquer desenvolvedor.

## 📚 Conteúdo do Módulo

Este módulo aborda o Git desde conceitos fundamentais até funcionalidades avançadas, preparando você para trabalhar efetivamente com controle de versão em projetos backend com Python. Você aprenderá não apenas comandos, mas também workflows profissionais e boas práticas da indústria.

### 1. Fundamentos do Git

Conceitos base necessários para entender e usar Git efetivamente.

**O que é Git**: Conceitos básicos de controle de versão
- Sistema de controle de versão distribuído
- Criado por Linus Torvalds em 2005
- Diferente de sistemas centralizados (SVN, CVS)
- Cada desenvolvedor tem cópia completa do histórico

**Por que usar Git**: Vantagens do controle de versão
- Histórico completo de mudanças
- Trabalho colaborativo eficiente
- Branches para desenvolvimento paralelo
- Backup automático do código
- Rastreabilidade de mudanças

**Instalação**: Instalação e configuração inicial
- Instalação em diferentes sistemas operacionais
- Configuração básica (nome, email)
- Configuração de editor padrão
- Verificação de instalação

**Conceitos Fundamentais**: Repository, commit, branch, merge
- **Repository (repositório)**: Diretório versionado por Git
- **Commit**: Snapshot das mudanças em um ponto no tempo
- **Branch**: Linha de desenvolvimento independente
- **Merge**: Combinação de branches
- **Remote**: Repositório remoto (GitHub, GitLab, etc.)

**Estados do Git**: Working directory, staging area, repository
- **Working Directory**: Arquivos no sistema de arquivos
- **Staging Area (Index)**: Área de preparação para commit
- **Repository**: Área onde commits são armazenados permanentemente
- Fluxo: Working → Staging → Repository

### 2. Comandos Básicos

Comandos fundamentais para uso diário do Git.

**git init**: Inicializar repositório
- Criar novo repositório Git
- Inicializar repositório existente
- Estrutura criada (.git directory)

**git clone**: Clonar repositório existente
- Baixar repositório remoto completo
- Clonar via HTTPS ou SSH
- Clonar branch específica

**git add**: Adicionar arquivos ao staging
- `git add arquivo.py`: Adicionar arquivo específico
- `git add .`: Adicionar todos os arquivos modificados
- `git add -p`: Adicionar partes de arquivo (interativo)

**git commit**: Criar commits
- `git commit -m "mensagem"`: Commit com mensagem
- `git commit`: Abrir editor para mensagem
- `git commit -a`: Adicionar e commitar (pula staging)
- `git commit --amend`: Modificar último commit

**git status**: Verificar status dos arquivos
- Ver arquivos modificados, staged, untracked
- Ver estado atual do working directory
- Informações sobre branches

**git log**: Visualizar histórico de commits
- `git log`: Histórico completo
- `git log --oneline`: Histórico compacto
- `git log --graph`: Visualizar branches
- `git log --all --graph --oneline --decorate`: Vista completa

**git diff**: Ver diferenças entre versões
- `git diff`: Diferenças no working directory
- `git diff --staged`: Diferenças no staging
- `git diff HEAD`: Diferenças desde último commit
- `git diff commit1 commit2`: Diferenças entre commits

### 3. Trabalhando com Branches

Gerenciamento de branches para desenvolvimento paralelo.

**git branch**: Criar e gerenciar branches
- `git branch`: Listar branches
- `git branch nome`: Criar nova branch
- `git branch -d nome`: Deletar branch (merged)
- `git branch -D nome`: Forçar deleção

**git checkout**: Alternar entre branches
- `git checkout branch`: Alternar para branch
- `git checkout -b nova`: Criar e alternar
- `git checkout arquivo`: Descartar mudanças em arquivo

**git switch**: Nova forma de alternar branches
- `git switch branch`: Alternar (Git 2.23+)
- `git switch -c nova`: Criar e alternar
- Mais intuitivo que `checkout`

**git merge**: Mesclar branches
- `git merge branch`: Mesclar branch no branch atual
- Merge commits vs fast-forward
- Resolução de conflitos

**Estratégias de Branching**: Git Flow, GitHub Flow, Trunk-based
- **Git Flow**: Desenvolvimento estruturado (feature, develop, release, main)
- **GitHub Flow**: Fluxo simples (feature branches → main)
- **Trunk-based**: Desenvolvimento direto na main
- Escolher estratégia baseado em projeto

**Resolução de Conflitos**: Lidar com merge conflicts
- Identificar arquivos com conflitos
- Marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`)
- Resolver conflitos manualmente
- Finalizar merge após resolução

### 4. Trabalho Colaborativo

Trabalhando com repositórios remotos e equipes.

**git remote**: Gerenciar repositórios remotos
- `git remote -v`: Listar remotes
- `git remote add origin url`: Adicionar remote
- `git remote remove nome`: Remover remote
- `git remote set-url`: Alterar URL

**git push**: Enviar commits para remoto
- `git push origin branch`: Enviar branch para remoto
- `git push -u origin branch`: Enviar e configurar upstream
- `git push --all`: Enviar todas as branches
- `git push --tags`: Enviar tags

**git pull**: Buscar e integrar mudanças remotas
- `git pull`: Buscar e merge automático
- `git pull origin branch`: Pull de branch específica
- Equivale a `git fetch` + `git merge`

**git fetch**: Buscar mudanças sem integrar
- `git fetch`: Buscar do remote sem merge
- `git fetch origin`: Buscar de remote específico
- `git fetch --all`: Buscar de todos os remotes
- Ver mudanças antes de integrar

**Pull Requests**: Criar e revisar PRs
- Criar PR no GitHub/GitLab
- Revisar código em PRs
- Discussões e comentários
- Merge via interface web

**Code Reviews**: Processo de revisão de código
- Revisar código de outros desenvolvedores
- Fornecer feedback construtivo
- Aprovar ou solicitar mudanças
- Boas práticas de code review

### 5. Histórico e Busca

Navegação e busca no histórico do Git.

**git log**: Opções avançadas de visualização
- `git log --oneline --graph --all`: Visualização completa
- `git log --author="nome"`: Filtrar por autor
- `git log --since="2 weeks ago"`: Filtrar por data
- `git log --grep="palavra"`: Buscar em mensagens
- `git log -p`: Mostrar diferenças
- `git log --follow arquivo`: Histórico de arquivo renomeado

**git show**: Detalhes de commits específicos
- `git show commit`: Detalhes do commit
- `git show commit:arquivo`: Versão de arquivo em commit
- `git show branch`: Último commit da branch

**git grep**: Buscar no código
- `git grep "texto"`: Buscar em todo repositório
- `git grep -n "texto"`: Com números de linha
- Busca em histórico e código atual

**git blame**: Ver autoria de linhas
- `git blame arquivo`: Ver quem modificou cada linha
- Útil para entender mudanças
- `git blame -L 10,20 arquivo`: Linhas específicas

**git bisect**: Busca binária de bugs
- Encontrar commit que introduziu bug
- Busca binária eficiente
- `git bisect start`, `git bisect good`, `git bisect bad`
- `git bisect reset`: Finalizar busca

### 6. Desfazendo Mudanças

Como desfazer mudanças de forma segura.

**git reset**: Desfazer commits (soft, mixed, hard)
- `git reset --soft HEAD~1`: Desfazer commit, manter mudanças staged
- `git reset --mixed HEAD~1`: Desfazer commit, manter mudanças unstaged (padrão)
- `git reset --hard HEAD~1`: Desfazer commit, descartar mudanças (cuidado!)
- `git reset commit`: Resetar para commit específico

**git revert**: Criar commit que desfaz mudanças
- `git revert commit`: Criar commit reverso
- Mais seguro que reset (preserva histórico)
- Útil para desfazer commits já enviados
- `git revert HEAD`: Reverter último commit

**git checkout**: Restaurar arquivos
- `git checkout -- arquivo`: Descartar mudanças em arquivo
- `git checkout branch -- arquivo`: Restaurar de outra branch
- Cuidado: pode perder mudanças não commitadas

**git restore**: Nova forma de restaurar arquivos
- `git restore arquivo`: Descartar mudanças (Git 2.23+)
- `git restore --staged arquivo`: Remover do staging
- Mais intuitivo que `checkout` para arquivos

**git clean**: Limpar arquivos não rastreados
- `git clean -n`: Dry run (mostrar o que será removido)
- `git clean -f`: Remover arquivos não rastreados
- `git clean -fd`: Incluir diretórios
- Cuidado: pode remover arquivos importantes

### 7. Stashing e Trabalho Temporário

Guardar mudanças temporariamente sem commit.

**git stash**: Guardar mudanças temporariamente
- `git stash`: Guardar mudanças atuais
- `git stash save "mensagem"`: Stash com mensagem
- `git stash -u`: Incluir arquivos untracked
- Útil para alternar branches com mudanças não commitadas

**git stash pop**: Restaurar mudanças guardadas
- `git stash pop`: Restaurar e remover stash mais recente
- `git stash pop stash@{n}`: Restaurar stash específico
- Aplica mudanças e remove do stash

**git stash list**: Listar stashes
- Ver todos os stashes guardados
- Identificar stash por índice

**git stash apply**: Aplicar sem remover
- `git stash apply`: Aplicar mudanças mas manter no stash
- Útil quando quer aplicar múltiplas vezes

**git stash drop**: Remover stash
- `git stash drop stash@{n}`: Remover stash específico
- `git stash clear`: Remover todos os stashes

**Casos de uso**: Quando usar stash
- Alternar branches com mudanças não commitadas
- Testar algo rapidamente
- Guardar trabalho em progresso
- Limpar working directory temporariamente

### 8. Tags e Releases

Marcação de versões e releases.

**git tag**: Criar tags para versões
- `git tag v1.0.0`: Criar tag leve
- `git tag -a v1.0.0 -m "mensagem"`: Tag anotada
- `git tag`: Listar todas as tags
- `git tag -d v1.0.0`: Deletar tag

**git tag -a**: Tags anotadas
- Tags com mensagem e metadados
- Recomendadas para releases
- Incluem autor, data, mensagem

**Versionamento Semântico**: SemVer (Semantic Versioning)
- Formato: MAJOR.MINOR.PATCH (ex: 2.1.3)
- MAJOR: Breaking changes
- MINOR: Novas funcionalidades (backward compatible)
- PATCH: Correções de bugs

**Releases**: Criar releases no GitHub/GitLab
- Criar release a partir de tag
- Notas de release (changelog)
- Binários e artefatos
- Distribuição de versões

### 9. Configuração Avançada

Personalização e configuração do Git.

**.gitignore**: Ignorar arquivos e pastas
- Padrões para arquivos a ignorar
- `*.pyc`, `__pycache__/`, `.env`, etc.
- Exemplos comuns para Python
- Gitignore global vs local

**git config**: Configurações do Git
- `git config --global user.name`: Configuração global
- `git config --global user.email`: Email global
- `git config --list`: Listar todas as configurações
- `git config --global core.editor`: Editor padrão

**Aliases**: Criar atalhos para comandos
- `git config --global alias.st status`
- `git config --global alias.co checkout`
- `git config --global alias.br branch`
- Personalizar workflow

**Hooks**: Git hooks para automação
- Hooks pre-commit, post-commit, pre-push
- Scripts em `.git/hooks/`
- Automação de tarefas (linting, testes)
- Exemplos práticos

**Git Attributes**: Atributos especiais de arquivos
- Configurar tratamento de arquivos
- Line endings (CRLF vs LF)
- Filtros e merge strategies
- `*.py linguist-detectable=false`

### 10. GitHub/GitLab/Bitbucket

Plataformas de hospedagem de código.

**Criando Repositórios**: No GitHub/GitLab
- Criar repositório novo
- Configurar descrição e README
- Escolher visibilidade (público/privado)
- Configurações iniciais

**Fork e Clone**: Trabalhando com forks
- Fork de repositórios de outros
- Clone de fork próprio
- Manter fork atualizado
- Contribuir para projetos open source

**Issues**: Sistema de issues
- Criar issues para bugs e features
- Labels e milestones
- Atribuir issues a desenvolvedores
- Fechar issues via commits

**Projects**: Gerenciamento de projetos
- Kanban boards
- Organização de tarefas
- Integração com issues e PRs

**Actions/CI/CD**: Integração contínua
- GitHub Actions para automação
- CI/CD pipelines
- Testes automatizados
- Deploy automático

**Wikis e Documentação**: Documentar projetos
- Wikis para documentação
- README.md e CONTRIBUTING.md
- GitHub Pages para sites de documentação

### 11. Workflows Avançados

Fluxos de trabalho avançados e otimização.

**Rebase vs Merge**: Quando usar cada um
- Merge: Preserva histórico completo
- Rebase: Histórico linear e limpo
- Trade-offs de cada abordagem
- Quando usar cada um

**git rebase**: Reorganizar histórico
- `git rebase branch`: Reaplicar commits sobre outra branch
- `git rebase -i`: Rebase interativo
- Reorganizar, editar, combinar commits
- Manter histórico limpo

**Interactive Rebase**: Editar histórico de commits
- `git rebase -i HEAD~n`: Editar últimos n commits
- Reordenar commits
- Editar mensagens
- Combinar commits (squash)
- Remover commits

**Cherry-pick**: Aplicar commits específicos
- `git cherry-pick commit`: Aplicar commit de outra branch
- Útil para portar correções de bugs
- Aplicar commits específicos sem merge completo

**Submodules**: Trabalhar com submódulos
- Repositórios dentro de repositórios
- Gerenciar dependências de código
- `git submodule add`, `git submodule update`
- Workflow com submódulos

**Subtrees**: Alternativa aos submódulos
- Incluir projeto como subdiretório
- Mais simples que submódulos
- Merges bidirecionais mais fáceis

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Usar Git para controle de versão em projetos Python
- Criar e gerenciar branches efetivamente para desenvolvimento paralelo
- Resolver conflitos de merge de forma confiável
- Colaborar em projetos usando Git e plataformas como GitHub/GitLab
- Entender e aplicar diferentes estratégias de branching (Git Flow, GitHub Flow)
- Usar GitHub/GitLab para hospedagem de código e colaboração
- Aplicar boas práticas de commit e mensagens descritivas
- Trabalhar com pull requests e code reviews
- Gerenciar histórico e desfazer mudanças de forma segura
- Configurar Git para seu workflow pessoal
- Usar recursos avançados como rebase, cherry-pick e hooks
- Contribuir para projetos open source

## 📋 Pré-requisitos

- Acesso a terminal/comando de linha
  - Terminal no macOS/Linux
  - Git Bash ou PowerShell no Windows
  - Conforto com linha de comando básica
- Entendimento básico de sistema de arquivos
  - Navegação de diretórios
  - Conceito de arquivos e pastas
- Conhecimento básico de programação (Python)
  - Para entender contexto de uso
  - Não precisa ser avançado
- Conta no GitHub, GitLab ou Bitbucket (recomendado)
  - Para prática de trabalho colaborativo
  - Gratuito para contas pessoais

## 🔧 Configuração Inicial

### Instalação

**macOS:**
```bash
# Com Homebrew
brew install git

# Ou download de https://git-scm.com/download/mac
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install git
```

**Windows:**
- Download de https://git-scm.com/download/win
- Instalador inclui Git Bash

### Configuração Básica

```bash
# Configurar nome e email (obrigatório)
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"

# Configurar branch padrão
git config --global init.defaultBranch main

# Configurar editor (opcional)
git config --global core.editor "code --wait"  # VS Code
# ou
git config --global core.editor "nano"  # Nano
# ou
git config --global core.editor "vim"   # Vim

# Verificar configuração
git config --list
```

## 📖 Recursos de Referência

### Documentação Oficial
- [Documentação Oficial do Git](https://git-scm.com/doc) - Referência completa
- [Pro Git Book](https://git-scm.com/book/) - Livro completo gratuito online
- [Git Reference](https://git-scm.com/docs) - Referência de comandos

### Tutoriais Interativos
- [Learn Git Branching](https://learngitbranching.js.org/) - Tutorial visual interativo
- [GitHub Learning Lab](https://lab.github.com/) - Tutoriais práticos do GitHub
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Tutoriais detalhados

### Guias e Cheat Sheets
- [GitHub Guides](https://guides.github.com/) - Guias do GitHub
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) - Referência rápida
- [GitHub Flow](https://guides.github.com/introduction/flow/) - Guia do GitHub Flow

## 🔐 Boas Práticas

### Commits
1. **Mensagens claras**: Use mensagens descritivas que expliquem o "porquê"
2. **Commits atômicos**: Um commit por funcionalidade lógica
3. **Conventional Commits**: Padrão de mensagens (feat:, fix:, docs:, etc.)
4. **Frequência**: Commite frequentemente, com pequenos incrementos
5. **Evite commits grandes**: Divida em commits menores e lógicos

### Branches
1. **Nomes descritivos**: Use nomes que indiquem propósito (feature/nova-api, fix/bug-login)
2. **Branch principal limpa**: Mantenha main/master estável
3. **Delete branches**: Apague branches mescladas
4. **Proteção**: Proteja branch principal em produção
5. **Nomenclatura consistente**: Use convenções da equipe

### Trabalho Colaborativo
1. **Pull antes de push**: Sempre faça pull antes de push
2. **Revisar mudanças**: Use `git diff` antes de commitar
3. **Comunicar**: Comunique mudanças grandes à equipe
4. **Code review**: Sempre revise código antes de merge
5. **Rebase local**: Rebasse commits locais antes de push

### Segurança
1. **.gitignore**: Nunca commite senhas, tokens ou arquivos sensíveis
2. **Chaves privadas**: Não commite chaves privadas
3. **Arquivos grandes**: Use Git LFS para arquivos grandes
4. **Histórico**: Cuidado ao reescrever histórico compartilhado
5. **Secrets scanning**: Use ferramentas para detectar secrets

## 💡 Comandos Essenciais

### Fluxo Básico Diário
```bash
# Ver status
git status

# Adicionar mudanças
git add .
# ou
git add arquivo.py

# Criar commit
git commit -m "Descrição clara do que mudou"

# Enviar para remoto
git push

# Buscar mudanças
git pull
```

### Branches
```bash
# Listar branches
git branch

# Criar branch
git branch nova-feature

# Alternar branch
git checkout nova-feature
# ou (Git 2.23+)
git switch nova-feature

# Criar e alternar
git checkout -b nova-feature
# ou
git switch -c nova-feature

# Mesclar branch
git merge nova-feature

# Deletar branch
git branch -d nova-feature
```

### Informações
```bash
# Histórico completo
git log

# Histórico compacto com gráfico
git log --oneline --graph --all

# Ver diferenças
git diff

# Detalhes do commit
git show
```

## 🌟 Workflows Comuns

### Feature Branch Workflow
1. Criar branch da main: `git checkout -b feature/nova-funcionalidade`
2. Desenvolver e commitar
3. Push da branch: `git push origin feature/nova-funcionalidade`
4. Criar Pull Request no GitHub/GitLab
5. Após aprovação, merge e deletar branch

### Git Flow
- **main/master**: Código em produção
- **develop**: Código em desenvolvimento
- **feature/**: Novas funcionalidades
- **release/**: Preparação para release
- **hotfix/**: Correções urgentes em produção

### Trunk-Based Development
- Desenvolvimento direto na main
- Branches muito curtas (horas/dias)
- Merge frequente na main
- Ideal para equipes pequenas e CI/CD robusto

## ⚠️ Importante

### Erros Comuns
- **Commits grandes demais**: Divida em commits menores e lógicos
- **Mensagens vagas**: Seja específico sobre o que mudou e porquê
- **Merge sem pull**: Sempre atualize antes de merge
- **Reescrever histórico compartilhado**: Evite force push em branches compartilhadas
- **Esquecer .gitignore**: Configure antes do primeiro commit
- **Commite arquivos sensíveis**: Use .gitignore e verifique antes de commitar

### Force Push
- **Nunca force push na main/master**
- Use apenas em branches próprias não compartilhadas
- Force push pode perder trabalho de outros desenvolvedores
- Sempre comunique antes de force push

### Backup
- Git é backup distribuído (cada clone é backup)
- Mas faça backup regular de repositórios importantes
- Use remotes múltiplos quando crítico
- GitHub/GitLab fornecem backup automático

## 🏆 Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Conseguir criar e gerenciar repositórios Git
- [ ] Ser capaz de fazer commits com mensagens descritivas
- [ ] Trabalhar com branches (criar, alternar, mesclar)
- [ ] Resolver conflitos de merge
- [ ] Usar GitHub/GitLab para hospedagem de código
- [ ] Criar e revisar Pull Requests
- [ ] Entender diferença entre merge e rebase
- [ ] Configurar .gitignore adequadamente
- [ ] Trabalhar com repositórios remotos (push, pull, fetch)
- [ ] Usar comandos avançados quando necessário

## 💻 Prática Recomendada

### Exercícios Práticos
1. Criar repositório local e fazer commits
2. Criar branches e praticar merge
3. Simular conflitos e resolvê-los
4. Trabalhar com repositório remoto (GitHub)
5. Criar Pull Request e fazer code review
6. Usar rebase interativo para limpar histórico
7. Configurar hooks e aliases

### Projetos Sugeridos
- Versionar projeto Python pessoal
- Contribuir para projeto open source
- Trabalhar em projeto colaborativo
- Praticar diferentes workflows

## 🎓 Estrutura Pedagógica

Este módulo segue uma abordagem prática:
1. **Conceitos primeiro**: Entenda o que Git faz antes de comandos
2. **Comandos básicos**: Domine fluxo diário
3. **Branches e colaboração**: Trabalho em equipe
4. **Avançado**: Recursos para otimizar workflow
5. **Prática contínua**: Use Git em todos os projetos

## 💡 Dica Final

Git tem uma curva de aprendizado, mas é essencial para desenvolvimento profissional. Pratique regularmente e não tenha medo de experimentar comandos (em repositórios de teste). O Git é uma ferramenta poderosa que, quando dominada, aumenta significativamente sua produtividade e permite colaboração efetiva em equipe.

**Lembre-se**: Git é melhor aprendido fazendo. Use em todos os seus projetos, mesmo os pequenos, para desenvolver fluência.

Este módulo está em desenvolvimento. Conteúdo adicional será adicionado conforme o curso progride, incluindo exercícios práticos guiados, simulações de workflows reais e exemplos avançados de uso do Git.
