from observador_pessoa import ObservadorPessoa
from sujeito_passaro import SujeitoPassaro

if __name__ == "__main__":
    pessoa1 = ObservadorPessoa("Eduardo")
    pessoa2 = ObservadorPessoa("Bruno")
    pessoa3 = ObservadorPessoa("Fabricio")
    pessoa4 = ObservadorPessoa("João")
    pessoa5 = ObservadorPessoa("Maria")
    pessoa6 = ObservadorPessoa("Pedro")

    passaro = SujeitoPassaro("Passaro")
    passaro.adicionarObservador(pessoa1)
    passaro.adicionarObservador(pessoa2)
    passaro.adicionarObservador(pessoa5)
    passaro.notificarObservadores("O passaro voou")
    passaro.notificarObservadores("O passaro pousou")