"""
Service Layer - Lógica de negócio
"""

from typing import List
from .dao_interface import UsuarioDAO
from .model import Usuario


class UsuarioService:
    
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao
    
    def cadastrarUsuario(self, nome: str, email: str) -> Usuario:
        # Validação de negócio
        if not nome or not email:
            raise ValueError("Nome e email são obrigatórios")
        
        # Verifica se email já existe
        if self.dao.buscarPorEmail(email):
            raise ValueError(f"Email {email} já está cadastrado")
        
        # Cria o usuário
        usuario = Usuario(nome=nome, email=email)
        return self.dao.criar(usuario)
    
    def listarUsuarios(self) -> List[Usuario]:
        return self.dao.buscarTodos()
    
    def obterUsuario(self, id: int) -> Usuario:
        return self.dao.buscarPorId(id)
    
    def atualizarUsuario(self, id: int, nome: str, email: str) -> bool:
        usuario = self.dao.buscarPorId(id)
        if not usuario:
            return False
        
        usuario.nome = nome
        usuario.email = email
        return self.dao.atualizar(usuario)
    
    def removerUsuario(self, id: int) -> bool:
        return self.dao.deletar(id)

