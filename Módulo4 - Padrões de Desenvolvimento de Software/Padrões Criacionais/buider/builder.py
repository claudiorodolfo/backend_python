from abc import ABC, abstractmethod
from product import Computador

# --- Builder (abstrato) ---
class ConstrutorComputador(ABC):
    """Interface/abstração de builder — define os métodos para construir partes do computador."""
    def __init__(self):
        self._pc = Computador()

    @abstractmethod
    def construirCpu(self):
        pass

    @abstractmethod
    def construirMemoria(self):
        pass

    @abstractmethod
    def construirArmazenamento(self):
        pass

    # métodos opcionais
    def construirGpu(self):
        # padrão: nada
        return

    def instalarSistema(self):
        # padrão: nada
        return

    def getResultado(self) -> Computador:
        """Retorna o produto final."""
        return self._pc
