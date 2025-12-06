import os
from typing import Dict

class CadastrarPessoaView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self) -> Dict:
        """Solicita dados do usuário para cadastro"""
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        
        # Email é obrigatório
        email = ""
        while not email.strip():
            email = input('Informe o e-mail (obrigatório): ')
            if not email.strip():
                print('E-mail é obrigatório! Por favor, informe um e-mail.\n')
        
        # Demais campos são opcionais
        nome = input('Informe o nome (opcional - pressione Enter para pular): ')
        idade = input('Informe a idade (opcional - pressione Enter para pular): ')
        altura = input('Informe a altura (opcional - pressione Enter para pular): ')

        return {
            "email": email,
            "nome": nome,
            "idade": idade,
            "altura": altura
        }

    def showSuccess(self, dados: Dict):
        """Exibe mensagem de sucesso com os dados cadastrados"""
        os.system('cls||clear')

        cabecalho = dados["head"]
        corpo = dados["body"]

        mensagem = f'''
            Usuário cadastrado com sucesso!

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
            Falha ao cadastrar usuário!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')