"""
    Entity sublayer - Camada de entidades.
    Subcamada do Model Layer.
"""
class Pessoa:
    def __init__(self, email: str, nome: str = None, idade: int = None, altura: float = None):
        self.__email = email
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def email(self):
        return self.__email

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura