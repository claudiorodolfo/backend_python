from interfaces import Pato

# Implementação de pato de grande porte
class PatoGrande(Pato):
    def grasnar(self) -> str:
        return "QUACK QUACK! (grasnido forte de pato grande)"
    
    def getPorte(self) -> str:
        return "Grande"

