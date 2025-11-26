from sujeito import Sujeito
from observador import Observador

class SujeitoPassaro(Sujeito):
    def __init__(self, nome: str):
        self.nome = nome
        self.observadores = []
        
    def adicionarObservador(self, observador: Observador):
        self.observadores.append(observador)

    def removerObservador(self, observador: Observador):
        self.observadores.remove(observador)

    def notificarObservadores(self, mensagem: str):
        for observador in self.observadores:
            observador.atualizar(mensagem)

