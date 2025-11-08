"""
Classe modelo para a tabela disciplina
"""

class Disciplina:
    def __init__(self, id: int, nome: str, carga_horaria: int | None = None,
                 descricao: str | None = None):
        self.__id = id
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__descricao = descricao
    
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
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, value):
        self.__carga_horaria = value
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, value):
        self.__descricao = value
    
    def __str__(self):
        return (f"Disciplina(id={self.__id}, nome='{self.__nome}', "
                f"carga_horaria={self.__carga_horaria})")

