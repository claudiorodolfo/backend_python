from pagamento import Pagamento, PagamentoOnlineCartao, PagamentoOfflineCartao, PagamentoOfflineBoleto, PagamentoOnlinePix

class PagamentoFactory:

    def criarPagamento(self, tipo: str, forma: str) -> Pagamento:
        """Cria instância de Pagamento com base no tipo e forma."""
        tipo = tipo.lower()
        forma = forma.lower()

        if tipo == "online":
            # pagamento online: suporta cartão e PIX, por exemplo
            if forma == "pix":
                return PagamentoOnlinePix()
            elif forma == "cartao":
                return PagamentoOnlineCartao()
            else:
                raise ValueError(f"'Forma de pagamento online, não suportada: {forma}'")
        elif tipo == "offline":
            # pagamento offline: cartão e boleto, por exemplo
            if forma == "boleto":
                return PagamentoOfflineBoleto()
            elif forma == "cartao":
                return PagamentoOfflineCartao()
            else:
                raise ValueError(f"'Forma de pagamento offline, não suportada: {forma}'")
        else:
            raise ValueError(f"Tipo de pagamento desconhecido: '{tipo}'")
