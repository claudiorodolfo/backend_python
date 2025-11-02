"""
04 - Exemplos Práticos com SQLite e Python
Módulo 01 - Introdução a SQL – Comandos Básicos

Este script demonstra como usar SQLite (biblioteca nativa do Python)
para criar banco de dados, tabelas e executar comandos SELECT e INSERT.
"""

import sqlite3
import os
from datetime import date

# Nome do arquivo de banco de dados
DB_FILE = 'exemplo_db.sqlite'

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_FILE)
    return conn

def criar_tabelas(conn):
    """Cria as tabelas necessárias no banco de dados."""
    cursor = conn.cursor()
    
    # Criar tabela de clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            idade INTEGER,
            cidade VARCHAR(50),
            data_cadastro DATE DEFAULT CURRENT_DATE
        )
    ''')
    
    # Criar tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            preco DECIMAL(10, 2) NOT NULL,
            categoria VARCHAR(50),
            estoque INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    print("✓ Tabelas criadas com sucesso!")

def inserir_dados(conn):
    """Insere dados de exemplo nas tabelas."""
    cursor = conn.cursor()
    
    # Inserir clientes
    clientes = [
        ('João Silva', 'joao.silva@email.com', 25, 'São Paulo'),
        ('Maria Santos', 'maria.santos@email.com', 30, 'Rio de Janeiro'),
        ('Pedro Costa', 'pedro.costa@email.com', 22, 'Belo Horizonte'),
        ('Ana Oliveira', 'ana.oliveira@email.com', 28, 'São Paulo'),
        ('Carlos Souza', 'carlos.souza@email.com', 35, 'Porto Alegre'),
        ('Julia Ferreira', 'julia.ferreira@email.com', 27, 'Curitiba'),
    ]
    
    cursor.executemany('''
        INSERT INTO clientes (nome, email, idade, cidade)
        VALUES (?, ?, ?, ?)
    ''', clientes)
    
    # Inserir produtos
    produtos = [
        ('Notebook', 2999.99, 'Eletrônicos', 15),
        ('Mouse', 49.90, 'Acessórios', 50),
        ('Teclado', 199.90, 'Acessórios', 30),
        ('Monitor', 799.90, 'Eletrônicos', 20),
        ('Headset', 299.90, 'Acessórios', 25),
    ]
    
    cursor.executemany('''
        INSERT INTO produtos (nome, preco, categoria, estoque)
        VALUES (?, ?, ?, ?)
    ''', produtos)
    
    conn.commit()
    print("✓ Dados inseridos com sucesso!")

def exemplo_select_todos(conn):
    """Exemplo: SELECT * - selecionar todas as colunas."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 1: SELECT * FROM clientes")
    print("="*60)
    
    cursor.execute('SELECT * FROM clientes')
    resultados = cursor.fetchall()
    
    print(f"\nTotal de registros: {len(resultados)}\n")
    for registro in resultados:
        print(f"ID: {registro[0]}, Nome: {registro[1]}, Email: {registro[2]}, "
              f"Idade: {registro[3]}, Cidade: {registro[4]}")

def exemplo_select_colunas_especificas(conn):
    """Exemplo: SELECT colunas específicas."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 2: SELECT nome, email FROM clientes")
    print("="*60)
    
    cursor.execute('SELECT nome, email FROM clientes')
    resultados = cursor.fetchall()
    
    print("\nNome\t\t\tEmail")
    print("-" * 60)
    for registro in resultados:
        print(f"{registro[0]}\t\t{registro[1]}")

def exemplo_where(conn):
    """Exemplos de uso de WHERE para filtrar dados."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 3: WHERE - Filtros")
    print("="*60)
    
    # Idade maior que 25
    print("\n--- Clientes com idade > 25 ---")
    cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 25')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"{registro[0]}: {registro[1]} anos")
    
    # Cidade específica
    print("\n--- Clientes de São Paulo ---")
    cursor.execute("SELECT nome, cidade FROM clientes WHERE cidade = 'São Paulo'")
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"{registro[0]}: {registro[1]}")
    
    # Múltiplas condições com AND
    print("\n--- Clientes de SP com idade > 25 ---")
    cursor.execute("""
        SELECT nome, idade, cidade 
        FROM clientes 
        WHERE cidade = 'São Paulo' AND idade > 25
    """)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"{registro[0]}: {registro[1]} anos, {registro[2]}")

def exemplo_order_by(conn):
    """Exemplos de ORDER BY para ordenação."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 4: ORDER BY - Ordenação")
    print("="*60)
    
    # Ordenar por nome (crescente)
    print("\n--- Clientes ordenados por nome (A-Z) ---")
    cursor.execute('SELECT nome FROM clientes ORDER BY nome ASC')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}")
    
    # Ordenar por idade (decrescente)
    print("\n--- Clientes ordenados por idade (mais velhos primeiro) ---")
    cursor.execute('SELECT nome, idade FROM clientes ORDER BY idade DESC')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}: {registro[1]} anos")
    
    # Ordenar por múltiplas colunas
    print("\n--- Clientes ordenados por cidade e depois nome ---")
    cursor.execute('SELECT nome, cidade FROM clientes ORDER BY cidade ASC, nome ASC')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}: {registro[1]}")

def exemplo_limit(conn):
    """Exemplos de LIMIT para limitar resultados."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 5: LIMIT - Limitar resultados")
    print("="*60)
    
    # Primeiros 3 clientes
    print("\n--- Primeiros 3 clientes ---")
    cursor.execute('SELECT nome FROM clientes LIMIT 3')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}")
    
    # Top 3 produtos mais caros
    print("\n--- Top 3 produtos mais caros ---")
    cursor.execute('SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 3')
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}: R$ {registro[1]:.2f}")

def exemplo_combinacoes(conn):
    """Exemplos combinando WHERE, ORDER BY e LIMIT."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 6: Combinações de cláusulas")
    print("="*60)
    
    # Produtos da categoria 'Acessórios' ordenados por preço
    print("\n--- Acessórios ordenados por preço ---")
    cursor.execute("""
        SELECT nome, preco, categoria 
        FROM produtos 
        WHERE categoria = 'Acessórios' 
        ORDER BY preco ASC
    """)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}: R$ {registro[1]:.2f} ({registro[2]})")
    
    # Clientes de SP com idade > 25, ordenados por nome, limitado a 2
    print("\n--- 2 primeiros clientes de SP com mais de 25 anos (ordenados por nome) ---")
    cursor.execute("""
        SELECT nome, idade, cidade 
        FROM clientes 
        WHERE cidade = 'São Paulo' AND idade > 25 
        ORDER BY nome ASC 
        LIMIT 2
    """)
    resultados = cursor.fetchall()
    for registro in resultados:
        print(f"  {registro[0]}: {registro[1]} anos, {registro[2]}")

def exemplo_insert_individual(conn):
    """Exemplo de inserção de um único registro."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 7: INSERT INTO - Inserir um registro")
    print("="*60)
    
    # Inserir um novo cliente
    cursor.execute('''
        INSERT INTO clientes (nome, email, idade, cidade)
        VALUES (?, ?, ?, ?)
    ''', ('Roberto Alves', 'roberto.alves@email.com', 40, 'Brasília'))
    
    conn.commit()
    print("✓ Novo cliente inserido!")
    
    # Verificar o registro inserido
    cursor.execute("SELECT * FROM clientes WHERE nome = 'Roberto Alves'")
    resultado = cursor.fetchone()
    print(f"\nCliente inserido: {resultado}")

def limpar_banco():
    """Remove o arquivo de banco de dados se existir."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"✓ Banco de dados '{DB_FILE}' removido.")

def main():
    """Função principal que executa todos os exemplos."""
    print("="*60)
    print("EXEMPLOS PRÁTICOS: SQLite com Python")
    print("Módulo 01 - Introdução a SQL – Comandos Básicos")
    print("="*60)
    
    # Limpar banco anterior (opcional - descomente se quiser começar do zero)
    # limpar_banco()
    
    # Criar conexão
    conn = criar_conexao()
    
    try:
        # Criar tabelas
        criar_tabelas(conn)
        
        # Verificar se já existem dados
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clientes')
        count = cursor.fetchone()[0]
        
        if count == 0:
            # Inserir dados apenas se a tabela estiver vazia
            inserir_dados(conn)
        else:
            print(f"✓ Banco de dados já contém {count} clientes.")
        
        # Executar exemplos
        exemplo_select_todos(conn)
        exemplo_select_colunas_especificas(conn)
        exemplo_where(conn)
        exemplo_order_by(conn)
        exemplo_limit(conn)
        exemplo_combinacoes(conn)
        exemplo_insert_individual(conn)
        
        print("\n" + "="*60)
        print("✓ Todos os exemplos foram executados!")
        print(f"✓ Banco de dados salvo em: {DB_FILE}")
        print("="*60)
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao executar operação: {e}")
    finally:
        # Fechar conexão
        conn.close()
        print("\n✓ Conexão fechada.")

if __name__ == '__main__':
    main()

