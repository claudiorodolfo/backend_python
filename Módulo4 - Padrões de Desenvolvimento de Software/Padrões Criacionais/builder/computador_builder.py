from abc import ABC, abstractmethod
from computador import Computador

class ComputadorBuilder(ABC):
    
    @abstractmethod
    def setCpu(self, cpu):
        pass

    @abstractmethod
    def setRam(self, ram):
        pass

    @abstractmethod
    def setArmazenamento(self, armazenamento):
        pass

    @abstractmethod
    def setGpu(self, gpu):
        pass
    
    def setMonitor(self, monitor):
        pass

    @abstractmethod
    def getResultado(self) -> Computador:
        pass
    
    def construir(self) -> Computador:
        return self.getResultado()

