from abc import ABC, abstractmethod

# Hierarquia de pagamentos
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoPix(Pagamento):
    def pagar(self, valor: float):
        print(f"Enviando PIX para valor de R$ {valor:.2f}.")

class PagamentoBoleto(Pagamento):
    def pagar(self, valor: float):
        print(f"Gerando boleto para R$ {valor:.2f}.")
