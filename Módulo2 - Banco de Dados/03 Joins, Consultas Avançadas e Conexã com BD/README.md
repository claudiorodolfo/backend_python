# 03 - JOINs, Consultas Avançadas e Conexão com BD

Este módulo aborda relacionamentos entre tabelas (JOINs), consultas avançadas com subconsultas e agrupamento, além da conexão de bancos de dados com Python.

## 📚 Conteúdo

### JOINs - Relacionamentos entre Tabelas

Os **JOINs** são usados para combinar dados de múltiplas tabelas baseado em relacionamentos. Eles são fundamentais para trabalhar com dados normalizados.

#### Tipos de JOIN

##### INNER JOIN

O **INNER JOIN** retorna apenas os registros que têm correspondência em ambas as tabelas.

**Sintaxe:**
```sql
SELECT colunas
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

**Exemplo:**
```sql
SELECT clientes.nome, pedidos.data_pedido, pedidos.valor_total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

**Visualização:**
```
clientes        pedidos
┌────┬─────┐    ┌────┬───────────┐
│ id │nome │    │ id │cliente_id │
├────┼─────┤    ├────┼───────────┤
│ 1  │João │───▶│ 1  │1          │ ← INNER JOIN retorna estes
│ 2  │Maria│    │ 2  │2          │
│ 3  │Pedro│    │ 3  │1          │
└────┴─────┘    └────┴───────────┘
     ▲                          (João não tem pedido)
     └────────────────────────── (Pedro não aparece no resultado)
```

##### LEFT JOIN (LEFT OUTER JOIN)

O **LEFT JOIN** retorna todos os registros da tabela à esquerda e os correspondentes da direita. Se não houver correspondência, retorna NULL.

**Sintaxe:**
```sql
SELECT colunas
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

**Exemplo:**
```sql
SELECT clientes.nome, pedidos.data_pedido
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

**Visualização:**
```
clientes        pedidos
┌────┬─────┐    ┌────┬───────────┐
│ id │nome │    │ id │cliente_id │
├────┼─────┤    ├────┼───────────┤
│ 1  │João │───▶│ 1  │1          │ ← LEFT JOIN retorna todos
│ 2  │Maria│───▶│ 2  │2          │   os clientes, mesmo sem
│ 3  │Pedro│    │ 3  │1          │   pedidos (NULL)
└────┴─────┘    └────┴───────────┘
     │
     └───────── (Pedro aparece com NULL nos dados do pedido)
```

**Uso comum**: Listar todos os clientes, incluindo os que não fizeram pedidos.

##### RIGHT JOIN (RIGHT OUTER JOIN)

O **RIGHT JOIN** retorna todos os registros da tabela à direita e os correspondentes da esquerda. Se não houver correspondência, retorna NULL.

**Sintaxe:**
```sql
SELECT colunas
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

**Nota**: SQLite não suporta RIGHT JOIN diretamente, mas pode ser simulado invertendo as tabelas no LEFT JOIN.

**Exemplo (usando LEFT JOIN invertido):**
```sql
SELECT clientes.nome, pedidos.data_pedido
FROM pedidos
LEFT JOIN clientes ON pedidos.cliente_id = clientes.id;
```

##### FULL OUTER JOIN

O **FULL OUTER JOIN** retorna todos os registros de ambas as tabelas. Onde não houver correspondência, retorna NULL.

**Nota**: SQLite não suporta FULL OUTER JOIN diretamente.

### Subconsultas (Subqueries)

**Subconsultas** são consultas SQL dentro de outras consultas. Elas podem ser usadas em SELECT, FROM, WHERE, e outras cláusulas.

#### Tipos de Subconsultas

##### Subconsulta Escalar

Retorna um único valor.

```sql
-- Encontrar clientes com idade maior que a média
SELECT nome, idade
FROM clientes
WHERE idade > (SELECT AVG(idade) FROM clientes);
```

##### Subconsulta em WHERE com IN

```sql
-- Encontrar produtos que estão em pedidos
SELECT * FROM produtos
WHERE id IN (SELECT DISTINCT produto_id FROM itens_pedido);
```

##### Subconsulta Correlacionada

A subconsulta referencia colunas da consulta externa.

```sql
-- Encontrar produtos mais caros que a média da sua categoria
SELECT p1.*
FROM produtos p1
WHERE p1.preco > (
    SELECT AVG(p2.preco)
    FROM produtos p2
    WHERE p2.categoria = p1.categoria
);
```

##### Subconsulta na Cláusula FROM

```sql
-- Calcular totais por categoria
SELECT categoria, COUNT(*) AS total
FROM (
    SELECT categoria FROM produtos
    WHERE estoque > 0
) AS produtos_com_estoque
GROUP BY categoria;
```

### ORDER BY - Ordenação Avançada

Ordenar por múltiplas colunas e usar CASE para ordenação customizada.

```sql
SELECT * FROM produtos
ORDER BY 
    categoria ASC,
    CASE 
        WHEN estoque < 10 THEN 1
        WHEN estoque < 20 THEN 2
        ELSE 3
    END,
    preco DESC;
```

### GROUP BY - Agrupamento de Dados

**GROUP BY** agrupa registros que têm o mesmo valor em colunas especificadas, geralmente usado com funções agregadas.

#### Funções Agregadas

- `COUNT()`: Conta registros
- `SUM()`: Soma valores
- `AVG()`: Média
- `MAX()`: Valor máximo
- `MIN()`: Valor mínimo

#### Exemplos com GROUP BY

```sql
-- Contar produtos por categoria
SELECT categoria, COUNT(*) AS total
FROM produtos
GROUP BY categoria;

-- Soma de valores por categoria
SELECT categoria, SUM(preco * estoque) AS valor_total
FROM produtos
GROUP BY categoria;

-- Média de preço por categoria
SELECT categoria, AVG(preco) AS preco_medio
FROM produtos
GROUP BY categoria;
```

#### HAVING - Filtrar Grupos

**HAVING** filtra grupos após o GROUP BY (diferente de WHERE que filtra antes).

```sql
-- Categorias com mais de 5 produtos
SELECT categoria, COUNT(*) AS total
FROM produtos
GROUP BY categoria
HAVING COUNT(*) > 5;
```

**Diferença WHERE vs HAVING:**
- **WHERE**: Filtra registros individuais antes do agrupamento
- **HAVING**: Filtra grupos após o agrupamento

### Banco de Dados Embarcado

Um **banco de dados embarcado** é um banco que não requer um servidor separado e é armazenado em um arquivo ou na memória.

**Características:**
- Não requer instalação/configuração de servidor
- Banco armazenado em arquivo único (geralmente)
- Ideal para aplicações desktop e desenvolvimento
- Exemplo: SQLite

### Biblioteca SQLite3 (Nativa do Python)

A biblioteca **sqlite3** vem incluída no Python e permite trabalhar com bancos SQLite.

#### Conceitos Básicos

**Conexão:**
```python
import sqlite3

conn = sqlite3.connect('banco.db')
```

**Cursor:**
```python
cursor = conn.cursor()
```

**Executar comandos:**
```python
cursor.execute('SELECT * FROM clientes')
```

**Commit (salvar mudanças):**
```python
conn.commit()
```

**Fechar conexão:**
```python
conn.close()
```

#### Context Manager (Recomendado)

Usar `with` garante que a conexão seja fechada automaticamente:

```python
with sqlite3.connect('banco.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    resultados = cursor.fetchall()
    # Conexão fechada automaticamente
```

### Criação de Tabelas via Python

```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE
        )
    ''')
    
    conn.commit()
```

### Inserção de Dados via Python

#### Inserção Individual
```python
cursor.execute('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', ('João Silva', 'joao@email.com'))

conn.commit()
```

#### Inserção Múltipla
```python
clientes = [
    ('Maria Santos', 'maria@email.com'),
    ('Pedro Costa', 'pedro@email.com'),
]

cursor.executemany('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', clientes)

conn.commit()
```

### Consultas via Python

#### Buscar Todos os Resultados
```python
cursor.execute('SELECT * FROM clientes')
todos = cursor.fetchall()
```

#### Buscar Um Resultado
```python
cursor.execute('SELECT * FROM clientes WHERE id = ?', (1,))
um = cursor.fetchone()
```

#### Buscar Vários Resultados
```python
cursor.execute('SELECT * FROM clientes WHERE idade > ?', (25,))
alguns = cursor.fetchmany(5)  # Próximos 5
```

## 🎯 Prática

### Arquivos Disponíveis

1. **`01_joins_explicacao.md`**: Explicações detalhadas de JOINs
2. **`02_exemplos_sql.sql`**: Scripts SQL com JOINs e subconsultas
3. **`03_conexao_python.md`**: Guia completo de conexão com Python
4. **`04_exercicios.md`**: Exercícios práticos
5. **`05_python_completo.py`**: Exemplos completos com Python

### Como Usar

```bash
# Executar exemplos Python
python 05_python_completo.py

# Executar scripts SQL
sqlite3 exemplo.db < 02_exemplos_sql.sql
```

## ✅ Objetivos de Aprendizado

Ao final desta seção, você será capaz de:
- [ ] Usar INNER JOIN para combinar tabelas
- [ ] Usar LEFT JOIN para incluir todos os registros de uma tabela
- [ ] Criar e usar subconsultas (subqueries)
- [ ] Agrupar dados com GROUP BY
- [ ] Filtrar grupos com HAVING
- [ ] Conectar Python a bancos SQLite
- [ ] Criar tabelas via Python
- [ ] Inserir dados via Python
- [ ] Consultar dados via Python
- [ ] Usar context managers para gerenciar conexões

## 📝 Próximos Passos

Após dominar estes conceitos, você estará pronto para:
- Trabalhar com ORMs (Object-Relational Mapping) como SQLAlchemy
- Integrar bancos de dados em aplicações web
- Trabalhar com frameworks como Django

---

## 🔗 Recursos Adicionais

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQL JOIN Visualizer](https://sql-join.com/)

