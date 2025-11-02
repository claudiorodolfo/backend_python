import sqlite3

def conectar_banco():
    """Conecta ao banco de dados SQLite"""
    # Nome simples do arquivo de banco de dados
    db_path = 'exemplo_bd.db'
    
    conn = sqlite3.connect(db_path)
    # Configurar para retornar dicionários nas consultas
    conn.row_factory = sqlite3.Row
    #print(linha["nome"])   # em vez de linha[0]
    
    #Isso instrui o SQLite a verificar e aplicar as restrições de integridade referencial, como:
    #não permitir excluir um registro pai que tem filhos;
    #impedir inserções com valores de chave estrangeira inexistentes;
    #aplicar comportamentos ON DELETE CASCADE, etc.
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def criar_tabelas(cur):
    """Cria as tabelas categoria e pessoa com diferentes tipos de dados SQL"""
    
    # Tabela categoria - mostra tipos básicos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    );
    """)
    
    # Tabela pessoa - mostra mais tipos de dados SQL
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        idade INTEGER CHECK (idade >= 0 AND idade <= 120),
        altura REAL,  -- altura em metros (ex: 1.75)
        peso REAL,    -- peso em kg
        data_nascimento TEXT,  -- SQLite não tem tipo DATE nativo
        ativo INTEGER DEFAULT 1,  -- SQLite usa INTEGER para BOOLEAN
        observacoes TEXT,
        telefone TEXT,
        categoria_id INTEGER NOT NULL,
        momento_cadastro TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
    );
    """)

def limpar_dados(cur):
    """Remove todos os dados das tabelas antes de inserir novos"""
    print("Limpando dados existentes...")
    
    # Deletar dados das tabelas (respeitando ordem das foreign keys)
    cur.execute("DELETE FROM pessoa;")
    cur.execute("DELETE FROM categoria;")
    
    # Resetar os contadores de AUTOINCREMENT
    cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('pessoa', 'categoria');")
    
    print("✓ Dados limpos com sucesso!")

def inserir_categorias(cur):
    """Insere dados na tabela categoria"""
    categorias = [
        ("Professor",),
        ("Aluno",),
        ("Técnico",)
    ]
    
    sql_insert = """
    INSERT INTO categoria (nome) 
    VALUES (?);
    """
    cur.executemany(sql_insert, categorias)

def inserir_pessoas(cur):
    """Insere dados na tabela pessoa com diferentes tipos de dados"""
    pessoas = [
        ("Ana Silva", "ana.silva@email.com", 25, 1.65, 58.5,
         "1998-05-15", 1, "Professora de Matemática", "71999999999", 1),
        ("Bruno Costa", "bruno.costa@email.com", 30, 1.80, 75.2,
         "1993-08-22", 1, "Aluno de Engenharia", "71988888888", 2),
        ("Carla Souza", "carla.souza@email.com", 22, 1.70, 62.0,
         "2001-12-03", 0, "Técnica em Informática", "71977777777", 3),
        ("Diego Santos", "diego.santos@email.com", 28, 1.75, 70.5, 
         "1995-03-10", 0, "Professor de Física", "71966666666", 1),
        ("João da Silva", "joao.silva@email.com", 20, 1.75, 70.5,
         "2002-01-01", 1, "Técnico de Informática", "71955555555", 3),
        ("Maria Oliveira", "maria.oliveira@email.com", 23, 1.60, 55.0,
         "1999-07-15", 1, "Aluna de Engenharia", "71944444444", 2),
        ("Pedro Santos", "pedro.santos@email.com", 27, 1.85, 80.0,
         "1996-02-20", 1, "Técnico de Matemática", "71933333333", 3),
        ("Lucas Oliveira", "lucas.oliveira@email.com", 21, 1.72, 68.5,
         "2001-09-10", 1, "Aluno de Física", "71922222222", 2),
        ("Julia Santos", "julia.santos@email.com", 24, 1.68, 60.0,
         "1998-04-25", 1, "Professora de Química", "71911111111", 1),
        ("Rafael Oliveira", "rafael.oliveira@email.com", 26, 1.80, 75.0,
         "1997-06-30", 1, "Aluno de História", "71900000000", 2),
        ("Camila Santos", "camila.santos@email.com", 29, 1.75, 65.5,
         "1994-09-12", 1, "Professora de Geografia", "71899999999", 1),
        ("Gustavo Oliveira", "gustavo.oliveira@email.com", 22, 1.70, 62.0,
         "2000-11-25", 1, "Aluno de Inglês", "71888888888", 2),
        ("Larissa Santos", "larissa.santos@email.com", 25, 1.65, 58.5,
         "1998-02-18", 1, "Técnica de Espanhol", "71877777777", 3),
        ("Bruno Oliveira", "bruno.oliveira@email.com", 28, 1.85, 75.0,
         "1995-05-10", 1, "Aluno de Física", "71866666666", 2),
        ("Letícia Santos", "leticia.santos@email.com", 21, 1.72, 68.5,
         "2001-08-05", 1, "Técnica de Química", "71855555555", 3),
        ("Ricardo Oliveira", "ricardo.oliveira@email.com", 24, 1.68, 60.0,
         "1998-03-15", 1, "Técnico de História", "71844444444", 3),
        ("Amanda Santos", "amanda.santos@email.com", 27, 1.80, 75.0,
         "1995-07-22", 1, "Aluna de Geografia", "71833333333", 2),
        ("Felipe Oliveira", "felipe.oliveira@email.com", 20, 1.75, 70.5,
         "2002-04-10", 1, "Professor de Inglês", "71822222222", 1),
        ("Fernanda Santos", "fernanda.santos@email.com", 23, 1.60, 55.0,
         "1999-06-25", 1, "Aluna de Espanhol", "71811111111", 2)
    ]
    
    sql_insert = """
    INSERT INTO pessoa (nome, email, idade, altura, peso, data_nascimento, 
                       ativo, observacoes, telefone, categoria_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cur.executemany(sql_insert, pessoas)


def atualizar_dados(cur):
    """Atualiza dados na tabela pessoa"""
    print("\n=== ATUALIZANDO DADOS ===")
    
    # UPDATE 1: Aumentar idade da Carla
    sql_update = "UPDATE pessoa SET idade = ? WHERE nome = ?;"
    cur.execute(sql_update, (23, "Carla Souza"))
    print("✓ Idade da Carla atualizada de 22 para 23 anos")
    
    # UPDATE 2: Ativar Carla
    sql_update = "UPDATE pessoa SET ativo = 1 WHERE nome = ?;"
    cur.execute(sql_update, ("Carla Souza",))
    print("✓ Carla foi ativada")

def mostrar_dados(cur):
    """Mostra os dados após fazer UPDATE"""
    print("\n=== DADOS APÓS O UPDATE ===")
    cur.execute("""
    SELECT p.id, p.nome, p.idade, c.nome as categoria, p.ativo
    FROM pessoa p,categoria c 
    WHERE p.categoria_id = c.id
    ORDER BY p.id;
    """)
    
    print("ID | Nome | Idade | Categoria | Ativo")
    print("-" * 50)
    for linha in cur.fetchall():
        status = "Sim" if linha["ativo"] else "Não"
        print(f"{linha["id"]} | {linha["nome"]} | {linha["idade"]} | {linha["categoria"]} | {status}")

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
    
    linha = cur.fetchone()
    if linha:
        print(f"TEXT: Nome = {linha[0]}")
        print(f"TEXT: Email = {linha[1]}")
        print(f"INTEGER: Idade = {linha[2]}")
        print(f"REAL: Altura = {linha[3]} metros")
        print(f"REAL: Peso = {linha[4]:.2f} kg")
        print(f"TEXT: Data Nascimento = {linha[5]}")
        print(f"TEXT: Momento Cadastro = {linha[6]}")
        print(f"INTEGER: Ativo = {linha[7]} ({'Sim' if linha[7] else 'Não'})")
        print(f"TEXT: Observações = {linha[8]}")

def mostrar_relacionamentos(cur):
    """Demonstra relacionamentos entre tabelas"""
    print("\n=== DEMONSTRAÇÃO DE RELACIONAMENTOS ===")
    
    # JOIN entre tabelas
    cur.execute("""
    SELECT 
        p.nome,
        c.nome as categoria
    FROM pessoa p, categoria c 
    WHERE p.categoria_id = c.id
    ORDER BY c.nome, p.nome;
    """)
    
    print("Pessoa | Categoria")
    print("-" * 30)
    for linha in cur.fetchall():
        print(f"{linha["nome"]} | {linha["categoria"]}")

def exemplo_sqlite():
    """Função principal que executa todas as operações"""
    conn = conectar_banco()
    cur = conn.cursor()
    
    try:
        # Criar tabelas
        print("Criando tabelas...")
        criar_tabelas(cur)
        conn.commit()
        print("✓ Tabelas criadas com sucesso!")
        
        # Limpar dados existentes antes de inserir novos
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
    exemplo_sqlite()