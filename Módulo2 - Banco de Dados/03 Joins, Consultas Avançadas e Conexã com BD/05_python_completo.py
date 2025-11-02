"""
05 - Exemplos Completos: Conexão Python com Banco de Dados
Módulo 03 - JOINs, Consultas Avançadas e Conexão com BD

Este script demonstra:
- Conexão com SQLite usando Python
- Criação de tabelas relacionadas
- Inserção de dados
- Consultas com JOINs
- Subconsultas
- GROUP BY e agregações
- Boas práticas e context managers
"""

import sqlite3
import os
from datetime import date
from contextlib import contextmanager

DB_FILE = 'exemplo_joins.db'

@contextmanager
def get_connection():
    """Context manager para gerenciar conexões com o banco de dados."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def criar_banco_completo():
    """Cria o banco de dados completo com todas as tabelas relacionadas."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Criar tabelas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL UNIQUE
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                preco DECIMAL(10, 2) NOT NULL,
                categoria_id INTEGER,
                estoque INTEGER DEFAULT 0,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                cidade VARCHAR(50)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                data_pedido DATE DEFAULT CURRENT_DATE,
                valor_total DECIMAL(10,2),
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario DECIMAL(10,2) NOT NULL,
                subtotal DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        ''')
        
        # Verificar se já existem dados
        cursor.execute('SELECT COUNT(*) FROM categorias')
        if cursor.fetchone()[0] == 0:
            # Inserir dados de exemplo
            categorias = [
                ('Eletrônicos',),
                ('Acessórios',),
                ('Informática',)
            ]
            cursor.executemany('INSERT INTO categorias (nome) VALUES (?)', categorias)
            
            produtos = [
                ('Notebook', 2999.99, 1, 15),
                ('Mouse', 49.90, 2, 50),
                ('Teclado', 199.90, 2, 30),
                ('Monitor', 799.90, 1, 20),
                ('Headset', 299.90, 2, 25),
            ]
            cursor.executemany('''
                INSERT INTO produtos (nome, preco, categoria_id, estoque)
                VALUES (?, ?, ?, ?)
            ''', produtos)
            
            clientes = [
                ('João Silva', 'joao.silva@email.com', 'São Paulo'),
                ('Maria Santos', 'maria.santos@email.com', 'Rio de Janeiro'),
                ('Pedro Costa', 'pedro.costa@email.com', 'Belo Horizonte'),
            ]
            cursor.executemany('''
                INSERT INTO clientes (nome, email, cidade)
                VALUES (?, ?, ?)
            ''', clientes)
            
            pedidos = [
                (1, 3249.89),
                (1, 199.90),
                (2, 799.90),
            ]
            cursor.executemany('''
                INSERT INTO pedidos (cliente_id, valor_total)
                VALUES (?, ?)
            ''', pedidos)
            
            itens = [
                (1, 1, 1, 2999.99, 2999.99),  # Pedido 1: Notebook
                (1, 2, 5, 49.90, 249.90),    # Pedido 1: 5 Mouses
                (2, 3, 1, 199.90, 199.90),    # Pedido 2: Teclado
                (3, 4, 1, 799.90, 799.90),     # Pedido 3: Monitor
            ]
            cursor.executemany('''
                INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
                VALUES (?, ?, ?, ?, ?)
            ''', itens)
            
            conn.commit()
            print("✓ Banco de dados criado e populado com dados de exemplo!")
        else:
            print("✓ Banco de dados já existe com dados.")

def exemplo_inner_join():
    """Exemplo 1: INNER JOIN - Clientes e seus pedidos."""
    print("\n" + "="*60)
    print("EXEMPLO 1: INNER JOIN - Clientes e Pedidos")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT 
                c.nome AS cliente,
                p.id AS pedido_id,
                p.data_pedido,
                p.valor_total
            FROM clientes c
            INNER JOIN pedidos p ON c.id = p.cliente_id
        ''')
        
        resultados = cursor.fetchall()
        print("\nCliente\t\t\tPedido ID\tData\t\tValor Total")
        print("-" * 60)
        for row in resultados:
            print(f"{row['cliente']}\t\t{row['pedido_id']}\t\t{row['data_pedido']}\tR$ {row['valor_total']:.2f}")

def exemplo_left_join():
    """Exemplo 2: LEFT JOIN - Todos os clientes, incluindo sem pedidos."""
    print("\n" + "="*60)
    print("EXEMPLO 2: LEFT JOIN - Todos os Clientes")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT 
                c.nome AS cliente,
                p.id AS pedido_id,
                p.valor_total
            FROM clientes c
            LEFT JOIN pedidos p ON c.id = p.cliente_id
        ''')
        
        resultados = cursor.fetchall()
        print("\nCliente\t\t\tPedido ID\tValor Total")
        print("-" * 60)
        for row in resultados:
            pedido_id = row['pedido_id'] if row['pedido_id'] else 'Sem pedidos'
            valor = f"R$ {row['valor_total']:.2f}" if row['valor_total'] else 'N/A'
            print(f"{row['cliente']}\t\t{pedido_id}\t\t{valor}")

def exemplo_multiplos_joins():
    """Exemplo 3: Múltiplos JOINs - Relatório completo."""
    print("\n" + "="*60)
    print("EXEMPLO 3: Múltiplos JOINs - Relatório Completo")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
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
            INNER JOIN produtos pr ON ip.produto_id = pr.id
            ORDER BY c.nome, p.id
        ''')
        
        resultados = cursor.fetchall()
        print("\nCliente\t\tPedido\tProduto\t\tQtd\tPreço Unit.\tSubtotal")
        print("-" * 70)
        for row in resultados:
            print(f"{row['cliente']}\t{row['pedido_id']}\t{row['produto']}\t{row['quantidade']}\t"
                  f"R$ {row['preco_unitario']:.2f}\tR$ {row['subtotal']:.2f}")

def exemplo_group_by():
    """Exemplo 4: GROUP BY - Agregações."""
    print("\n" + "="*60)
    print("EXEMPLO 4: GROUP BY - Agregações")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Total de pedidos e valor por cliente
        print("\n--- Total de Pedidos e Valor por Cliente ---")
        cursor.execute('''
            SELECT 
                c.nome AS cliente,
                COUNT(p.id) AS total_pedidos,
                SUM(p.valor_total) AS valor_total
            FROM clientes c
            LEFT JOIN pedidos p ON c.id = p.cliente_id
            GROUP BY c.id, c.nome
        ''')
        
        resultados = cursor.fetchall()
        print("Cliente\t\t\tPedidos\tValor Total")
        print("-" * 50)
        for row in resultados:
            print(f"{row['cliente']}\t\t{row['total_pedidos']}\tR$ {row['valor_total'] or 0:.2f}")
        
        # Produtos por categoria
        print("\n--- Produtos por Categoria ---")
        cursor.execute('''
            SELECT 
                cat.nome AS categoria,
                COUNT(p.id) AS total_produtos,
                AVG(p.preco) AS preco_medio
            FROM categorias cat
            LEFT JOIN produtos p ON cat.id = p.categoria_id
            GROUP BY cat.id, cat.nome
        ''')
        
        resultados = cursor.fetchall()
        print("Categoria\t\tProdutos\tPreço Médio")
        print("-" * 50)
        for row in resultados:
            print(f"{row['categoria']}\t\t{row['total_produtos']}\t\tR$ {row['preco_medio'] or 0:.2f}")

def exemplo_having():
    """Exemplo 5: HAVING - Filtrar grupos."""
    print("\n" + "="*60)
    print("EXEMPLO 5: HAVING - Filtrar Grupos")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Categorias com mais de 1 produto
        cursor.execute('''
            SELECT 
                cat.nome AS categoria,
                COUNT(p.id) AS total_produtos
            FROM categorias cat
            INNER JOIN produtos p ON cat.id = p.categoria_id
            GROUP BY cat.id, cat.nome
            HAVING COUNT(p.id) > 1
        ''')
        
        resultados = cursor.fetchall()
        print("\n--- Categorias com mais de 1 produto ---")
        print("Categoria\t\tTotal de Produtos")
        print("-" * 40)
        for row in resultados:
            print(f"{row['categoria']}\t\t{row['total_produtos']}")

def exemplo_subconsulta():
    """Exemplo 6: Subconsultas."""
    print("\n" + "="*60)
    print("EXEMPLO 6: Subconsultas")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Clientes que fizeram pedidos acima da média
        cursor.execute('''
            SELECT 
                c.nome,
                p.valor_total
            FROM clientes c
            INNER JOIN pedidos p ON c.id = p.cliente_id
            WHERE p.valor_total > (
                SELECT AVG(valor_total) FROM pedidos
            )
        ''')
        
        resultados = cursor.fetchall()
        print("\n--- Clientes com pedidos acima da média ---")
        print("Cliente\t\t\tValor Total")
        print("-" * 40)
        for row in resultados:
            print(f"{row['nome']}\t\tR$ {row['valor_total']:.2f}")
        
        # Produtos que foram pedidos (com IN)
        cursor.execute('''
            SELECT nome, preco
            FROM produtos
            WHERE id IN (
                SELECT DISTINCT produto_id FROM itens_pedido
            )
        ''')
        
        resultados = cursor.fetchall()
        print("\n--- Produtos que foram pedidos ---")
        print("Produto\t\t\tPreço")
        print("-" * 40)
        for row in resultados:
            print(f"{row['nome']}\t\tR$ {row['preco']:.2f}")

def exemplo_inserir_dados():
    """Exemplo 7: Inserir dados via Python."""
    print("\n" + "="*60)
    print("EXEMPLO 7: Inserir Dados via Python")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Inserir um novo cliente
        print("\n--- Inserindo novo cliente ---")
        cursor.execute('''
            INSERT INTO clientes (nome, email, cidade)
            VALUES (?, ?, ?)
        ''', ('Ana Oliveira', 'ana.oliveira@email.com', 'Curitiba'))
        
        # Obter o ID do cliente inserido
        cliente_id = cursor.lastrowid
        print(f"✓ Cliente inserido com ID: {cliente_id}")
        
        # Inserir um pedido para este cliente
        cursor.execute('''
            INSERT INTO pedidos (cliente_id, valor_total)
            VALUES (?, ?)
        ''', (cliente_id, 499.90))
        
        pedido_id = cursor.lastrowid
        print(f"✓ Pedido criado com ID: {pedido_id}")
        
        # Inserir itens do pedido
        cursor.execute('SELECT id FROM produtos WHERE nome = ?', ('Headset',))
        produto_id = cursor.fetchone()['id']
        
        cursor.execute('''
            INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
            VALUES (?, ?, ?, ?, ?)
        ''', (pedido_id, produto_id, 1, 299.90, 299.90))
        
        print("✓ Item do pedido inserido")
        print("\n✓ Dados inseridos com sucesso!")

def exemplo_buscar_um_registro():
    """Exemplo 8: Buscar um único registro."""
    print("\n" + "="*60)
    print("EXEMPLO 8: Buscar um Único Registro")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Buscar um cliente específico
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (1,))
        cliente = cursor.fetchone()
        
        if cliente:
            print(f"\nCliente encontrado:")
            print(f"  ID: {cliente['id']}")
            print(f"  Nome: {cliente['nome']}")
            print(f"  Email: {cliente['email']}")
            print(f"  Cidade: {cliente['cidade']}")
        else:
            print("Cliente não encontrado")

def exemplo_context_manager():
    """Exemplo 9: Usando context manager para segurança."""
    print("\n" + "="*60)
    print("EXEMPLO 9: Context Manager para Gerenciar Conexões")
    print("="*60)
    
    # O contexto manager garante commit/rollback automático
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # Operações que podem falhar
            cursor.execute('SELECT * FROM clientes WHERE id = 999')
            resultado = cursor.fetchone()
            
            if not resultado:
                print("Registro não encontrado (operacao simulada)")
            
            # Se tudo correr bem, commit automático
            # Se houver erro, rollback automático
            
    except Exception as e:
        print(f"Erro capturado: {e}")
        print("Rollback automático executado")

def exemplo_row_factory():
    """Exemplo 10: Usando row_factory para acesso por nome."""
    print("\n" + "="*60)
    print("EXEMPLO 10: Row Factory - Acesso por Nome de Coluna")
    print("="*60)
    
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM clientes LIMIT 1')
        row = cursor.fetchone()
        
        print("\nAcesso por nome de coluna:")
        print(f"  row['nome']: {row['nome']}")
        print(f"  row['email']: {row['email']}")
        print(f"\nAcesso por índice (também funciona):")
        print(f"  row[1]: {row[1]}")
        print(f"  row[2]: {row[2]}")

def main():
    """Função principal."""
    print("="*60)
    print("EXEMPLOS COMPLETOS: Conexão Python com Banco de Dados")
    print("Módulo 03 - JOINs, Consultas Avançadas e Conexão com BD")
    print("="*60)
    
    # Criar banco de dados
    criar_banco_completo()
    
    # Executar exemplos
    exemplo_inner_join()
    exemplo_left_join()
    exemplo_multiplos_joins()
    exemplo_group_by()
    exemplo_having()
    exemplo_subconsulta()
    exemplo_inserir_dados()
    exemplo_buscar_um_registro()
    exemplo_context_manager()
    exemplo_row_factory()
    
    print("\n" + "="*60)
    print("✓ Todos os exemplos foram executados!")
    print(f"✓ Banco de dados: {DB_FILE}")
    print("="*60)

if __name__ == '__main__':
    main()

