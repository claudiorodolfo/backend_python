"""
Classe modelo para a tabela pessoa
"""
from model.categoria import Categoria

class Pessoa:
    def __init__(self, id: int, nome: str, categoria: Categoria, email: str,
                 altura: float | None = None,
                 peso: float | None = None, dataNascimento: str | None = None,
                 ativo: bool = True,
                 telefone: str | None = None):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__altura = altura
        self.__peso = peso
        self.__dataNascimento = dataNascimento
        self.__ativo = ativo
        self.__telefone = telefone
        self.__categoria = categoria
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, value):
        self.__altura = value
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, value):
        self.__peso = value
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, value):
        self.__dataNascimento = value
    
    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, value):
        self.__ativo = value
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, value):
        self.__telefone = value
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, value):
        self.__categoria = value
    
    def __str__(self):
        return (f"Pessoa(id={self.__id}, nome='{self.__nome}', "
                f"email='{self.__email}', "
                f"categoria_id={self.__categoria.id})")

