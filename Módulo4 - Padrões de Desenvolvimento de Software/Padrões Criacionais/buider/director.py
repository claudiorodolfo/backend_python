from builder import ConstrutorComputador
from product import Computador

# --- Diretor ---
class DiretorComputador:
    """Diretor é responsável por definir a ordem de construção e dirigir o builder."""
    def __init__(self, builder: ConstrutorComputador):
        self._builder = builder

    def fabricarBasico(self):
        """Constrói uma configuração básica: CPU + Memória + Armazenamento."""
        self._builder.construirCpu()
        self._builder.construirMemoria()
        self._builder.construirArmazenamento()

    def fabricarCompleto(self):
        """Constrói uma configuração completa: todas as partes."""
        self._builder.construirCpu()
        self._builder.construirMemoria()
        self._builder.construirArmazenamento()
        self._builder.construirGpu()
        self._builder.instalarSistema()

    def construir(self) -> Computador:
        return self._builder.getResultado()