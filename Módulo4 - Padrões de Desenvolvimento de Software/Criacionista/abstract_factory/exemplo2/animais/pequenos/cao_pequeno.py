from interfaces import Cao

# Implementação de cão de pequeno porte
class CaoPequeno(Cao):
    def latir(self) -> str:
        return "Au au! (latido agudo de cão pequeno)"
    
    def getPorte(self) -> str:
        return "Pequeno"

