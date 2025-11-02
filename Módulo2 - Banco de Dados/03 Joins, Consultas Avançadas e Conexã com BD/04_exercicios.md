# 04 - Exercícios Práticos
## Módulo 03 - JOINs, Consultas Avançadas e Conexão com BD

Este documento contém exercícios práticos para fixar os conceitos aprendidos.

## 📋 Pré-requisitos

Execute o script `05_python_completo.py` ou o arquivo SQL `02_exemplos_sql.sql` para criar o banco de dados de exemplo.

## 🎯 Exercícios

### Exercício 1: INNER JOIN Básico

**Objetivo**: Combinar dados de duas tabelas

**Tarefa**: 
Liste todos os pedidos com os nomes dos clientes que fizeram cada pedido.

**Solução**:
```sql
SELECT 
    c.nome AS cliente,
    p.id AS pedido_id,
    p.data_pedido,
    p.valor_total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;
```

---

### Exercício 2: Múltiplos JOINs

**Objetivo**: Combinar dados de múltiplas tabelas

**Tarefa**: 
Crie um relatório mostrando: cliente, produto comprado, quantidade e preço unitário de cada item.

**Solução**:
```sql
SELECT 
    c.nome AS cliente,
    pr.nome AS produto,
    ip.quantidade,
    ip.preco_unitario
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos pr ON ip.produto_id = pr.id;
```

---

### Exercício 3: LEFT JOIN

**Objetivo**: Incluir todos os registros de uma tabela

**Tarefa**: 
Liste todos os produtos e suas categorias. Inclua produtos mesmo que não tenham categoria (se houver).

**Solução**:
```sql
SELECT 
    p.nome AS produto,
    c.nome AS categoria
FROM produtos p
LEFT JOIN categorias c ON p.categoria_id = c.id;
```

---

### Exercício 4: LEFT JOIN para Encontrar Registros Sem Relacionamento

**Objetivo**: Usar LEFT JOIN para identificar registros órfãos

**Tarefa**: 
Encontre todos os clientes que nunca fizeram pedidos.

**Solução**:
```sql
SELECT 
    c.nome AS cliente,
    c.email
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE p.id IS NULL;
```

---

### Exercício 5: Subconsulta Escalar

**Objetivo**: Usar subconsultas para comparações

**Tarefa**: 
Encontre produtos com preço maior que a média de todos os produtos.

**Solução**:
```sql
SELECT 
    nome,
    preco
FROM produtos
WHERE preco > (
    SELECT AVG(preco) FROM produtos
);
```

---

### Exercício 6: Subconsulta com IN

**Objetivo**: Usar subconsultas com IN

**Tarefa**: 
Liste todos os clientes que fizeram pedidos.

**Solução**:
```sql
SELECT *
FROM clientes
WHERE id IN (
    SELECT DISTINCT cliente_id FROM pedidos
);
```

---

### Exercício 7: Subconsulta Correlacionada

**Objetivo**: Usar subconsultas que referenciam a consulta externa

**Tarefa**: 
Encontre produtos mais caros que a média de preço da sua categoria.

**Solução**:
```sql
SELECT 
    p1.nome,
    p1.preco,
    c.nome AS categoria
FROM produtos p1
INNER JOIN categorias c ON p1.categoria_id = c.id
WHERE p1.preco > (
    SELECT AVG(p2.preco)
    FROM produtos p2
    WHERE p2.categoria_id = p1.categoria_id
);
```

---

### Exercício 8: GROUP BY Básico

**Objetivo**: Agrupar dados e usar funções agregadas

**Tarefa**: 
Conte quantos produtos existem em cada categoria.

**Solução**:
```sql
SELECT 
    c.nome AS categoria,
    COUNT(p.id) AS total_produtos
FROM categorias c
LEFT JOIN produtos p ON c.id = p.categoria_id
GROUP BY c.id, c.nome;
```

---

### Exercício 9: GROUP BY com Múltiplas Agregações

**Objetivo**: Usar múltiplas funções agregadas

**Tarefa**: 
Para cada cliente, mostre o total de pedidos, valor total gasto e valor médio por pedido.

**Solução**:
```sql
SELECT 
    c.nome AS cliente,
    COUNT(p.id) AS total_pedidos,
    SUM(p.valor_total) AS valor_total,
    AVG(p.valor_total) AS valor_medio
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome;
```

---

### Exercício 10: HAVING

**Objetivo**: Filtrar grupos após agrupamento

**Tarefa**: 
Encontre clientes que fizeram mais de 1 pedido.

**Solução**:
```sql
SELECT 
    c.nome AS cliente,
    COUNT(p.id) AS total_pedidos
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome
HAVING COUNT(p.id) > 1;
```

---

### Exercício 11: HAVING com Condição Complexa

**Objetivo**: Usar HAVING com condições avançadas

**Tarefa**: 
Encontre categorias cujo valor total em estoque (preço × estoque) seja maior que R$ 10.000.

**Solução**:
```sql
SELECT 
    c.nome AS categoria,
    SUM(p.preco * p.estoque) AS valor_total_estoque
FROM categorias c
INNER JOIN produtos p ON c.id = p.categoria_id
GROUP BY c.id, c.nome
HAVING SUM(p.preco * p.estoque) > 10000;
```

---

### Exercício 12: Consulta Complexa Combinada

**Objetivo**: Combinar JOINs, subconsultas, GROUP BY e HAVING

**Tarefa**: 
Encontre os 3 produtos mais vendidos (por quantidade total) que estão na categoria 'Eletrônicos'.

**Solução**:
```sql
SELECT 
    pr.nome AS produto,
    SUM(ip.quantidade) AS total_vendido
FROM produtos pr
INNER JOIN categorias c ON pr.categoria_id = c.id
INNER JOIN itens_pedido ip ON pr.id = ip.produto_id
WHERE c.nome = 'Eletrônicos'
GROUP BY pr.id, pr.nome
ORDER BY total_vendido DESC
LIMIT 3;
```

---

### Exercício 13: Python - Conexão Básica

**Objetivo**: Conectar Python ao banco de dados

**Tarefa**: 
Crie um script Python que:
1. Conecta ao banco SQLite
2. Lista todos os clientes
3. Fecha a conexão

**Solução**:
```python
import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conn.close()
```

---

### Exercício 14: Python - Usando Context Manager

**Objetivo**: Usar context manager para gerenciar conexões

**Tarefa**: 
Reescreva o exercício anterior usando `with` (context manager).

**Solução**:
```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    
    for cliente in clientes:
        print(cliente)
# Conexão fechada automaticamente
```

---

### Exercício 15: Python - JOIN em Python

**Objetivo**: Executar JOINs via Python

**Tarefa**: 
Crie um script Python que lista clientes e seus pedidos usando JOIN.

**Solução**:
```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            c.nome AS cliente,
            p.id AS pedido_id,
            p.valor_total
        FROM clientes c
        INNER JOIN pedidos p ON c.id = p.cliente_id
    ''')
    
    resultados = cursor.fetchall()
    for row in resultados:
        print(f"{row[0]}: Pedido {row[1]} - R$ {row[2]}")
```

---

### Exercício 16: Python - Inserir Dados com Parâmetros

**Objetivo**: Inserir dados de forma segura

**Tarefa**: 
Crie um script que insere um novo cliente usando parâmetros (prepared statements).

**Solução**:
```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO clientes (nome, email, cidade)
        VALUES (?, ?, ?)
    ''', ('Novo Cliente', 'novo@email.com', 'São Paulo'))
    
    conn.commit()
    print(f"Cliente inserido com ID: {cursor.lastrowid}")
```

---

### Exercício 17: Python - GROUP BY

**Objetivo**: Executar agregações via Python

**Tarefa**: 
Crie um script que calcula o valor total de pedidos por cliente.

**Solução**:
```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            c.nome,
            SUM(p.valor_total) AS total
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome
    ''')
    
    resultados = cursor.fetchall()
    print("Cliente\t\tValor Total")
    print("-" * 40)
    for row in resultados:
        print(f"{row[0]}\t\tR$ {row[1] or 0:.2f}")
```

---

## 🎓 Desafios

### Desafio 1: Relatório Complexo

Crie uma query que mostre:
- Cliente
- Total de pedidos
- Produto mais caro comprado
- Valor total gasto
- Média de valor por pedido

### Desafio 2: Análise de Vendas

Crie um relatório que mostre:
- Categoria
- Produto mais vendido (por quantidade)
- Produto mais lucrativo (por valor total)
- Total de unidades vendidas da categoria

### Desafio 3: Sistema Python Completo

Crie um módulo Python que:
- Classe `Database` para gerenciar conexões
- Métodos para CRUD de clientes
- Métodos para consultas complexas (JOINs, GROUP BY)
- Tratamento de erros adequado
- Usa context managers

### Desafio 4: Otimização de Queries

Analise as queries criadas e:
1. Identifique possíveis melhorias
2. Sugira índices que poderiam melhorar performance
3. Teste com EXPLAIN QUERY PLAN (SQLite)

---

## ✅ Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Conseguir usar INNER JOIN para combinar tabelas
- [ ] Entender diferença entre INNER e LEFT JOIN
- [ ] Criar subconsultas escalares e correlacionadas
- [ ] Usar GROUP BY com funções agregadas
- [ ] Filtrar grupos com HAVING
- [ ] Conectar Python a SQLite
- [ ] Criar tabelas via Python
- [ ] Inserir e consultar dados via Python
- [ ] Usar context managers para gerenciar conexões
- [ ] Compreender prepared statements e segurança

---

## 📝 Dicas

1. **Sempre use aliases** para tornar queries mais legíveis
2. **Prefira INNER JOIN** quando precisar apenas de correspondências
3. **Use LEFT JOIN** quando precisar incluir todos os registros de uma tabela
4. **Subconsultas podem ser lentas** - avalie se JOIN não resolve
5. **GROUP BY requer** que colunas não agregadas estejam no GROUP BY
6. **HAVING filtra grupos**, WHERE filtra registros
7. **Sempre use prepared statements** (?, %s) para evitar SQL injection
8. **Use context managers** para garantir fechamento de conexões
9. **Teste queries complexas** em dados de exemplo primeiro
10. **Documente queries complexas** para facilitar manutenção

Boa prática! 🚀

