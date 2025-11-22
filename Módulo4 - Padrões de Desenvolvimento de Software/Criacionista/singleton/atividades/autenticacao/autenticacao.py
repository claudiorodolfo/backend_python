class AuthManager:
    _instance = None

    def __new__(classe):
        if classe._instance is None:
            classe._instance = super().__new__(classe)
            # inicializa estado único
            classe._instance._usuariosRegistrados = {}  # dicionário com dados de registro dos usuários
            classe._instance._loginUsuariosAutenticados = []  # lista com ids dos usuários autenticados
        return classe._instance
        
    def getInstance(self):
        # __new__ já implementa o Singleton, então este método apenas cria/retorna a instância
        return self._instance
    
    def registrar(self, login: str, senha: str, tipo: str):
        self._usuariosRegistrados[login] = {
            "senha": senha,
            "tipo": tipo
        }

    def login(self, login: str, senha: str):
        usuarioAux = self._usuariosRegistrados.get(login)
        logado = False

        if usuarioAux is not None:   
            if usuarioAux["senha"] == senha:
                logado = True
                # Adiciona o login do usuário à lista de autenticados
                if login not in self._loginUsuariosAutenticados:
                    self._loginUsuariosAutenticados.append(login)
    
        return logado

    def estaLogado(self, login: str):
        return login in self._loginUsuariosAutenticados

    def logout(self, login: str):
        if login in self._loginUsuariosAutenticados:
            self._loginUsuariosAutenticados.remove(login)

    def todosUsuariosAutenticados(self):
        # Retorna um dicionário com os dados completos dos usuários autenticados
        usuariosAutenticados = {}
        for login in self._loginUsuariosAutenticados:
            if login in self._usuariosRegistrados:
                usuariosAutenticados[login] = self._usuariosRegistrados[login].copy()
        return usuariosAutenticados

    def todosUsuariosRegistrados(self):
        return self._usuariosRegistrados