import copy

class Prototype:
    def clone(self):
        # usa cópia profunda
        return copy.deepcopy(self)

class Pessoa(Prototype):
    def __init__(self, nome, idade, endereco):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco

    def __str__(self):
        return f"Pessoa(nome={self._nome}, idade={self._idade}, endereco={self._endereco})"

if __name__ == "__main__":
    original = Pessoa("Alice", 30, {"cidade": "Salvador", "cep": "40000"})
    pessoaClone = original.clone()
    pessoaClone._nome = "Bob"
    pessoaClone._endereco["cidade"] = "Vitória"
    print(original)       # Pessoa(nome=Alice, idade=30, endereco={'cidade': 'Salvador', …})
    print(pessoaClone)   # Pessoa(nome=Bob, idade=30, endereco={'cidade': 'Vitória', …})
