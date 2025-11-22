from animal import Animal
from cao import Cao
from gato import Gato

# Factory Method: classe responsável por criar animais
class AnimalFactory:
    @staticmethod
    def criarAnimal(type: str) -> Animal:
        if type == "cao":
            return Cao()
        elif type == "gato":
            return Gato()
        else:
            raise ValueError(f"Tipo de animal não conhecido: {animalType}")