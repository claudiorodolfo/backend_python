import os
from controllers.pessoa_controller import PessoaController
from views.cadastrar_pessoa_view import CadastrarPessoaView
from views.buscar_pessoa_view import BuscarPessoaView
from views.listar_todas_pessoas_view import ListarTodasPessoasView
from views.atualizar_pessoa import AtualizarPessoaView
from views.apagar_pessoa import ApagarPessoaView


class PessoaRoutes:
    """
    Router Sublayer - Gerencia as rotas da aplicação. 
    Subcamada do Controller Layer.
    """
    def __init__(self, pessoa_controller: PessoaController):
        self.pessoaController = pessoa_controller

        self.cadastrarView = CadastrarPessoaView()
        self.buscarView = BuscarPessoaView()
        self.listarTodasPessoasView = ListarTodasPessoasView()
        self.atualizarView = AtualizarPessoaView()
        self.apagarView = ApagarPessoaView()

    def cadastrarPessoa(self):
        """Rota para cadastrar uma pessoa"""
        informacoes_pessoa  = self.cadastrarView.show()
        resposta = self.pessoaController.cadastrarPessoa(informacoes_pessoa)

        if resposta["success"]:
            self.cadastrarView.showSuccess(resposta["data"])
        else:
            self.cadastrarView.showFailure(resposta["error"])

    def listarTodasPessoas(self):
        """Rota para buscar todas as pessoas"""
        resposta = self.pessoaController.listarTodasPessoas()

        if resposta["success"]:
            self.listarTodasPessoasView.showSuccess(resposta["data"])
        else:
            self.listarTodasPessoasView.showFailure(resposta["error"])

    def buscarPessoa(self):
        """Rota para buscar uma pessoa por email"""
        informacoes_pessoa = self.buscarView.show()
        email = informacoes_pessoa.get("email", "").strip()
        resposta = self.pessoaController.buscarPorEmail(email)

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
            print(f'\n  {resposta_busca["error"]["body"]["error"]}')
            print('A pessoa deve existir para ser atualizada.\n')
            input('Pressione Enter para continuar...')
        
        # Mostrar view de atualização com dados atuais (se encontrados)
        informacoes_pessoa = self.atualizarView.show(pessoa_atual, email)
        resposta = self.pessoaController.atualizarPessoa(informacoes_pessoa)

        if resposta["success"]:
            self.atualizarView.showSuccess(resposta["data"])
        else:
            self.atualizarView.showFailure(resposta["error"])

    def apagarPessoa(self):
        """Rota para apagar uma pessoa"""
        informacoes_pessoa = self.apagarView.show()
        resposta = self.pessoaController.apagarPessoa(informacoes_pessoa)

        if resposta["success"]:
            self.apagarView.showSuccess(resposta["data"])
        else:
            self.apagarView.showFailure(resposta["error"])