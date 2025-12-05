import os
from typing import Dict

class BuscarPessoaView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita o e-mail da pessoa para busca"""
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        email = input('Informe o e-mail da pessoa para busca: ')

        return {
            "email": email
        }

    def showSuccess(self, dados: Dict):
        """Exibe os dados da pessoa encontrada"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]
        
        mensagem = f'''
            Pessoa encontrada com sucesso!

            Tipo: {cabecalho["type"]}
            Registros: {cabecalho["count"]}
            Informações:
                Email: {corpo["email"]}
                Nome: {corpo["nome"]}
                Idade: {corpo["idade"]}
                Altura: {corpo["altura"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')

    def showFailure(self, erro: Dict):
        """Exibe mensagem de erro"""
        os.system('cls||clear')

        cabecalho = erro["head"]
        corpo = erro["body"]

        mensagem = f'''
            Falha ao encontrar usuário!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')
