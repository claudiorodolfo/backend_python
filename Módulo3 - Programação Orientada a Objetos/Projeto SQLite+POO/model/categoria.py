"""
Classe modelo para a tabela categoria
"""

class Categoria: 
    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome
    
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
    
    def __str__(self):
        return f"Categoria(id={self.__id}, nome='{self.__nome}')"

