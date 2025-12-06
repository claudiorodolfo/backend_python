import os
from typing import Dict, Optional

class AtualizarPessoaView:
    """
    View Layer - Camada de apresentação
    Responsável apenas por entrada e saída de dados (I/O)
    """
    def show(self, pessoa_atual: Optional[Dict] = None, email: str = "") -> Dict:
        """Solicita dados da pessoa para atualizar"""
        os.system('cls||clear')

        print('Atualizar Pessoa \n\n')
        
        # Se já temos o email (passado como parâmetro), não precisa pedir novamente
        if email:
            print(f'E-mail: {email}\n')
            email_atual = email
        else:
            email_atual = input('Digite o e-mail da pessoa: ')
        
        # Pré-preencher campos com valores atuais se disponíveis
        nome_atual = pessoa_atual.get("nome", "") if pessoa_atual else ""
        idade_atual = str(pessoa_atual.get("idade", "")) if pessoa_atual and pessoa_atual.get("idade") is not None else ""
        altura_atual = str(pessoa_atual.get("altura", "")) if pessoa_atual and pessoa_atual.get("altura") is not None else ""
        
        nome = input(f'Digite o nome da pessoa (atual: {nome_atual if nome_atual else "vazio"}): ').strip()
        if not nome:
            nome = nome_atual if nome_atual else None
        
        idade = input(f'Digite a idade da pessoa (atual: {idade_atual if idade_atual else "vazio"}): ').strip()
        if not idade:
            idade = idade_atual if idade_atual else None
        
        altura = input(f'Digite a altura da pessoa (atual: {altura_atual if altura_atual else "vazio"}): ').strip()
        if not altura:
            altura = altura_atual if altura_atual else None

        return {
            "email": email_atual,
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

        corpo = erro["body"]

        mensagem = f'''
            Falha ao atualizar pessoa!

            Erro: {corpo["error"]}
        '''
        print(mensagem)
        input('\nPressione Enter para continuar...')