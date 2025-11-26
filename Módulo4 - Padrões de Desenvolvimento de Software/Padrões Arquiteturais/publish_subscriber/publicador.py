class Publicador:
    def __init__(self, topico, pub_sub):
        self.topico = topico
        self.pub_sub = pub_sub
        self.mensagens = []

    def publicar(self, mensagem):
        msg = {
            "topico": self.topico,
            "mensagem": mensagem
        }
        self.pub_sub.receberMensagemPorTopico(msg)
