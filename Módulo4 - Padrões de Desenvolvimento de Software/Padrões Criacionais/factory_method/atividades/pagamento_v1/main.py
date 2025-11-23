from fabricas_concretas import FactoryPagamentoOnline, FactoryPagamentoOffline
from fabrica_abstrata import PagamentoFactory

def cliente_pagamento(factory: PagamentoFactory, tipo: str, valor: float):
    factory.realizarPagamento(tipo, valor)

if __name__ == "__main__":
    # fábrica online
    factoryOnline = FactoryPagamentoOnline()
    cliente_pagamento(factoryOnline, "pix", 120.0)
    cliente_pagamento(factoryOnline, "cartao", 300.0)

    # fábrica offline
    factoryOffline = FactoryPagamentoOffline()
    cliente_pagamento(factoryOffline, "boleto", 500.0)
    cliente_pagamento(factoryOffline, "cartao", 75.25)