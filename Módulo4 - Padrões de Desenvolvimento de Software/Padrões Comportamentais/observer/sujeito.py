from abc import ABC, abstractmethod
from observador import Observador

class Sujeito(ABC):

    @abstractmethod
    def adicionarObservador(self, observador: Observador):
        pass

    @abstractmethod
    def removerObservador(self, observador: Observador):
        pass

    @abstractmethod
    def notificarObservadores(self, mensagem: str):
        pass
