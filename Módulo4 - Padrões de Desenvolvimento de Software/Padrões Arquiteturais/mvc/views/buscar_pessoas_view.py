import os
from typing import Dict

class BuscarPessoasView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita o nome da pessoa para busca"""
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        nome = input('Informe o nome da pessoa para busca: ')

        return {
            "nome": nome
        }

    def showSuccess(self, dados: Dict):
        """Exibe os dados da pessoa encontrada"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]
        
        mensagem = f'''
            Usuário cadastrado com sucesso!

            Tipo: {cabecalho["type"]}
            Registros: {cabecalho["count"]}
            Informações:
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
