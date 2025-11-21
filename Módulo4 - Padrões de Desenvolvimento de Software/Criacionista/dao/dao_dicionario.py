"""
DAO Concreto - Implementação em memória
"""

from typing import List
from .dao_interface import UsuarioDAO
from .model import Usuario


class DicionarioUsuarioDAO(UsuarioDAO):
    
    def __init__(self):
        self._usuarios = {}
        self._nextId = 1
    
    def criar(self, usuario: Usuario) -> Usuario:
        usuario.id = self._nextId
        self._nextId += 1
        self._usuarios[usuario.id] = usuario
        return usuario
    
    def buscarPorId(self, id: int) -> Usuario:
        return self._usuarios.get(id)
    
    def buscarTodos(self) -> List[Usuario]:
        return self._usuarios.values()
    
    def atualizar(self, usuario: Usuario) -> bool:
        if usuario.id and usuario.id in self._usuarios:
            self._usuarios[usuario.id] = usuario
            return True
        return False
    
    def deletar(self, id: int) -> bool:
        if id in self._usuarios:
            del self._usuarios[id]
            return True
        return False
    
    def buscarPorEmail(self, email: str) -> Usuario:
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario
        return None

