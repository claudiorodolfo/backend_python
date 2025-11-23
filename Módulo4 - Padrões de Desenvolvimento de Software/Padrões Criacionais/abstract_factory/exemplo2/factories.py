from interfaces import Botao, CaixaSelecao
from light_theme import BotaoClaro, CaixaSelecaoClara
from dark_theme import BotaoEscuro, CaixaSelecaoEscura
from abstract_factory import FabricaGUI

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

