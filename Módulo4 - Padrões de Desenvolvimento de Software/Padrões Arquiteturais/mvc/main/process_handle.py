from views.index_view import IndexView
from models.repository.repositorio_pessoa import RepositorioPessoas
from controllers.pessoa_controller import PessoaController
from routes.pessoa_routes import PessoaRoutes


class ProcessHandle:
    """
    Application Handler - Ponto de entrada da aplicação
    Configura as dependências e inicializa o roteador
    Similar ao que frameworks fazem com app.run() ou main()
    """
    def __init__(self):
        self.repository = RepositorioPessoas()
        self.pessoaController = PessoaController(self.repository)
        self.pessoaRoutes = PessoaRoutes(self.pessoaController)
        self.indexView = IndexView()

    def start(self):
        """Inicia o loop principal da aplicação"""
        while True:
            comando = self.indexView.show()
            
            match int(comando["comando"]):
                case 0:
                    print('\nSaindo do sistema...')
                    exit()
                case 1:
                    self.pessoaRoutes.cadastrarPessoa()
                case 2:
                    self.pessoaRoutes.buscarPessoa()
                case 3:
                    self.pessoaRoutes.atualizarPessoa()
                case 4:
                    self.pessoaRoutes.apagarPessoa()
                case _:
                    print('\nComando não encontrado!!\n\n')
                    input('Pressione Enter para continuar...')
