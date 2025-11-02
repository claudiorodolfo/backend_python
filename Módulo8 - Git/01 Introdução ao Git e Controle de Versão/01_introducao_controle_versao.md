# Introdução ao Controle de Versão e Git

## O que é Controle de Versão?

**Controle de versão** é um sistema que registra mudanças em arquivos ao longo do tempo, permitindo que você recupere versões específicas quando necessário. É como um "save game" do seu código, mas muito mais poderoso.

### Por que o Controle de Versão é Importante?

1. **Histórico Completo**: Veja todas as mudanças feitas no código e quando foram feitas
2. **Rastreabilidade**: Saiba quem fez cada mudança e por quê
3. **Backup Automático**: Seu código está sempre salvo
4. **Colaboração**: Múltiplas pessoas podem trabalhar no mesmo projeto sem conflitos
5. **Experimentação Segura**: Teste ideias sem medo de perder trabalho
6. **Reverter Mudanças**: Volte a versões anteriores se algo der errado

### Tipos de Sistemas de Controle de Versão

**1. Controle de Versão Local**
- Mantém um banco de dados de mudanças localmente
- Exemplo: RCS (Revision Control System)
- Limitação: Não suporta colaboração em equipe

**2. Controle de Versão Centralizado**
- Um servidor central contém todas as versões
- Clientes fazem check-out do código do servidor
- Exemplos: CVS, Subversion (SVN), Perforce
- Limitação: Servidor é ponto único de falha

**3. Controle de Versão Distribuído**
- Cada desenvolvedor tem uma cópia completa do repositório
- Trabalho pode ser feito offline
- Exemplos: Git, Mercurial, Bazaar
- Vantagem: Mais robusto e flexível

## O que é Git?

**Git** é um sistema de controle de versão distribuído criado por Linus Torvalds em 2005 para gerenciar o desenvolvimento do Linux.

### Características Principais do Git

- **Distribuído**: Cada clone é um backup completo
- **Rápido**: Operações locais são instantâneas
- **Flexível**: Suporta diversos workflows
- **Poderoso**: Ferramentas avançadas de manipulação de histórico
- **Livre e Open Source**: Gratuito e de código aberto

## Conceitos Fundamentais

### 1. Repositório (Repository)

Um **repositório** é um diretório que contém seu projeto e todo o histórico de versões. Pode ser:
- **Local**: No seu computador
- **Remoto**: Em um servidor (GitHub, GitLab, etc.)

### 2. Commit

Um **commit** é uma "fotografia" do estado dos seus arquivos em um momento específico. Contém:
- Snapshot dos arquivos
- Mensagem descritiva
- Autor e data
- Hash único (identificador)

**Analogia**: Como um checkpoint em um jogo - você pode voltar a ele a qualquer momento.

### 3. Branch (Ramificação)

Uma **branch** é uma linha independente de desenvolvimento. Permite:
- Trabalhar em funcionalidades sem afetar o código principal
- Experimentar sem risco
- Desenvolver em paralelo

**Analogia**: Como uma linha do tempo alternativa - você pode criar uma versão alternativa do futuro.

### 4. Merge (Mesclagem)

**Merge** é o processo de combinar mudanças de diferentes branches ou commits.

**Analogia**: Juntar duas estradas em uma só.

## Estados dos Arquivos no Git

Os arquivos no Git podem estar em três estados:

### 1. Working Directory (Diretório de Trabalho)

Arquivos modificados que ainda não foram preparados para commit.

```bash
# Arquivo modificado mas não adicionado
Arquivo: exemplo.py (modificado)
```

### 2. Staging Area (Área de Preparação)

Arquivos que foram adicionados e estão prontos para serem commitados.

```bash
# Arquivo adicionado ao staging
git add exemplo.py
# Arquivo agora está "staged"
```

### 3. Repository (Repositório)

Arquivos que foram commitados e fazem parte do histórico permanente.

```bash
# Arquivo commitado
git commit -m "Adiciona exemplo.py"
# Arquivo agora está no repositório
```

## Fluxo de Trabalho Básico

```
Working Directory → git add → Staging Area → git commit → Repository
     (modificado)              (preparado)              (salvo)
```

### Passos do Fluxo:

1. **Modificar arquivos** no working directory
2. **Adicionar ao staging** com `git add`
3. **Criar commit** com `git commit`
4. **Enviar para remoto** (opcional) com `git push`

## Resumo

- **Controle de Versão**: Sistema que gerencia mudanças em arquivos
- **Git**: Sistema de controle de versão distribuído
- **Repositório**: Diretório versionado com histórico completo
- **Commit**: Snapshot das mudanças em um momento específico
- **Branch**: Linha independente de desenvolvimento
- **Merge**: Combinação de mudanças de diferentes branches

Estes são os conceitos fundamentais que você precisa entender antes de começar a usar Git na prática!
