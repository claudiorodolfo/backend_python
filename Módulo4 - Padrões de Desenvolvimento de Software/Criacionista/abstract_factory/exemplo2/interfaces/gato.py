from abc import abstractmethod
from interfaces.animal import Animal

# Interface abstrata para Gato
class Gato(Animal):
    @abstractmethod
    def miar(self) -> str:
        pass
    
    @abstractmethod
    def getPorte(self) -> str:
        pass

