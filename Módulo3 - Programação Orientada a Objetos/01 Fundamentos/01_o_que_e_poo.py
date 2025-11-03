"""
O que é Programação Orientada a Objetos

Este exemplo demonstra os conceitos básicos de POO comparando
com uma abordagem sem classes.
"""

# ==========================================
# ABORDAGEM SEM POO (Procedural)
# ==========================================

def criarPessoa(nome, idade):
    """Cria um dicionário representando uma pessoa."""
    return {"nome": nome, "idade": idade}


def fazerAniversario(pessoa):
    """Aumenta a idade da pessoa em 1."""
    pessoa["idade"] += 1
    return pessoa


def apresentar(pessoa):
    """Apresenta a pessoa."""
    print(f"Olá, eu sou {pessoa['nome']} e tenho {pessoa['idade']} anos.")


# Uso da abordagem procedural
print("=" * 50)
print("ABORDAGEM PROCEDURAL")
print("=" * 50)

pessoa1 = criarPessoa("Maria", 25)
apresentar(pessoa1)
fazerAniversario(pessoa1)
apresentar(pessoa1)


# ==========================================
# ABORDAGEM COM POO (Orientada a Objetos)
# ==========================================

class Pessoa:
    """
    Representa uma pessoa no sistema.
    
    Uma classe agrupa dados (atributos) e comportamentos (métodos)
    relacionados em uma única unidade coesa.
    """
    
    def __init__(self, nome, idade):
        """
        Construtor da classe.
        
        Este método é chamado automaticamente quando criamos
        um objeto (instância) desta classe.
        """
        self.nome = nome    # Atributo: característica do objeto
        self.idade = idade  # Atributo: característica do objeto
    
    def fazerAniversario(self):
        """
        Método: comportamento do objeto.
        
        Métodos são funções que pertencem à classe e operam
        sobre os dados do objeto (atributos).
        """
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos.")
    
    def apresentar(self):
        """Método para apresentar a pessoa."""
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")


# Uso da abordagem orientada a objetos
print("\n" + "=" * 50)
print("ABORDAGEM ORIENTADA A OBJETOS")
print("=" * 50)

# Criando um objeto (instância) da classe Pessoa
pessoa2 = Pessoa("João", 30)
pessoa2.apresentar()
pessoa2.fazerAniversario()


# ==========================================
# VANTAGENS DA POO
# ==========================================

print("\n" + "=" * 50)
print("VANTAGENS DA POO")
print("=" * 50)

print("""
1. ORGANIZAÇÃO: Dados e comportamentos relacionados ficam juntos
   - Não precisa passar dados como parâmetros
   - Tudo está encapsulado no objeto

2. REUTILIZAÇÃO: Uma classe pode ser usada para criar múltiplos objetos
   - Cada objeto mantém seus próprios dados
   - Mas compartilha os mesmos comportamentos

3. MANUTENIBILIDADE: Mais fácil de entender e modificar
   - Código relacionado está no mesmo lugar
   - Mudanças são localizadas

4. MODELAGEM: Representa melhor o mundo real
   - Objetos do mundo real têm características e comportamentos
   - POO modela isso naturalmente
""")


# ==========================================
# EXEMPLO: MÚLTIPLAS INSTÂNCIAS
# ==========================================

print("\n" + "=" * 50)
print("MÚLTIPLAS INSTÂNCIAS")
print("=" * 50)

# Podemos criar quantos objetos quisermos da mesma classe
aluno1 = Pessoa("Ana", 20)
aluno2 = Pessoa("Bruno", 22)
aluno3 = Pessoa("Carla", 19)

print("\nAlunos criados:")
aluno1.apresentar()
aluno2.apresentar()
aluno3.apresentar()

print("\nCada objeto é independente:")
aluno1.fazerAniversario()  # Só afeta aluno1
aluno2.apresentar()         # aluno2 não mudou

