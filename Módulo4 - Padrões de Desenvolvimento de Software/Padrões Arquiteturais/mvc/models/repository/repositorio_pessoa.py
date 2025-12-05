from models.entities.pessoa import Pessoa


class RepositorioPessoas:
    """
    Repository sublayer - Camada de acesso a dados
    Subcamada do Model Layer.
    Responsável apenas por operações CRUD básicas
    """
    def __init__(self):
        self.__pessoas = []

    def criar(self, pessoa: Pessoa) -> Pessoa:
        """Cria uma nova pessoa no repositório"""
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorEmail(self, pessoa: Pessoa) -> Pessoa:
        """Busca uma pessoa por email (comparação exata)"""
        email_busca = pessoa.email.lower().strip()
        for p in self.__pessoas:
            # Verifica se o email buscado corresponde exatamente ao email da pessoa
            if email_busca == p.email.lower().strip():
                return p
        return None
    
    def atualizar(self, pessoa: Pessoa) -> Pessoa:
        """Atualiza uma pessoa no repositório"""
        for index, p in enumerate(self.__pessoas):
            if p.email == pessoa.email:
                self.__pessoas[index] = pessoa
                return pessoa
        return None
    
    def apagar(self, pessoa: Pessoa) -> bool:
        """Apaga uma pessoa no repositório"""
        for index, p in enumerate(self.__pessoas):
            if p.email == pessoa.email:
                del self.__pessoas[index]
                return True
        return False

    def listarTodas(self) -> list:
        """Lista todas as pessoas"""
        return self.__pessoas.copy()