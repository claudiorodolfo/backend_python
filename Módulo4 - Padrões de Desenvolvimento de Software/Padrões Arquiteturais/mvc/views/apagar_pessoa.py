import os
from typing import Dict

class ApagarPessoaView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita o email da pessoa para apagar"""
        os.system('cls||clear')

        email = input('Digite o email da pessoa: ')

        return {
            "email": email
        }

    def showSuccess(self, dados: Dict):
        """Exibe os dados da pessoa apagada"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]

        mensagem = f'''
            Pessoa apagada com sucesso!

            Tipo: {cabecalho["type"]}
            Registros: {cabecalho["count"]}
            Informações:
                Email: {corpo["email"]}

            Pressione Enter para continuar...
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')

    def showFailure(self, erro: Dict):
        """Exibe mensagem de erro"""
        os.system('cls||clear')

        corpo = erro["body"]

        mensagem = f'''
            Falha ao apagar pessoa!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')