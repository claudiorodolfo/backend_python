"""
Classe modelo para a tabela pessoa
"""
from model.categoria import Categoria

class Pessoa:
    def __init__(self, id: int, nome: str, categoria: Categoria, email: str,
                 idade: int | None = None, altura: float | None = None,
                 peso: float | None = None, data_nascimento: str | None = None,
                 ativo: bool = True, observacoes: str | None = None,
                 telefone: str | None = None, momento_cadastro: str | None = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.data_nascimento = data_nascimento
        self.ativo = ativo
        self.observacoes = observacoes
        self.telefone = telefone
        self.momento_cadastro = momento_cadastro
        self.categoria = categoria
    
    def __str__(self):
        return (f"Pessoa(id={self.id}, nome='{self.nome}', "
                f"email='{self.email}', idade={self.idade}, "
                f"categoria_id={self.categoria.id})")

