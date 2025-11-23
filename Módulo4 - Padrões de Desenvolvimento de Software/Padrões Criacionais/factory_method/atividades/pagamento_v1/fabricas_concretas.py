from fabrica_abstrata import PagamentoFactory
from pagamento import Pagamento, PagamentoPix, PagamentoCartao, PagamentoBoleto


""" 
Poderia ser uma classe abstrata e as subclasses implementariam
novamente o padrão Factory Method, mas para deixar mais simples, 
deixei nessa camada o uso do Simple Factory. 
Na versão 2 há a implementação usando o Factory Method novamente, nesta camada.
"""
class FactoryPagamentoOnline(PagamentoFactory):
    def criarPagamento(self, tipo: str) -> Pagamento:
        print(f"Pagamento online.",end=" ")
        tipo = tipo.lower()
        # boleto não é permitido online
        if tipo == "pix":
            return PagamentoPix()
        elif tipo == "cartao":
            return PagamentoCartao()
        else:
            # para boleto, ou outras formas de pagamento online não suportadas
            raise ValueError(f"Pagamento online não suporta tipo: {tipo}")

""" 
Poderia ser uma classe abstrata e as subclasses implementariam
novamente o padrão Factory Method, mas para deixar mais simples, 
deixei nessa camada o uso do Simple Factory. 
Na versão 2 há a implementação usando o Factory Method novamente, nesta camada.
"""
class FactoryPagamentoOffline(PagamentoFactory):
    def criarPagamento(self, tipo: str) -> Pagamento:
        print(f"Pagamento offline.",end=" ")
        tipo = tipo.lower()
        # pix não é permitido offline
        if tipo == "boleto":
            return PagamentoBoleto()
        elif tipo == "cartao":
            return PagamentoCartao()
        else:
            # para pix, ou outras formas de pagamento offline não suportadas
            raise ValueError(f"Pagamento offline não suporta tipo: {tipo}")