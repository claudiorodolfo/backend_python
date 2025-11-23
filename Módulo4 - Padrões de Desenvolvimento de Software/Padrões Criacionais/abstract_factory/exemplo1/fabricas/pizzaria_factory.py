from fabricas.abstract_factory import DeliveryFactory
from comidas.comida import Comida
from comidas.pizza import Pizza
from bebidas.bebida import Bebida
from bebidas.refrigerante import Refrigerante

# Fábricas concretas
class PizzariaFactory(DeliveryFactory):
    def criarComida(self) -> Comida:
        return Pizza()
    
    def criarBebida(self) -> Bebida:
        return Refrigerante()
