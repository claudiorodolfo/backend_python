from interfaces import Gato

# Implementação de gato de pequeno porte
class GatoPequeno(Gato):
    def miar(self) -> str:
        return "Miau! (miado agudo de gato pequeno)"
    
    def getPorte(self) -> str:
        return "Pequeno"

