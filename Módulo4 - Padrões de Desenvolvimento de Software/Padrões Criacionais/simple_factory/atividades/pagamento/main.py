from factory import PagamentoFactory

def realizar_pagamento(tipo: str, forma: str, valor: float):
    factory = PagamentoFactory()
    pagamento = factory.criarPagamento(tipo, forma)
    pagamento.pagar(valor)


if __name__ == "__main__":
    realizar_pagamento("online", "pix", 120.0)         # PIX online
    realizar_pagamento("online", "cartao", 300.0)      # Cartão online
    realizar_pagamento("offline", "boleto", 500.0)     # Boleto offline
    realizar_pagamento("offline", "cartao", 75.25)     # Cartão offline