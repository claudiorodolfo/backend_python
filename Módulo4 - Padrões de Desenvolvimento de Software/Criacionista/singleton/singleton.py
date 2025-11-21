import random

class ConectorBD:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, valor=None):
        # Inicializa só uma vez
        if not hasattr(self, "inicializado"):
            self._id = random.randint(1, 1000000)
            print(f"ID da conexão: {self._id}")
            self.inicializado = True

    @classmethod
    def getInstancia(cls, valor=None):
        """Retorna a instância única do Singleton."""
        if cls._instancia is None:
            cls._instancia = cls(valor)
        return cls._instancia

