"""
Sobrescrita de Métodos (Override)

Sobrescrita é quando uma subclasse redefine um método da classe pai,
fornecendo uma implementação específica.
"""

# ==========================================
# O QUE É SOBRESCRITA?
# ==========================================

print("=" * 60)
print("O QUE É SOBRESCRITA (OVERRIDE)?")
print("=" * 60)

print("""
SOBRESCRITA ocorre quando:
  • Uma subclasse redefine um método da classe pai
  • A subclasse fornece sua própria implementação
  • O método da subclasse substitui o método do pai

Vantagens:
  ✓ Permite especialização de comportamento
  ✓ Cada classe pode ter comportamento específico
  ✓ Mantém a mesma interface (polimorfismo)
""")


# ==========================================
# EXEMPLO 1: SOBRESCRITA BÁSICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Sobrescrita Básica")
print("=" * 60)

class Animal:
    """Classe pai."""
    
    def fazerSom(self):
        """Método que será sobrescrito."""
        print("Algum som genérico")
    
    def mover(self):
        """Método que não será sobrescrito."""
        print("Movendo-se de alguma forma")


class Cachorro(Animal):
    """Subclasse que sobrescreve fazer_som()."""
    
    def fazerSom(self):
        """Sobrescreve o método da classe pai."""
        print("Au au!")


class Gato(Animal):
    """Outra subclasse que sobrescreve fazer_som()."""
    
    def fazerSom(self):
        """Sobrescreve o método da classe pai."""
        print("Miau!")


class Pato(Animal):
    """Subclasse que mantém comportamento padrão para mover()."""
    
    def fazerSom(self):
        """Sobrescreve fazer_som()."""
        print("Quack quack!")
    
    def mover(self):
        """Também sobrescreve mover()."""
        print("Nadando na água")


# Testando sobrescrita
print("\nCriando animais:")
animal = Animal()
cachorro = Cachorro()
gato = Gato()
pato = Pato()

print("\nMétodo fazerSom() - cada um tem implementação própria:")
animal.fazerSom()      # Implementação da classe pai
cachorro.fazerSom()    # Sobrescrito em Cachorro
gato.fazerSom()        # Sobrescrito em Gato
pato.fazerSom()        # Sobrescrito em Pato

print("\nMétodo mover() - alguns sobrescrevem, outros não:")
animal.mover()          # Implementação da classe pai
cachorro.mover()        # Herdado (não sobrescrito)
gato.mover()            # Herdado (não sobrescrito)
pato.mover()            # Sobrescrito em Pato


# ==========================================
# EXEMPLO 2: SOBRESCRITA COM LÓGICA ESPECÍFICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Sobrescrita com Lógica Específica")
print("=" * 60)

class Forma:
    """Classe base para formas geométricas."""
    
    def calcularArea(self):
        """Método genérico que será sobrescrito."""
        return 0
    
    def calcularPerimetro(self):
        """Método genérico que será sobrescrito."""
        return 0
    
    def exibirInfo(self):
        """Método que usa métodos sobrescritos."""
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")


class Retangulo(Forma):
    """Retangulo sobrescreve métodos de cálculo."""
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcularArea(self):
        """Sobrescreve com cálculo específico de retângulo."""
        return self.largura * self.altura
    
    def calcularPerimetro(self):
        """Sobrescreve com cálculo específico de retângulo."""
        return 2 * (self.largura + self.altura)


class Circulo(Forma):
    """Circulo sobrescreve métodos de cálculo."""
    
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        """Sobrescreve com cálculo específico de círculo."""
        return 3.14159 * self.raio ** 2
    
    def calcularPerimetro(self):
        """Sobrescreve com cálculo específico de círculo."""
        return 2 * 3.14159 * self.raio


class Triangulo(Forma):
    """Triangulo sobrescreve métodos de cálculo."""
    
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcularPerimetro(self):
        """Sobrescreve com cálculo específico de triângulo."""
        return self.lado1 + self.lado2 + self.lado3
    
    # Não sobrescreve calcular_area() - usa implementação do pai (retorna 0)
    # Isso pode ser intencional ou um erro a ser corrigido


# Testando
print("\nCriando formas:")
retangulo = Retangulo(5, 3)
circulo = Circulo(4)
triangulo = Triangulo(3, 4, 5)

print("\nInformações das formas:")
print("Retângulo:")
retangulo.exibirInfo()  # Usa métodos sobrescritos

print("\nCírculo:")
circulo.exibirInfo()    # Usa métodos sobrescritos

print("\nTriângulo:")
triangulo.exibirInfo()  # Perímetro sobrescrito, área não


# ==========================================
# EXEMPLO 3: SOBRESCRITA PARCIAL
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Sobrescrita Parcial")
print("=" * 60)

class Funcionario:
    """Classe base para funcionários."""
    
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcularSalario(self):
        """Método base que será sobrescrito."""
        return self.salario_base
    
    def trabalhar(self):
        """Método genérico."""
        print(f"{self.nome} está trabalhando")
    
    def exibirInfo(self):
        """Método que usa calcularSalario() (que pode ser sobrescrito)."""
        salario = self.calcularSalario()
        print(f"{self.nome} - Salário: R${salario:.2f}")


class Vendedor(Funcionario):
    """Vendedor sobrescreve calcular_salario() para incluir comissão."""
    
    def __init__(self, nome, salario_base, vendas_mes):
        super().__init__(nome, salario_base)
        self.vendas_mes = vendas_mes
    
    def calcularSalario(self):
        """Sobrescreve adicionando comissão."""
        comissao = self.vendas_mes * 0.1  # 10% das vendas
        return self.salario_base + comissao


class Gerente(Funcionario):
    """Gerente sobrescreve calcular_salario() para incluir bônus."""
    
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcularSalario(self):
        """Sobrescreve adicionando bônus."""
        return self.salario_base + self.bonus


class Estagiario(Funcionario):
    """Estagiário NÃO sobrescreve calcular_salario()."""
    
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    
    # Não sobrescreve calcular_salario() - usa implementação do pai
    # Mas pode ter métodos específicos
    def aprender(self):
        """Método específico de Estagiario."""
        print(f"{self.nome} está aprendendo")


# Testando
print("\nCriando funcionários:")
funcionario = Funcionario("Ana", 3000)
vendedor = Vendedor("Bruno", 3000, 5000)  # R$5000 em vendas
gerente = Gerente("Carla", 5000, 1000)    # R$1000 de bônus
estagiario = Estagiario("Daniel", 1500)

print("\nSalários calculados:")
funcionario.exibirInfo()   # Salário base
vendedor.exibirInfo()      # Salário + comissão (sobrescrito)
gerente.exibirInfo()       # Salário + bônus (sobrescrito)
estagiario.exibirInfo()    # Salário base (não sobrescrito)

print("\nComportamentos:")
vendedor.trabalhar()        # Método herdado
estagiario.aprender()       # Método específico


# ==========================================
# EXEMPLO 4: SOBRESCRITA COM VALIDAÇÃO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Sobrescrita com Validação")
print("=" * 60)

class Produto:
    """Classe base para produtos."""
    
    def __init__(self, nome, preco_base):
        self.nome = nome
        self._preco_base = preco_base
    
    def calcularPreco(self):
        """Método que será sobrescrito."""
        return self._preco_base
    
    def aplicarDesconto(self, percentual):
        """Método genérico."""
        if not (0 <= percentual <= 100):
            raise ValueError("Desconto deve estar entre 0 e 100")
        self._preco_base *= (1 - percentual / 100)


class ProdutoComImposto(Produto):
    """Produto que adiciona imposto ao preço."""
    
    def __init__(self, nome, preco_base, percentualImposto):
        super().__init__(nome, preco_base)
        self.percentualImposto = percentualImposto
    
    def calcularPreco(self):
        """Sobrescreve adicionando imposto."""
        imposto = self._preco_base * (self.percentualImposto / 100)
        return self._preco_base + imposto


class ProdutoPromocional(Produto):
    """Produto com desconto automático."""
    
    def __init__(self, nome, preco_base, descontoPromocional):
        super().__init__(nome, preco_base)
        if not (0 <= descontoPromocional <= 100):
            raise ValueError("Desconto promocional inválido")
        self.descontoPromocional = descontoPromocional
    
    def calcularPreco(self):
        """Sobrescreve aplicando desconto promocional."""
        return self._preco_base * (1 - self.descontoPromocional / 100)


# Testando
print("\nCriando produtos:")
produtoNormal = Produto("Livro", 50.00)
produtoImposto = ProdutoComImposto("Eletrônico", 100.00, 20)  # 20% imposto
produtoPromo = ProdutoPromocional("Roupa", 80.00, 15)  # 15% desconto

print("\nPreços calculados:")
print(f"{produtoNormal.nome}: R${produtoNormal.calcularPreco():.2f}")
print(f"{produtoImposto.nome}: R${produtoImposto.calcularPreco():.2f}")
print(f"{produtoPromo.nome}: R${produtoPromo.calcularPreco():.2f}")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE SOBRESCRITA")
print("=" * 60)

print("""
✓ Sobrescrita permite redefinir métodos da classe pai
✓ Cada subclasse pode ter implementação própria
✓ Mantém a mesma interface (polimorfismo)
✓ Pode sobrescrever parcialmente (alguns métodos)
✓ Use quando comportamento precisa ser especializado
✓ Combine com super() para manter funcionalidade do pai
✓ Permite polimorfismo (próximo tópico)
""")

