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

        mensagem = f'''
            Usuário encontrado com sucesso!

            Tipo: {dados["head"]["type"]}
            Registros: {dados["head"]["count"]}
            Informações:
                Nome: {dados["body"]["nome"]}
                Idade: {dados["body"]["idade"]}
                Altura: {dados["body"]["altura"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')

    def showFailure(self, erro: str):
        """Exibe mensagem de erro"""
        os.system('cls||clear')

        mensagem = f'''
            Falha ao encontrar usuário!

            Erro: {erro}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')
