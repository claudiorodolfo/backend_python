from observador_pessoa import ObservadorPessoa
from sujeito_passaro import SujeitoPassaro

if __name__ == "__main__":
    pessoa1 = ObservadorPessoa("Eduardo")
    pessoa2 = ObservadorPessoa("Bruno")
    pessoa3 = ObservadorPessoa("Fabricio")

    passaro = SujeitoPassaro("Passaro")
    passaro.adicionarObservador(pessoa1)
    passaro.adicionarObservador(pessoa2)
    passaro.adicionarObservador(pessoa3)
    passaro.notificarObservadores("O passaro voou")
    passaro.notificarObservadores("O passaro pousou")