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
        match forma:
            case "pix":
                return PagamentoOnlinePix()
            case "cartao":
                return PagamentoOnlineCartao()
            case _:
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
        match forma:
            case "boleto":
                return PagamentoOfflineBoleto()
            case "cartao":
                return PagamentoOfflineCartao()
            case _:
                raise ValueError(f"Pagamento offline não suporta forma: {forma}")
