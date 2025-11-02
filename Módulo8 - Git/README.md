# Módulo 8 - Git

Este módulo apresenta o Git, sistema de controle de versão distribuído essencial para o desenvolvimento de software profissional, especialmente no contexto de desenvolvimento backend.

## 📚 Sobre Este Módulo

Este módulo está em construção e abordará o Git desde conceitos fundamentais até funcionalidades avançadas, preparando você para trabalhar efetivamente com controle de versão em projetos de backend com Python.

## 🎯 Tópicos a Serem Abordados

### Fundamentos do Git
- **O que é Git**: Conceitos básicos de controle de versão
- **Por que usar Git**: Vantagens do controle de versão
- **Instalação**: Instalação e configuração inicial
- **Conceitos Fundamentais**: Repository, commit, branch, merge
- **Estados do Git**: Working directory, staging area, repository

### Comandos Básicos
- **git init**: Inicializar repositório
- **git clone**: Clonar repositório existente
- **git add**: Adicionar arquivos ao staging
- **git commit**: Criar commits
- **git status**: Verificar status dos arquivos
- **git log**: Visualizar histórico de commits
- **git diff**: Ver diferenças entre versões

### Trabalhando com Branches
- **git branch**: Criar e gerenciar branches
- **git checkout**: Alternar entre branches
- **git switch**: Nova forma de alternar branches
- **git merge**: Mesclar branches
- **Estratégias de Branching**: Git Flow, GitHub Flow, Trunk-based
- **Resolução de Conflitos**: Lidar com merge conflicts

### Trabalho Colaborativo
- **git remote**: Gerenciar repositórios remotos
- **git push**: Enviar commits para remoto
- **git pull**: Buscar e integrar mudanças remotas
- **git fetch**: Buscar mudanças sem integrar
- **Pull Requests**: Criar e revisar PRs
- **Code Reviews**: Processo de revisão de código

### Histórico e Busca
- **git log**: Opções avançadas de visualização
- **git show**: Detalhes de commits específicos
- **git grep**: Buscar no código
- **git blame**: Ver autoria de linhas
- **git bisect**: Busca binária de bugs

### Desfazendo Mudanças
- **git reset**: Desfazer commits (soft, mixed, hard)
- **git revert**: Criar commit que desfaz mudanças
- **git checkout**: Restaurar arquivos
- **git restore**: Nova forma de restaurar arquivos
- **git clean**: Limpar arquivos não rastreados

### Stashing e Trabalho Temporário
- **git stash**: Guardar mudanças temporariamente
- **git stash pop**: Restaurar mudanças guardadas
- **git stash list**: Listar stashes
- **Casos de uso**: Quando usar stash

### Tags e Releases
- **git tag**: Criar tags para versões
- **git tag -a**: Tags anotadas
- **Versionamento Semântico**: SemVer (Semantic Versioning)
- **Releases**: Criar releases no GitHub/GitLab

### Configuração Avançada
- **.gitignore**: Ignorar arquivos e pastas
- **git config**: Configurações do Git
- **Aliases**: Criar atalhos para comandos
- **Hooks**: Git hooks para automação
- **Git Attributes**: Atributos especiais de arquivos

### GitHub/GitLab/Bitbucket
- **Criando Repositórios**: No GitHub/GitLab
- **Fork e Clone**: Trabalhando com forks
- **Issues**: Sistema de issues
- **Projects**: Gerenciamento de projetos
- **Actions/CI/CD**: Integração contínua
- **Wikis e Documentação**: Documentar projetos

### Workflows Avançados
- **Rebase vs Merge**: Quando usar cada um
- **git rebase**: Reorganizar histórico
- **Interactive Rebase**: Editar histórico de commits
- **Cherry-pick**: Aplicar commits específicos
- **Submodules**: Trabalhar com submódulos
- **Subtrees**: Alternativa aos submódulos

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Usar Git para controle de versão em projetos
- Criar e gerenciar branches efetivamente
- Resolver conflitos de merge
- Colaborar em projetos usando Git
- Entender diferentes estratégias de branching
- Usar GitHub/GitLab para hospedagem de código
- Aplicar boas práticas de commit e mensagens
- Trabalhar com pull requests e code reviews
- Gerenciar histórico e desfazer mudanças
- Configurar Git para seu workflow

## 📋 Pré-requisitos

- Acesso a terminal/comando de linha
- Entendimento básico de sistema de arquivos
- Conhecimento básico de programação (Python)
- Conta no GitHub, GitLab ou Bitbucket (recomendado)

## 🔧 Configuração Inicial

### Instalação
```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt install git

# Windows
# Download de https://git-scm.com/download/win
```

### Configuração Básica
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
git config --global init.defaultBranch main
```

## 📖 Recursos de Referência

- [Documentação Oficial do Git](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/) - Livro completo gratuito
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Learn Git Branching](https://learngitbranching.js.org/) - Tutorial interativo
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## 🔐 Boas Práticas

### Commits
1. **Mensagens claras**: Use mensagens descritivas
2. **Commits atômicos**: Um commit por funcionalidade lógica
3. **Conventional Commits**: Padrão de mensagens (feat:, fix:, docs:, etc.)
4. **Frequência**: Commite frequentemente, com pequenos incrementos

### Branches
1. **Nomes descritivos**: Use nomes que indiquem propósito
2. **Branch principal limpo**: Mantenha main/master estável
3. **Delete branches**: Apague branches mescladas
4. **Proteção**: Proteja branch principal em produção

### Trabalho Colaborativo
1. **Pull antes de push**: Sempre faça pull antes de push
2. **Revisar mudanças**: Use `git diff` antes de commitar
3. **Comunicar**: Comunique mudanças grandes à equipe
4. **Code review**: Sempre revise código antes de merge

### Segurança
1. **.gitignore**: Nunca commite senhas ou tokens
2. **Chaves privadas**: Não commite chaves privadas
3. **Arquivos grandes**: Use Git LFS para arquivos grandes
4. **Histórico**: Cuidado ao reescrever histórico compartilhado

## 💡 Comandos Essenciais

### Fluxo Básico Diário
```bash
git status                    # Ver status
git add .                     # Adicionar mudanças
git commit -m "mensagem"     # Criar commit
git push                      # Enviar para remoto
git pull                      # Buscar mudanças
```

### Branches
```bash
git branch                    # Listar branches
git branch nova-feature       # Criar branch
git checkout nova-feature     # Alternar branch
git merge nova-feature        # Mesclar branch
```

### Informações
```bash
git log                       # Histórico
git log --oneline --graph     # Histórico compacto
git diff                      # Diferenças
git show                      # Detalhes do commit
```

## 🌟 Workflows Comuns

### Feature Branch Workflow
1. Criar branch da main: `git checkout -b feature/nova-funcionalidade`
2. Desenvolver e commitar
3. Push da branch: `git push origin feature/nova-funcionalidade`
4. Criar Pull Request
5. Após aprovação, merge e deletar branch

### Git Flow
- **main/master**: Código em produção
- **develop**: Código em desenvolvimento
- **feature/**: Novas funcionalidades
- **release/**: Preparação para release
- **hotfix/**: Correções urgentes

## ⚠️ Importante

Este módulo está em desenvolvimento. Conteúdo adicional será adicionado conforme o curso progride.

### Erros Comuns
- **Commits grandes demais**: Divida em commits menores
- **Mensagens vagas**: Seja específico sobre o que mudou
- **Merge sem pull**: Sempre atualize antes de merge
- **Reescrever histórico compartilhado**: Evite force push em branches compartilhadas
- **Esquecer .gitignore**: Configure antes do primeiro commit

### Dica Final
Git tem uma curva de aprendizado, mas é essencial para desenvolvimento profissional. Pratique regularmente e não tenha medo de experimentar comandos (em repositórios de teste). O Git é uma ferramenta poderosa que, quando dominada, aumenta significativamente sua produtividade.

