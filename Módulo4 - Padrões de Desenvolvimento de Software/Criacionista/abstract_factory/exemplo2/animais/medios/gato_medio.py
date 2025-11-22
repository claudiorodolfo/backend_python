from interfaces import Gato

# Implementação de gato de médio porte
class GatoMedio(Gato):
    def miar(self) -> str:
        return "MIAU! (miado médio de gato de médio porte)"
    
    def getPorte(self) -> str:
        return "Médio"

