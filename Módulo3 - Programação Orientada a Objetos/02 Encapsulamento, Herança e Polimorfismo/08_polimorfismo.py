"""
Polimorfismo

Polimorfismo é a capacidade de objetos de diferentes classes
responderem à mesma interface (mesmo método) de formas diferentes.
"""

# ==========================================
# O QUE É POLIMORFISMO?
# ==========================================

print("=" * 60)
print("O QUE É POLIMORFISMO?")
print("=" * 60)

print("""
POLIMORFISMO = "Muitas formas"

Um mesmo método pode ter comportamentos diferentes
dependendo do objeto que o chama.

Conceito:
  • Diferentes classes implementam o mesmo método
  • Cada classe fornece sua própria implementação
  • Código genérico funciona com qualquer implementação

Vantagens:
  ✓ Flexibilidade
  ✓ Código mais genérico e reutilizável
  ✓ Facilita extensão (adicionar novos tipos)
  ✓ Melhor manutenibilidade
""")


# ==========================================
# EXEMPLO 1: POLIMORFISMO BÁSICO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Polimorfismo Básico")
print("=" * 60)

class Animal:
    """Classe base que define a interface."""
    
    def fazerSom(self):
        """Método que será polimórfico."""
        pass


class Cachorro(Animal):
    def fazerSom(self):
        """Implementação específica para cachorro."""
        return "Au au!"


class Gato(Animal):
    def fazerSom(self):
        """Implementação específica para gato."""
        return "Miau!"


class Pato(Animal):
    def fazerSom(self):
        """Implementação específica para pato."""
        return "Quack quack!"


# POLIMORFISMO EM AÇÃO
print("\nCriando lista de animais:")
animais = [
    Cachorro(),
    Gato(),
    Pato(),
    Cachorro()
]

print("\nCada animal faz um som diferente (polimorfismo):")
for animal in animais:
    print(f"  {animal.__class__.__name__}: {animal.fazerSom()}")


# ==========================================
# EXEMPLO 2: POLIMORFISMO COM FORMAS GEOMÉTRICAS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Polimorfismo com Formas")
print("=" * 60)

class Forma:
    """Classe base para formas geométricas."""
    
    def calcularArea(self):
        """Método polimórfico."""
        pass
    
    def calcularPerimetro(self):
        """Método polimórfico."""
        pass


class Retangulo(Forma):
    """Implementação para retângulo."""
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcularArea(self):
        """Cálculo específico para retângulo."""
        return self.largura * self.altura
    
    def calcularPerimetro(self):
        """Cálculo específico para retângulo."""
        return 2 * (self.largura + self.altura)


class Circulo(Forma):
    """Implementação para círculo."""
    
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        """Cálculo específico para círculo."""
        return 3.14159 * self.raio ** 2
    
    def calcularPerimetro(self):
        """Cálculo específico para círculo."""
        return 2 * 3.14159 * self.raio


class Triangulo(Forma):
    """Implementação para triângulo."""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        """Cálculo específico para triângulo."""
        return (self.base * self.altura) / 2
    
    def calcularPerimetro(self):
        """Cálculo aproximado (para simplificar)."""
        # Triângulo precisa de 3 lados, mas vamos usar base + altura
        return self.base + self.altura + (self.base ** 2 + self.altura ** 2) ** 0.5


# POLIMORFISMO: mesmo método, comportamentos diferentes
print("\nCriando formas diferentes:")
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4),
    Retangulo(10, 2)
]

print("\nCalculando área de cada forma (polimorfismo):")
for forma in formas:
    area = forma.calcularArea()
    perimetro = forma.calcularPerimetro()
    tipo = forma.__class__.__name__
    print(f"  {tipo}: Área = {area:.2f}, Perímetro = {perimetro:.2f}")


# ==========================================
# EXEMPLO 3: POLIMORFISMO COM FUNCIONÁRIOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Polimorfismo com Funcionários")
print("=" * 60)

class Funcionario:
    """Classe base."""
    
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salarioBase = salario_base
    
    def calcularSalario(self):
        """Método polimórfico."""
        return self.salarioBase
    
    def trabalhar(self):
        """Método polimórfico."""
        print(f"{self.nome} está trabalhando")


class Vendedor(Funcionario):
    """Vendedor com comissão."""
    
    def __init__(self, nome, salario_base, vendas_mes):
        super().__init__(nome, salario_base)
        self.vendasMes = vendas_mes
    
    def calcularSalario(self):
        """Implementação específica: salário + comissão."""
        comissao = self.vendasMes * 0.1
        return self.salarioBase + comissao
    
    def trabalhar(self):
        """Implementação específica."""
        print(f"{self.nome} está vendendo produtos")


class Gerente(Funcionario):
    """Gerente com bônus."""
    
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcularSalario(self):
        """Implementação específica: salário + bônus."""
        return self.salarioBase + self.bonus
    
    def trabalhar(self):
        """Implementação específica."""
        print(f"{self.nome} está gerenciando a equipe")


class Desenvolvedor(Funcionario):
    """Desenvolvedor sem alteração."""
    
    def trabalhar(self):
        """Implementação específica."""
        print(f"{self.nome} está programando")


# POLIMORFISMO: tratar todos como Funcionario
print("\nCriando equipe:")
equipe = [
    Funcionario("Ana", 3000),
    Vendedor("Bruno", 3000, 5000),
    Gerente("Carla", 5000, 1000),
    Desenvolvedor("Daniel", 4000)
]

print("\nTodos trabalham (polimorfismo):")
for funcionario in equipe:
    funcionario.trabalhar()

print("\nSalários calculados (polimorfismo):")
for funcionario in equipe:
    salario = funcionario.calcularSalario()
    tipo = funcionario.__class__.__name__
    print(f"  {funcionario.nome} ({tipo}): R${salario:.2f}")


# ==========================================
# EXEMPLO 4: POLIMORFISMO EM FUNÇÃO GENÉRICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Função Genérica com Polimorfismo")
print("=" * 60)

def processarFormas(listaFormas):
    """
    Função genérica que funciona com qualquer forma.
    
    Esta função demonstra o poder do polimorfismo:
    funciona com qualquer objeto que tenha calcularArea().
    
    Args:
        lista_formas: Lista de objetos Forma
    """
    totalArea = 0
    print("\nProcessando formas:")
    for forma in listaFormas:
        area = forma.calcularArea()
        totalArea += area
        print(f"  {forma.__class__.__name__}: {area:.2f}")
    
    print(f"\nTotal de área: {totalArea:.2f}")
    return totalArea


# A função funciona com qualquer tipo de forma!
print("\nProcessando formas diferentes:")
formasMisturadas = [
    Retangulo(4, 5),
    Circulo(3),
    Triangulo(6, 4),
    Retangulo(2, 8),
    Circulo(5)
]

processarFormas(formasMisturadas)


# ==========================================
# EXEMPLO 5: POLIMORFISMO COM DUCK TYPING
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 5: Duck Typing (Polimorfismo Sem Herança)")
print("=" * 60)

print("""
Em Python, polimorfismo não requer herança explícita.
Se um objeto tem o método necessário, funciona!

"Isso que anda como pato e faz quack é pato"
""")

class Arquiteto:
    """Classe que não herda de Funcionario, mas tem calcular_salario()."""
    
    def __init__(self, nome, salario_base, projetos):
        self.nome = nome
        self.salarioBase = salario_base
        self.projetos = projetos
    
    def calcularSalario(self):
        """Tem o método, então funciona com polimorfismo!"""
        return self.salarioBase + (self.projetos * 500)


# Duck Typing: se tem calcular_salario(), funciona!
print("\nAdicionando Arquiteto à equipe:")
equipe_extendida = equipe + [Arquiteto("Eduarda", 4500, 3)]

print("\nCalculando salários (funciona mesmo sem herança):")
for pessoa in equipe_extendida:
    salario = pessoa.calcularSalario()  # Funciona se tiver o método!
    print(f"  {pessoa.nome}: R${salario:.2f}")


# ==========================================
# VANTAGENS DO POLIMORFISMO
# ==========================================

print("\n" + "=" * 60)
print("VANTAGENS DO POLIMORFISMO")
print("=" * 60)

print("""
1. FLEXIBILIDADE
   ✓ Código genérico funciona com diferentes tipos
   ✓ Fácil adicionar novos tipos

2. REUTILIZAÇÃO
   ✓ Uma função/método serve para vários tipos
   ✓ Menos duplicação de código

3. MANUTENIBILIDADE
   ✓ Mudanças isoladas por classe
   ✓ Código mais fácil de entender

4. EXTENSIBILIDADE
   ✓ Adicionar novos tipos sem modificar código existente
   ✓ Princípio Aberto/Fechado (SOLID)

5. TESTABILIDADE
   ✓ Fácil criar objetos de teste
   ✓ Mock objects funcionam naturalmente
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE POLIMORFISMO")
print("=" * 60)

print("""
✓ Polimorfismo = "muitas formas"
✓ Mesmo método, comportamentos diferentes por objeto
✓ Permite código genérico e reutilizável
✓ Funciona com herança ou duck typing
✓ Facilita extensão e manutenção
✓ É um dos 4 pilares da POO
✓ Combine com herança e sobrescrita
✓ Python suporta fortemente (duck typing)
""")

