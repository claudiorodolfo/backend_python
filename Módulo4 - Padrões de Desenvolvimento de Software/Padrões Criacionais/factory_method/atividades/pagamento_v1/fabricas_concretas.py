from fabrica_abstrata import PagamentoFactory
from pagamento import Pagamento, PagamentoOnlinePix, PagamentoOnlineCartao, PagamentoOfflineBoleto, PagamentoOfflineCartao


""" 
Poderia ser uma classe abstrata e as subclasses implementariam
novamente o padrão Factory Method, mas para deixar mais simples, 
deixei nessa camada o uso do Simple Factory. 
Na versão 2 há a implementação usando o Factory Method novamente, nesta camada.
"""
class FactoryPagamentoOnline(PagamentoFactory):
    def criarPagamento(self, forma: str) -> Pagamento:
        forma = forma.lower()
        # boleto não é permitido online
        if forma == "pix":
            return PagamentoOnlinePix()
        elif forma == "cartao":
            return PagamentoOnlineCartao()
        else:
            # para boleto, ou outras formas de pagamento online não suportadas
            raise ValueError(f"Pagamento online não suporta forma: {forma}")

""" 
Poderia ser uma classe abstrata e as subclasses implementariam
novamente o padrão Factory Method, mas para deixar mais simples, 
deixei nessa camada o uso do Simple Factory. 
Na versão 2 há a implementação usando o Factory Method novamente, nesta camada.
"""
class FactoryPagamentoOffline(PagamentoFactory):
    def criarPagamento(self, forma: str) -> Pagamento:
        forma = forma.lower()
        # pix não é permitido offline
        if forma == "boleto":
            return PagamentoOfflineBoleto()
        elif forma == "cartao":
            return PagamentoOfflineCartao()
        else:
            # para pix, ou outras formas de pagamento offline não suportadas
            raise ValueError(f"Pagamento offline não suporta forma: {forma}")