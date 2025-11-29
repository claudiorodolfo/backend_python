from bebida_decorator import BebidaDecorator

class Acucar(BebidaDecorator):
    def getDescription(self) -> str:
        return self._bebida.getDescription() + ", açúcar"

    def getCost(self) -> float:
        return self._bebida.getCost() + 0.50