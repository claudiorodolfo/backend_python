from observador import Observador

class ObservadorPessoa(Observador):

    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, mensagem: str) -> None:
        print(f"{self.nome} recebeu a mensagem: {mensagem}")
