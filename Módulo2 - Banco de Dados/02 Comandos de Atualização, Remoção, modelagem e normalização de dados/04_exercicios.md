# 04 - Exercícios Práticos
## Módulo 02 - Comandos de Atualização, Remoção, Modelagem e Normalização

Este documento contém exercícios práticos para fixar os conceitos aprendidos.

## 📋 Pré-requisitos

Execute o script `05_python_pratico.py` ou o arquivo SQL `02_exemplos_sql.sql` para criar o banco de dados de exemplo.

## 🎯 Exercícios

### Exercício 1: UPDATE Básico

**Objetivo**: Praticar atualização de dados

**Tarefas**:
1. Atualize a idade do cliente com ID 1 para 27 anos
2. Atualize o email do cliente chamado "Maria Santos" para "maria.santos.novo@email.com"
3. Atualize a cidade de todos os clientes de "São Paulo" para "São Paulo - SP"

**Solução**:
```sql
-- 1. Atualizar idade
UPDATE clientes SET idade = 27 WHERE id = 1;

-- 2. Atualizar email
UPDATE clientes SET email = 'maria.santos.novo@email.com' WHERE nome = 'Maria Santos';

-- 3. Atualizar cidade
UPDATE clientes SET cidade = 'São Paulo - SP' WHERE cidade = 'São Paulo';
```

---

### Exercício 2: UPDATE com Cálculos

**Objetivo**: Atualizar dados usando cálculos

**Tarefas**:
1. Aumente o preço de todos os produtos em 15%
2. Reduza o estoque de produtos da categoria 'Eletrônicos' em 5 unidades
3. Atualize a idade de todos os clientes, adicionando 1 ano

**Solução**:
```sql
-- 1. Aumentar preços em 15%
UPDATE produtos SET preco = preco * 1.15;

-- 2. Reduzir estoque
UPDATE produtos SET estoque = estoque - 5 WHERE categoria = 'Eletrônicos';

-- 3. Aumentar idade
UPDATE clientes SET idade = idade + 1;
```

---

### Exercício 3: UPDATE com Múltiplas Condições

**Objetivo**: Aplicar UPDATE com condições complexas

**Tarefas**:
1. Atualize o preço de produtos da categoria 'Acessórios' com preço menor que R$ 100, aumentando em 20%
2. Atualize a cidade de clientes de São Paulo com idade maior que 25 para "São Paulo - Capital"

**Solução**:
```sql
-- 1. Preço de acessórios baratos
UPDATE produtos 
SET preco = preco * 1.20 
WHERE categoria = 'Acessórios' AND preco < 100;

-- 2. Cidade de clientes específicos
UPDATE clientes 
SET cidade = 'São Paulo - Capital' 
WHERE cidade = 'São Paulo' AND idade > 25;
```

---

### Exercício 4: DELETE Básico

**Objetivo**: Praticar remoção de dados (CUIDADO!)

**⚠️ IMPORTANTE**: Sempre use SELECT primeiro para verificar!

**Tarefas**:
1. Remova o cliente com ID 5 (verifique primeiro com SELECT!)
2. Remova produtos com estoque igual a zero (verifique primeiro!)
3. Remova clientes com idade menor que 18 anos

**Solução**:
```sql
-- 1. Verificar primeiro
SELECT * FROM clientes WHERE id = 5;
-- Depois remover
DELETE FROM clientes WHERE id = 5;

-- 2. Verificar primeiro
SELECT * FROM produtos WHERE estoque = 0;
-- Depois remover (se correto)
DELETE FROM produtos WHERE estoque = 0;

-- 3. Verificar primeiro
SELECT * FROM clientes WHERE idade < 18;
-- Depois remover (se correto)
DELETE FROM clientes WHERE idade < 18;
```

---

### Exercício 5: Transações

**Objetivo**: Usar transações para operações seguras

**Tarefa**: 
Crie uma transação que:
1. Atualiza o preço de um produto
2. Atualiza o estoque
3. Se algo der errado, reverta tudo

**Solução**:
```sql
BEGIN TRANSACTION;

-- Atualizar preço
UPDATE produtos SET preco = 3500.00 WHERE id = 1;

-- Verificar se está correto (em produção, verificar resultado)
-- Se estiver correto:
COMMIT;

-- OU se houver erro:
-- ROLLBACK;
```

---

### Exercício 6: Normalização - Identificar Problemas

**Objetivo**: Identificar problemas de normalização

**Tarefa**: 
Analise a seguinte tabela e identifique problemas de normalização:

```sql
CREATE TABLE pedidos_ruim (
    id INTEGER PRIMARY KEY,
    cliente_nome VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_cidade VARCHAR(50),
    produto_nome VARCHAR(100),
    produto_preco DECIMAL(10,2),
    produto_categoria VARCHAR(50),
    quantidade INTEGER,
    valor_total DECIMAL(10,2),
    data_pedido DATE
);
```

**Problemas identificados:**
1. Dados duplicados (cliente repetido em cada pedido)
2. Dados do produto duplicados
3. Inconsistências possíveis
4. Violação da 3FN (se categoria dependesse de outra coluna)

**Solução Normalizada**:
```sql
-- Tabelas separadas
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    cidade VARCHAR(50)
);

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    categoria VARCHAR(50)
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    data_pedido DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE itens_pedido (
    id INTEGER PRIMARY KEY,
    pedido_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

---

### Exercício 7: Aplicar 1ª Forma Normal

**Objetivo**: Normalizar tabela violando 1FN

**Tarefa**: 
Normalize a seguinte tabela que viola a 1FN:

```sql
CREATE TABLE clientes_telefones (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    telefones VARCHAR(200)  -- PROBLEMA: múltiplos valores
);
```

**Solução**:
```sql
-- Opção 1: Tabela separada
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE telefones (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    numero VARCHAR(20),
    tipo VARCHAR(20),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

---

### Exercício 8: Aplicar 2ª Forma Normal

**Objetivo**: Normalizar tabela violando 2FN

**Tarefa**: 
Normalize a seguinte tabela (chave composta com dependência parcial):

```sql
CREATE TABLE pedidos_produtos (
    pedido_id INTEGER,
    produto_id INTEGER,
    produto_nome VARCHAR(100),  -- PROBLEMA: depende só de produto_id
    quantidade INTEGER,
    PRIMARY KEY (pedido_id, produto_id)
);
```

**Solução**:
```sql
CREATE TABLE produtos (
    produto_id INTEGER PRIMARY KEY,
    produto_nome VARCHAR(100)
);

CREATE TABLE pedidos_produtos (
    pedido_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
```

---

### Exercício 9: Aplicar 3ª Forma Normal

**Objetivo**: Normalizar tabela violando 3FN

**Tarefa**: 
Normalize a seguinte tabela (dependência transitiva):

```sql
CREATE TABLE clientes_enderecos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(2)  -- PROBLEMA: estado depende de cidade
);
```

**Solução**:
```sql
CREATE TABLE cidades (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    estado VARCHAR(2)
);

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    cidade_id INTEGER,
    FOREIGN KEY (cidade_id) REFERENCES cidades(id)
);
```

---

### Exercício 10: Modelagem Completa

**Objetivo**: Criar modelo completo normalizado

**Tarefa**: 
Modele um sistema de biblioteca com:
- Livros (título, autor, ISBN, ano)
- Usuários (nome, email, telefone)
- Empréstimos (data_emprestimo, data_devolucao)
- Categorias de livros

**Solução**:
```sql
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    ano_publicacao INTEGER,
    categoria_id INTEGER,
    disponivel BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    data_emprestimo DATE DEFAULT CURRENT_DATE,
    data_devolucao DATE,
    data_devolucao_prevista DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

---

## 🎓 Desafios

### Desafio 1: Sistema de Vendas Complexo

Modele um sistema de vendas com:
- Vendedores fazem vendas
- Vendas contêm múltiplos produtos
- Produtos têm fornecedores
- Clientes fazem compras
- Necessário rastrear histórico de preços

### Desafio 2: Normalização Reversa

Analise um banco de dados existente (pode ser um exemplo online) e:
1. Identifique problemas de normalização
2. Proponha solução normalizada
3. Compare estrutura antes/depois

### Desafio 3: Performance vs Normalização

Crie duas versões do mesmo modelo:
1. Totalmente normalizado (3FN)
2. Com desnormalizações estratégicas

Execute consultas em ambas e compare performance.

---

## ✅ Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Conseguir usar UPDATE com segurança (sempre com WHERE)
- [ ] Conseguir usar DELETE com segurança (sempre verificar antes)
- [ ] Entender o uso de transações (COMMIT/ROLLBACK)
- [ ] Identificar problemas de normalização
- [ ] Aplicar 1ª, 2ª e 3ª formas normais
- [ ] Criar modelos normalizados do zero
- [ ] Entender trade-offs entre normalização e performance

---

## 📝 Dicas

1. **Sempre teste com SELECT** antes de UPDATE/DELETE
2. **Use transações** para operações críticas
3. **Faça backups** antes de operações em massa
4. **Comece normalizado**, depois otimize se necessário
5. **Documente** suas decisões de modelagem
6. **Pense no uso real** ao modelar (quais consultas serão mais frequentes?)

Boa prática! 🚀

