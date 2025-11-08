"""
DAO (Data Access Object) para operações de banco de dados da tabela usuario
"""

from bd.database import DatabaseConnection
from dao.pessoa_dao import PessoaDAO
from model.usuario import Usuario

class UsuarioDAO:
    def __init__(self, db: DatabaseConnection):
        self.__db = db
    
    def salvar(self, usuario: Usuario):
        cur = self.__db.cursor()
        
        pessoaId = usuario.pessoa.id
        
        if usuario.id is None:
            # INSERT
            cur.execute("""
                INSERT INTO usuario (login, senha, tipo, pessoa_id)
                VALUES (?, ?, ?, ?);
            """, (usuario.login, usuario.senha, usuario.tipo, pessoaId))
            
            usuario.id = cur.lastrowid
        else:
            # UPDATE
            cur.execute("""
                UPDATE usuario SET login = ?, senha = ?, tipo = ?, pessoa_id = ?
                WHERE id = ?;
            """, (usuario.login, usuario.senha, usuario.tipo, pessoaId, usuario.id))
        
        return usuario.id
    
    def buscarPorId(self, id: int):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM usuario WHERE id = ?;", (id,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorLogin(self, login: str):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM usuario WHERE login = ?;", (login,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorPessoaId(self, pessoaId: int):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM usuario WHERE pessoa_id = ?;", (pessoaId,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def listarTodos(self):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM usuario ORDER BY login;")
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def criarDeRow(self, row):
        # Buscar a pessoa usando o PessoaDAO
        pessoaDao = PessoaDAO(self.__db)
        pessoa = pessoaDao.buscarPorId(row['pessoa_id'])
        
        return Usuario(
            id=row['id'],
            login=row['login'],
            senha=row['senha'],
            tipo=row['tipo'],
            pessoa=pessoa
        )
    
    def deletar(self, usuario: Usuario):
        cur = self.__db.cursor()
        cur.execute("DELETE FROM usuario WHERE id = ?;", (usuario.id,))
        
        return cur.rowcount > 0

