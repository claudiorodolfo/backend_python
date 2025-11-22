from abc import abstractmethod
from interfaces.animal import Animal

# Interface abstrata para Pato
class Pato(Animal):
    @abstractmethod
    def grasnar(self) -> str:
        pass
    
    @abstractmethod
    def getPorte(self) -> str:
        pass

