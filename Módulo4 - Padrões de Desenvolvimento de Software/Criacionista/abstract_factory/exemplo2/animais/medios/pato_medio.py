from interfaces import Pato

# Implementação de pato de médio porte
class PatoMedio(Pato):
    def grasnar(self) -> str:
        return "QUACK! (grasnido médio de pato de médio porte)"
    
    def getPorte(self) -> str:
        return "Médio"

