from abc import ABC, abstractmethod

# Hierarquia de pagamentos

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoOnlineCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoOnlinePix(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Enviando PIX para valor de R$ {valor:.2f}.")

class PagamentoOfflineCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Offline.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoOfflineBoleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento Offline.",end=" ")
        print(f"Gerando boleto para R$ {valor:.2f}.")
