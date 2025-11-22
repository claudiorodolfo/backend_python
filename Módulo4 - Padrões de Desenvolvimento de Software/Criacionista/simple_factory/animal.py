from abc import ABC, abstractmethod

# Interface / produto
class Animal(ABC):
    @abstractmethod
    def fazSom(self) -> str:
        pass