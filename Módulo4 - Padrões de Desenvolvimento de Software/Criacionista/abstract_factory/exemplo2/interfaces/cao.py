from abc import abstractmethod
from interfaces.animal import Animal

# Interface abstrata para Cão
class Cao(Animal):
    @abstractmethod
    def latir(self) -> str:
        pass
    
    @abstractmethod
    def getPorte(self) -> str:
        pass

