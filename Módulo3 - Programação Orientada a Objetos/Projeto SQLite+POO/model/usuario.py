"""
Classe modelo para a tabela usuario (relacionamento 1:1 com Pessoa)
"""
from model.pessoa import Pessoa

class Usuario:
    def __init__(self, id: int, login: str, senha: str, tipo: str, pessoa: Pessoa):
        self.__id = id
        self.__login = login
        self.__senha = senha
        self.__tipo = tipo
        self.__pessoa = pessoa
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, value):
        self.__login = value
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, value):
        self.__senha = value
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, value):
        self.__tipo = value
    
    @property
    def pessoa(self):
        return self.__pessoa
    
    @pessoa.setter
    def pessoa(self, value):
        self.__pessoa = value
    
    def __str__(self):
        return (f"Usuario(id={self.__id}, login='{self.__login}', "
                f"tipo='{self.__tipo}', pessoa_id={self.__pessoa.id})")

