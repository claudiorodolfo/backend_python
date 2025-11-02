# 02 - Comandos de Atualização, Remoção, Modelagem e Normalização de Dados

Este módulo aborda os comandos para modificar e remover dados, além de conceitos fundamentais de modelagem e normalização de banco de dados.

## 📚 Conteúdo

### Comando UPDATE - Atualização de Dados

O comando **UPDATE** é usado para modificar dados existentes em uma tabela. É essencial para manter os dados atualizados.

#### Sintaxe Básica
```sql
UPDATE nome_da_tabela
SET coluna1 = valor1, coluna2 = valor2, ...
WHERE condição;
```

**⚠️ ATENÇÃO**: Sempre use WHERE! Sem a cláusula WHERE, o UPDATE modifica TODOS os registros da tabela.

#### Exemplos Práticos

**Atualizar um único registro:**
```sql
UPDATE clientes
SET idade = 26
WHERE id = 1;
```

**Atualizar múltiplas colunas:**
```sql
UPDATE clientes
SET idade = 30, cidade = 'São Paulo'
WHERE email = 'joao@email.com';
```

**Atualizar múltiplos registros:**
```sql
UPDATE produtos
SET estoque = estoque - 10
WHERE categoria = 'Eletrônicos';
```

**Atualizar com valores calculados:**
```sql
UPDATE produtos
SET preco = preco * 1.10  -- Aumento de 10%
WHERE categoria = 'Acessórios';
```

### Cláusula WHERE em UPDATE

A cláusula **WHERE** é **crítica** no UPDATE, pois determina quais registros serão modificados.

#### Boas Práticas

1. **Sempre teste primeiro com SELECT:**
   ```sql
   -- Antes de atualizar, veja quais registros serão afetados
   SELECT * FROM clientes WHERE cidade = 'São Paulo';
   
   -- Depois faça o UPDATE
   UPDATE clientes SET cidade = 'São Paulo - SP' WHERE cidade = 'São Paulo';
   ```

2. **Use condições específicas:**
   ```sql
   -- ✅ BOM: Específico
   UPDATE clientes SET idade = 26 WHERE id = 1;
   
   -- ❌ PERIGOSO: Muito genérico
   UPDATE clientes SET idade = 26 WHERE nome LIKE '%João%';
   ```

3. **Valide a quantidade de registros afetados:**
   - Muitos SGBDs retornam quantos registros foram atualizados
   - Verifique se o número está correto

### Comando DELETE - Remoção de Dados

O comando **DELETE** remove registros de uma tabela. Use com extremo cuidado!

#### Sintaxe Básica
```sql
DELETE FROM nome_da_tabela
WHERE condição;
```

**⚠️ ATENÇÃO CRÍTICA**: Sem a cláusula WHERE, o DELETE remove TODOS os registros da tabela!

#### Exemplos Práticos

**Remover um único registro:**
```sql
DELETE FROM clientes
WHERE id = 5;
```

**Remover múltiplos registros:**
```sql
DELETE FROM produtos
WHERE estoque = 0;
```

**Remover com condições complexas:**
```sql
DELETE FROM clientes
WHERE idade < 18 AND cidade = 'São Paulo';
```

#### DELETE vs TRUNCATE vs DROP

- **DELETE**: Remove registros específicos (pode ter WHERE)
- **TRUNCATE**: Remove TODOS os registros da tabela (mais rápido, não pode ter WHERE)
- **DROP**: Remove a tabela inteira (estrutura e dados)

```sql
-- DELETE: Remove registros específicos
DELETE FROM clientes WHERE id = 1;

-- TRUNCATE: Remove todos os registros (mais rápido)
TRUNCATE TABLE clientes;

-- DROP: Remove a tabela inteira
DROP TABLE clientes;
```

### Cuidados e Boas Práticas

#### ⚠️ Antes de Atualizar ou Remover

1. **Faça backup dos dados importantes**
2. **Teste em ambiente de desenvolvimento primeiro**
3. **Use SELECT para verificar quais registros serão afetados**
4. **Use transações para poder reverter operações**
5. **Use WHERE sempre e de forma específica**

#### 🛡️ Proteções Recomendadas

```python
# Exemplo em Python: Sempre verificar antes de deletar
import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# 1. Primeiro verificar
cursor.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,))
registro = cursor.fetchone()

if registro:
    # 2. Confirmar ação (em produção, pedir confirmação do usuário)
    resposta = input(f"Tem certeza que deseja deletar {registro[1]}? (s/n): ")
    
    if resposta.lower() == 's':
        # 3. Executar DELETE
        cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
        conn.commit()
        print("✓ Registro removido com sucesso!")
    else:
        print("Operação cancelada.")
else:
    print("Registro não encontrado.")
```

### Modelagem de Dados

**Modelagem de dados** é o processo de criar um modelo conceitual dos dados que serão armazenados no banco de dados.

#### Fases da Modelagem

1. **Modelagem Conceitual**
   - Identificar entidades
   - Identificar atributos
   - Identificar relacionamentos
   - Criar Diagrama ER

2. **Modelagem Lógica**
   - Converter ER para estrutura de tabelas
   - Definir tipos de dados
   - Definir chaves primárias e estrangeiras

3. **Modelagem Física**
   - Implementar no SGBD específico
   - Criar índices
   - Otimizações

#### Princípios de Boa Modelagem

1. **Atomicidade**: Cada campo deve representar um único valor
2. **Normalização**: Evitar redundâncias
3. **Integridade**: Garantir consistência dos dados
4. **Performance**: Balancear normalização com performance
5. **Clareza**: Nomes claros e descritivos

### Normalização de Dados

**Normalização** é o processo de organizar dados em tabelas para reduzir redundâncias e melhorar a integridade dos dados.

#### Objetivos da Normalização

- ✅ Eliminar redundância de dados
- ✅ Prevenir inconsistências
- ✅ Facilitar manutenção
- ✅ Melhorar integridade referencial
- ✅ Otimizar estrutura

#### Formas Normais

##### 1ª Forma Normal (1FN)

**Regra**: Cada coluna deve conter apenas valores atômicos (indivisíveis). Não pode haver listas ou múltiplos valores em uma coluna.

**❌ Antes (NÃO normalizado):**
```
┌────┬─────────┬──────────────────────┐
│ id │ nome    │ telefones            │
├────┼─────────┼──────────────────────┤
│ 1  │ João    │ (11) 9999-1111,      │
│    │         │ (11) 8888-2222       │
└────┴─────────┴──────────────────────┘
```

**✅ Depois (1FN):**
```
┌────┬─────────┬──────────────────┐
│ id │ nome    │ telefone         │
├────┼─────────┼──────────────────┤
│ 1  │ João    │ (11) 9999-1111   │
│ 1  │ João    │ (11) 8888-2222   │
└────┴─────────┴──────────────────┘

-- Ou criar tabela separada:
┌────┬─────────┐  ┌────┬─────────────┬──────────┐
│ id │ nome    │  │ id │ cliente_id  │ telefone │
├────┼─────────┤  ├────┼─────────────┼──────────┤
│ 1  │ João    │  │ 1  │ 1           │ 9999-1111│
└────┴─────────┘  │ 2  │ 1           │ 8888-2222│
                  └────┴─────────────┴──────────┘
```

##### 2ª Forma Normal (2FN)

**Regra**: Deve estar em 1FN e todos os atributos não-chave devem depender completamente da chave primária.

**❌ Antes (NÃO normalizado):**
```
┌────┬──────────┬──────────────┬─────────────┬─────────┐
│ id │ produto  │ preco        │ categoria   │ estoque │
├────┼──────────┼──────────────┼─────────────┼─────────┤
│ 1  │ Notebook │ 2999.99      │ Eletrônicos │ 15      │
└────┴──────────┴──────────────┴─────────────┴─────────┘
```

Se `categoria` é independente do produto específico (vários produtos podem ter a mesma categoria), deve ser separado.

**✅ Depois (2FN):**
```
┌────┬──────────┬──────────────┬─────────┐  ┌─────────────┬──────────────┐
│ id │ produto  │ categoria_id │ preco   │  │ categoria_id│ nome         │
├────┼──────────┼──────────────┼─────────┤  ├─────────────┼──────────────┤
│ 1  │ Notebook │ 1            │ 2999.99 │  │ 1           │ Eletrônicos  │
└────┴──────────┴──────────────┴─────────┘  └─────────────┴──────────────┘
```

##### 3ª Forma Normal (3FN)

**Regra**: Deve estar em 2FN e não pode haver dependência transitiva (atributos não-chave dependendo de outros atributos não-chave).

**❌ Antes (NÃO normalizado):**
```
┌────┬──────────┬──────────────┬─────────┬─────────────┐
│ id │ produto  │ categoria_id │ cidade  │ estado      │
├────┼──────────┼──────────────┼─────────┼─────────────┤
│ 1  │ Notebook │ 1            │ SP      │ São Paulo   │
└────┴──────────┴──────────────┴─────────┴─────────────┘
```

Se `estado` depende de `cidade` (e não diretamente do produto), deve ser separado.

**✅ Depois (3FN):**
```
┌────┬──────────┬──────────────┬─────────┐  ┌─────────┬─────────────┐
│ id │ produto  │ categoria_id │ cidade  │  │ cidade  │ estado      │
├────┼──────────┼──────────────┼─────────┤  ├─────────┼─────────────┤
│ 1  │ Notebook │ 1            │ SP      │  │ SP      │ São Paulo   │
└────┴──────────┴──────────────┴─────────┘  └─────────┴─────────────┘
```

### Impacto da Modelagem na Performance e Integridade

#### Impactos Positivos da Normalização

✅ **Integridade de Dados:**
- Dados atualizados em um único lugar
- Menos inconsistências
- Melhor integridade referencial

✅ **Manutenibilidade:**
- Estrutura mais clara
- Mais fácil de entender e modificar
- Mudanças centralizadas

✅ **Economia de Espaço:**
- Menos redundância
- Menos dados duplicados

#### Impactos Negativos (Desnormalização)

❌ **Performance:**
- Mais JOINs necessários em consultas
- Consultas podem ser mais lentas
- Mais tabelas para gerenciar

**Solução**: Em alguns casos, uma desnormalização controlada pode melhorar performance, mas deve ser feita com cuidado.

#### Balanceamento

A modelagem ideal balanceia:
- **Normalização**: Para integridade e manutenibilidade
- **Performance**: Evitar sobre-normalização que prejudique consultas
- **Uso real**: Modelar baseado em como os dados serão consultados

## 🎯 Prática

### Arquivos Disponíveis

1. **`01_comandos_update_delete.md`**: Explicações detalhadas dos comandos
2. **`02_exemplos_sql.sql`**: Scripts SQL práticos
3. **`03_modelagem_normalizacao.md`**: Guia completo de modelagem
4. **`04_exercicios.md`**: Exercícios práticos
5. **`05_python_pratico.py`**: Exemplos com Python

### Como Usar

```bash
# Executar exemplos Python
python 05_python_pratico.py

# Executar scripts SQL
sqlite3 exemplo.db < 02_exemplos_sql.sql
```

## ✅ Objetivos de Aprendizado

Ao final desta seção, você será capaz de:
- [ ] Usar UPDATE para modificar dados existentes
- [ ] Aplicar WHERE corretamente em UPDATE
- [ ] Usar DELETE para remover registros
- [ ] Entender cuidados ao modificar/remover dados
- [ ] Compreender conceitos de modelagem de dados
- [ ] Aplicar 1ª, 2ª e 3ª formas normais
- [ ] Balancear normalização e performance
- [ ] Identificar problemas de modelagem

## 📝 Próximos Passos

Após dominar estes conceitos, avance para:
- **Módulo 03**: JOINs, consultas avançadas e conexão com Python

