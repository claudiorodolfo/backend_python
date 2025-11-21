"""
Diretor que orquestra a construção usando um builder
"""
from computador_builder import ComputadorBuilder
from enum import Enum

class TipoComputador(Enum):
    """Enum para definir os tipos de computadores disponíveis"""
    PC_GAMER = "pc_gamer"
    ESCRITORIO = "escritorio"
    NOTEBOOK = "notebook"

class Diretor:
    def __init__(self, builder: ComputadorBuilder):
        self.builder = builder

    def construir(self, tipo: TipoComputador = None):
        """
        Método genérico que constrói o computador baseado no tipo especificado.
        Se nenhum tipo for especificado, usa as configurações padrão do builder.
        """
        if tipo == TipoComputador.PC_GAMER:
            return (self.builder
                    .setCpu("Intel i9-13900K")
                    .setRam("32GB DDR5")
                    .setArmazenamento("2TB SSD NVMe")
                    .setGpu("RTX 4080")
                    .setMonitor("27\" 4K 144Hz")
                    .construir())
        elif tipo == TipoComputador.ESCRITORIO:
            return (self.builder
                    .setCpu("Intel i5-12400")
                    .setRam("16GB DDR4")
                    .setArmazenamento("512GB SSD")
                    .setGpu("GPU Integrada")
                    .setMonitor("24\" Full HD")
                    .construir())
        elif tipo == TipoComputador.NOTEBOOK:
            builder = (self.builder
                      .setCpu("AMD Ryzen 7 5800H")
                      .setRam("16GB DDR4")
                      .setArmazenamento("1TB SSD")
                      .setGpu("RTX 3060")
                      .setMonitor("15.6\" Full HD"))
            # Verifica se o builder suporta métodos específicos de notebook
            if hasattr(builder, 'setBateria'):
                builder = builder.setBateria("80Wh")
            if hasattr(builder, 'setPeso'):
                builder = builder.setPeso("2.1kg")
            return builder.construir()
        else:
            # Se nenhum tipo for especificado, retorna o builder para construção customizada
            return self.builder

