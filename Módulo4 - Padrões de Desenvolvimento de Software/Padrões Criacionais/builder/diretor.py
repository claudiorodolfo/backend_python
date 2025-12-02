from computador_builder import ComputadorBuilder
from enum import Enum

class TipoComputador(Enum):
    PC_GAMER = "pc_gamer"
    ESCRITORIO = "escritorio"
    NOTEBOOK = "notebook"

class Diretor:
    
    def __init__(self, builder: ComputadorBuilder):
        self.builder = builder

    def construir(self, tipo: TipoComputador = None):
        if tipo is None:
            return self.builder
        
        match tipo:
            case TipoComputador.PC_GAMER:
                self.builder.setCpu("Intel i9-13900K")
                self.builder.setRam("32GB DDR5")
                self.builder.setArmazenamento("2TB SSD NVMe")
                self.builder.setGpu("RTX 4080")
                self.builder.setMonitor("27\" 4K 144Hz")
                return self.builder.construir()
                
            case TipoComputador.ESCRITORIO:
                self.builder.setCpu("Intel i5-12400")
                self.builder.setRam("16GB DDR4")
                self.builder.setArmazenamento("512GB SSD")
                self.builder.setGpu("GPU Integrada")
                self.builder.setMonitor("24\" Full HD")
                return self.builder.construir()
                
            case TipoComputador.NOTEBOOK:
                self.builder.setCpu("AMD Ryzen 7 5800H")
                self.builder.setRam("16GB DDR4")
                self.builder.setArmazenamento("1TB SSD")
                self.builder.setGpu("RTX 3060")
                self.builder.setMonitor("15.6\" Full HD")
                
                if hasattr(self.builder, 'setBateria'):
                    self.builder.setBateria("80Wh")
                if hasattr(self.builder, 'setPeso'):
                    self.builder.setPeso("2.1kg")
                
                return self.builder.construir()
                
            case _:
                return self.builder

