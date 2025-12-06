import os
from controllers.pessoa_controller import PessoaController
from views.cadastrar_pessoa_view import CadastrarPessoaView
from views.buscar_pessoa_view import BuscarPessoaView
from views.buscar_todas_pessoas_view import BuscarTodasPessoasView
from views.atualizar_pessoa import AtualizarPessoaView
from views.apagar_pessoa import ApagarPessoaView


class PessoaRoutes:
    """
    Router Sublayer - Gerencia as rotas da aplicação. 
    Subcamada do Controller Layer.
    """
    def __init__(self, pessoaController: PessoaController):
        self.pessoaController = pessoaController
        self.cadastrarView = CadastrarPessoaView()
        self.buscarView = BuscarPessoaView()
        self.buscarTodasPessoasView = BuscarTodasPessoasView()
        self.atualizarView = AtualizarPessoaView()
        self.apagarView = ApagarPessoaView()

    def cadastrarPessoa(self):
        """Rota para cadastrar uma pessoa"""
        informacoesPessoa = self.cadastrarView.show()
        resposta = self.pessoaController.cadastrarPessoa(informacoesPessoa)

        if resposta["success"]:
            self.cadastrarView.showSuccess(resposta["data"])
        else:
            self.cadastrarView.showFailure(resposta["error"])

    def buscarTodasPessoas(self):
        """Rota para buscar todas as pessoas"""
        resposta = self.pessoaController.buscarTodasPessoas()

        if resposta["success"]:
            self.buscarTodasPessoasView.showSuccess(resposta["data"])
        else:
            self.buscarTodasPessoasView.showFailure(resposta["error"])

    def buscarPessoa(self):
        """Rota para buscar uma pessoa por email"""
        informacoesPessoa = self.buscarView.show()
        resposta = self.pessoaController.buscarPorEmail(informacoesPessoa["email"])

        if resposta["success"]:
            self.buscarView.showSuccess(resposta["data"])
        else:
            self.buscarView.showFailure(resposta["error"])

    def atualizarPessoa(self):
        """Rota para atualizar uma pessoa"""
        # Primeiro, solicitar apenas o email para buscar a pessoa
        os.system('cls||clear')
        print('Atualizar Pessoa \n\n')
        email = ""
        while not email.strip():
            email = input('Digite o e-mail da pessoa para atualizar (obrigatório): ')
            if not email.strip():
                print('E-mail é obrigatório! Por favor, informe um e-mail.\n')
        
        # Buscar pessoa existente para mostrar valores atuais
        resposta_busca = self.pessoaController.buscarPorEmail(email)
        pessoa_atual = None
        if resposta_busca["success"]:
            pessoa_atual = resposta_busca["data"]["body"]
        else:
            # Se não encontrou, ainda permite continuar, mas sem mostrar valores atuais
            print(f'\n⚠️  {resposta_busca["error"]["body"]["error"]}')
            print('Você pode continuar, mas a pessoa deve existir para ser atualizada.\n')
            input('Pressione Enter para continuar...')
        
        # Mostrar view de atualização com dados atuais (se encontrados)
        informacoesPessoa = self.atualizarView.show(pessoa_atual, email)
        
        resposta = self.pessoaController.atualizarPessoa(informacoesPessoa)

        if resposta["success"]:
            self.atualizarView.showSuccess(resposta["data"])
        else:
            self.atualizarView.showFailure(resposta["error"])

    def apagarPessoa(self):
        """Rota para apagar uma pessoa"""
        informacoesPessoa = self.apagarView.show()
        resposta = self.pessoaController.apagarPessoa(informacoesPessoa)

        if resposta["success"]:
            self.apagarView.showSuccess(resposta["data"])
        else:
            self.apagarView.showFailure(resposta["error"])