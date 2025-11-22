from fabricas.abstract_factory import DeliveryFactory
from comidas.comida import Comida
from comidas.hamburguer import Hamburguer
from bebidas.bebida import Bebida
from bebidas.milkshake import Milkshake

# Fábricas concretas
class HamburgueriaFactory(DeliveryFactory):
    def criarComida(self) -> Comida:
        return Hamburguer()
    
    def criarBebida(self) -> Bebida:
        return Milkshake()

