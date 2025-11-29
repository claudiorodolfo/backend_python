from bebiba import Bebida

class CafeSimples(Bebida):
    def getDescription(self) -> str:
        return "Café simples"

    def getCost(self) -> float:
        # custo base do café
        return 3.00