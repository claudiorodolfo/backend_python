from abc import ABC, abstractmethod
from pagamento import Pagamento

# Fábrica abstrata
class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, forma: str) -> Pagamento:
        pass

    # opcional: método template, por exemplo, para realizar pagamento
    def realizarPagamento(self, forma: str, valor: float) -> None:
        pagamento = self.criarPagamento(forma)
        pagamento.pagar(valor)