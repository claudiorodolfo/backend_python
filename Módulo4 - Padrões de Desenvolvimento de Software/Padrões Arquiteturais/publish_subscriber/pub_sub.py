class PubSub:
    def __init__(self):
        self.inscritosPorTopico = {}
        self.filaMensagens = []

    def adicionarInscrito(self, topico, inscrito):
        if topico not in self.inscritosPorTopico:
            self.inscritosPorTopico[topico] = []
        self.inscritosPorTopico[topico].append(inscrito)

    def removerInscrito(self, topico, inscrito):
        if topico in self.inscritosPorTopico:
            self.inscritosPorTopico[topico].remove(inscrito)

    def receberMensagemPorTopico(self, mensagem):
        self.filaMensagens.append(mensagem)

    def publicarPorTopico(self, topico, mensagem):
        for inscrito in self.inscritosPorTopico[topico]:
            inscrito.atualizar(topico, mensagem)

    def broadcast(self):
        for mensagem in self.filaMensagens:
            # Envia a mensagem para todos os inscritos de todos os tópicos
            for topico in self.inscritosPorTopico:
                for inscrito in self.inscritosPorTopico[topico]:
                    inscrito.atualizar(mensagem["topico"], mensagem["mensagem"])
        self.filaMensagens = []
