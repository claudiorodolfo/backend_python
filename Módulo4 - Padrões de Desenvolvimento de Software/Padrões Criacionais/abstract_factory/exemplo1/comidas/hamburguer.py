from comidas.comida import Comida

class Hamburguer(Comida):
    def removerIngrediente(self, ingrediente):
        print(f"Ingrediente {ingrediente} removido do hamburguer!")
