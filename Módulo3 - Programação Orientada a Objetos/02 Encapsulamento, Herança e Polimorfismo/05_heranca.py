"""
Herança

Herança permite criar uma nova classe baseada em uma classe existente,
reutilizando código e especializando comportamento.
"""

# ==========================================
# CONCEITO DE HERANÇA
# ==========================================

print("=" * 60)
print("CONCEITO DE HERANÇA")
print("=" * 60)

print("""
HERANÇA permite:
  • Criar uma nova classe (SUBCLASSE/FILHA) baseada em outra (SUPERCLASSE/PAI)
  • Reutilizar código da classe pai
  • Especializar comportamento na classe filha
  • Representar relação "É-UM" (ex: Cachorro É-UM Animal)

Vantagens:
  ✓ Evita duplicação de código
  ✓ Facilita manutenção
  ✓ Permite especialização
  ✓ Modela relacionamentos do mundo real
""")


# ==========================================
# EXEMPLO 1: HERANÇA BÁSICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Herança Básica")
print("=" * 60)

class Animal:
    """
    Classe pai (superclasse).
    
    Define características e comportamentos comuns a todos os animais.
    """
    
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        """Comportamento genérico."""
        print("Algum som")
    
    def mover(self):
        """Comportamento genérico."""
        print(f"{self.nome} está se movendo")
    
    def exibir_info(self):
        """Exibe informações do animal."""
        print(f"{self.nome} é um(a) {self.especie}")


class Cachorro(Animal):
    """
    Classe filha (subclasse).
    
    Cachorro HERDA de Animal e especializa comportamentos.
    """
    
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai
        super().__init__(nome, "Cachorro")
        self.raca = raca
    
    def fazer_som(self):
        """Sobrescreve o método da classe pai."""
        print(f"{self.nome} faz: Au au!")


class Gato(Animal):
    """Outra subclasse de Animal."""
    
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor
    
    def fazer_som(self):
        """Sobrescreve o método da classe pai."""
        print(f"{self.nome} faz: Miau!")


# Testando herança
print("\nCriando animais:")
animal_generico = Animal("Animal", "Genérico")
cachorro = Cachorro("Rex", "Golden Retriever")
gato = Gato("Felix", "Branco")

print("\nAnimais fazem som:")
animal_generico.fazer_som()
cachorro.fazer_som()  # Comportamento especializado
gato.fazer_som()      # Comportamento especializado

print("\nMétodos herdados:")
animal_generico.mover()
cachorro.mover()  # Método herdado da classe Animal
gato.mover()      # Método herdado da classe Animal

print("\nInformações:")
cachorro.exibir_info()  # Método herdado
print(f"  Raça: {cachorro.raca}")  # Atributo próprio
gato.exibir_info()
print(f"  Cor: {gato.cor}")  # Atributo próprio


# ==========================================
# EXEMPLO 2: HERANÇA EM MÚLTIPLOS NÍVEIS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Herança em Múltiplos Níveis")
print("=" * 60)

class Veiculo:
    """Classe base para veículos."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        print(f"{self.marca} {self.modelo} ligado")
    
    def desligar(self):
        print(f"{self.marca} {self.modelo} desligado")


class VeiculoTerrestre(Veiculo):
    """Classe intermediária - veículos terrestres."""
    
    def __init__(self, marca, modelo, num_rodas):
        super().__init__(marca, modelo)
        self.num_rodas = num_rodas
    
    def andar(self):
        print(f"{self.marca} {self.modelo} está andando")


class Carro(VeiculoTerrestre):
    """Carro herda de VeiculoTerrestre (que herda de Veiculo)."""
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 4)
    
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando!")


class Moto(VeiculoTerrestre):
    """Moto também herda de VeiculoTerrestre."""
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 2)
    
    def empinar(self):
        print(f"{self.marca} {self.modelo} empinando!")


# Testando hierarquia
print("\nCriando veículos:")
carro = Carro("Toyota", "Corolla")
moto = Moto("Honda", "CB600")

print("\nMétodos herdados:")
carro.ligar()      # Herdado de Veiculo
carro.andar()      # Herdado de VeiculoTerrestre
carro.acelerar()   # Próprio de Carro

print()
moto.ligar()       # Herdado de Veiculo
moto.andar()       # Herdado de VeiculoTerrestre
moto.empinar()     # Próprio de Moto


# ==========================================
# EXEMPLO 3: HERANÇA COM ATRIBUTOS EXTRAS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Herança com Atributos Extras")
print("=" * 60)

class Funcionario:
    """Classe base para funcionários."""
    
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando")
    
    def calcular_salario(self):
        return self._salario
    
    def exibir_info(self):
        print(f"{self.nome} - Salário: R${self.calcular_salario():.2f}")


class Gerente(Funcionario):
    """Gerente herda de Funcionario e adiciona bônus."""
    
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    
    def calcular_salario(self):
        """Sobrescreve para incluir bônus."""
        return self._salario + self.bonus


class Desenvolvedor(Funcionario):
    """Desenvolvedor herda de Funcionario."""
    
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
    
    def programar(self):
        """Método específico de Desenvolvedor."""
        print(f"{self.nome} está programando em {self.linguagem}")


# Testando
print("\nCriando funcionários:")
func1 = Funcionario("Ana", 3000)
gerente = Gerente("Bruno", 5000, 1000)
dev = Desenvolvedor("Carla", 4000, "Python")

print("\nFuncionários trabalhando:")
func1.trabalhar()
gerente.trabalhar()
dev.trabalhar()

print("\nSalários:")
func1.exibir_info()
gerente.exibir_info()  # Inclui bônus
dev.exibir_info()

print("\nMétodos específicos:")
dev.programar()


# ==========================================
# EXEMPLO 4: VERIFICANDO HERANÇA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Verificando Relações de Herança")
print("=" * 60)

print("\nVerificando tipos:")
print(f"cachorro é instância de Cachorro? {isinstance(cachorro, Cachorro)}")
print(f"cachorro é instância de Animal? {isinstance(cachorro, Animal)}")
print(f"cachorro é instância de Gato? {isinstance(cachorro, Gato)}")

print("\nVerificando subclasses:")
print(f"Cachorro é subclasse de Animal? {issubclass(Cachorro, Animal)}")
print(f"Cachorro é subclasse de Gato? {issubclass(Cachorro, Gato)}")
print(f"Carro é subclasse de Veiculo? {issubclass(Carro, Veiculo)}")
print(f"Carro é subclasse de VeiculoTerrestre? {issubclass(Carro, VeiculoTerrestre)}")

print("\nVerificando métodos e atributos:")
print(f"Métodos de Cachorro: {[m for m in dir(cachorro) if not m.startswith('__')]}")
print(f"Atributos de cachorro: {cachorro.__dict__}")


# ==========================================
# HERANÇA MÚLTIPLA
# ==========================================

print("\n" + "=" * 60)
print("HERANÇA MÚLTIPLA (Breve Introdução)")
print("=" * 60)

class Volante:
    """Classe para coisas que têm volante."""
    
    def girar_volante(self):
        print("Girando o volante")


class Motor:
    """Classe para coisas que têm motor."""
    
    def ligar_motor(self):
        print("Ligando o motor")


class CarroCompleto(Volante, Motor):
    """Carro herda de Volante E Motor (herança múltipla)."""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def dirigir(self):
        print(f"{self.modelo}:")
        self.ligar_motor()
        self.girar_volante()
        print("Carro em movimento!")


# Testando herança múltipla
print("\nCriando carro com herança múltipla:")
carro_completo = CarroCompleto("Fusca")
carro_completo.dirigir()


# ==========================================
# QUANDO USAR HERANÇA
# ==========================================

print("\n" + "=" * 60)
print("QUANDO USAR HERANÇA")
print("=" * 60)

print("""
USE HERANÇA QUANDO:
  ✓ Há relação "É-UM" (Cachorro É-UM Animal)
  ✓ Classes compartilham comportamentos comuns
  ✓ Precisa especializar comportamento
  ✓ Quer evitar duplicação de código

NÃO USE HERANÇA QUANDO:
  ✗ Relação é "TEM-UM" (use composição)
  ✗ Não há relação de especialização real
  ✗ Apenas para reutilizar código sem relação lógica

LEMBRE-SE:
  • Herança cria acoplamento forte
  • Prefira composição quando possível
  • Herança deve representar relacionamento lógico
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE HERANÇA")
print("=" * 60)

print("""
✓ Herança permite reutilizar código de uma classe pai
✓ Subclasse herda atributos e métodos da superclasse
✓ Permite especializar comportamento
✓ Representa relação "É-UM"
✓ Sintaxe: class Filha(Pai):
✓ Use super() para chamar métodos da classe pai
✓ isinstance() e issubclass() verificam relações
✓ Evite herança múltipla complexa
""")

