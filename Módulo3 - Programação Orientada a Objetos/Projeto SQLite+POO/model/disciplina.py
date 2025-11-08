"""
Classe modelo para a tabela disciplina
"""

class Disciplina:
    def __init__(self, id: int, nome: str, cargaHoraria: int | None = None,
                 descricao: str | None = None):
        self.__id = id
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
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
    def cargaHoraria(self):
        return self.__cargaHoraria
    
    @cargaHoraria.setter
    def cargaHoraria(self, value):
        self.__cargaHoraria = value
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, value):
        self.__descricao = value
    
    def __str__(self):
        return (f"Disciplina(id={self.__id}, nome='{self.__nome}', "
                f"cargaHoraria={self.__cargaHoraria})")

