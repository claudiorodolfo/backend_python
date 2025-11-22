from interfaces import Cao, Gato, Pato
from animais.grandes import CaoGrande, GatoGrande, PatoGrande
from .fabrica_animais import FabricaAnimais

# Fábrica concreta para animais de grande porte
class FabricaAnimaisGrandes(FabricaAnimais):
    def _inicializar_tipos(self):
        """Registra os tipos de animais de grande porte que esta fábrica pode criar"""
        self._tipos_animais = {
            'cao': CaoGrande,
            'gato': GatoGrande,
            'pato': PatoGrande
        }

