import os
from typing import Dict

class BuscarTodasPessoasView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita a listagem de todas as pessoas"""
        os.system('cls||clear')

        print('Buscar Todas Pessoas \n\n')
        return {}

    def showSuccess(self, dados: Dict):
        """Exibe os dados das pessoas encontradas"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]

        print('Buscar Todas Pessoas \n\n')
        print(f'Total de pessoas encontradas: {cabecalho["count"]}\n')
        
        if isinstance(corpo, list) and len(corpo) > 0:
            for i, pessoa in enumerate(corpo, 1):
                print(f'--- Pessoa {i} ---')
                print(f'Email: {pessoa.get("email", "N/A")}')
                print(f'Nome: {pessoa.get("nome", "N/A")}')
                print(f'Idade: {pessoa.get("idade", "N/A")}')
                print(f'Altura: {pessoa.get("altura", "N/A")}')
                print()
        else:
            print('Nenhuma pessoa encontrada.')
        
        input('\nPressione Enter para continuar...')

    def showFailure(self, erro: Dict):
        """Exibe mensagem de erro"""
        os.system('cls||clear')
        corpo = erro["body"]

        mensagem = f'''
            Falha ao listar pessoas!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')
