"""
Builder concreto para construção de computadores de escritório
"""
from computador import Computador
from computador_builder import ComputadorBuilder

class EscritorioBuilder(ComputadorBuilder):
    def __init__(self):
        self.computador = Computador()

    def setCpu(self, cpu):
        self.computador.cpu = cpu
        return self

    def setRam(self, ram):
        self.computador.ram = ram
        return self

    def setArmazenamento(self, armazenamento):
        self.computador.armazenamento = armazenamento
        return self

    def setGpu(self, gpu):
        self.computador.gpu = gpu
        return self

    def setMonitor(self, monitor):
        self.computador.monitor = monitor
        return self

    def getResultado(self) -> Computador:
        # Validação: Computador de escritório pode usar GPU integrada
        if not self.computador.gpu:
            self.computador.gpu = "GPU Integrada"
        return self.computador
    
    def construir(self) -> Computador:
        """Método de conveniência que chama getResultado()"""
        return self.getResultado()

