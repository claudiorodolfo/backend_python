from interfaces import Botao, CaixaSelecao

# Produtos concretos para "tema claro"
class BotaoClaro(Botao):
    def renderizar(self) -> str:
        return "Botão claro"

class CaixaSelecaoClara(CaixaSelecao):
    def renderizar(self) -> str:
        return "Checkbox claro"

