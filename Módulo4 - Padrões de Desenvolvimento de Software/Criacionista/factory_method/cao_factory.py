from animal_factory import AnimalFactory
from animal import Animal
from cao import Cao

# Concrete Creator - Factory Method Pattern
class CaoFactory(AnimalFactory):
    
    def criarAnimal(self) -> Animal:
        """Factory Method: cria uma instância de Cao"""
        return Cao()

