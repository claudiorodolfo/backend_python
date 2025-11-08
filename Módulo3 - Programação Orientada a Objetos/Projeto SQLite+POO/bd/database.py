"""
Classe para gerenciar conexão com o banco de dados SQLite
"""
import sqlite3

class DatabaseConnection:
    def __init__(self, dbPath: str = 'exemplo_bd.db'):
        self.__dbPath = dbPath
        self.__conn = None
    
    def conectar(self):
        if self.__conn is None:
            # isolation_level=None ativa autocommit (cada operação é commitada automaticamente)
            self.__conn = sqlite3.connect(self.__dbPath, isolation_level=None)
            self.__conn.row_factory = sqlite3.Row
            self.__conn.execute("PRAGMA foreign_keys = ON")
        return self.__conn
    
    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self.__conn:
            self.__conn.close()
            self.__conn = None
    

    
    def cursor(self):
        """Retorna um cursor para executar queries"""
        if self.__conn is None:
            self.conectar()
        return self.__conn.cursor()
    
    def criarTabelas(self):
        cur = self.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS categoria (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            );
            """
        )
        cur.execute("""
        CREATE TABLE IF NOT EXISTS pessoa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            altura REAL,
            peso REAL,
            data_nascimento TEXT,
            ativo INTEGER DEFAULT 1,
            telefone TEXT,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        );
        """)
        # Tabela usuario (relacionamento 1:1 com pessoa)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER NOT NULL,
            login TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (id) REFERENCES pessoa(id) ON DELETE CASCADE
        );
        """)
        # Tabela disciplina
        cur.execute("""
        CREATE TABLE IF NOT EXISTS disciplina (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            carga_horaria INTEGER,
            descricao TEXT
        );
        """)
        # Tabela intermediária para relacionamento N:N entre pessoa e disciplina
        cur.execute("""
        CREATE TABLE IF NOT EXISTS pessoa_disciplina (
            pessoa_id INTEGER NOT NULL,
            disciplina_id INTEGER NOT NULL,
            PRIMARY KEY (pessoa_id, disciplina_id),
            FOREIGN KEY (pessoa_id) REFERENCES pessoa(id) ON DELETE CASCADE,
            FOREIGN KEY (disciplina_id) REFERENCES disciplina(id) ON DELETE CASCADE
        );
        """)
    
    def limparDados(self):
        cur = self.cursor()
        cur.execute("DELETE FROM pessoa_disciplina;")
        cur.execute("DELETE FROM usuario;")
        cur.execute("DELETE FROM disciplina;")
        cur.execute("DELETE FROM pessoa;")
        cur.execute("DELETE FROM categoria;")
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('pessoa', 'categoria', 'usuario', 'disciplina');")

