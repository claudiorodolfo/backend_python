from abc import ABC, abstractmethod

# Interfaces de produtos abstratos
class Comida(ABC):
    @abstractmethod
    def removerIngrediente(self, ingrediente):
        pass


