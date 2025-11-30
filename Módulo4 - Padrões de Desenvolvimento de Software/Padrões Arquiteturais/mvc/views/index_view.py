from typing import Dict

class IndexView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        mensagem = '''
        Sistema Cadastral

        * 0 - Sair
        * 1 - Cadastrar Pessoa
        * 2 - Buscar Pessoa Por Nome
        '''

        print(mensagem)
        comando = input('Comando: ')

        return {
            "comando": comando
        }
