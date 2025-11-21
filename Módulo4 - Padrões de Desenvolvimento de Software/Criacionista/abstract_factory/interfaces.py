from abc import ABC, abstractmethod

# Interfaces de produtos
class Botao(ABC):
    @abstractmethod
    def renderizar(self) -> str:
        pass

class CaixaSelecao(ABC):
    @abstractmethod
    def renderizar(self) -> str:
        pass

