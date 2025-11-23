from animal_factory import AnimalFactory
from animal import Animal
from gato import Gato

# Concrete Creator - Factory Method Pattern
class GatoFactory(AnimalFactory):
    
    def criarAnimal(self) -> Animal:
        """Factory Method: cria uma instância de Gato"""
        return Gato()

