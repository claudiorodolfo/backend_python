-- ============================================
-- 02 - Exemplos Práticos de JOINs e Consultas Avançadas
-- Módulo 03 - JOINs, Consultas Avançadas e Conexão com BD
-- ============================================

-- ============================================
-- PREPARAÇÃO: Criar tabelas relacionadas
-- ============================================

CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    categoria_id INTEGER,
    estoque INTEGER DEFAULT 0,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cidade VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data_pedido DATE DEFAULT CURRENT_DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

-- Inserir dados de exemplo
INSERT OR IGNORE INTO categorias (nome) VALUES 
    ('Eletrônicos'),
    ('Acessórios'),
    ('Informática');

INSERT OR IGNORE INTO produtos (nome, preco, categoria_id, estoque) VALUES 
    ('Notebook', 2999.99, 1, 15),
    ('Mouse', 49.90, 2, 50),
    ('Teclado', 199.90, 2, 30),
    ('Monitor', 799.90, 1, 20),
    ('Headset', 299.90, 2, 25),
    ('Webcam', 199.90, 2, 40),
    ('Tablet', 1499.90, 1, 10),
    ('Smartphone', 2499.90, 1, 12);

INSERT OR IGNORE INTO clientes (nome, email, cidade) VALUES 
    ('João Silva', 'joao.silva@email.com', 'São Paulo'),
    ('Maria Santos', 'maria.santos@email.com', 'Rio de Janeiro'),
    ('Pedro Costa', 'pedro.costa@email.com', 'Belo Horizonte'),
    ('Ana Oliveira', 'ana.oliveira@email.com', 'São Paulo');

INSERT OR IGNORE INTO pedidos (cliente_id, valor_total) VALUES 
    (1, 3249.89),
    (1, 199.90),
    (2, 799.90),
    (3, 2999.99);

INSERT OR IGNORE INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal) VALUES 
    (1, 1, 1, 2999.99, 2999.99),  -- Pedido 1: Notebook
    (1, 2, 5, 49.90, 249.90),      -- Pedido 1: 5 Mouses
    (2, 3, 1, 199.90, 199.90),      -- Pedido 2: Teclado
    (3, 4, 1, 799.90, 799.90),      -- Pedido 3: Monitor
    (4, 1, 1, 2999.99, 2999.99);    -- Pedido 4: Notebook

-- ============================================
-- INNER JOIN - Combina apenas registros que têm correspondência
-- ============================================

-- Exemplo 1: JOIN simples - Clientes e seus pedidos
SELECT 
    clientes.nome AS cliente,
    pedidos.id AS pedido_id,
    pedidos.data_pedido,
    pedidos.valor_total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- Exemplo 2: Múltiplos JOINs - Cliente, Pedido e Itens
SELECT 
    c.nome AS cliente,
    p.id AS pedido_id,
    pr.nome AS produto,
    ip.quantidade,
    ip.preco_unitario,
    ip.subtotal
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos pr ON ip.produto_id = pr.id;

-- Exemplo 3: JOIN com WHERE - Filtrar resultados
SELECT 
    c.nome AS cliente,
    p.valor_total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE p.valor_total > 500;

-- Exemplo 4: JOIN com tabelas relacionadas - Produtos e Categorias
SELECT 
    p.nome AS produto,
    p.preco,
    c.nome AS categoria,
    p.estoque
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id;

-- ============================================
-- LEFT JOIN - Inclui todos os registros da tabela à esquerda
-- ============================================

-- Exemplo 1: Todos os clientes, mesmo os sem pedidos
SELECT 
    clientes.nome AS cliente,
    pedidos.id AS pedido_id,
    pedidos.valor_total
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- Resultado mostra:
-- João Silva - tem pedidos
-- Maria Santos - tem pedidos
-- Pedro Costa - tem pedidos
-- Ana Oliveira - NULL (sem pedidos)

-- Exemplo 2: Produtos que nunca foram vendidos
SELECT 
    p.nome AS produto,
    p.preco
FROM produtos p
LEFT JOIN itens_pedido ip ON p.id = ip.produto_id
WHERE ip.id IS NULL;

-- Exemplo 3: Categorias e seus produtos (incluindo categorias sem produtos)
SELECT 
    c.nome AS categoria,
    p.nome AS produto
FROM categorias c
LEFT JOIN produtos p ON c.id = p.categoria_id;

-- ============================================
-- RIGHT JOIN (Simulado com LEFT JOIN invertido)
-- ============================================

-- SQLite não suporta RIGHT JOIN, mas podemos simular invertendo as tabelas

-- Exemplo: Todos os pedidos, mesmo os de clientes inexistentes
-- (Neste caso, não temos esse problema, mas mostra a sintaxe)
SELECT 
    p.id AS pedido_id,
    c.nome AS cliente
FROM pedidos p
LEFT JOIN clientes c ON p.cliente_id = c.id;

-- ============================================
-- SUBCONSULTAS (SUBQUERIES)
-- ============================================

-- Exemplo 1: Subconsulta escalar - Clientes acima da idade média
-- (Usando um exemplo com dados que temos)
SELECT 
    nome,
    cidade
FROM clientes
WHERE id IN (
    SELECT DISTINCT cliente_id 
    FROM pedidos 
    WHERE valor_total > (
        SELECT AVG(valor_total) FROM pedidos
    )
);

-- Exemplo 2: Subconsulta com IN - Produtos que foram pedidos
SELECT 
    nome,
    preco
FROM produtos
WHERE id IN (
    SELECT DISTINCT produto_id 
    FROM itens_pedido
);

-- Exemplo 3: Subconsulta correlacionada - Produtos mais caros que a média da categoria
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

-- Exemplo 4: Subconsulta na cláusula FROM
SELECT 
    categoria,
    COUNT(*) AS total_produtos,
    AVG(preco) AS preco_medio
FROM (
    SELECT 
        c.nome AS categoria,
        p.preco
    FROM produtos p
    INNER JOIN categorias c ON p.categoria_id = c.id
    WHERE p.estoque > 0
) AS produtos_com_estoque
GROUP BY categoria;

-- Exemplo 5: Subconsulta com EXISTS
SELECT 
    c.nome
FROM clientes c
WHERE EXISTS (
    SELECT 1 
    FROM pedidos p 
    WHERE p.cliente_id = c.id
);

-- ============================================
-- GROUP BY - Agrupamento de Dados
-- ============================================

-- Exemplo 1: Contar produtos por categoria
SELECT 
    c.nome AS categoria,
    COUNT(*) AS total_produtos
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.id, c.nome;

-- Exemplo 2: Valor total em estoque por categoria
SELECT 
    c.nome AS categoria,
    SUM(p.preco * p.estoque) AS valor_total_estoque
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.id, c.nome;

-- Exemplo 3: Média de preço por categoria
SELECT 
    c.nome AS categoria,
    AVG(p.preco) AS preco_medio,
    MIN(p.preco) AS preco_minimo,
    MAX(p.preco) AS preco_maximo
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.id, c.nome;

-- Exemplo 4: Total de pedidos e valor total por cliente
SELECT 
    c.nome AS cliente,
    COUNT(p.id) AS total_pedidos,
    SUM(p.valor_total) AS valor_total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome;

-- Exemplo 5: Produtos mais vendidos (por quantidade)
SELECT 
    pr.nome AS produto,
    SUM(ip.quantidade) AS total_vendido
FROM produtos pr
INNER JOIN itens_pedido ip ON pr.id = ip.produto_id
GROUP BY pr.id, pr.nome
ORDER BY total_vendido DESC;

-- ============================================
-- HAVING - Filtrar grupos após GROUP BY
-- ============================================

-- Exemplo 1: Categorias com mais de 2 produtos
SELECT 
    c.nome AS categoria,
    COUNT(*) AS total
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.id, c.nome
HAVING COUNT(*) > 2;

-- Exemplo 2: Clientes com valor total de pedidos maior que 1000
SELECT 
    c.nome AS cliente,
    SUM(p.valor_total) AS valor_total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome
HAVING SUM(p.valor_total) > 1000;

-- Exemplo 3: Categorias com valor médio de produtos maior que 500
SELECT 
    c.nome AS categoria,
    AVG(p.preco) AS preco_medio
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.id, c.nome
HAVING AVG(p.preco) > 500;

-- ============================================
-- COMBINAÇÕES COMPLEXAS
-- ============================================

-- Exemplo 1: Clientes que compraram produtos de uma categoria específica
SELECT DISTINCT
    c.nome AS cliente,
    cat.nome AS categoria
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos pr ON ip.produto_id = pr.id
INNER JOIN categorias cat ON pr.categoria_id = cat.id
WHERE cat.nome = 'Eletrônicos';

-- Exemplo 2: Relatório completo de vendas
SELECT 
    c.nome AS cliente,
    p.id AS pedido_id,
    p.data_pedido,
    pr.nome AS produto,
    ip.quantidade,
    ip.subtotal,
    p.valor_total AS total_pedido
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos pr ON ip.produto_id = pr.id
ORDER BY p.data_pedido DESC, c.nome;

-- Exemplo 3: Ranking de produtos por valor total vendido
SELECT 
    pr.nome AS produto,
    COUNT(DISTINCT p.id) AS total_pedidos,
    SUM(ip.quantidade) AS total_unidades_vendidas,
    SUM(ip.subtotal) AS valor_total_vendido
FROM produtos pr
INNER JOIN itens_pedido ip ON pr.id = ip.produto_id
INNER JOIN pedidos p ON ip.pedido_id = p.id
GROUP BY pr.id, pr.nome
ORDER BY valor_total_vendido DESC;

-- ============================================
-- ORDER BY Avançado
-- ============================================

-- Exemplo 1: Ordenação por múltiplas colunas
SELECT 
    c.nome AS categoria,
    p.nome AS produto,
    p.preco
FROM produtos p
INNER JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nome ASC, p.preco DESC;

-- Exemplo 2: Ordenação com CASE (prioridade customizada)
SELECT 
    p.nome,
    p.estoque,
    CASE 
        WHEN p.estoque < 10 THEN 'Crítico'
        WHEN p.estoque < 20 THEN 'Baixo'
        ELSE 'Normal'
    END AS status_estoque
FROM produtos p
ORDER BY 
    CASE 
        WHEN p.estoque < 10 THEN 1
        WHEN p.estoque < 20 THEN 2
        ELSE 3
    END,
    p.nome;

-- ============================================
-- FUNÇÕES ÚTEIS
-- ============================================

-- Contar total de registros em uma tabela
SELECT COUNT(*) AS total_clientes FROM clientes;

-- Verificar se existem registros relacionados
SELECT 
    c.nome,
    CASE 
        WHEN EXISTS (SELECT 1 FROM pedidos WHERE cliente_id = c.id)
        THEN 'Tem pedidos'
        ELSE 'Sem pedidos'
    END AS status
FROM clientes c;

-- ============================================
-- NOTAS FINAIS
-- ============================================

/*
 * DICAS IMPORTANTES:
 * 
 * 1. Sempre use aliases (AS) para tornar queries mais legíveis
 * 2. Prefira INNER JOIN quando precisar apenas de correspondências
 * 3. Use LEFT JOIN quando precisar incluir todos os registros de uma tabela
 * 4. Subconsultas podem ser mais lentas - avalie se JOIN não resolve
 * 5. GROUP BY requer que todas as colunas no SELECT sejam agregadas ou estejam no GROUP BY
 * 6. HAVING filtra grupos, WHERE filtra registros
 * 7. Sempre teste queries complexas em dados de exemplo primeiro
 */

