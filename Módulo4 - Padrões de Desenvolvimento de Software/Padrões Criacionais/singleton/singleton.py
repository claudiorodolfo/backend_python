import random

# BDManager Singleton
class BDManager:
    _instancia = None  # atributo de classe: armazena a instância única

    def __new__(cls):
        # __new__ é chamado **antes** de __init__, quando Python vai “criar” um objeto
        if cls._instancia is None:
            # Se ainda não existe uma instância, cria uma nova
            cls._instancia = super().__new__(cls)
            # Inicializa atributos “singleton” (só uma vez)
            cls._instancia._path = None
        return cls._instancia  # retorna a instância única

    def getInstancia(self, path):
        # Aqui self já é a instância única
        self._path = path
        # Inicializa só uma vez
        if not hasattr(self, "inicializado"):
            self._id = random.randint(1, 1000000)
           # self.inicializado = True
        return self

