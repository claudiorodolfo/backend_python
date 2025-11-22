from interfaces import Gato

# Implementação de gato de grande porte
class GatoGrande(Gato):
    def miar(self) -> str:
        return "MIAU MIAU! (miado profundo de gato grande)"
    
    def getPorte(self) -> str:
        return "Grande"

