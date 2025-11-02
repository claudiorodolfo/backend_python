"""
Exercícios Práticos - Introdução ao Git e Controle de Versão

Estes exercícios práticos devem ser realizados no terminal usando comandos Git.
Cada exercício tem instruções específicas. Siga os passos e execute os comandos Git necessários.

IMPORTANTE: Execute estes exercícios em um diretório de prática separado do seu projeto principal.
"""

# ============================================================================
# EXERCÍCIO 1: Configuração Inicial e Verificação
# ============================================================================

"""
Objetivo: Verificar se o Git está instalado e configurado corretamente.

Tarefas:
1. Verificar versão do Git instalada
2. Verificar configurações globais (nome e email)
3. Se ainda não configurou, configurar nome e email

Comandos úteis:
- git --version
- git config --list --global
- git config --global user.name "Seu Nome"
- git config --global user.email "seu.email@example.com"
"""

# ============================================================================
# EXERCÍCIO 2: Criar Primeiro Repositório
# ============================================================================

"""
Objetivo: Criar seu primeiro repositório Git local.

Tarefas:
1. Criar um diretório chamado 'exercicio-git-01'
2. Entrar no diretório
3. Inicializar um repositório Git
4. Verificar que o repositório foi criado (ver pasta .git)

Comandos úteis:
- mkdir exercicio-git-01
- cd exercicio-git-01
- git init
- ls -la (para ver pasta .git no Linux/Mac)
"""

# ============================================================================
# EXERCÍCIO 3: Primeiro Commit
# ============================================================================

"""
Objetivo: Fazer seu primeiro commit.

Tarefas:
1. Criar um arquivo README.md com o conteúdo: "# Meu Primeiro Repositório Git"
2. Verificar o status do repositório
3. Adicionar o arquivo ao staging area
4. Verificar o status novamente
5. Criar um commit com a mensagem: "Primeiro commit: adiciona README"
6. Verificar o histórico de commits

Comandos úteis:
- echo "# Meu Primeiro Repositório Git" > README.md
- git status
- git add README.md
- git commit -m "Primeiro commit: adiciona README"
- git log
- git log --oneline
"""

# ============================================================================
# EXERCÍCIO 4: Trabalhando com Múltiplos Arquivos
# ============================================================================

"""
Objetivo: Praticar o fluxo completo com múltiplos arquivos.

Tarefas:
1. Criar arquivo calculadora.py com código Python simples:
   ```python
   def somar(a, b):
       return a + b
   
   if __name__ == "__main__":
       print(somar(2, 3))
   ```
2. Criar arquivo .gitignore com conteúdo: "*.pyc\n__pycache__/"
3. Ver status (deve mostrar 2 arquivos novos)
4. Adicionar apenas calculadora.py ao staging
5. Fazer commit: "feat: Adiciona função de soma"
6. Adicionar .gitignore
7. Fazer commit: "chore: Adiciona .gitignore"
8. Ver histórico completo

Comandos úteis:
- git status
- git add calculadora.py
- git commit -m "mensagem"
- git log --oneline --graph
"""

# ============================================================================
# EXERCÍCIO 5: Modificando e Comitando Mudanças
# ============================================================================

"""
Objetivo: Modificar arquivos existentes e fazer novos commits.

Tarefas:
1. Modificar calculadora.py para adicionar função subtrair:
   ```python
   def somar(a, b):
       return a + b
   
   def subtrair(a, b):
       return a - b
   
   if __name__ == "__main__":
       print(somar(2, 3))
       print(subtrair(5, 2))
   ```
2. Ver diferenças antes de adicionar (git diff)
3. Adicionar ao staging
4. Ver diferenças do staging (git diff --staged)
5. Fazer commit: "feat: Adiciona função de subtração"
6. Ver detalhes do último commit (git show)

Comandos úteis:
- git diff
- git diff --staged
- git add calculadora.py
- git commit -m "mensagem"
- git show
"""

# ============================================================================
# EXERCÍCIO 6: Inspecionando Histórico
# ============================================================================

"""
Objetivo: Aprender a navegar e inspecionar o histórico.

Tarefas:
1. Ver histórico completo (git log)
2. Ver histórico compacto (git log --oneline)
3. Ver histórico com estatísticas (git log --stat)
4. Ver detalhes do último commit (git show)
5. Ver detalhes do penúltimo commit (git show HEAD~1)
6. Ver diferença entre dois últimos commits (git diff HEAD~1 HEAD)

Comandos úteis:
- git log
- git log --oneline
- git log --stat
- git show
- git show HEAD~1
- git diff HEAD~1 HEAD
"""

# ============================================================================
# EXERCÍCIO 7: Removendo Arquivos do Staging
# ============================================================================

"""
Objetivo: Praticar adicionar e remover arquivos do staging.

Tarefas:
1. Criar arquivo teste.py com conteúdo: "print('teste')"
2. Adicionar teste.py ao staging
3. Verificar status (deve mostrar como staged)
4. Remover do staging usando: git restore --staged teste.py
   (ou git reset HEAD teste.py em versões antigas)
5. Verificar status novamente
6. Agora adicionar novamente e fazer commit

Comandos úteis:
- git add teste.py
- git status
- git restore --staged teste.py
- git reset HEAD teste.py  # versão antiga
"""

# ============================================================================
# EXERCÍCIO 8: Mensagens de Commit Descritivas
# ============================================================================

"""
Objetivo: Praticar escrever boas mensagens de commit.

Tarefas:
1. Adicionar função multiplicar ao calculadora.py
2. Fazer commit seguindo padrão Conventional Commits:
   "feat: Adiciona função de multiplicação"
3. Modificar README.md adicionando seção de uso
4. Fazer commit: "docs: Atualiza README com instruções de uso"
5. Corrigir um bug (ex: tratamento de divisão por zero)
6. Fazer commit: "fix: Adiciona validação para divisão por zero"
7. Ver histórico e verificar que mensagens estão claras

Comandos úteis:
- git commit -m "tipo: descrição"
- git log --oneline
"""

# ============================================================================
# EXERCÍCIO 9: Projeto Completo - Sistema de Notas
# ============================================================================

"""
Objetivo: Criar um pequeno projeto com múltiplos commits seguindo boas práticas.

Tarefas:
Criar um sistema simples de gerenciamento de notas de alunos:

1. Commit 1: "docs: Cria estrutura inicial do projeto"
   - Criar README.md básico

2. Commit 2: "feat: Implementa classe Aluno"
   - Criar aluno.py com classe Aluno básica

3. Commit 3: "feat: Adiciona método para adicionar notas"
   - Modificar aluno.py para adicionar notas

4. Commit 4: "feat: Implementa cálculo de média"
   - Adicionar método calcular_media()

5. Commit 5: "fix: Corrige cálculo de média com lista vazia"
   - Adicionar validação para evitar divisão por zero

6. Commit 6: "test: Adiciona testes básicos"
   - Criar test_aluno.py com testes simples

7. Ver histórico final e verificar que cada commit é atômico e descritivo

Comandos úteis:
- git log --oneline --graph
- git log --stat
"""

# ============================================================================
# EXERCÍCIO 10: Descartar Mudanças (Cuidado!)
# ============================================================================

"""
Objetivo: Entender como descartar mudanças não commitadas.

⚠️ ATENÇÃO: Este exercício mostra comandos destrutivos. 
Use apenas em arquivos de teste!

Tarefas:
1. Criar arquivo teste_descarte.py
2. Fazer commit: "chore: Adiciona arquivo de teste"
3. Modificar o arquivo
4. Ver diferenças (git diff)
5. Descartar mudanças com: git restore teste_descarte.py
   (ou git checkout -- teste_descarte.py em versões antigas)
6. Verificar que mudanças foram descartadas
7. Deletar arquivo (git rm teste_descarte.py)
8. Fazer commit: "chore: Remove arquivo de teste"

Comandos úteis:
- git diff
- git restore arquivo.py
- git checkout -- arquivo.py  # versão antiga
- git rm arquivo.py
- git status
"""

# ============================================================================
# DICAS GERAIS PARA OS EXERCÍCIOS
# ============================================================================

"""
1. Sempre execute 'git status' antes e depois de cada operação para entender 
   o estado atual.

2. Use 'git diff' frequentemente para ver o que mudou.

3. Faça commits pequenos e frequentes - cada commit deve representar uma 
   mudança lógica.

4. Use mensagens de commit descritivas seguindo padrões como Conventional Commits.

5. Use 'git log' para verificar seu progresso e entender o histórico.

6. Não tenha medo de experimentar - você pode sempre criar um novo diretório 
   e começar de novo se algo der errado.

7. Mantenha um diretório de prática separado para estes exercícios.
"""

# ============================================================================
# SOLUÇÃO PASSO A PASSO - EXERCÍCIO 9 (Exemplo)
# ============================================================================

"""
# 1. Criar diretório e inicializar
mkdir sistema-notas
cd sistema-notas
git init

# 2. Primeiro commit
echo "# Sistema de Gerenciamento de Notas" > README.md
git add README.md
git commit -m "docs: Cria estrutura inicial do projeto"

# 3. Segundo commit
cat > aluno.py << 'EOF'
class Aluno:
    def __init__(self, nome):
        self.nome = nome
EOF
git add aluno.py
git commit -m "feat: Implementa classe Aluno"

# 4. Terceiro commit
cat > aluno.py << 'EOF'
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
EOF
git add aluno.py
git commit -m "feat: Adiciona método para adicionar notas"

# Continue seguindo o padrão para os outros commits...
"""

# ============================================================================
# CHECKLIST DE CONCLUSÃO
# ============================================================================

"""
Após completar os exercícios, você deve ser capaz de:

[ ] Verificar instalação e configuração do Git
[ ] Criar um novo repositório local
[ ] Fazer commits com mensagens descritivas
[ ] Verificar status e diferenças
[ ] Adicionar e remover arquivos do staging
[ ] Navegar pelo histórico de commits
[ ] Descartar mudanças não commitadas
[ ] Trabalhar com múltiplos arquivos
[ ] Seguir boas práticas de commits
[ ] Entender o fluxo básico de trabalho com Git

Se conseguiu completar todos, você está pronto para o próximo módulo!
"""
