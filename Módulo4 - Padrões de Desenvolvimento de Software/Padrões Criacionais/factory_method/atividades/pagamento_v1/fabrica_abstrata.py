from abc import ABC, abstractmethod
from pagamento import Pagamento

# Fábrica abstrata
class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, tipo: str) -> Pagamento:
        pass

    # opcional: método template, por exemplo, para realizar pagamento
    def realizarPagamento(self, tipo: str, valor: float) -> None:
        pagamento = self.criarPagamento(tipo)
        pagamento.pagar(valor)