"""
DAO (Data Access Object) para operações de banco de dados da tabela pessoa
"""

from bd.database import DatabaseConnection
from dao.categoria_dao import CategoriaDAO
from model.pessoa import Pessoa

class PessoaDAO:
    def __init__(self, db: DatabaseConnection):
        self.__db = db
    
    def salvar(self, pessoa: Pessoa):
        cur = self.__db.cursor()
        
        # Converter boolean para integer (SQLite)
        ativoInt = 1 if pessoa.ativo else 0
        
        categoriaId = pessoa.categoria.id
        
        if pessoa.id is None:
            # INSERT
            cur.execute("""
                INSERT INTO pessoa (nome, email, altura, peso, data_nascimento,
                                 ativo, telefone, categoria_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (pessoa.nome, pessoa.email, pessoa.altura, pessoa.peso,
                  pessoa.data_nascimento, ativoInt, pessoa.telefone,
                  categoriaId))

            pessoa.id = cur.lastrowid
        else:
            # UPDATE
            cur.execute("""
                UPDATE pessoa SET nome = ?, email = ?, altura = ?, peso = ?,
                               data_nascimento = ?, ativo = ?,
                               telefone = ?, categoria_id = ?
                WHERE id = ?;
            """, (pessoa.nome, pessoa.email, pessoa.altura, pessoa.peso,
                  pessoa.data_nascimento, ativoInt, pessoa.telefone,
                  categoriaId, pessoa.id))
        
        return pessoa.id
    
    def buscarPorId(self, id: int):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE id = ?;", (id,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorNome(self, nome: str):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE nome LIKE ?;", (f'%{nome}%',))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def listarTodas(self, comCategoria: bool = False):
        cur = self.__db.cursor()
        
        if comCategoria:
            cur.execute("""
                SELECT p.*, c.nome as categoria_nome
                FROM pessoa p
                JOIN categoria c ON p.categoria_id = c.id
                ORDER BY p.nome;
            """)
        else:
            cur.execute("SELECT * FROM pessoa ORDER BY nome;")
        
        rows = cur.fetchall()
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def buscarPorCategoria(self, categoriaId: int):
        cur = self.__db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE categoria_id = ? ORDER BY nome;", (categoriaId,))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def criarDeRow(self, row):
        # Buscar a categoria usando o CategoriaDAO
        categoriaDao = CategoriaDAO(self.__db)
        categoria = categoriaDao.buscarPorId(row['categoria_id'])
        
        return Pessoa(
            id=row['id'],
            nome=row['nome'],
            email=row['email'],
            altura=row['altura'],
            peso=row['peso'],
            data_nascimento=row['data_nascimento'],
            ativo=bool(row['ativo']),
            telefone=row['telefone'],
            categoria=categoria
        )
    
    def deletar(self, pessoa: Pessoa):        
        cur = self.__db.cursor()
        cur.execute("DELETE FROM pessoa WHERE id = ?;", (pessoa.id,))

        return cur.rowcount > 0
    
    def obterCategoria(self, pessoa: Pessoa):
        return pessoa.categoria

