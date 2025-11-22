from abc import ABC, abstractmethod

# Classe base abstrata para todos os animais
class Animal(ABC):
    @abstractmethod
    def getPorte(self) -> str:
        pass

