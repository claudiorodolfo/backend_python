import os
from typing import Dict

class CadastrarPessoasView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita dados do usuário para cadastro"""
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        nome = input('Informe o nome da pessoa: ')
        idade = input('Informe a idade da pessoa: ')
        altura = input('Informe a altura da pessoa: ')

        return {
            "nome": nome,
            "idade": idade,
            "altura": altura
        }

    def showSuccess(self, dados: Dict):
        """Exibe mensagem de sucesso com os dados cadastrados"""
        os.system('cls||clear')

        mensagem = f'''
            Usuário cadastrado com sucesso!

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
            Falha ao cadastrar usuário!

            Erro: {erro}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')