from animal import Animal

# Produto concreto
class Gato(Animal):
    def fazSom(self) -> str:
        return "Miau!"