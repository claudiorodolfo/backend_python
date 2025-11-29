from abc import ABC, abstractmethod
from pagamento import Pagamento

# Fábrica abstrata
class PagamentoFactory(ABC):
    @abstractmethod
    def criarPix(self) -> Pagamento:
        pass
    
    @abstractmethod
    def criarCartao(self) -> Pagamento:
        pass
    
    @abstractmethod
    def criarBoleto(self) -> Pagamento:
        pass