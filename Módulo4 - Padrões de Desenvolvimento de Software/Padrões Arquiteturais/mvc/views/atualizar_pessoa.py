import os
from typing import Dict

class AtualizarPessoaView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita dados da pessoa para atualizar"""
        os.system('cls||clear')

        email = input('Digite o e-mail da pessoa: ')
        nome = input('Digite o nome da pessoa: ')
        idade = input('Digite a idade da pessoa: ')
        altura = input('Digite a altura da pessoa: ')

        return {
            "email": email,
            "nome": nome,
            "idade": idade,
            "altura": altura
        }

    def showSuccess(self, dados: Dict):
        """Exibe os dados da pessoa atualizada"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]

        mensagem = f'''
            Pessoa atualizada com sucesso!
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')

    def showFailure(self, erro: Dict):
        """Exibe mensagem de erro"""
        os.system('cls||clear')

        corpo = erro["body"]

        mensagem = f'''
            Falha ao atualizar pessoa!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')