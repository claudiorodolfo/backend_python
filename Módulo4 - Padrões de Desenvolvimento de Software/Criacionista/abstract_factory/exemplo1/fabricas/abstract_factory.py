from abc import ABC, abstractmethod
from comidas.comida import Comida
from bebidas.bebida import Bebida
# Fábrica abstrata
class DeliveryFactory(ABC):
    @abstractmethod
    def criarComida(self) -> Comida:
        pass
    
    @abstractmethod
    def criarBebida(self) -> Bebida:
        pass

