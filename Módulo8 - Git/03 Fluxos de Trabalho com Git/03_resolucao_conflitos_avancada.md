# Resolução Avançada de Conflitos de Merge

## Entendendo Conflitos em Profundidade

Conflitos ocorrem quando Git não consegue determinar automaticamente como combinar mudanças. Isso acontece quando:
1. **Mesma linha modificada** em ambas as branches
2. **Linhas próximas modificadas** (contexto similar)
3. **Arquivo deletado** em uma branch e modificado na outra
4. **Arquivo renomeado** em ambas as branches de formas diferentes

## Tipos de Conflitos

### 1. Conflitos de Conteúdo

O tipo mais comum - mesmo arquivo, linhas modificadas.

```python
# Branch main
def processar(dados):
    resultado = dados * 2
    return resultado

# Branch feature
def processar(dados):
    resultado = dados * 3
    return resultado

# Conflito:
<<<<<<< HEAD
    resultado = dados * 2
=======
    resultado = dados * 3
>>>>>>> feature/melhorias
```

### 2. Conflitos de Adição/Deleção

Arquivo deletado em uma branch, modificado na outra.

```bash
# Branch main: deletou arquivo.py
git rm arquivo.py

# Branch feature: modificou arquivo.py
# ... modificações ...

# Conflito:
CONFLICT (modify/delete): arquivo.py deleted in HEAD and modified in feature.
```

### 3. Conflitos de Renomeação

Arquivo renomeado de formas diferentes.

```bash
# Branch main: renomeou A.py → B.py
# Branch feature: renomeou A.py → C.py

# Conflito:
CONFLICT (rename/rename): A.py renamed to B.py in HEAD and to C.py in feature.
```

## Estratégias de Resolução

### Estratégia 1: Manter Uma Versão

Escolher completamente uma das versões.

```python
# Resolução: Manter versão da main
def processar(dados):
    resultado = dados * 2
    return resultado
```

**Quando usar:**
- Uma versão está claramente correta
- Outra versão foi substituída
- Mudanças não são compatíveis

### Estratégia 2: Combinar Ambas

Manter elementos úteis de ambas as versões.

```python
# Versão combinada
def processar(dados):
    # Validar primeiro
    if dados is None:
        raise ValueError("Dados não podem ser None")
    
    # Processar (versão melhorada)
    resultado = dados * 2
    
    # Logging (adicionado na feature)
    print(f"Processado: {resultado}")
    
    return resultado
```

**Quando usar:**
- Ambas as mudanças são úteis
- Mudanças em partes diferentes do código
- Quer melhorar com elementos de ambas

### Estratégia 3: Reescrever Completamente

Criar nova solução melhor que ambas.

```python
# Nova implementação que resolve melhor o problema
def processar(dados):
    """
    Processa dados com validação e tratamento de erros melhorado.
    """
    if not isinstance(dados, (int, float)):
        raise TypeError("Dados devem ser numéricos")
    
    if dados < 0:
        raise ValueError("Dados não podem ser negativos")
    
    # Lógica melhorada combinando ideias de ambas as versões
    resultado = dados * 2.5  # Valor intermediário otimizado
    
    return resultado
```

**Quando usar:**
- Ambas as versões têm problemas
- Oportunidade de melhorar ainda mais
- Refatoração necessária

## Ferramentas para Resolução

### 1. Resolução Manual (Editor de Texto)

```bash
# 1. Identificar conflitos
git status

# 2. Abrir arquivo com conflito
# 3. Localizar marcadores <<<<<<<, =======, >>>>>>>
# 4. Editar manualmente
# 5. Remover marcadores
# 6. Salvar arquivo
```

**Vantagens:**
- Controle total
- Entende contexto completo
- Não requer ferramentas extras

**Desvantagens:**
- Trabalhoso para muitos conflitos
- Pode ser confuso

### 2. Ferramentas Visuais de Merge

```bash
# Configurar VS Code como mergetool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Usar ferramenta
git mergetool
```

**Ferramentas populares:**
- **VS Code**: Excelente suporte integrado
- **Meld**: Visual de 3 vias
- **KDiff3**: Potente e configurável
- **Beyond Compare**: Comercial, muito poderoso

### 3. VS Code (Recomendado)

VS Code detecta conflitos automaticamente e oferece:
- Destaque visual de conflitos
- Botões para aceitar mudanças
- Editor de 3 vias lado a lado
- Preview do resultado

**Usar no VS Code:**
1. Abrir arquivo com conflito
2. VS Code mostra opções:
   - "Accept Current Change"
   - "Accept Incoming Change"
   - "Accept Both Changes"
   - "Compare Changes"
3. Editar manualmente se necessário
4. Salvar

## Fluxo de Resolução Passo a Passo

### Durante Merge

```bash
# 1. Iniciar merge
git switch main
git merge feature/nova-feature

# 2. Conflito detectado
# Auto-merging arquivo.py
# CONFLICT (content): Merge conflict in arquivo.py
# Automatic merge failed; fix conflicts and then commit the result.

# 3. Ver status
git status
# Mostra: both modified: arquivo.py
```

### Resolver Conflitos

```bash
# 4. Identificar arquivos com conflito
git status
# ou
git diff --name-only --diff-filter=U

# 5. Resolver cada arquivo
# Opção A: Manualmente (editar arquivo)
# Opção B: Ferramenta visual
git mergetool

# 6. Verificar resolução
git status
# Deve mostrar: all conflicts fixed

# 7. Adicionar arquivos resolvidos
git add arquivo.py

# 8. Finalizar merge
git commit
# Git abre editor com mensagem de merge padrão
```

### Cancelar Merge (se necessário)

```bash
# Antes de finalizar (antes de git commit)
git merge --abort

# Volta ao estado anterior ao merge
```

## Exemplos Práticos

### Exemplo 1: Conflito Simples

```python
# main: arquivo.py
def calcular(a, b):
    return a + b

# feature: arquivo.py
def calcular(a, b):
    return a * b

# Após merge (conflito):
<<<<<<< HEAD
    return a + b
=======
    return a * b
>>>>>>> feature/multiply

# Resolução: Escolher multiplicação (mais recente)
def calcular(a, b):
    return a * b
```

### Exemplo 2: Conflito com Mudanças Diferentes

```python
# main: arquivo.py
def processar(dados):
    if dados is None:
        return None
    resultado = dados * 2
    return resultado

# feature: arquivo.py
def processar(dados):
    resultado = dados * 3
    print(f"Processado: {resultado}")
    return resultado

# Conflito (múltiplas áreas):
<<<<<<< HEAD
def processar(dados):
    if dados is None:
        return None
    resultado = dados * 2
=======
def processar(dados):
    resultado = dados * 3
    print(f"Processado: {resultado}")
>>>>>>> feature/melhorias
    return resultado

# Resolução: Combinar ambas
def processar(dados):
    if dados is None:
        return None
    resultado = dados * 3  # Versão melhorada da feature
    print(f"Processado: {resultado}")  # Logging da feature
    return resultado
```

### Exemplo 3: Conflito em Arquivo Deletado

```bash
# main: deletou arquivo.py
git rm arquivo.py
git commit -m "remove: Remove arquivo.py"

# feature: modificou arquivo.py
# ... modificações ...
git commit -m "feat: Melhora arquivo.py"

# Conflito:
CONFLICT (modify/delete): arquivo.py deleted in HEAD and modified in feature.

# Resolução:
# Opção 1: Manter deletado (se realmente não precisa)
git rm arquivo.py

# Opção 2: Manter modificado (se feature é importante)
git add arquivo.py
```

## Prevenindo Conflitos

### 1. Atualização Frequente

```bash
# Atualizar branch frequentemente
git fetch origin
git merge origin/main  # ou rebase
```

### 2. Comunicação

- Informar equipe sobre mudanças grandes
- Coordenar quem trabalha em quê
- Evitar trabalhar nos mesmos arquivos simultaneamente

### 3. Arquivos Pequenos

- Arquivos menores = menos chance de conflito
- Dividir arquivos grandes em módulos

### 4. Commits Frequentes

- Commits pequenos = conflitos menores
- Fácil de resolver e entender

### 5. Branches Curtas

- Integrar mudanças cedo
- Branches longas = mais conflitos

## Conflitos em Rebase

Rebase também pode ter conflitos, mas processo é diferente:

```bash
# Iniciar rebase
git rebase main

# Conflito durante rebase
# ... resolver conflitos em cada commit ...

# Após resolver
git add arquivo.py
git rebase --continue

# Ou abortar
git rebase --abort
```

**Diferença**: No rebase, você resolve conflitos commit por commit, não todos de uma vez.

## Comandos Úteis

```bash
# Ver arquivos em conflito
git diff --name-only --diff-filter=U

# Ver conflitos de um arquivo
git diff arquivo.py

# Listar conflitos
git status

# Usar ferramenta visual
git mergetool

# Ver versão de arquivo em branch específica
git show branch:arquivo.py

# Comparar versões
git diff main feature -- arquivo.py

# Cancelar merge
git merge --abort
```

## Dicas Avançadas

### Resolver Conflito Mantendo Ambas Versões

```python
# Se quer manter código de ambas as branches
def processar(dados):
    # Versão da main
    resultado_main = dados * 2
    
    # Versão da feature
    resultado_feature = dados * 3
    
    # Combinar de alguma forma
    return (resultado_main + resultado_feature) / 2
```

### Usar Versão de Arquivo Específica

```bash
# Manter versão da branch sendo mergeada
git checkout --theirs arquivo.py

# Manter versão da branch atual
git checkout --ours arquivo.py

# Depois resolver manualmente partes específicas
```

### Resolver Múltiplos Arquivos

```bash
# Resolver todos os conflitos de uma vez
for arquivo in $(git diff --name-only --diff-filter=U); do
    echo "Resolvendo $arquivo..."
    # Editar ou usar ferramenta
    git mergetool "$arquivo"
done
```

## Resumo

**Resolução de conflitos:**
1. Identificar arquivos com conflito
2. Entender mudanças de ambas as versões
3. Escolher estratégia (manter, combinar, reescrever)
4. Resolver manualmente ou com ferramenta
5. Verificar resolução
6. Adicionar e finalizar merge

**Prevenção:**
- Atualizar frequentemente
- Comunicar com equipe
- Commits pequenos
- Branches curtas

Conflitos são normais em colaboração - a chave é resolver de forma clara e eficiente!
