# 03 - Exercícios Práticos
## Módulo 01 - Introdução a SQL – Comandos Básicos

Este documento contém exercícios práticos para fixar os conceitos aprendidos. Tente resolver antes de ver as soluções!

## 📋 Pré-requisitos

Antes de começar, execute o script `04_sqlite_pratico.py` para criar o banco de dados de exemplo, ou execute os comandos SQL do arquivo `02_exemplos_sql.sql`.

## 🎯 Exercícios

### Exercício 1: SELECT Básico

**Objetivo**: Familiarizar-se com o comando SELECT

**Tarefas**:
1. Selecione todos os dados da tabela `clientes`
2. Selecione apenas os nomes de todos os clientes
3. Selecione nome e email de todos os clientes

**Solução**:
```sql
-- 1. Todos os dados
SELECT * FROM clientes;

-- 2. Apenas nomes
SELECT nome FROM clientes;

-- 3. Nome e email
SELECT nome, email FROM clientes;
```

---

### Exercício 2: Filtros com WHERE

**Objetivo**: Aplicar filtros em consultas

**Tarefas**:
1. Encontre todos os clientes com idade maior que 25 anos
2. Encontre todos os clientes de São Paulo
3. Encontre clientes com idade entre 25 e 35 anos (inclusive)
4. Encontre produtos com preço menor que R$ 300,00
5. Encontre produtos da categoria 'Eletrônicos'

**Solução**:
```sql
-- 1. Idade > 25
SELECT * FROM clientes WHERE idade > 25;

-- 2. Clientes de São Paulo
SELECT * FROM clientes WHERE cidade = 'São Paulo';

-- 3. Idade entre 25 e 35
SELECT * FROM clientes WHERE idade >= 25 AND idade <= 35;

-- 4. Produtos < R$ 300
SELECT * FROM produtos WHERE preco < 300;

-- 5. Eletrônicos
SELECT * FROM produtos WHERE categoria = 'Eletrônicos';
```

---

### Exercício 3: Ordenação com ORDER BY

**Objetivo**: Ordenar resultados de consultas

**Tarefas**:
1. Liste os clientes ordenados por nome (A-Z)
2. Liste os produtos ordenados por preço (do mais barato ao mais caro)
3. Liste os clientes ordenados por idade (do mais velho ao mais novo)
4. Liste os clientes ordenados primeiro por cidade e depois por nome

**Solução**:
```sql
-- 1. Por nome (A-Z)
SELECT * FROM clientes ORDER BY nome ASC;

-- 2. Produtos por preço (crescente)
SELECT * FROM produtos ORDER BY preco ASC;

-- 3. Clientes por idade (decrescente)
SELECT * FROM clientes ORDER BY idade DESC;

-- 4. Por cidade e depois nome
SELECT * FROM clientes ORDER BY cidade ASC, nome ASC;
```

---

### Exercício 4: LIMIT

**Objetivo**: Limitar quantidade de resultados

**Tarefas**:
1. Mostre apenas os 3 primeiros clientes
2. Mostre os 5 produtos mais caros
3. Mostre os 3 clientes mais jovens

**Solução**:
```sql
-- 1. Primeiros 3 clientes
SELECT * FROM clientes LIMIT 3;

-- 2. 5 produtos mais caros
SELECT * FROM produtos ORDER BY preco DESC LIMIT 5;

-- 3. 3 clientes mais jovens
SELECT * FROM clientes ORDER BY idade ASC LIMIT 3;
```

---

### Exercício 5: Combinações

**Objetivo**: Combinar múltiplas cláusulas

**Tarefas**:
1. Encontre clientes de São Paulo com idade maior que 25, ordenados por nome
2. Encontre produtos da categoria 'Acessórios' com preço menor que R$ 200, ordenados por preço
3. Mostre os 3 produtos mais baratos da categoria 'Eletrônicos'

**Solução**:
```sql
-- 1. Clientes SP > 25 anos, ordenados
SELECT * FROM clientes 
WHERE cidade = 'São Paulo' AND idade > 25 
ORDER BY nome ASC;

-- 2. Acessórios < R$ 200, ordenados
SELECT * FROM produtos 
WHERE categoria = 'Acessórios' AND preco < 200 
ORDER BY preco ASC;

-- 3. 3 mais baratos de Eletrônicos
SELECT * FROM produtos 
WHERE categoria = 'Eletrônicos' 
ORDER BY preco ASC 
LIMIT 3;
```

---

### Exercício 6: INSERT INTO

**Objetivo**: Inserir novos registros

**Tarefas**:
1. Insira um novo cliente com os seguintes dados:
   - Nome: "Lucas Mendes"
   - Email: "lucas.mendes@email.com"
   - Idade: 29
   - Cidade: "Salvador"

2. Insira três novos produtos de uma vez:
   - Tablet - R$ 1.499,90 - Eletrônicos - Estoque: 10
   - Smartphone - R$ 2.499,90 - Eletrônicos - Estoque: 12
   - Webcam - R$ 199,90 - Acessórios - Estoque: 40

**Solução**:
```sql
-- 1. Inserir um cliente
INSERT INTO clientes (nome, email, idade, cidade)
VALUES ('Lucas Mendes', 'lucas.mendes@email.com', 29, 'Salvador');

-- 2. Inserir múltiplos produtos
INSERT INTO produtos (nome, preco, categoria, estoque)
VALUES 
    ('Tablet', 1499.90, 'Eletrônicos', 10),
    ('Smartphone', 2499.90, 'Eletrônicos', 12),
    ('Webcam', 199.90, 'Acessórios', 40);
```

---

### Exercício 7: Desafio - Consultas Complexas

**Objetivo**: Criar consultas mais complexas

**Tarefas**:
1. Encontre todos os clientes que têm idade maior que a média de idade de todos os clientes
   - Dica: Use subconsulta com AVG()

2. Liste os produtos ordenados por categoria, e dentro de cada categoria, ordene por preço (decrescente)

3. Encontre os clientes cujo nome contém a letra 'a' (case-insensitive se possível), ordenados por idade

**Solução**:
```sql
-- 1. Clientes acima da média de idade
SELECT * FROM clientes 
WHERE idade > (SELECT AVG(idade) FROM clientes);

-- 2. Produtos por categoria e preço
SELECT * FROM produtos 
ORDER BY categoria ASC, preco DESC;

-- 3. Nomes com 'a', ordenados por idade
SELECT * FROM clientes 
WHERE nome LIKE '%a%' OR nome LIKE '%A%'
ORDER BY idade ASC;

-- Alternativa com UPPER (se suportado):
-- SELECT * FROM clientes 
-- WHERE UPPER(nome) LIKE '%A%'
-- ORDER BY idade ASC;
```

---

### Exercício 8: Análise de Dados

**Objetivo**: Explorar os dados com funções agregadas básicas

**Tarefas**:
1. Conte quantos clientes existem no total
2. Conte quantos clientes temos por cidade
3. Calcule a média de idade dos clientes
4. Encontre o produto mais caro
5. Calcule o valor total em estoque (soma de preço × estoque)

**Solução**:
```sql
-- 1. Total de clientes
SELECT COUNT(*) AS total_clientes FROM clientes;

-- 2. Clientes por cidade
SELECT cidade, COUNT(*) AS quantidade 
FROM clientes 
GROUP BY cidade;

-- 3. Média de idade
SELECT AVG(idade) AS media_idade FROM clientes;

-- 4. Produto mais caro
SELECT * FROM produtos 
ORDER BY preco DESC 
LIMIT 1;

-- Ou usando MAX:
-- SELECT MAX(preco) AS preco_maximo FROM produtos;

-- 5. Valor total em estoque
SELECT SUM(preco * estoque) AS valor_total_estoque 
FROM produtos;
```

---

## 🎓 Desafios Adicionais

### Desafio 1: Banco de Dados de Biblioteca

Crie um banco de dados para uma biblioteca com as seguintes tabelas:
- **livros**: id, titulo, autor, ano_publicacao, categoria, disponivel
- **usuarios**: id, nome, email, telefone

Insira pelo menos 5 livros e 5 usuários. Em seguida:
1. Liste todos os livros disponíveis
2. Encontre livros publicados depois de 2000
3. Ordene livros por título
4. Liste usuários cujo nome começa com 'M'

### Desafio 2: Sistema de Vendas

Crie um banco de dados para um sistema de vendas:
- **produtos**: id, nome, preco, categoria
- **vendas**: id, produto_id, quantidade, data_venda, valor_total

Insira dados de exemplo e:
1. Liste todas as vendas ordenadas por data (mais recente primeiro)
2. Encontre vendas com valor total maior que R$ 100
3. Liste os 5 produtos mais vendidos (por quantidade)

---

## ✅ Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Conseguir escrever consultas SELECT básicas
- [ ] Aplicar filtros com WHERE usando diferentes operadores
- [ ] Ordenar resultados com ORDER BY
- [ ] Limitar resultados com LIMIT
- [ ] Inserir dados com INSERT INTO (individual e múltiplo)
- [ ] Combinar múltiplas cláusulas em uma consulta
- [ ] Entender a estrutura de tabelas (colunas, tipos de dados)

---

## 📝 Notas

- Sempre teste suas queries antes de considerá-las corretas
- Use SELECT para verificar dados antes de fazer operações de modificação
- Experimente diferentes combinações de cláusulas
- Pratique criando suas próprias tabelas e dados

Boa prática! 🚀

