from controllers.pessoa_controller import PessoaController
from views.cadastrar_pessoa_view import CadastrarPessoaView
from views.buscar_pessoa_view import BuscarPessoaView
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
        informacoesPessoa = self.atualizarView.show()
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