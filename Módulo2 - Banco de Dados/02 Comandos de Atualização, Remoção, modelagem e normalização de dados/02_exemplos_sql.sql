-- ============================================
-- 02 - Exemplos Práticos de UPDATE e DELETE
-- Módulo 02 - Comandos de Atualização, Remoção, Modelagem e Normalização
-- ============================================

-- IMPORTANTE: Execute primeiro o script do Módulo 01 para criar as tabelas
-- ou copie as tabelas aqui antes de executar este script.

-- ============================================
-- PREPARAÇÃO: Criar tabelas se não existirem
-- ============================================

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    idade INTEGER,
    cidade VARCHAR(50),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50),
    estoque INTEGER DEFAULT 0
);

-- Inserir dados de exemplo se não existirem
INSERT OR IGNORE INTO clientes (nome, email, idade, cidade)
VALUES 
    ('João Silva', 'joao.silva@email.com', 25, 'São Paulo'),
    ('Maria Santos', 'maria.santos@email.com', 30, 'Rio de Janeiro'),
    ('Pedro Costa', 'pedro.costa@email.com', 22, 'Belo Horizonte'),
    ('Ana Oliveira', 'ana.oliveira@email.com', 28, 'São Paulo'),
    ('Carlos Souza', 'carlos.souza@email.com', 35, 'Porto Alegre');

INSERT OR IGNORE INTO produtos (nome, preco, categoria, estoque)
VALUES 
    ('Notebook', 2999.99, 'Eletrônicos', 15),
    ('Mouse', 49.90, 'Acessórios', 50),
    ('Teclado', 199.90, 'Acessórios', 30),
    ('Monitor', 799.90, 'Eletrônicos', 20);

-- ============================================
-- COMANDO UPDATE - ATUALIZAÇÃO DE DADOS
-- ============================================

-- Exemplo 1: Atualizar um único registro por ID
-- ⚠️ IMPORTANTE: Sempre use WHERE para evitar atualizar todos os registros!
UPDATE clientes
SET idade = 26
WHERE id = 1;

-- Verificar o resultado
SELECT * FROM clientes WHERE id = 1;

-- Exemplo 2: Atualizar múltiplas colunas
UPDATE clientes
SET idade = 31, cidade = 'São Paulo - SP'
WHERE email = 'maria.santos@email.com';

-- Verificar o resultado
SELECT * FROM clientes WHERE email = 'maria.santos@email.com';

-- Exemplo 3: Atualizar múltiplos registros (todos que atendem a condição)
-- Atualizar idade de todos os clientes de São Paulo
UPDATE clientes
SET idade = idade + 1
WHERE cidade = 'São Paulo';

-- Verificar quantos registros foram atualizados
SELECT COUNT(*) AS atualizados FROM clientes WHERE cidade = 'São Paulo';

-- Exemplo 4: Atualizar usando cálculo
-- Aumentar preço de todos os produtos em 10%
UPDATE produtos
SET preco = preco * 1.10
WHERE categoria = 'Eletrônicos';

-- Verificar o resultado
SELECT nome, preco FROM produtos WHERE categoria = 'Eletrônicos';

-- Exemplo 5: Atualizar baseado em outra coluna
-- Reduzir estoque quando preço for maior que 500
UPDATE produtos
SET estoque = estoque - 5
WHERE preco > 500;

-- Verificar o resultado
SELECT nome, preco, estoque FROM produtos WHERE preco > 500;

-- Exemplo 6: Atualizar com condição complexa (AND, OR)
-- Atualizar cidade de clientes jovens de São Paulo
UPDATE clientes
SET cidade = 'São Paulo - Capital'
WHERE cidade = 'São Paulo' AND idade < 30;

-- Verificar
SELECT * FROM clientes WHERE cidade LIKE 'São Paulo%';

-- Exemplo 7: Atualizar baseado em lista (IN)
UPDATE produtos
SET categoria = 'Informática'
WHERE categoria IN ('Eletrônicos', 'Acessórios');

-- Verificar
SELECT DISTINCT categoria FROM produtos;

-- Exemplo 8: Atualizar com valor NULL
-- Marcar estoque como NULL para produtos sem estoque (exemplo didático)
-- ⚠️ Geralmente não é boa prática, mas demonstra a possibilidade
UPDATE produtos
SET estoque = NULL
WHERE estoque = 0;

-- Reverter (desfazer exemplo 8)
UPDATE produtos
SET estoque = 0
WHERE estoque IS NULL;

-- ============================================
-- BOAS PRÁTICAS: SEMPRE VERIFICAR ANTES DE ATUALIZAR
-- ============================================

-- ❌ ERRADO: Atualizar sem verificar
-- UPDATE clientes SET idade = 30 WHERE nome LIKE '%João%';

-- ✅ CORRETO: Verificar primeiro com SELECT
-- Passo 1: Ver quais registros serão afetados
SELECT * FROM clientes WHERE nome LIKE '%João%';

-- Passo 2: Se estiver correto, fazer o UPDATE
-- UPDATE clientes SET idade = 30 WHERE nome LIKE '%João%';

-- ============================================
-- COMANDO DELETE - REMOÇÃO DE DADOS
-- ============================================

-- ⚠️ ATENÇÃO CRÍTICA: DELETE sem WHERE remove TODOS os registros!
-- ⚠️ Sempre teste com SELECT primeiro!

-- Exemplo 1: Remover um único registro por ID
-- Primeiro, verificar o que será removido
SELECT * FROM clientes WHERE id = 5;

-- Depois, remover (se estiver correto)
-- DELETE FROM clientes WHERE id = 5;

-- Exemplo 2: Remover múltiplos registros baseado em condição
-- Remover produtos sem estoque
SELECT * FROM produtos WHERE estoque = 0;

-- Se estiver correto:
-- DELETE FROM produtos WHERE estoque = 0;

-- Exemplo 3: Remover com condição complexa
-- Remover clientes jovens de uma cidade específica
SELECT * FROM clientes WHERE idade < 25 AND cidade = 'Belo Horizonte';

-- Se estiver correto:
-- DELETE FROM clientes WHERE idade < 25 AND cidade = 'Belo Horizonte';

-- Exemplo 4: Remover com IN
-- Remover produtos de categorias específicas (exemplo didático - geralmente não recomendado)
SELECT * FROM produtos WHERE categoria IN ('Acessórios');

-- Se estiver correto:
-- DELETE FROM produtos WHERE categoria IN ('Acessórios');

-- ============================================
-- COMPARAÇÃO: DELETE vs TRUNCATE vs DROP
-- ============================================

-- DELETE: Remove registros específicos (com WHERE)
-- DELETE FROM clientes WHERE id = 1;

-- TRUNCATE: Remove TODOS os registros da tabela (mais rápido que DELETE)
-- Não funciona no SQLite diretamente, mas existe em outros SGBDs:
-- TRUNCATE TABLE clientes;

-- No SQLite, equivalente é:
-- DELETE FROM clientes;  -- Remove todos os registros
-- E depois:
-- VACUUM;  -- Recupera espaço

-- DROP: Remove a tabela inteira (estrutura e dados)
-- ⚠️ MUITO PERIGOSO!
-- DROP TABLE clientes;

-- ============================================
-- TRANSACções - REVERTER OPERAÇÕES
-- ============================================

-- Usar transações permite reverter operações se algo der errado

-- Iniciar transação (SQLite começa automaticamente)
BEGIN TRANSACTION;

-- Executar operações
UPDATE clientes SET idade = 100 WHERE id = 1;

-- Verificar se está correto
SELECT * FROM clientes WHERE id = 1;

-- Se estiver correto, confirmar:
COMMIT;

-- OU se estiver errado, reverter:
-- ROLLBACK;

-- ============================================
-- EXEMPLOS DE MODELAGEM
-- ============================================

-- Exemplo: Tabela não normalizada (PROBLEMA)
CREATE TABLE IF NOT EXISTS pedidos_nao_normalizado (
    id INTEGER PRIMARY KEY,
    cliente_nome VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_cidade VARCHAR(50),
    produto_nome VARCHAR(100),
    produto_preco DECIMAL(10,2),
    produto_categoria VARCHAR(50),
    quantidade INTEGER,
    valor_total DECIMAL(10,2)
);

-- Problemas:
-- 1. Dados duplicados (cliente repetido em cada pedido)
-- 2. Inconsistências (se email mudar, precisa atualizar todos os pedidos)
-- 3. Espaço desperdiçado

-- Exemplo: Tabelas normalizadas (SOLUÇÃO)
-- Já temos clientes e produtos criados acima

-- Criar tabela de pedidos normalizada
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

-- Vantagens:
-- 1. Dados do cliente em um só lugar
-- 2. Facilita atualizações
-- 3. Melhor integridade
-- 4. Economia de espaço

-- Inserir exemplo de pedido normalizado
INSERT INTO pedidos (cliente_id, valor_total)
VALUES (1, 3249.89);

INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
VALUES 
    (1, 1, 1, 2999.99, 2999.99),  -- Notebook
    (1, 2, 5, 49.90, 249.90);      -- Mouse (5 unidades)

-- Consultar pedido com informações relacionadas
SELECT 
    p.id AS pedido_id,
    c.nome AS cliente,
    pr.nome AS produto,
    ip.quantidade,
    ip.preco_unitario,
    ip.subtotal
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
JOIN itens_pedido ip ON p.id = ip.pedido_id
JOIN produtos pr ON ip.produto_id = pr.id
WHERE p.id = 1;

-- ============================================
-- EXEMPLOS DE NORMALIZAÇÃO
-- ============================================

-- 1ª FORMA NORMAL (1FN): Valores atômicos

-- ❌ NÃO normalizado - telefones múltiplos em uma coluna
CREATE TABLE IF NOT EXISTS clientes_nao_1fn (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    telefones VARCHAR(200)  -- PROBLEMA: múltiplos valores
);

-- ✅ Normalizado - tabela separada para telefones
CREATE TABLE IF NOT EXISTS telefones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    numero VARCHAR(20) NOT NULL,
    tipo VARCHAR(20),  -- 'celular', 'residencial', 'comercial'
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- 2ª FORMA NORMAL (2FN): Dependência completa da chave primária

-- Já está normalizado se cada atributo depende da chave primária completa

-- 3ª FORMA NORMAL (3FN): Sem dependências transitivas

-- ❌ NÃO normalizado - estado depende de cidade
CREATE TABLE IF NOT EXISTS clientes_nao_3fn (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(50)  -- PROBLEMA: estado depende de cidade, não de id
);

-- ✅ Normalizado - tabela separada para cidades
CREATE TABLE IF NOT EXISTS cidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    UNIQUE(nome, estado)
);

-- Adicionar cidade_id na tabela clientes
-- ALTER TABLE clientes ADD COLUMN cidade_id INTEGER;
-- ALTER TABLE clientes ADD FOREIGN KEY (cidade_id) REFERENCES cidades(id);

-- ============================================
-- NOTAS FINAIS
-- ============================================

/*
 * LEMBRETES IMPORTANTES:
 * 
 * 1. SEMPRE use WHERE em UPDATE e DELETE
 * 2. SEMPRE teste com SELECT antes de modificar
 * 3. USE transações para operações críticas
 * 4. FAÇA backup antes de operações em massa
 * 5. Normalize para integridade, mas balance com performance
 * 6. Use chaves estrangeiras para integridade referencial
 */

