-- ============================================
-- 02 - Exemplos Práticos de SQL
-- Módulo 01 - Introdução a SQL – Comandos Básicos
-- ============================================

-- Criar banco de dados (SQLite)
-- Para outros SGBDs, use: CREATE DATABASE exemplo_db;

-- ============================================
-- CRIAÇÃO DE TABELAS
-- ============================================

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    idade INTEGER,
    cidade VARCHAR(50),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela de produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50),
    estoque INTEGER DEFAULT 0
);

-- ============================================
-- INSERÇÃO DE DADOS (INSERT INTO)
-- ============================================

-- Inserir um único cliente
INSERT INTO clientes (nome, email, idade, cidade)
VALUES ('João Silva', 'joao.silva@email.com', 25, 'São Paulo');

-- Inserir múltiplos clientes de uma vez
INSERT INTO clientes (nome, email, idade, cidade)
VALUES 
    ('Maria Santos', 'maria.santos@email.com', 30, 'Rio de Janeiro'),
    ('Pedro Costa', 'pedro.costa@email.com', 22, 'Belo Horizonte'),
    ('Ana Oliveira', 'ana.oliveira@email.com', 28, 'São Paulo'),
    ('Carlos Souza', 'carlos.souza@email.com', 35, 'Porto Alegre'),
    ('Julia Ferreira', 'julia.ferreira@email.com', 27, 'Curitiba'),
    ('Roberto Alves', 'roberto.alves@email.com', 40, 'Brasília'),
    ('Fernanda Lima', 'fernanda.lima@email.com', 24, 'São Paulo'),
    ('Lucas Mendes', 'lucas.mendes@email.com', 29, 'Salvador');

-- Inserir produtos
INSERT INTO produtos (nome, preco, categoria, estoque)
VALUES 
    ('Notebook', 2999.99, 'Eletrônicos', 15),
    ('Mouse', 49.90, 'Acessórios', 50),
    ('Teclado', 199.90, 'Acessórios', 30),
    ('Monitor', 799.90, 'Eletrônicos', 20),
    ('Headset', 299.90, 'Acessórios', 25),
    ('Webcam', 199.90, 'Acessórios', 40),
    ('Tablet', 1499.90, 'Eletrônicos', 10),
    ('Smartphone', 2499.90, 'Eletrônicos', 12);

-- ============================================
-- CONSULTA DE DADOS (SELECT)
-- ============================================

-- Selecionar todas as colunas de todos os clientes
SELECT * FROM clientes;

-- Selecionar colunas específicas
SELECT nome, email, cidade FROM clientes;

-- Selecionar apenas nomes
SELECT nome FROM clientes;

-- ============================================
-- FILTROS COM WHERE
-- ============================================

-- Clientes com idade maior que 25
SELECT * FROM clientes WHERE idade > 25;

-- Clientes de São Paulo
SELECT * FROM clientes WHERE cidade = 'São Paulo';

-- Clientes com idade entre 25 e 35
SELECT * FROM clientes WHERE idade >= 25 AND idade <= 35;

-- Clientes de São Paulo OU Rio de Janeiro
SELECT * FROM clientes WHERE cidade = 'São Paulo' OR cidade = 'Rio de Janeiro';

-- Clientes cujo nome começa com 'J'
SELECT * FROM clientes WHERE nome LIKE 'J%';

-- Clientes cujo nome contém 'Silva'
SELECT * FROM clientes WHERE nome LIKE '%Silva%';

-- Clientes cujo email termina com '@email.com'
SELECT * FROM clientes WHERE email LIKE '%@email.com';

-- Clientes com idade diferente de 25
SELECT * FROM clientes WHERE idade != 25;

-- Clientes de cidades específicas (IN)
SELECT * FROM clientes WHERE cidade IN ('São Paulo', 'Rio de Janeiro', 'Belo Horizonte');

-- Clientes com idade não nula
SELECT * FROM clientes WHERE idade IS NOT NULL;

-- Produtos com preço menor que 500
SELECT * FROM produtos WHERE preco < 500;

-- Produtos da categoria 'Eletrônicos'
SELECT * FROM produtos WHERE categoria = 'Eletrônicos';

-- Produtos com estoque maior que 20
SELECT * FROM produtos WHERE estoque > 20;

-- ============================================
-- ORDENAÇÃO COM ORDER BY
-- ============================================

-- Ordenar clientes por nome (crescente)
SELECT * FROM clientes ORDER BY nome ASC;

-- Ordenar clientes por idade (decrescente)
SELECT * FROM clientes ORDER BY idade DESC;

-- Ordenar produtos por preço (do mais barato ao mais caro)
SELECT * FROM produtos ORDER BY preco ASC;

-- Ordenar produtos por preço (do mais caro ao mais barato)
SELECT * FROM produtos ORDER BY preco DESC;

-- Ordenar clientes por cidade e depois por nome
SELECT * FROM clientes ORDER BY cidade ASC, nome ASC;

-- Ordenar produtos por categoria e depois por preço
SELECT * FROM produtos ORDER BY categoria ASC, preco DESC;

-- ============================================
-- LIMITAR RESULTADOS COM LIMIT
-- ============================================

-- Mostrar apenas os 5 primeiros clientes
SELECT * FROM clientes LIMIT 5;

-- Mostrar os 3 produtos mais caros
SELECT * FROM produtos ORDER BY preco DESC LIMIT 3;

-- Mostrar os 5 clientes mais jovens
SELECT * FROM clientes ORDER BY idade ASC LIMIT 5;

-- Pular os 3 primeiros e mostrar os próximos 5 (OFFSET)
SELECT * FROM clientes LIMIT 5 OFFSET 3;

-- ============================================
-- COMBINAÇÕES DE CLAÚSULAS
-- ============================================

-- Clientes de São Paulo ordenados por idade (decrescente)
SELECT * FROM clientes 
WHERE cidade = 'São Paulo' 
ORDER BY idade DESC;

-- Produtos com preço entre 100 e 1000, ordenados por categoria e preço
SELECT * FROM produtos 
WHERE preco >= 100 AND preco <= 1000 
ORDER BY categoria ASC, preco ASC;

-- Top 3 produtos mais caros da categoria 'Eletrônicos'
SELECT * FROM produtos 
WHERE categoria = 'Eletrônicos' 
ORDER BY preco DESC 
LIMIT 3;

-- Clientes com idade maior que 25, de São Paulo, ordenados por nome
SELECT * FROM clientes 
WHERE idade > 25 AND cidade = 'São Paulo' 
ORDER BY nome ASC;

-- Produtos com estoque maior que 20, ordenados por preço (crescente), limitado a 5
SELECT * FROM produtos 
WHERE estoque > 20 
ORDER BY preco ASC 
LIMIT 5;

-- ============================================
-- FUNÇÕES AGREGADAS BÁSICAS (Preview)
-- ============================================

-- Contar total de clientes
SELECT COUNT(*) AS total_clientes FROM clientes;

-- Média de idade dos clientes
SELECT AVG(idade) AS media_idade FROM clientes;

-- Soma do estoque de produtos
SELECT SUM(estoque) AS total_estoque FROM produtos;

-- Maior preço entre os produtos
SELECT MAX(preco) AS preco_maximo FROM produtos;

-- Menor preço entre os produtos
SELECT MIN(preco) AS preco_minimo FROM produtos;

-- ============================================
-- CONSULTAS ÚTEIS PARA EXPLORAR OS DADOS
-- ============================================

-- Verificar quantos clientes temos por cidade
SELECT cidade, COUNT(*) AS quantidade 
FROM clientes 
GROUP BY cidade;

-- Verificar produtos por categoria
SELECT categoria, COUNT(*) AS quantidade 
FROM produtos 
GROUP BY categoria;

-- Verificar a média de preço por categoria
SELECT categoria, AVG(preco) AS preco_medio 
FROM produtos 
GROUP BY categoria;

-- ============================================
-- NOTAS IMPORTANTES
-- ============================================

/*
 * SQLite usa INTEGER PRIMARY KEY AUTOINCREMENT
 * Para outros SGBDs:
 *   MySQL: AUTO_INCREMENT
 *   PostgreSQL: SERIAL ou BIGSERIAL
 *   SQL Server: IDENTITY(1,1)
 *
 * DATE DEFAULT CURRENT_DATE funciona no SQLite
 * Para outros SGBDs:
 *   MySQL: DATE DEFAULT (CURRENT_DATE)
 *   PostgreSQL: DATE DEFAULT CURRENT_DATE (mesmo que SQLite)
 */

