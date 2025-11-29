from bebida_decorator import BebidaDecorator

class Chocolate(BebidaDecorator):
    def getDescription(self) -> str:
        return self._bebida.getDescription() + ", chocolate"

    def getCost(self) -> float:
        return self._bebida.getCost() + 2.00