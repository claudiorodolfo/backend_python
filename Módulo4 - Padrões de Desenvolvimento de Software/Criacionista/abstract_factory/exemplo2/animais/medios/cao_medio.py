from interfaces import Cao

# Implementação de cão de médio porte
class CaoMedio(Cao):
    def latir(self) -> str:
        return "AU AU! (latido médio de cão de médio porte)"
    
    def getPorte(self) -> str:
        return "Médio"

