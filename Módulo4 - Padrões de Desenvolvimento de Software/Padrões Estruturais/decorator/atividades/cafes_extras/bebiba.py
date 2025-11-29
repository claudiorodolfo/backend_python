from abc import ABC, abstractmethod

class Bebida(ABC):

    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getCost(self) -> float:
        pass