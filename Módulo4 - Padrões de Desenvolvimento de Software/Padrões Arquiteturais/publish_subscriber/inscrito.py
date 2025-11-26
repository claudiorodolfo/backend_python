class Inscrito:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, topico, mensagem):
        print(f"{self.nome} recebeu a mensagem do tópico '{topico}': {mensagem}")