#pip3 install psycopg2-binary
#python3 -m pip install psycopg2-binary
#PgAdmin 4

import psycopg2
import os
from datetime import date, datetime
from dotenv import load_dotenv

#date
#hoje = date(2025, 10, 15)   # ano, mês, dia
#print(hoje)                 # saída: 2025-10-15
#hoje = date.today()
#print(hoje)                 # saída: 2025-10-25 (por exemplo)

#datetime
#momento = datetime(2025, 10, 25, 14, 30, 0)  # ano, mês, dia, hora, minuto, segundo
#print(momento)                                # saída: 2025-10-25 14:30:00
#agora = datetime.now()
#print(agora)  # saída: 2025-10-25 01:25:37.123456
#agora = datetime.today()  #(parecido com now(), mas sem fuso horário)
#print(agora)  # saída: 2025-10-25 01:25:37

# Carrega as variáveis de ambiente do arquivo config.env
load_dotenv('config.env')

def conectar_banco():
    """Conecta ao banco de dados PostgreSQL"""
    host = os.getenv('DB_HOST', '')
    dbname = os.getenv('DB_NAME', '')
    user = os.getenv('DB_USER', '')
    password = os.getenv('DB_PASSWORD', '')
    port = os.getenv('DB_PORT', '')
    
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    return conn

def criar_tabelas(cur):
    """Cria as tabelas categoria e pessoa com diferentes tipos de dados SQL"""
    
    # Tabela categoria - mostra tipos básicos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id SERIAL NOT NULL,
        nome VARCHAR(50) NOT NULL UNIQUE,
        PRIMARY KEY (id)
    );
    """)
    
    # Tabela pessoa - mostra mais tipos de dados SQL
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pessoa (
        id SERIAL NOT NULL,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE,
        idade INTEGER CHECK (idade >= 0 AND idade <= 120),
        altura DECIMAL(3,2),    -- altura em metros (ex: 1.75)
        peso FLOAT,             -- peso em kg
        data_nascimento DATE,
        ativo BOOLEAN DEFAULT TRUE,
        observacoes TEXT,
        telefone CHAR(11),
        categoria_id INTEGER NOT NULL,
        momento_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
    );
    """)

def limpar_dados(cur):
    """Remove todos os dados das tabelas para evitar duplicação"""
    print("Limpando dados existentes...")
    
    # Remove dados da tabela pessoa primeiro (devido à foreign key)
    cur.execute("DELETE FROM pessoa;")
    print("✓ Dados da tabela 'pessoa' removidos")
    
    # Remove dados da tabela categoria
    cur.execute("DELETE FROM categoria;")
    print("✓ Dados da tabela 'categoria' removidos")
    
    # Reseta os contadores de ID (SERIAL)
    cur.execute("ALTER SEQUENCE pessoa_id_seq RESTART WITH 1;")
    cur.execute("ALTER SEQUENCE categoria_id_seq RESTART WITH 1;")
    print("✓ Contadores de ID resetados")

def inserir_categorias(cur):
    """Insere dados na tabela categoria"""
    categorias = [
        ("Professor",),
        ("Aluno",),
        ("Técnico",)
    ]
    
    sql_insert = """
    INSERT INTO categoria (nome) 
    VALUES (%s);
    """
    cur.executemany(sql_insert, categorias)

def inserir_pessoas(cur):
    """Insere dados na tabela pessoa com diferentes tipos de dados"""
    pessoas = [
        ("Ana Silva", "ana.silva@email.com", 25, 1.65, 58.5,
         date(1998,5,15), True, "Professora de Matemática", "71999999999", 1),
        ("Bruno Costa", "bruno.costa@email.com", 30, 1.80, 75.2,
         date(1993,8,22), True, "Aluno de Engenharia", "71988888888", 2),
        ("Carla Souza", "carla.souza@email.com", 22, 1.70, 62.0,
         date(2001,12,3), False, "Técnica em Informática", "71977777777", 3),
        ("Diego Santos", "diego.santos@email.com", 28, 1.75, 70.5, 
         date(1995,3,10), False, "Professor de Física", "71966666666", 1),
        ("João da Silva", "joao.silva@email.com", 20, 1.75, 70.5,
         date(2002,1,1), True, "Técnico de Informática", "71955555555", 3),
        ("Maria Oliveira", "maria.oliveira@email.com", 23, 1.60, 55.0,
         date(1999,7,15), True, "Aluna de Engenharia", "71944444444", 2),
        ("Pedro Santos", "pedro.santos@email.com", 27, 1.85, 80.0,
         date(1996,2,20), True, "Técnico de Matemática", "71933333333", 3),
        ("Lucas Oliveira", "lucas.oliveira@email.com", 21, 1.72, 68.5,
         date(2001,9,10), True, "Aluno de Física", "71922222222", 2),
        ("Julia Santos", "julia.santos@email.com", 24, 1.68, 60.0,
         date(1998,4,25), True, "Professora de Química", "71911111111", 1),
        ("Rafael Oliveira", "rafael.oliveira@email.com", 26, 1.80, 75.0,
         date(1997,6,30), True, "Aluno de História", "71900000000", 2),
        ("Camila Santos", "camila.santos@email.com", 29, 1.75, 65.5,
         date(1994,9,12), True, "Professora de Geografia", "71899999999", 1),
        ("Gustavo Oliveira", "gustavo.oliveira@email.com", 22, 1.70, 62.0,
         date(2000,11,25), True, "Aluno de Inglês", "71888888888", 2),
        ("Larissa Santos", "larissa.santos@email.com", 25, 1.65, 58.5,
         date(1998,2,18), True, "Técnica de Espanhol", "71877777777", 3),
        ("Bruno Oliveira", "bruno.oliveira@email.com", 28, 1.85, 75.0,
         date(1995,5,10), True, "Aluno de Física", "71866666666", 2),
        ("Letícia Santos", "leticia.santos@email.com", 21, 1.72, 68.5,
         date(2001,8,5), True, "Técnica de Química", "71855555555", 3),
        ("Ricardo Oliveira", "ricardo.oliveira@email.com", 24, 1.68, 60.0,
         date(1998,3,15), True, "Técnico de História", "71844444444", 3),
        ("Amanda Santos", "amanda.santos@email.com", 27, 1.80, 75.0,
         date(1995,7,22), True, "Aluna de Geografia", "71833333333", 2),
        ("Felipe Oliveira", "felipe.oliveira@email.com", 20, 1.75, 70.5,
         date(2002,4,10), True, "Professor de Inglês", "71822222222", 1),
        ("Fernanda Santos", "fernanda.santos@email.com", 23, 1.60, 55.0,
         date(1999,6,25), True, "Aluna de Espanhol", "71811111111", 2)
    ]
    
    sql_insert = """
    INSERT INTO pessoa (nome, email, idade, altura, peso, data_nascimento, 
                       ativo, observacoes, telefone, categoria_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cur.executemany(sql_insert, pessoas)

def atualizar_dados(cur):
    """Atualiza dados na tabela pessoa"""
    print("\n=== ATUALIZANDO DADOS ===")
    
    # UPDATE 1: Aumentar idade da Carla
    sql_update = "UPDATE pessoa SET idade = %s WHERE nome = %s;"
    cur.execute(sql_update, (23, "Carla Souza"))
    print("✓ Idade da Carla atualizada de 22 para 23 anos")
    
    # UPDATE 2: Ativar Carla
    sql_update = "UPDATE pessoa SET ativo = TRUE WHERE nome = %s;"
    cur.execute(sql_update, ("Carla Souza",))
    print("✓ Carla foi ativada")

def mostrar_dados(cur):
    """Mostra os dados após fazer UPDATE"""
    print("\n=== DADOS APÓS O UPDATE ===")
    cur.execute("""
    SELECT p.id, p.nome, p.idade, c.nome as categoria, p.ativo
    FROM pessoa p, categoria c 
    WHERE p.categoria_id = c.id
    ORDER BY p.id;
    """)
    
    print("ID | Nome | Idade | Categoria | Ativo")
    print("-" * 50)
    for row in cur.fetchall():
        status = "Sim" if row[4] else "Não"
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {status}")

def mostrar_tipos_dados(cur):
    """Demonstra diferentes tipos de dados SQL"""
    print("\n=== DEMONSTRAÇÃO DE TIPOS DE DADOS ===")
    
    # Mostrar dados com diferentes tipos
    cur.execute("""
    SELECT 
        nome,
        email,
        idade,
        altura,
        peso,
        data_nascimento,
        momento_cadastro,
        ativo,
        observacoes
    FROM pessoa 
    WHERE nome = 'Ana Silva';
    """)
    
    row = cur.fetchone()
    if row:
        print(f"VARCHAR: Nome = {row[0]}")
        print(f"VARCHAR: Email = {row[1]}")
        print(f"INTEGER: Idade = {row[2]}")
        print(f"DECIMAL: Altura = {row[3]} metros")
        print(f"REAL: Peso = {row[4]:.2f} kg")
        print(f"DATE: Data Nascimento = {row[5]}")
        print(f"TIMESTAMP: Momento Cadastro = {row[6]}")
        print(f"BOOLEAN: Ativo = {row[7]}")
        print(f"TEXT: Observações = {row[8]}")

def mostrar_relacionamentos(cur):
    """Demonstra relacionamentos entre tabelas"""
    print("\n=== DEMONSTRAÇÃO DE RELACIONAMENTOS ===")
    
    # JOIN entre tabelas
    cur.execute("""
    SELECT 
        p.nome,
        c.nome as categoria
    FROM pessoa p,categoria c 
    WHERE p.categoria_id = c.id
    ORDER BY c.nome, p.nome;
    """)
    
    print("Pessoa | Categoria")
    print("-" * 30)
    for row in cur.fetchall():
        print(f"{row[0]} | {row[1]}")

def exemplo_postgresql():
    """Função principal que executa todas as operações"""
    conn = conectar_banco()
    cur = conn.cursor()
    
    try:
        # Criar tabelas
        print("Criando tabelas...")
        criar_tabelas(cur)
        conn.commit()
        print("✓ Tabelas criadas com sucesso!")
        
        # Limpar dados existentes para evitar duplicação
        limpar_dados(cur)
        conn.commit()
        
        # Inserir dados
        print("\nInserindo dados...")
        inserir_categorias(cur)
        inserir_pessoas(cur)
        conn.commit()
        print("✓ Dados inseridos com sucesso!")
        
        # Mostrar dados antes do update
        mostrar_dados(cur)
        
        # Atualizar dados
        atualizar_dados(cur)
        conn.commit()
        
        # Mostrar dados após update
        mostrar_dados(cur)
        
        # Demonstrar tipos de dados
        mostrar_tipos_dados(cur)
        
        # Demonstrar relacionamentos
        mostrar_relacionamentos(cur)
        
    except Exception as e:
        print(f"Erro: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        print("\n✓ Conexão com banco de dados encerrada!")

if __name__ == "__main__":
    exemplo_postgresql()