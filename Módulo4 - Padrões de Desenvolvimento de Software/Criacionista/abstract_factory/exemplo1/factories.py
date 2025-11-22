from abc import ABC, abstractmethod
from interfaces import Botao, CaixaSelecao
from light_theme import BotaoClaro, CaixaSelecaoClara
from dark_theme import BotaoEscuro, CaixaSelecaoEscura

# Fábrica abstrata
class FabricaGUI(ABC):
    @abstractmethod
    def criarBotao(self) -> Botao:
        pass

    @abstractmethod
    def criarCaixaSelecao(self) -> CaixaSelecao:
        pass

# Fábricas concretas
class FabricaClara(FabricaGUI):
    def criarBotao(self) -> Botao:
        return BotaoClaro()

    def criarCaixaSelecao(self) -> CaixaSelecao:
        return CaixaSelecaoClara()

class FabricaEscura(FabricaGUI):
    def criarBotao(self) -> Botao:
        return BotaoEscuro()

    def criarCaixaSelecao(self) -> CaixaSelecao:
        return CaixaSelecaoEscura()

