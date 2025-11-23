"""
DAO Interface - Define contrato para acesso a dados
"""

from abc import ABC, abstractmethod
from typing import List
from .model import Usuario


class UsuarioDAO(ABC):
    
    @abstractmethod
    def criar(self, usuario: Usuario) -> Usuario:
        pass
    
    @abstractmethod
    def buscarPorId(self, id: int) -> Usuario:
        pass
    
    @abstractmethod
    def buscarTodos(self) -> List[Usuario]:
        pass
    
    @abstractmethod
    def atualizar(self, usuario: Usuario) -> bool:
        pass
    
    @abstractmethod
    def deletar(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def buscarPorEmail(self, email: str) -> Usuario:
        pass

