from controllers.pessoa_controller import PessoaController
from views.cadastrar_pessoas_view import CadastrarPessoasView
from views.buscar_pessoas_view import BuscarPessoasView


class PessoaRoutes:
    """
    Router Sublayer - Gerencia as rotas da aplicação. 
    Subcamada do Controller Layer.
    """
    def __init__(self, pessoaController: PessoaController):
        self.pessoaController = pessoaController
        self.cadastrarView = CadastrarPessoasView()
        self.buscarView = BuscarPessoasView()

    def cadastrarPessoa(self):
        """Rota para cadastrar uma pessoa"""
        informacoesPessoa = self.cadastrarView.show()
        resposta = self.pessoaController.cadastrarPessoa(informacoesPessoa)

        if resposta["success"]:
            self.cadastrarView.showSuccess(resposta["data"])
        else:
            self.cadastrarView.showFailure(resposta["error"])

    def buscarPessoa(self):
        """Rota para buscar uma pessoa por nome"""
        informacoesPessoa = self.buscarView.show()
        resposta = self.pessoaController.buscarPorNome(informacoesPessoa["nome"])

        if resposta["success"]:
            self.buscarView.showSuccess(resposta["data"])
        else:
            self.buscarView.showFailure(resposta["error"])

