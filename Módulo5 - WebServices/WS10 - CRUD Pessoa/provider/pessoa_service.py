from pessoa import Pessoa

class PessoaService:

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
        email_busca = pessoa.email.lower().strip()
        for index, p in enumerate(self.__pessoas):
            if email_busca == p.email.lower().strip():
                self.__pessoas[index] = pessoa
                return pessoa
        return None
    
    def apagar(self, pessoa: Pessoa) -> bool:
        """Apaga uma pessoa no repositório"""
        email_busca = pessoa.email.lower().strip()
        for index, p in enumerate(self.__pessoas):
            if email_busca == p.email.lower().strip():
                del self.__pessoas[index]
                return True
        return False

    def listarTodas(self) -> list:
        """Lista todas as pessoas"""
        return self.__pessoas.copy()