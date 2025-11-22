from interfaces import Cao, Gato, Pato
from animais.medios import CaoMedio, GatoMedio, PatoMedio
from .fabrica_animais import FabricaAnimais

# Fábrica concreta para animais de médio porte
class FabricaAnimaisMedios(FabricaAnimais):
    def _inicializar_tipos(self):
        """Registra os tipos de animais de médio porte que esta fábrica pode criar"""
        self._tipos_animais = {
            'cao': CaoMedio,
            'gato': GatoMedio,
            'pato': PatoMedio
        }

