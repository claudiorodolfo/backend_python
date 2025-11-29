from cafe_simples import CafeSimples
from chocolate_decorator import Chocolate
from leite_decorator import Leite
from chantilly_decorator import Chantilly
from acucar_decorator import Acucar

if __name__ == "__main__":

    # Café simples
    bebida1 = CafeSimples()
    print("1)", bebida1.getDescription(), " - R$", bebida1.getCost())

    # Café com leite e chocolate
    bebida2 = Chocolate(Leite(CafeSimples()))
    print("2)", bebida2.getDescription(), " - R$", bebida2.getCost())

    # Café com chantilly
    bebida3 = Chantilly(CafeSimples())
    print("3)", bebida3.getDescription(), " - R$", bebida3.getCost())

    # Café com leite, açúcar e chantilly
    bebida4 = Chantilly(Acucar(Leite(CafeSimples())))
    print("4)", bebida4.getDescription(), " - R$", bebida4.getCost())