"""
DAO Concreto - Persistência em arquivo de texto (JSON)
"""

import json
import os
from typing import List
from .dao_interface import UsuarioDAO
from .model import Usuario


class ArquivoUsuarioDAO(UsuarioDAO):
    
    def __init__(self, filePath: str = "usuarios.txt"):
        self._filePath = filePath
        self._usuarios = {}
        self._nextId = 1
        self._carregarDados()
    
    def _carregarDados(self):
        if os.path.exists(self._filePath):
            try:
                with open(self._filePath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._usuarios = {}
                    for id_str, usuario_data in data.get('usuarios', {}).items():
                        id_int = int(id_str)
                        usuario = Usuario(
                            id=id_int,
                            nome=usuario_data.get('nome', ''),
                            email=usuario_data.get('email', '')
                        )
                        self._usuarios[id_int] = usuario
                    self._nextId = data.get('nextId', 1)
            except (json.JSONDecodeError, IOError) as e:
                # Se houver erro ao ler, inicia com dados vazios
                self._usuarios = {}
                self._nextId = 1
    
    def _salvarDados(self):
        try:
            data = {
                'usuarios': {
                    str(id): {
                        'nome': usuario.nome,
                        'email': usuario.email
                    }
                    for id, usuario in self._usuarios.items()
                },
                'nextId': self._nextId
            }
            with open(self._filePath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise Exception(f"Erro ao salvar dados no arquivo: {e}")
    
    def criar(self, usuario: Usuario) -> Usuario:
        usuario.id = self._nextId
        self._nextId += 1
        self._usuarios[usuario.id] = usuario
        self._salvarDados()
        return usuario
    
    def buscarPorId(self, id: int) -> Usuario:
        return self._usuarios.get(id)
    
    def buscarTodos(self) -> List[Usuario]:
        return self._usuarios.values()
    
    def atualizar(self, usuario: Usuario) -> bool:
        if usuario.id and usuario.id in self._usuarios:
            self._usuarios[usuario.id] = usuario
            self._salvarDados()
            return True
        return False
    
    def deletar(self, id: int) -> bool:
        if id in self._usuarios:
            del self._usuarios[id]
            self._salvarDados()
            return True
        return False
    
    def buscarPorEmail(self, email: str) -> Usuario:
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario
        return None

