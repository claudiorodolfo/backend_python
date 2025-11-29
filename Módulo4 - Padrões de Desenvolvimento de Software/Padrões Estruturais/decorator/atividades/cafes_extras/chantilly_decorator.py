from bebida_decorator import BebidaDecorator

class Chantilly(BebidaDecorator):
    def getDescription(self) -> str:
        return self._bebida.getDescription() + ", chantilly"

    def getCost(self) -> float:
        return self._bebida.getCost() + 2.50