from comidas.comida import Comida

class Pizza(Comida):
    def removerIngrediente(self, ingrediente):
        print(f"Ingrediente {ingrediente} removido da pizza!")
