from bebida_decorator import BebidaDecorator
from bebiba import Bebida

class Leite(BebidaDecorator):
    def getDescription(self) -> str:
        return self._bebida.getDescription() + ", leite"

    def getCost(self) -> float:
        return self._bebida.getCost() + 1.50