from abc import ABC, abstractmethod
from animal import Animal

# Creator abstrato - Factory Method Pattern
class AnimalFactory(ABC):
    
    @abstractmethod
    def criarAnimal(self) -> Animal:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass

