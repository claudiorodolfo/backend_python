"""
DAO Concreto - Implementação SQLite
"""

import sqlite3
from contextlib import contextmanager
from typing import List
from .dao_interface import UsuarioDAO
from .model import Usuario


class SQLiteUsuarioDAO(UsuarioDAO):
    
    def __init__(self, dbPath: str = "usuarios.db"):
        self._dbPath = dbPath
        self._criarTabela()
    
    @contextmanager
    def _getConnection(self):
        conn = sqlite3.connect(self._dbPath)
        conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def _criarTabela(self):
        with self._getConnection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            """)
    
    def _rowToUsuario(self, row: sqlite3.Row) -> Usuario:
        return Usuario(id=row['id'], nome=row['nome'], email=row['email'])
    
    def criar(self, usuario: Usuario) -> Usuario:
        with self._getConnection() as conn:
            cursor = conn.execute(
                "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
                (usuario.nome, usuario.email)
            )
            usuario.id = cursor.lastrowid
            return usuario
    
    def buscarPorId(self, id: int) -> Usuario:
        with self._getConnection() as conn:
            cursor = conn.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
            row = cursor.fetchone()
            return self._rowToUsuario(row) if row else None
    
    def buscarTodos(self) -> List[Usuario]:
        with self._getConnection() as conn:
            cursor = conn.execute("SELECT * FROM usuarios ORDER BY id")
            return [self._rowToUsuario(row) for row in cursor.fetchall()]
    
    def atualizar(self, usuario: Usuario) -> bool:
        if not usuario.id:
            return False
        
        with self._getConnection() as conn:
            cursor = conn.execute(
                "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
                (usuario.nome, usuario.email, usuario.id)
            )
            return cursor.rowcount > 0
    
    def deletar(self, id: int) -> bool:
        with self._getConnection() as conn:
            cursor = conn.execute("DELETE FROM usuarios WHERE id = ?", (id,))
            return cursor.rowcount > 0
    
    def buscarPorEmail(self, email: str) -> Usuario:
        with self._getConnection() as conn:
            cursor = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            row = cursor.fetchone()
            return self._rowToUsuario(row) if row else None

