# Merge e Resolução de Conflitos

## O que é Merge?

**Merge** (mesclagem) é o processo de combinar mudanças de diferentes branches ou commits em uma única branch. É como juntar duas estradas em uma só.

### Por que Fazer Merge?

- Integrar trabalho de uma branch de feature na branch principal
- Combinar mudanças de diferentes desenvolvedores
- Atualizar sua branch com mudanças da branch principal
- Mesclar branches de diferentes features

## Tipos de Merge

### 1. Fast-Forward Merge

Ocorre quando a branch de destino não teve novas mudanças desde que a branch de origem foi criada.

```
Antes:
main:  A---B
           \
feature:    C---D

Depois (fast-forward):
main:  A---B---C---D
```

**Como funciona:**
- Git simplesmente move o ponteiro da branch principal para frente
- Não cria commit de merge
- Histórico linear e limpo

```bash
# Exemplo de fast-forward
git switch main
git merge feature/login
# Output: Fast-forward
```

### 2. Merge Commit (Three-Way Merge)

Ocorre quando ambas as branches tiveram mudanças independentes.

```
Antes:
main:    A---B---E
             \
feature:      C---D

Depois (merge commit):
main:    A---B---E---M
             \     /
feature:      C---D
```

**Como funciona:**
- Git cria um commit especial de merge
- Combina automaticamente mudanças em arquivos diferentes
- Pode haver conflitos se o mesmo arquivo foi modificado em ambos os lados

```bash
# Exemplo de merge commit
git switch main
git merge feature/login
# Output: Merge made by the 'recursive' strategy.
```

## Fazendo Merge

### Merge Básico

```bash
# 1. Garantir que está na branch de destino (geralmente main)
git switch main

# 2. Atualizar a branch de destino (boas práticas)
git pull origin main

# 3. Fazer merge da branch de origem
git merge nome-da-branch

# 4. Se tudo correu bem, fazer push
git push origin main
```

### Exemplo Completo

```bash
# Situação: Terminaram o trabalho em feature/login e querem integrar

# 1. Trocar para main
git switch main

# 2. Atualizar main
git pull origin main

# 3. Fazer merge
git merge feature/login

# 4. Ver resultado
git log --oneline --graph

# 5. Enviar para remoto
git push origin main

# 6. Deletar branch de feature (opcional, após merge bem-sucedido)
git branch -d feature/login
```

## Conflitos de Merge

### O que são Conflitos?

Conflitos ocorrem quando:
- O mesmo arquivo foi modificado em ambas as branches
- As mudanças estão nas mesmas linhas ou próximas
- Git não consegue decidir automaticamente qual versão usar

### Como Identificar Conflitos

Ao fazer merge, Git pode mostrar:

```bash
Auto-merging arquivo.py
CONFLICT (content): Merge conflict in arquivo.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Marcadores de Conflito

Arquivos com conflitos têm marcadores especiais:

```python
<<<<<<< HEAD
# Código da branch atual (main)
def calcular():
    return 2 + 2
=======
# Código da branch sendo mergeada (feature)
def calcular():
    return 3 + 3
>>>>>>> feature/nova-logica
```

**Entendendo os marcadores:**
- `<<<<<<< HEAD`: Início do código da branch atual
- `=======`: Separador entre as duas versões
- `>>>>>>> feature/nova-logica`: Fim do código da branch sendo mergeada

## Resolvendo Conflitos

### Passo a Passo

```bash
# 1. Identificar arquivos com conflito
git status
# Mostra arquivos com "both modified"

# 2. Abrir arquivo e localizar marcadores de conflito
# Editar arquivo removendo marcadores e escolhendo código correto

# 3. Adicionar arquivo resolvido ao staging
git add arquivo.py

# 4. Verificar que não há mais conflitos
git status

# 5. Finalizar merge com commit
git commit
# Git abre editor com mensagem de merge padrão
# Você pode aceitar ou modificar

# 6. Verificar resultado
git log --oneline --graph
```

### Exemplo Prático de Resolução

**Antes (com conflito):**
```python
<<<<<<< HEAD
def processar_dados(dados):
    resultado = dados * 2
    return resultado
=======
def processar_dados(dados):
    resultado = dados * 3
    return resultado
>>>>>>> feature/melhorias
```

**Opção 1: Manter versão da main**
```python
def processar_dados(dados):
    resultado = dados * 2
    return resultado
```

**Opção 2: Manter versão da feature**
```python
def processar_dados(dados):
    resultado = dados * 3
    return resultado
```

**Opção 3: Combinar ambas (comum)**
```python
def processar_dados(dados):
    # Lógica melhorada combinando ambas as abordagens
    resultado = dados * 2
    resultado_validado = validar_resultado(resultado)
    return resultado_validado * 1.5
```

**Opção 4: Lógica completamente nova**
```python
def processar_dados(dados):
    # Nova implementação que resolve melhor o problema
    if dados < 10:
        return dados * 2
    else:
        return dados * 3
```

### Estratégias de Resolução

1. **Manter uma versão**: Escolher código de uma das branches
2. **Combinar**: Juntar elementos úteis de ambas as versões
3. **Reescrever**: Criar nova solução melhor que ambas
4. **Consultar equipe**: Em projetos colaborativos, discutir com o autor

## Ferramentas para Resolver Conflitos

### 1. Editor de Texto Manual

Editar arquivo diretamente removendo marcadores:
- Simples mas trabalhoso
- Bom para conflitos pequenos

### 2. Git Merge Tools

```bash
# Abrir ferramenta visual de merge
git mergetool

# Configurar ferramenta (exemplo VS Code)
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

**Ferramentas populares:**
- VS Code
- VimDiff
- KDiff3
- Beyond Compare
- Meld

### 3. VS Code (Recomendado)

VS Code tem excelente suporte para merge:
- Destaque visual de conflitos
- Botões para aceitar mudanças
- Editor integrado de 3 vias

## Cancelando Merge

Se você iniciou um merge mas mudou de ideia:

```bash
# Antes de resolver conflitos e commitar
git merge --abort

# Isso volta ao estado anterior ao merge
```

⚠️ **Atenção**: Só funciona antes de finalizar o merge com `git commit`!

## Merge vs Rebase

### Merge (o que aprendemos)

- Preserva histórico completo
- Cria commit de merge
- Mostra claramente quando branches foram integradas
- **Recomendado para branches compartilhadas**

### Rebase (avançado, veremos depois)

- Histórico linear
- Não cria commit de merge
- "Reescreve" histórico
- **Apenas para branches locais**

## Exemplo Completo: Merge com Conflito

```bash
# Situação: Duas pessoas trabalharam no mesmo arquivo

# === Desenvolvedor 1 (main) ===
git switch main
cat > app.py << 'EOF'
def calcular():
    return 10 + 20
EOF
git add app.py
git commit -m "feat: Implementa calculadora básica"
git push origin main

# === Desenvolvedor 2 (feature) ===
git switch -c feature/melhorias
cat > app.py << 'EOF'
def calcular():
    return 30 + 40
EOF
git add app.py
git commit -m "feat: Melhora lógica de cálculo"

# === Tentando fazer merge ===
git switch main
git merge feature/melhorias

# ❌ CONFLITO detectado!
# Git mostra: CONFLICT (content): Merge conflict in app.py

# === Resolver conflito ===
# 1. Ver arquivo
cat app.py
# Mostra marcadores de conflito

# 2. Editar arquivo (escolher solução)
cat > app.py << 'EOF'
def calcular():
    return 10 + 20  # Versão escolhida
EOF

# 3. Adicionar arquivo resolvido
git add app.py

# 4. Finalizar merge
git commit -m "Merge branch 'feature/melhorias'"

# 5. Ver resultado
git log --oneline --graph
```

## Prevenindo Conflitos

### Boas Práticas

1. **Atualizar frequentemente**: 
   ```bash
   git pull origin main  # Antes de começar trabalho
   ```

2. **Commits frequentes e pequenos**: Reduz chance de conflitos grandes

3. **Comunicação**: Coordenar com equipe sobre quem trabalha em quê

4. **Branches curtas**: Integrar cedo reduz conflitos

5. **Trabalhar em arquivos diferentes**: Quando possível

## Comandos Úteis

```bash
# Fazer merge
git merge nome-branch

# Verificar status durante merge
git status

# Ver arquivos em conflito
git diff --name-only --diff-filter=U

# Cancelar merge
git merge --abort

# Usar ferramenta de merge
git mergetool

# Ver merge de forma mais clara
git log --oneline --graph --all
```

## Resumo

- **Merge**: Combina branches em uma
- **Fast-forward**: Quando não há divergência
- **Merge commit**: Quando há mudanças em ambas as branches
- **Conflitos**: Quando Git não pode decidir automaticamente
- **Resolução**: Editar arquivo, remover marcadores, commitar
- **Prevenção**: Atualizar frequentemente e comunicar com equipe

## Próximos Passos

Agora você sabe:
- ✅ Fazer merge de branches
- ✅ Identificar conflitos
- ✅ Resolver conflitos manualmente

No próximo arquivo, você aprenderá sobre **GitHub** e **repositórios remotos**!
