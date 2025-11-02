"""
05 - Exemplos Práticos com Python: UPDATE, DELETE, Modelagem
Módulo 02 - Comandos de Atualização, Remoção, Modelagem e Normalização

Este script demonstra como usar Python com SQLite para:
- Atualizar dados com UPDATE
- Remover dados com DELETE
- Trabalhar com transações
- Boas práticas de segurança
"""

import sqlite3
import os
from datetime import date

DB_FILE = 'exemplo_db.sqlite'

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_FILE)
    return conn

def preparar_banco(conn):
    """Prepara o banco de dados com tabelas e dados de exemplo."""
    cursor = conn.cursor()
    
    # Criar tabelas
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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            preco DECIMAL(10, 2) NOT NULL,
            categoria VARCHAR(50),
            estoque INTEGER DEFAULT 0
        )
    ''')
    
    # Verificar se já existem dados
    cursor.execute('SELECT COUNT(*) FROM clientes')
    count_clientes = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM produtos')
    count_produtos = cursor.fetchone()[0]
    
    if count_clientes == 0:
        # Inserir clientes de exemplo
        clientes = [
            ('João Silva', 'joao.silva@email.com', 25, 'São Paulo'),
            ('Maria Santos', 'maria.santos@email.com', 30, 'Rio de Janeiro'),
            ('Pedro Costa', 'pedro.costa@email.com', 22, 'Belo Horizonte'),
            ('Ana Oliveira', 'ana.oliveira@email.com', 28, 'São Paulo'),
            ('Carlos Souza', 'carlos.souza@email.com', 35, 'Porto Alegre'),
        ]
        cursor.executemany('''
            INSERT INTO clientes (nome, email, idade, cidade)
            VALUES (?, ?, ?, ?)
        ''', clientes)
    
    if count_produtos == 0:
        # Inserir produtos de exemplo
        produtos = [
            ('Notebook', 2999.99, 'Eletrônicos', 15),
            ('Mouse', 49.90, 'Acessórios', 50),
            ('Teclado', 199.90, 'Acessórios', 30),
            ('Monitor', 799.90, 'Eletrônicos', 20),
        ]
        cursor.executemany('''
            INSERT INTO produtos (nome, preco, categoria, estoque)
            VALUES (?, ?, ?, ?)
        ''', produtos)
    
    conn.commit()
    print("✓ Banco de dados preparado!")

def exemplo_update_simples(conn):
    """Exemplo 1: UPDATE simples - atualizar um único registro."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 1: UPDATE Simples")
    print("="*60)
    
    # Mostrar dados antes
    print("\n--- Antes da atualização ---")
    cursor.execute('SELECT * FROM clientes WHERE id = 1')
    antes = cursor.fetchone()
    print(f"Cliente: {antes[1]}, Idade: {antes[3]}")
    
    # Atualizar
    cursor.execute('''
        UPDATE clientes 
        SET idade = ? 
        WHERE id = ?
    ''', (26, 1))
    
    conn.commit()
    
    # Mostrar dados depois
    print("\n--- Depois da atualização ---")
    cursor.execute('SELECT * FROM clientes WHERE id = 1')
    depois = cursor.fetchone()
    print(f"Cliente: {depois[1]}, Idade: {depois[3]}")
    print(f"✓ Registros atualizados: {cursor.rowcount}")

def exemplo_update_multiplas_colunas(conn):
    """Exemplo 2: UPDATE com múltiplas colunas."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 2: UPDATE com Múltiplas Colunas")
    print("="*60)
    
    # Mostrar antes
    print("\n--- Antes ---")
    cursor.execute("SELECT * FROM clientes WHERE email = 'maria.santos@email.com'")
    antes = cursor.fetchone()
    print(f"Nome: {antes[1]}, Idade: {antes[3]}, Cidade: {antes[4]}")
    
    # Atualizar múltiplas colunas
    cursor.execute('''
        UPDATE clientes
        SET idade = ?, cidade = ?
        WHERE email = ?
    ''', (31, 'Rio de Janeiro - RJ', 'maria.santos@email.com'))
    
    conn.commit()
    
    # Mostrar depois
    print("\n--- Depois ---")
    cursor.execute("SELECT * FROM clientes WHERE email = 'maria.santos@email.com'")
    depois = cursor.fetchone()
    print(f"Nome: {depois[1]}, Idade: {depois[3]}, Cidade: {depois[4]}")
    print(f"✓ Registros atualizados: {cursor.rowcount}")

def exemplo_update_calculo(conn):
    """Exemplo 3: UPDATE com cálculo."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 3: UPDATE com Cálculo (Aumento de Preço)")
    print("="*60)
    
    # Mostrar preços antes
    print("\n--- Preços antes do aumento (10%) ---")
    cursor.execute("SELECT nome, preco FROM produtos WHERE categoria = 'Eletrônicos'")
    antes = cursor.fetchall()
    for produto in antes:
        print(f"  {produto[0]}: R$ {produto[1]:.2f}")
    
    # Aumentar preços em 10%
    cursor.execute('''
        UPDATE produtos
        SET preco = preco * 1.10
        WHERE categoria = 'Eletrônicos'
    ''')
    
    conn.commit()
    
    # Mostrar preços depois
    print("\n--- Preços depois do aumento ---")
    cursor.execute("SELECT nome, preco FROM produtos WHERE categoria = 'Eletrônicos'")
    depois = cursor.fetchall()
    for produto in depois:
        print(f"  {produto[0]}: R$ {produto[1]:.2f}")
    print(f"✓ Registros atualizados: {cursor.rowcount}")

def exemplo_update_multiplos_registros(conn):
    """Exemplo 4: UPDATE afetando múltiplos registros."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 4: UPDATE de Múltiplos Registros")
    print("="*60)
    
    # Mostrar antes
    print("\n--- Clientes de São Paulo (antes) ---")
    cursor.execute("SELECT id, nome, idade FROM clientes WHERE cidade = 'São Paulo'")
    antes = cursor.fetchall()
    for cliente in antes:
        print(f"  {cliente[1]}: {cliente[2]} anos")
    
    # Aumentar idade em 1 ano para todos de SP
    cursor.execute('''
        UPDATE clientes
        SET idade = idade + 1
        WHERE cidade = 'São Paulo'
    ''')
    
    conn.commit()
    
    # Mostrar depois
    print("\n--- Clientes de São Paulo (depois) ---")
    cursor.execute("SELECT id, nome, idade FROM clientes WHERE cidade = 'São Paulo'")
    depois = cursor.fetchall()
    for cliente in depois:
        print(f"  {cliente[1]}: {cliente[2]} anos")
    print(f"✓ Registros atualizados: {cursor.rowcount}")

def exemplo_delete_seguro(conn):
    """Exemplo 5: DELETE com segurança - verificar antes de deletar."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 5: DELETE Seguro (com verificação)")
    print("="*60)
    
    # Primeiro, verificar o que será removido
    cliente_id = 5
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
    registro = cursor.fetchone()
    
    if registro:
        print(f"\n⚠️  Registro que será removido:")
        print(f"   ID: {registro[0]}")
        print(f"   Nome: {registro[1]}")
        print(f"   Email: {registro[2]}")
        
        # Em uma aplicação real, pedir confirmação do usuário
        # Por aqui, vamos apenas simular
        print("\n   Simulando confirmação...")
        
        # Deletar
        cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        conn.commit()
        
        print(f"✓ Registro removido com sucesso!")
        print(f"✓ Registros removidos: {cursor.rowcount}")
        
        # Verificar que foi removido
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
        if cursor.fetchone() is None:
            print("✓ Confirmação: Registro não existe mais")
    else:
        print(f"   Registro com ID {cliente_id} não encontrado")

def exemplo_delete_multiplos(conn):
    """Exemplo 6: DELETE de múltiplos registros."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 6: DELETE de Múltiplos Registros")
    print("="*60)
    
    # Primeiro, verificar quais serão removidos
    print("\n--- Produtos que serão removidos (estoque = 0) ---")
    cursor.execute('SELECT id, nome, estoque FROM produtos WHERE estoque = 0')
    produtos = cursor.fetchall()
    
    if produtos:
        for produto in produtos:
            print(f"   {produto[1]} (ID: {produto[0]}, Estoque: {produto[2]})")
        
        # Deletar (comentado para não perder dados - descomente para testar)
        # cursor.execute('DELETE FROM produtos WHERE estoque = 0')
        # conn.commit()
        # print(f"\n✓ Registros removidos: {cursor.rowcount}")
        print("\n   (DELETE comentado para preservar dados de exemplo)")
    else:
        print("   Nenhum produto com estoque zero encontrado")

def exemplo_transacao(conn):
    """Exemplo 7: Usando transações para reverter operações."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 7: Transações (ROLLBACK)")
    print("="*60)
    
    # Estado inicial
    print("\n--- Estado inicial ---")
    cursor.execute('SELECT nome, idade FROM clientes WHERE id = 2')
    inicial = cursor.fetchone()
    print(f"Cliente: {inicial[0]}, Idade: {inicial[1]}")
    
    # Iniciar transação
    print("\n--- Iniciando transação e fazendo UPDATE ---")
    try:
        cursor.execute('''
            UPDATE clientes
            SET idade = 999
            WHERE id = 2
        ''')
        
        # Verificar o valor durante a transação
        cursor.execute('SELECT nome, idade FROM clientes WHERE id = 2')
        durante = cursor.fetchone()
        print(f"Cliente: {durante[0]}, Idade: {durante[1]} (durante transação)")
        
        # Simular um problema e fazer ROLLBACK
        print("\n--- Problema detectado! Fazendo ROLLBACK ---")
        conn.rollback()
        
        # Verificar que voltou ao estado original
        cursor.execute('SELECT nome, idade FROM clientes WHERE id = 2')
        depois = cursor.fetchone()
        print(f"Cliente: {depois[0]}, Idade: {depois[1]} (após rollback)")
        print("✓ Transação revertida com sucesso!")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro: {e}")
        print("✓ Transação revertida")

def exemplo_boas_praticas(conn):
    """Exemplo 8: Boas práticas - sempre verificar antes."""
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("EXEMPLO 8: Boas Práticas")
    print("="*60)
    
    # BOA PRÁTICA: Verificar antes de atualizar
    print("\n--- Boa Prática: Verificar antes de UPDATE ---")
    
    # Passo 1: Ver quais registros serão afetados
    condicao = "nome LIKE '%João%'"
    cursor.execute(f'SELECT COUNT(*) FROM clientes WHERE {condicao}')
    count = cursor.fetchone()[0]
    print(f"Registros que serão afetados: {count}")
    
    if count > 0:
        cursor.execute(f'SELECT id, nome FROM clientes WHERE {condicao}')
        registros = cursor.fetchall()
        print("Registros específicos:")
        for reg in registros:
            print(f"   ID {reg[0]}: {reg[1]}")
        
        # Passo 2: Se estiver correto, executar UPDATE
        # (comentado para não alterar dados)
        # cursor.execute(f'UPDATE clientes SET idade = 30 WHERE {condicao}')
        # conn.commit()
        print("\n   ✓ UPDATE seria executado aqui (comentado para exemplo)")

def main():
    """Função principal."""
    print("="*60)
    print("EXEMPLOS PRÁTICOS: UPDATE, DELETE e Transações")
    print("Módulo 02 - Comandos de Atualização, Remoção, Modelagem")
    print("="*60)
    
    conn = criar_conexao()
    
    try:
        preparar_banco(conn)
        
        exemplo_update_simples(conn)
        exemplo_update_multiplas_colunas(conn)
        exemplo_update_calculo(conn)
        exemplo_update_multiplos_registros(conn)
        exemplo_delete_seguro(conn)
        exemplo_delete_multiplos(conn)
        exemplo_transacao(conn)
        exemplo_boas_praticas(conn)
        
        print("\n" + "="*60)
        print("✓ Todos os exemplos foram executados!")
        print(f"✓ Banco de dados: {DB_FILE}")
        print("="*60)
        
    except sqlite3.Error as e:
        print(f"❌ Erro do banco de dados: {e}")
        conn.rollback()
    except Exception as e:
        print(f"❌ Erro: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("\n✓ Conexão fechada.")

if __name__ == '__main__':
    main()

