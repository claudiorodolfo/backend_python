from models.entities.pessoa import Pessoa


class RepositorioPessoas:
    """
    Repository sublayer - Camada de acesso a dados
    Subcamada do Model Layer.
    Responsável apenas por operações CRUD básicas
    """
    def __init__(self):
        self.__pessoas = []

    def create(self, pessoa: Pessoa) -> Pessoa:
        """Cria uma nova pessoa no repositório"""
        self.__pessoas.append(pessoa)
        return pessoa

    def findByNome(self, nome: str) -> Pessoa:
        """Busca uma pessoa pelo nome"""
        for pessoa in self.__pessoas:
            if pessoa.nome == nome:
                return pessoa
        return None

    def listAll(self) -> list:
        """Lista todas as pessoas"""
        return self.__pessoas.copy()