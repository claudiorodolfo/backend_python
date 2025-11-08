"""
DAO (Data Access Object) para operações de banco de dados da tabela disciplina
e da tabela intermediária pessoa_disciplina (relacionamento N:N)
"""

from bd.database import DatabaseConnection
from model.disciplina import Disciplina
from model.pessoa import Pessoa
from dao.pessoa_dao import PessoaDAO

class DisciplinaDAO:
    def __init__(self, db: DatabaseConnection):
        self.__db = db
    
    def salvar(self, disciplina: Disciplina):
        cur = self.__db.cursor()
        
        if disciplina.id is None:
            # INSERT
            cur.execute("""
                INSERT INTO disciplina (nome, carga_horaria, descricao)
                VALUES (?, ?, ?);
            """, (disciplina.nome, disciplina.carga_horaria, disciplina.descricao))
            
            disciplina.id = cur.lastrowid
        else:
            # UPDATE
            cur.execute("""
                UPDATE disciplina SET nome = ?, carga_horaria = ?, descricao = ?
                WHERE id = ?;
            """, (disciplina.nome, disciplina.carga_horaria, disciplina.descricao, disciplina.id))
        
        return disciplina.id
    
    def buscarPorId(self, id: int):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM disciplina WHERE id = ?;", (id,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorNome(self, nome: str):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM disciplina WHERE nome LIKE ?;", (f'%{nome}%',))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def listarTodas(self):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM disciplina ORDER BY nome;")
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def criarDeRow(self, row):
        return Disciplina(
            id=row['id'],
            nome=row['nome'],
            carga_horaria=row['carga_horaria'],
            descricao=row['descricao']
        )
    
    def deletar(self, disciplina: Disciplina):
        cur = self.__db.cursor()
        cur.execute("DELETE FROM disciplina WHERE id = ?;", (disciplina.id,))
        
        return cur.rowcount > 0
    
    # Métodos para gerenciar relacionamento N:N com Pessoa
    
    def vincularPessoa(self, pessoa: Pessoa, disciplina: Disciplina):
        """Vincula uma pessoa a uma disciplina"""
        cur = self.__db.cursor()
        
        # Verificar se já existe o vínculo
        cur.execute("""
            SELECT * FROM pessoa_disciplina 
            WHERE pessoa_id = ? AND disciplina_id = ?;
        """, (pessoa.id, disciplina.id))
        
        if cur.fetchone():
            return False  # Já existe o vínculo
        
        cur.execute("""
            INSERT INTO pessoa_disciplina (pessoa_id, disciplina_id)
            VALUES (?, ?);
        """, (pessoa.id, disciplina.id))
        
        return True
    
    def desvincularPessoa(self, pessoa: Pessoa, disciplina: Disciplina):
        """Remove o vínculo entre uma pessoa e uma disciplina"""
        cur = self.__db.cursor()
        cur.execute("""
            DELETE FROM pessoa_disciplina 
            WHERE pessoa_id = ? AND disciplina_id = ?;
        """, (pessoa.id, disciplina.id))
        
        return cur.rowcount > 0
    
    def buscarPessoasPorDisciplina(self, disciplinaId: int):
        """Retorna todas as pessoas vinculadas a uma disciplina"""
        cur = self.__db.cursor()
        cur.execute("""
            SELECT p.*
            FROM pessoa p
            INNER JOIN pessoa_disciplina pd ON p.id = pd.pessoa_id
            WHERE pd.disciplina_id = ?
            ORDER BY p.nome;
        """, (disciplinaId,))
        
        rows = cur.fetchall()
        pessoaDao = PessoaDAO(self.__db)
        
        resultado = []
        for row in rows:
            resultado.append(pessoaDao.criarDeRow(row))
        return resultado
    
    def buscarDisciplinasPorPessoa(self, pessoaId: int):
        """Retorna todas as disciplinas vinculadas a uma pessoa"""
        cur = self.__db.cursor()
        cur.execute("""
            SELECT d.*
            FROM disciplina d
            INNER JOIN pessoa_disciplina pd ON d.id = pd.disciplina_id
            WHERE pd.pessoa_id = ?
            ORDER BY d.nome;
        """, (pessoaId,))
        
        rows = cur.fetchall()
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado

