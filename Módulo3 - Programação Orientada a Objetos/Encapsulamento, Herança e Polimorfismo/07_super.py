"""
Usando super()

A função super() permite acessar métodos e atributos da classe pai,
mantendo a hierarquia e permitindo extensão de funcionalidade.
"""

# ==========================================
# O QUE É super()?
# ==========================================

print("=" * 60)
print("O QUE É super()?")
print("=" * 60)

print("""
super() permite:
  • Acessar métodos da classe pai
  • Chamar construtores da classe pai
  • Estender funcionalidade sem perder a implementação original
  • Manter a hierarquia de classes

Por que usar?
  ✓ Evita duplicar código
  ✓ Mantém consistência
  ✓ Facilita manutenção
  ✓ Permite extensão controlada
""")


# ==========================================
# EXEMPLO 1: super() NO CONSTRUTOR
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: super() no Construtor")
print("=" * 60)

class Animal:
    """Classe pai."""
    
    def __init__(self, nome, especie):
        print(f"Construtor de Animal chamado")
        self.nome = nome
        self.especie = especie


class Cachorro(Animal):
    """Subclasse usando super() no construtor."""
    
    def __init__(self, nome, especie, raca):
        # Chama o construtor da classe pai
        super().__init__(nome, especie)
        print(f"Construtor de Cachorro chamado")
        self.raca = raca  # Atributo adicional


class Gato(Animal):
    """Outra subclasse usando super()."""
    
    def __init__(self, nome, especie, cor):
        super().__init__(nome, especie)
        print(f"Construtor de Gato chamado")
        self.cor = cor


# Testando
print("\nCriando animais:")
cachorro = Cachorro("Rex", "Canino", "Golden Retriever")
print(f"\nCachorro criado:")
print(f"  Nome: {cachorro.nome}")      # Herdado de Animal
print(f"  Espécie: {cachorro.especie}")  # Herdado de Animal
print(f"  Raça: {cachorro.raca}")      # Próprio de Cachorro

gato = Gato("Felix", "Felino", "Branco")
print(f"\nGato criado:")
print(f"  Nome: {gato.nome}")
print(f"  Espécie: {gato.especie}")
print(f"  Cor: {gato.cor}")


# ==========================================
# EXEMPLO 2: super() COM MÉTODOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: super() com Métodos")
print("=" * 60)

class Funcionario:
    """Classe base."""
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def trabalhar(self):
        """Método que será estendido."""
        print(f"{self.nome} está trabalhando")
    
    def exibir_info(self):
        """Método que será estendido."""
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")


class Gerente(Funcionario):
    """Subclasse que estende métodos usando super()."""
    
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def trabalhar(self):
        """Estende o método trabalhar() usando super()."""
        super().trabalhar()  # Chama implementação do pai
        print(f"{self.nome} está gerenciando o departamento {self.departamento}")
    
    def exibir_info(self):
        """Estende o método exibir_info() usando super()."""
        super().exibir_info()  # Chama implementação do pai
        print(f"Departamento: {self.departamento}")
        print(f"Cargo: Gerente")


# Testando
print("\nCriando funcionário:")
funcionario = Funcionario("Ana", 3000)
funcionario.trabalhar()
print()
funcionario.exibir_info()

print("\nCriando gerente:")
gerente = Gerente("Bruno", 5000, "TI")
gerente.trabalhar()
print()
gerente.exibir_info()


# ==========================================
# EXEMPLO 3: EXTENSÃO DE FUNCIONALIDADE
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Extensão de Funcionalidade")
print("=" * 60)

class Veiculo:
    """Classe base para veículos."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
    
    def ligar(self):
        """Liga o veículo."""
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} ligado")
        else:
            print(f"{self.marca} {self.modelo} já está ligado")
    
    def desligar(self):
        """Desliga o veículo."""
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} desligado")
        else:
            print(f"{self.marca} {self.modelo} já está desligado")


class Carro(Veiculo):
    """Carro estende funcionalidade de Veiculo."""
    
    def __init__(self, marca, modelo, combustivel):
        super().__init__(marca, modelo)
        self.combustivel = combustivel
        self.nivel_combustivel = 100
    
    def ligar(self):
        """Estende ligar() com verificação de combustível."""
        if self.nivel_combustivel <= 0:
            print(f"{self.marca} {self.modelo} sem combustível!")
            return
        
        super().ligar()  # Chama método do pai
        print(f"Motor {self.combustivel} em funcionamento")
    
    def abastecer(self, litros):
        """Método específico de Carro."""
        if self.ligado:
            print("Desligue o carro antes de abastecer!")
            return
        
        self.nivel_combustivel = min(100, self.nivel_combustivel + litros)
        print(f"Abastecido. Nível: {self.nivel_combustivel}%")


# Testando
print("\nCriando carro:")
carro = Carro("Toyota", "Corolla", "Gasolina")

print("\nTentando ligar:")
carro.ligar()

print("\nAbastecendo:")
carro.abastecer(20)

print("\nLigando novamente:")
carro.ligar()


# ==========================================
# EXEMPLO 4: super() EM MÚLTIPLOS NÍVEIS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: super() em Múltiplos Níveis")
print("=" * 60)

class Pessoa:
    """Classe base."""
    
    def __init__(self, nome):
        print("Construtor de Pessoa")
        self.nome = nome
    
    def apresentar(self):
        print(f"Sou {self.nome}")


class Funcionario(Pessoa):
    """Classe intermediária."""
    
    def __init__(self, nome, cargo):
        print("Construtor de Funcionario")
        super().__init__(nome)
        self.cargo = cargo
    
    def apresentar(self):
        super().apresentar()
        print(f"Trabalho como {self.cargo}")


class Gerente(Funcionario):
    """Classe final na hierarquia."""
    
    def __init__(self, nome, cargo, departamento):
        print("Construtor de Gerente")
        super().__init__(nome, cargo)
        self.departamento = departamento
    
    def apresentar(self):
        super().apresentar()
        print(f"Gerencio o departamento {self.departamento}")


# Testando hierarquia
print("\nCriando gerente (veja a ordem de chamada):")
gerente = Gerente("Carla", "Gerente de TI", "Tecnologia")

print("\nApresentando (veja a ordem de execução):")
gerente.apresentar()


# ==========================================
# EXEMPLO 5: super() vs CHAMADA DIRETA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 5: super() vs Chamada Direta")
print("=" * 60)

class ClasseA:
    def metodo(self):
        print("Método de A")


class ClasseB(ClasseA):
    def metodo_com_super(self):
        """Usa super() - mais flexível."""
        super().metodo()
        print("Extensão em B")


class ClasseC(ClasseA):
    def metodo_com_chamada_direta(self):
        """Chama diretamente - menos flexível."""
        ClasseA.metodo(self)
        print("Extensão em C")


# Ambos funcionam, mas super() é preferível
print("\nUsando super():")
obj_b = ClasseB()
obj_b.metodo_com_super()

print("\nUsando chamada direta:")
obj_c = ClasseC()
obj_c.metodo_com_chamada_direta()

print("""
VANTAGENS DO super():
  ✓ Funciona mesmo se a hierarquia mudar
  ✓ Mais flexível e manutenível
  ✓ Respeita a ordem de resolução de métodos (MRO)
  ✓ Recomendado pela comunidade Python
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE super()")
print("=" * 60)

print("""
✓ super() acessa métodos e atributos da classe pai
✓ Use no construtor: super().__init__(parametros)
✓ Use em métodos: super().metodo_pai()
✓ Permite estender funcionalidade sem perder implementação original
✓ Funciona em hierarquias de múltiplos níveis
✓ Mais flexível que chamada direta ao nome da classe
✓ Recomendado para código Python moderno
✓ Respeita a ordem de resolução de métodos (MRO)
""")

