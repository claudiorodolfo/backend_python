"""
Exercícios Práticos - Fluxo de Trabalho com Branches e GitHub

Estes exercícios práticos devem ser realizados no terminal usando comandos Git.
Cada exercício tem instruções específicas. Siga os passos e execute os comandos Git necessários.

IMPORTANTE: 
- Execute estes exercícios em um diretório de prática separado
- Para exercícios que requerem GitHub, você precisará de uma conta
- Alguns exercícios podem ser feitos apenas localmente simulando o fluxo
"""

# ============================================================================
# EXERCÍCIO 1: Criando e Trabalhando com Branches
# ============================================================================

"""
Objetivo: Praticar criação, troca e trabalho em branches.

Tarefas:
1. Criar repositório: 'exercicio-branches'
2. Fazer commit inicial na main: "docs: Adiciona README"
3. Criar branch feature/calculadora
4. Na branch feature, criar arquivo calculadora.py com função somar()
5. Fazer commit: "feat: Adiciona função de soma"
6. Voltar para main e verificar que calculadora.py não existe
7. Voltar para feature/calculadora
8. Adicionar função subtrair()
9. Fazer commit: "feat: Adiciona função de subtração"
10. Ver histórico de ambas as branches

Comandos úteis:
- git switch -c feature/calculadora
- git switch main
- git branch
- git log --oneline --graph --all
"""

# ============================================================================
# EXERCÍCIO 2: Merge Simples (Fast-Forward)
# ============================================================================

"""
Objetivo: Praticar merge quando não há divergência.

Tarefas:
1. Continuando do exercício anterior
2. Estar na branch main
3. Fazer merge de feature/calculadora
4. Verificar que foi fast-forward (git log mostrará histórico linear)
5. Verificar que calculadora.py agora existe na main
6. Ver histórico: git log --oneline --graph
7. Deletar branch feature/calculadora (agora que foi mergeada)

Comandos úteis:
- git switch main
- git merge feature/calculadora
- git log --oneline --graph
- git branch -d feature/calculadora
"""

# ============================================================================
# EXERCÍCIO 3: Merge com Conflitos
# ============================================================================

"""
Objetivo: Praticar resolução de conflitos de merge.

Tarefas:
1. Criar novo repositório: 'exercicio-conflitos'
2. Commit inicial: arquivo app.py com função calcular() retornando 10
3. Criar branch feature/melhorias
4. Na feature, modificar calcular() para retornar 20
5. Commitar: "feat: Melhora lógica de cálculo"
6. Voltar para main
7. Modificar calcular() na main para retornar 15
8. Commitar: "feat: Atualiza cálculo"
9. Tentar fazer merge de feature/melhorias
10. Resolver conflito escolhendo uma versão (ou combinando)
11. Finalizar merge
12. Verificar resultado

Comandos úteis:
- git merge feature/melhorias
- git status (mostrará arquivos em conflito)
- Editar arquivo manualmente para resolver
- git add arquivo.py
- git commit
"""

# ============================================================================
# EXERCÍCIO 4: Múltiplas Branches
# ============================================================================

"""
Objetivo: Trabalhar com várias branches simultaneamente.

Tarefas:
1. Repositório: 'exercicio-multiplas-branches'
2. Main: criar app.py com classe App básica
3. Branch feature/auth: adicionar método login()
4. Branch feature/database: adicionar método connect_db()
5. Branch feature/api: adicionar método create_endpoint()
6. Fazer merge de feature/auth na main
7. Resolver conflitos se houver ao fazer merge de feature/database
8. Fazer merge de feature/api
9. Ver histórico final com todas as branches integradas

Comandos úteis:
- git switch -c feature/auth
- git switch -c feature/database
- git log --oneline --graph --all
"""

# ============================================================================
# EXERCÍCIO 5: Criando Repositório no GitHub (Requer Conta)
# ============================================================================

"""
Objetivo: Conectar repositório local com GitHub.

Tarefas:
1. Criar repositório no GitHub (via web)
   - Nome: 'meu-primeiro-repo-git'
   - Público ou privado (sua escolha)
   - NÃO criar README, .gitignore ou license
2. Criar repositório local com alguns arquivos
3. Adicionar remote origin
4. Fazer primeiro push
5. Verificar no GitHub que arquivos aparecem

Comandos úteis:
- git remote add origin https://github.com/usuario/repo.git
- git branch -M main
- git push -u origin main
- git remote -v (verificar)
"""

# ============================================================================
# EXERCÍCIO 6: Push e Pull
# ============================================================================

"""
Objetivo: Praticar enviar e buscar código do remoto.

Tarefas:
1. Continuando do exercício anterior (ou criar novo repo no GitHub)
2. Fazer mudança local: adicionar arquivo novo
3. Commitar e fazer push
4. Verificar no GitHub que mudança apareceu
5. Simular mudança remota:
   - Editar arquivo diretamente no GitHub (via web)
   - Fazer commit via interface web
6. Localmente, fazer pull
7. Verificar que mudança foi baixada
8. Ver histórico: git log --oneline --graph

Comandos úteis:
- git push origin main
- git pull origin main
- git fetch origin (apenas buscar, sem integrar)
- git log origin/main..main
"""

# ============================================================================
# EXERCÍCIO 7: Branches Remotas
# ============================================================================

"""
Objetivo: Trabalhar com branches no repositório remoto.

Tarefas:
1. Criar branch local: feature/nova-funcionalidade
2. Fazer alguns commits na branch
3. Fazer push da branch: git push -u origin feature/nova-funcionalidade
4. Verificar no GitHub que branch aparece
5. Ver branches remotas: git branch -r
6. Ver todas as branches: git branch -a
7. Simular que outra pessoa fez push na main (editar no GitHub)
8. Atualizar sua main local: git pull origin main
9. Atualizar sua feature com mudanças da main: git merge main (ou rebase)

Comandos úteis:
- git push -u origin feature/nome
- git branch -r
- git branch -a
- git fetch origin
- git merge origin/main
"""

# ============================================================================
# EXERCÍCIO 8: Clone de Repositório
# ============================================================================

"""
Objetivo: Praticar clonar repositórios existentes.

Tarefas:
1. Criar repositório no GitHub com alguns arquivos
2. Clonar para novo diretório local
3. Verificar que arquivos foram baixados
4. Ver remotes configurados: git remote -v
5. Fazer mudança e commit
6. Fazer push
7. Verificar no GitHub original

Comandos úteis:
- git clone https://github.com/usuario/repo.git
- git clone URL novo-diretorio
- git remote -v
"""

# ============================================================================
# EXERCÍCIO 9: Pull Request Simulado (Local)
# ============================================================================

"""
Objetivo: Simular workflow de Pull Request localmente.

Tarefas:
1. Repositório: 'exercicio-pr-simulado'
2. Criar branch main com código inicial
3. Criar branch feature/login
4. Desenvolver feature completa na branch
5. Fazer merge na main (simulando PR aprovado)
6. Verificar que merge foi bem-sucedido
7. Deletar branch de feature
8. Ver histórico final

Nota: Em ambiente real, isso seria feito via GitHub, mas aqui você pratica o fluxo.

Comandos úteis:
- git switch main
- git merge feature/login
- git log --oneline --graph
- git branch -d feature/login
"""

# ============================================================================
# EXERCÍCIO 10: Pull Request Real (Requer GitHub)
# ============================================================================

"""
Objetivo: Criar Pull Request real no GitHub.

Tarefas:
1. Criar repositório no GitHub: 'exercicio-pr'
2. Clonar localmente
3. Criar branch: feature/adicionar-docs
4. Adicionar arquivo DOCS.md com documentação
5. Commitar e fazer push
6. No GitHub, criar Pull Request:
   - Título: "docs: Adiciona documentação do projeto"
   - Descrição explicando mudanças
   - Comparar feature/adicionar-docs com main
7. Revisar PR (mesmo que seja você mesmo)
8. Fazer merge do PR via interface web
9. Localmente, atualizar main: git pull origin main
10. Deletar branch local: git branch -d feature/adicionar-docs

Comandos úteis:
- git clone URL
- git push -u origin feature/adicionar-docs
- git pull origin main (após merge)
"""

# ============================================================================
# EXERCÍCIO 11: Colaboração Simulada (Dois Diretórios)
# ============================================================================

"""
Objetivo: Simular trabalho de dois desenvolvedores.

Tarefas:
1. Criar repositório no GitHub (ou usar local como "remoto")
2. Clonar em dois diretórios diferentes:
   - desenvolvedor1/
   - desenvolvedor2/
3. Desenvolvedor 1:
   - Criar branch feature/login
   - Desenvolver funcionalidade
   - Push da branch
4. Desenvolvedor 2:
   - Criar branch feature/database
   - Desenvolver funcionalidade diferente
   - Push da branch
5. Desenvolvedor 1:
   - Fazer merge de sua feature na main
   - Push da main atualizada
6. Desenvolvedor 2:
   - Atualizar main local
   - Continuar trabalhando
   - Ver como colaboração funciona

Este exercício mostra como múltiplas pessoas podem trabalhar simultaneamente.
"""

# ============================================================================
# EXERCÍCIO 12: Resolução de Conflitos Complexos
# ============================================================================

"""
Objetivo: Praticar resolução de múltiplos conflitos.

Tarefas:
1. Repositório: 'exercicio-conflitos-complexos'
2. Main: criar arquivo config.py com várias configurações
3. Branch feature/ui: modificar várias linhas de config.py
4. Branch feature/api: modificar outras linhas do mesmo arquivo
5. Fazer merge de feature/ui na main
6. Fazer merge de feature/api na main (haverá conflitos)
7. Resolver conflitos manualmente:
   - Manter algumas mudanças de ui
   - Manter algumas mudanças de api
   - Combinar quando fizer sentido
8. Finalizar merge
9. Verificar que todas as mudanças necessárias estão presentes

Comandos úteis:
- git merge feature/ui
- git merge feature/api (terá conflitos)
- Editar arquivo para resolver
- git add config.py
- git commit
"""

# ============================================================================
# EXERCÍCIO 13: Workflow Completo de Feature
# ============================================================================

"""
Objetivo: Praticar workflow completo do início ao fim.

Tarefas:
1. Repositório no GitHub: 'exercicio-workflow-completo'
2. Clonar localmente
3. Atualizar main: git pull origin main
4. Criar branch: feature/sistema-notificacoes
5. Desenvolver feature completa:
   - Arquivo notificacoes.py com classe Notificacao
   - Método enviar_email()
   - Método enviar_sms()
   - Testes básicos
   - Documentação
6. Commits pequenos e frequentes:
   - "feat: Cria classe Notificacao"
   - "feat: Implementa envio de email"
   - "feat: Implementa envio de SMS"
   - "test: Adiciona testes básicos"
   - "docs: Adiciona documentação"
7. Push da branch
8. Criar PR no GitHub (se tiver conta) ou fazer merge local simulando
9. Após "aprovação", fazer merge
10. Atualizar localmente e deletar branch

Este exercício integra todos os conceitos aprendidos.
"""

# ============================================================================
# EXERCÍCIO 14: Gerenciamento de Branches
# ============================================================================

"""
Objetivo: Praticar gerenciamento avançado de branches.

Tarefas:
1. Criar repositório com várias branches:
   - main
   - feature/a
   - feature/b
   - bugfix/x
   - hotfix/y
2. Listar todas as branches
3. Ver diferenças entre branches
4. Ver commits que estão em uma branch mas não em outra
5. Renomear uma branch
6. Deletar branch que foi mergeada
7. Tentar deletar branch que não foi mergeada (usar -D)
8. Ver histórico gráfico de todas as branches

Comandos úteis:
- git branch -a
- git diff branch1 branch2
- git log branch1..branch2
- git branch -m novo-nome
- git branch -d nome (merged)
- git branch -D nome (forçar)
- git log --oneline --graph --all
"""

# ============================================================================
# EXERCÍCIO 15: Boas Práticas em Ação
# ============================================================================

"""
Objetivo: Aplicar todas as boas práticas aprendidas.

Tarefas:
Criar um pequeno projeto seguindo todas as boas práticas:

1. Projeto: Sistema de Biblioteca
2. Estrutura de commits seguindo Conventional Commits
3. Branches com nomes descritivos
4. Commits atômicos (uma mudança por commit)
5. Mensagens de commit claras e descritivas
6. Múltiplas features em branches separadas
7. Resolução adequada de conflitos
8. Histórico limpo e organizado
9. Se tiver GitHub: PRs bem descritos

Exemplo de estrutura:
- feat: Adiciona classe Livro
- feat: Implementa sistema de empréstimo
- fix: Corrige validação de data
- docs: Atualiza README
- test: Adiciona testes para empréstimo

Este exercício consolida todo o aprendizado!
"""

# ============================================================================
# DICAS GERAIS
# ============================================================================

"""
1. Sempre execute 'git status' frequentemente para entender estado atual

2. Use 'git log --oneline --graph --all' para visualizar histórico completo

3. Em conflitos, leia cuidadosamente ambas as versões antes de decidir

4. Commits pequenos e frequentes são melhor que commits grandes raros

5. Mantenha branches atualizadas com main regularmente

6. Use mensagens de commit descritivas seguindo padrões

7. Para exercícios com GitHub, você pode usar repositórios privados para prática

8. Não tenha medo de experimentar - você pode sempre criar novo repositório

9. Se algo der errado, você pode sempre voltar para estado anterior com git log

10. Pratique o fluxo completo várias vezes até se sentir confortável
"""

# ============================================================================
# CHECKLIST DE CONCLUSÃO
# ============================================================================

"""
Após completar os exercícios, você deve ser capaz de:

[ ] Criar e trocar entre branches facilmente
[ ] Fazer merge de branches sem conflitos
[ ] Resolver conflitos de merge manualmente
[ ] Trabalhar com repositórios remotos (GitHub)
[ ] Fazer push e pull de código
[ ] Criar e gerenciar Pull Requests
[ ] Colaborar efetivamente em equipe
[ ] Seguir boas práticas de commits e branches
[ ] Navegar pelo histórico complexo
[ ] Gerenciar múltiplas branches simultaneamente

Se conseguiu completar todos, você está pronto para workflows avançados!
"""
