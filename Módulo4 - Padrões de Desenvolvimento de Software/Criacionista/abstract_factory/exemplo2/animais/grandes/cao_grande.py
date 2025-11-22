from interfaces import Cao

# Implementação de cão de grande porte
class CaoGrande(Cao):
    def latir(self) -> str:
        return "AU AU AU! (latido profundo e forte de cão grande)"
    
    def getPorte(self) -> str:
        return "Grande"

