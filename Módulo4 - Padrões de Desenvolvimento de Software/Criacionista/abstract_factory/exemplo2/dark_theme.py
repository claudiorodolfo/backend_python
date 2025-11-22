from interfaces import Botao, CaixaSelecao

# Produtos concretos para "tema escuro"
class BotaoEscuro(Botao):
    def renderizar(self) -> str:
        return "Botão escuro"

class CaixaSelecaoEscura(CaixaSelecao):
    def renderizar(self) -> str:
        return "Checkbox escuro"

