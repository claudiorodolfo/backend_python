# https://www.youtube.com/watch?v=9gJYU28PHz4
from fabricas.pizzaria_factory import PizzariaFactory
from fabricas.hamburgueria_factory import HamburgueriaFactory

if __name__ == "__main__":
    
    tipo = input("Digite o tipo de fábrica: [pizzaria, hamburgueria] ")

    if tipo == "pizzaria":
        factory = PizzariaFactory()
    elif tipo == "hamburgueria":
        factory = HamburgueriaFactory()
    else:
        raise ValueError("Tipo de fábrica inválido")
    
    comida = factory.criarComida()
    bebida = factory.criarBebida()
    
    ingrediente = input("Digite o ingrediente: ")
    comida.removerIngrediente(ingrediente)
    bebida.escolherSemAcucar()

