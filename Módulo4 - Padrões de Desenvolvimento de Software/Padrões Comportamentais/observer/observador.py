from abc import ABC, abstractmethod

class Observador(ABC):

    @abstractmethod
    def atualizar(self, mensagem: str) -> None:
        pass
