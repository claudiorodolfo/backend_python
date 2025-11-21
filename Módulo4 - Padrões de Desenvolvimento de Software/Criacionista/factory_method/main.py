from animal_factory import AnimalFactory

# Uso
if __name__ == "__main__":
    animal1 = AnimalFactory.criarAnimal("cao")
    print(animal1.fazSom())  # Saída: Au au!

    animal2 = AnimalFactory.criarAnimal("gato")
    print(animal2.fazSom())  # Saída: Miau!

