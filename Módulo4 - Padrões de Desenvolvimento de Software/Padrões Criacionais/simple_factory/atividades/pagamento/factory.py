from pagamento import Pagamento, PagamentoCartao, PagamentoBoleto, PagamentoPix

class PagamentoFactory:

    def criarPagamento(self, canal: str, tipo: str) -> Pagamento:
        """Cria instância de Pagamento com base no canal e tipo."""
        canal = canal.lower()
        tipo = tipo.lower()

        if canal == "online":
            print(f"Pagamento online.",end=" ")
            # pagamento online: suporta cartão e PIX, por exemplo
            if tipo == "pix":
                return PagamentoPix()
            elif tipo == "cartao":
                return PagamentoCartao()
            else:
                raise ValueError(f"Pagamento online não suporta tipo: '{tipo}'")
        elif canal == "offline":
            print(f"Pagamento offline.",end=" ")
            # pagamento offline: cartão e boleto, por exemplo
            if tipo == "boleto":
                return PagamentoBoleto()
            elif tipo == "cartao":
                return PagamentoCartao()
            else:
                raise ValueError(f"Pagamento offline não suporta tipo: '{tipo}'")
        else:
            raise ValueError(f"Canal de pagamento desconhecido: '{canal}'")
