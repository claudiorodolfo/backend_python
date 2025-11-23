from fabricas_concretas import FactoryPagamentoOnline, FactoryPagamentoOffline

if __name__ == "__main__":
    # fábrica online - Factory Method puro
    factoryOnline = FactoryPagamentoOnline()
    pagamento_pix = factoryOnline.criarPix()
    pagamento_pix.pagar(120.0)
    
    pagamento_cartao = factoryOnline.criarCartao()
    pagamento_cartao.pagar(300.0)

    # fábrica offline - Factory Method puro
    factoryOffline = FactoryPagamentoOffline()
    pagamento_boleto = factoryOffline.criarBoleto()
    pagamento_boleto.pagar(500.0)
    
    pagamento_cartao_offline = factoryOffline.criarCartao()
    pagamento_cartao_offline.pagar(75.25)