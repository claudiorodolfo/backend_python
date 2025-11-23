from abc import ABC, abstractmethod

# Hierarquia de pagamentos

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float) -> None:
        pass

class PagamentoCartao(Pagamento):
    def pagar(self, valor: float) -> None:
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoBoleto(Pagamento):
    def pagar(self, valor: float) -> None:
        print(f"Gerando boleto para R$ {valor:.2f}.")

class PagamentoPix(Pagamento):
    def pagar(self, valor: float) -> None:
        print(f"Enviando PIX para valor de R$ {valor:.2f}.")