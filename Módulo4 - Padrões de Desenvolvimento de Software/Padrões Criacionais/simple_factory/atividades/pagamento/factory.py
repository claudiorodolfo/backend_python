from pagamento import Pagamento, PagamentoOnlineCartao, PagamentoOfflineCartao, PagamentoOfflineBoleto, PagamentoOnlinePix

class PagamentoFactory:

    def criarPagamento(self, tipo: str, forma: str) -> Pagamento:
        """Cria instância de Pagamento com base no tipo e forma."""
        tipo = tipo.lower()
        forma = forma.lower()

        match tipo:
            case "online":
                # pagamento online: suporta cartão e PIX, por exemplo
                match forma:
                    case "pix":
                        return PagamentoOnlinePix()
                    case "cartao":
                        return PagamentoOnlineCartao()
                    case _:
                        raise ValueError(f"'Forma de pagamento online, não suportada: {forma}'")
            case "offline":
                # pagamento offline: cartão e boleto, por exemplo
                match forma:
                    case "boleto":
                        return PagamentoOfflineBoleto()
                    case "cartao":
                        return PagamentoOfflineCartao()
                    case _:
                        raise ValueError(f"'Forma de pagamento offline, não suportada: {forma}'")