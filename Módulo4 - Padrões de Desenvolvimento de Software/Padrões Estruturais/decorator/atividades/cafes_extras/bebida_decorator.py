from bebiba import Bebida
from abc import ABC, abstractmethod

class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self._bebida = bebida

    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getCost(self) -> float:
        pass