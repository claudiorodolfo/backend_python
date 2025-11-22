from abc import ABC, abstractmethod
from interfaces import Botao, CaixaSelecao

# Fábrica abstrata
class FabricaGUI(ABC):
    @abstractmethod
    def criarBotao(self) -> Botao:
        pass

    @abstractmethod
    def criarCaixaSelecao(self) -> CaixaSelecao:
        pass
