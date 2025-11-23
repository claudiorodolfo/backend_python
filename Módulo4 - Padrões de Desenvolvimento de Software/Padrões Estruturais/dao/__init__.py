"""
Padrão DAO (Data Access Object)
================================

O padrão DAO é um padrão estrutural que abstrai o acesso a dados,
separando a lógica de negócio da lógica de persistência.

Componentes:
- DAO Interface: Define os métodos de acesso a dados
- DAO Concreto: Implementa a interface com acesso real ao banco
- Model/Entity: Representa a entidade de negócio
- Database Connection: Gerencia conexões com o banco

Benefícios:
- Separação de responsabilidades
- Facilita testes (mock do DAO)
- Permite trocar implementação de persistência facilmente
- Código mais organizado e manutenível
"""

from .model import Usuario
from .dao_interface import UsuarioDAO
from .dao_sqlite import SQLiteUsuarioDAO
from .dao_dicionario import DicionarioUsuarioDAO
from .dao_arquivo import ArquivoUsuarioDAO
from .service import UsuarioService

__all__ = [
    'Usuario',
    'UsuarioDAO',
    'SQLiteUsuarioDAO',
    'DicionarioUsuarioDAO',
    'ArquivoUsuarioDAO',
    'UsuarioService',
]

