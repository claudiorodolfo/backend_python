from cao_factory import CaoFactory
from gato_factory import GatoFactory

# Uso do Factory Method Pattern
if __name__ == "__main__":
    # Cada factory concreta cria seu próprio tipo de animal
    cao_factory = CaoFactory()
    animal1 = cao_factory.criarAnimal()
    print(animal1.fazSom())  # Saída: Au au!

    gato_factory = GatoFactory()
    animal2 = gato_factory.criarAnimal()
    print(animal2.fazSom())  # Saída: Miau!

