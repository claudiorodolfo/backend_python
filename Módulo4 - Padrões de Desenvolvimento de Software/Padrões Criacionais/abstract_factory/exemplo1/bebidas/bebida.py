from abc import ABC, abstractmethod

# Interfaces de produtos abstratos
class Bebida(ABC):
    @abstractmethod
    def escolherSemAcucar(self):
        pass

