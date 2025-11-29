from fabrica_abstrata import PagamentoFactory
from pagamento import Pagamento, PagamentoPix, PagamentoCartao, PagamentoBoleto


class FactoryPagamentoOnline(PagamentoFactory):
    """Factory Method: cada método específico cria um tipo de pagamento"""
    
    def criarPix(self) -> Pagamento:
        print(f"Pagamento online.", end=" ")
        return PagamentoPix()
    
    def criarCartao(self) -> Pagamento:
        print(f"Pagamento online.", end=" ")
        return PagamentoCartao()
    
    def criarBoleto(self) -> Pagamento:
        # no contexto online, boleto não é permitido
        raise ValueError("Pagamento online não suporta boleto")

class FactoryPagamentoOffline(PagamentoFactory):
    """Factory Method: cada método específico cria um tipo de pagamento"""
    
    def criarPix(self) -> Pagamento:
        # no mundo offline, PIX não é usado
        raise ValueError("Pagamento offline não suporta PIX")
    
    def criarCartao(self) -> Pagamento:
        print(f"Pagamento offline.", end=" ")
        return PagamentoCartao()
    
    def criarBoleto(self) -> Pagamento:
        print(f"Pagamento offline.", end=" ")
        return PagamentoBoleto()