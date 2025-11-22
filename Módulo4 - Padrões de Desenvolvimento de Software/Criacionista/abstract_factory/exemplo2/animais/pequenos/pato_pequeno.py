from interfaces import Pato

# Implementação de pato de pequeno porte
class PatoPequeno(Pato):
    def grasnar(self) -> str:
        return "Quack! (grasnido agudo de pato pequeno)"
    
    def getPorte(self) -> str:
        return "Pequeno"

