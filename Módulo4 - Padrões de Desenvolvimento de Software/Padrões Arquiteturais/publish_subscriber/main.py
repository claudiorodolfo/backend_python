from inscrito import Inscrito
from publicador import Publicador
from pub_sub import PubSub

if __name__ == "__main__":
    eduardo = Inscrito("Eduardo")
    maria = Inscrito("Maria")
    jose = Inscrito("José")

    bus = PubSub()

    blog1 = Publicador("Blog do Sena", bus)
    blog2 = Publicador("Blog Ricardo Nolasco", bus)

    bus.adicionarInscrito("Blog do Sena", eduardo)
    bus.adicionarInscrito("Blog do Sena", maria)
    bus.adicionarInscrito("Blog Ricardo Nolasco", maria)
    bus.adicionarInscrito("Blog Ricardo Nolasco", jose)

    blog1.publicar("O blog do Sena foi publicado")
    blog2.publicar("O blog Ricardo Nolasco foi publicado")

    bus.broadcast()