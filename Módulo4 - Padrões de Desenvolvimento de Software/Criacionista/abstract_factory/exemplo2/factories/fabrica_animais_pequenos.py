from interfaces import Cao, Gato, Pato
from animais.pequenos import CaoPequeno, GatoPequeno, PatoPequeno
from .fabrica_animais import FabricaAnimais

# Fábrica concreta para animais de pequeno porte
class FabricaAnimaisPequenos(FabricaAnimais):
    def _inicializar_tipos(self):
        """Registra os tipos de animais de pequeno porte que esta fábrica pode criar"""
        self._tipos_animais = {
            'cao': CaoPequeno,
            'gato': GatoPequeno,
            'pato': PatoPequeno
        }

