"""
Definição de Classes

Este exemplo mostra diferentes formas de definir classes em Python,
com exemplos práticos de sintaxe e boas práticas.
"""

# ==========================================
# SINTAXE BÁSICA DE UMA CLASSE
# ==========================================

print("=" * 60)
print("SINTAXE BÁSICA")
print("=" * 60)

print("""
Sintaxe:
    class NomeDaClasse:
        \"\"\"Docstring (opcional mas recomendado)\"\"\"
        
        def metodo1(self):
            pass
        
        def metodo2(self):
            pass
""")


# ==========================================
# EXEMPLO 1: CLASSE SIMPLES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Classe Simples")
print("=" * 60)

class Retangulo:
    """
    Representa um retângulo com largura e altura.
    
    Esta classe demonstra a definição básica de uma classe
    com atributos e métodos simples.
    """
    
    def calcularArea(self):
        """Calcula a área do retângulo."""
        return self.largura * self.altura
    
    def calcularPerimetro(self):
        """Calcula o perímetro do retângulo."""
        return 2 * (self.largura + self.altura)


# Nota: Esta classe não tem __init__, então precisamos
# definir os atributos depois de criar o objeto
ret = Retangulo()
ret.largura = 5
ret.altura = 3
print(f"Área: {ret.calcularArea()}")
print(f"Perímetro: {ret.calcularPerimetro()}")


# ==========================================
# EXEMPLO 2: CLASSE COM CONSTRUTOR
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Classe com Construtor")
print("=" * 60)

class Circulo:
    """
    Representa um círculo com raio.
    
    Esta classe mostra como usar __init__ para
    inicializar atributos automaticamente.
    """
    
    def __init__(self, raio):
        """
        Construtor: inicializa o círculo com um raio.
        
        Args:
            raio: Raio do círculo (número positivo)
        """
        self.raio = raio
    
    def calcularArea(self):
        """Calcula a área do círculo."""
        return 3.14159 * self.raio ** 2
    
    def calcularPerimetro(self):
        """Calcula o perímetro (circunferência) do círculo."""
        return 2 * 3.14159 * self.raio


# Uso mais limpo com construtor
circulo = Circulo(5)
print(f"Raio: {circulo.raio}")
print(f"Área: {circulo.calcularArea():.2f}")
print(f"Perímetro: {circulo.calcularPerimetro():.2f}")


# ==========================================
# EXEMPLO 3: CLASSE COM MÚLTIPLOS MÉTODOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Classe com Múltiplos Métodos")
print("=" * 60)

class Livro:
    """
    Representa um livro em uma biblioteca.
    
    Demonstra uma classe com múltiplos atributos
    e comportamentos diversos.
    """
    
    def __init__(self, titulo, autor, paginas):
        """Inicializa um livro."""
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.emprestado = False
    
    def emprestar(self):
        """Marca o livro como emprestado."""
        if not self.emprestado:
            self.emprestado = True
            print(f"'{self.titulo}' foi emprestado.")
        else:
            print(f"'{self.titulo}' já está emprestado!")
    
    def devolver(self):
        """Marca o livro como devolvido."""
        if self.emprestado:
            self.emprestado = False
            print(f"'{self.titulo}' foi devolvido.")
        else:
            print(f"'{self.titulo}' não estava emprestado.")
    
    def exibirInfo(self):
        """Exibe informações do livro."""
        status = "Emprestado" if self.emprestado else "Disponível"
        print(f"""
        Título: {self.titulo}
        Autor: {self.autor}
        Páginas: {self.paginas}
        Status: {status}
        """)


# Testando a classe Livro
livro1 = Livro("1984", "George Orwell", 328)
livro1.exibirInfo()
livro1.emprestar()
livro1.exibirInfo()
livro1.devolver()


# ==========================================
# EXEMPLO 4: CLASSE COM VALORES PADRÃO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Parâmetros Opcionais no Construtor")
print("=" * 60)

class Produto:
    """
    Representa um produto em uma loja.
    
    Demonstra uso de valores padrão nos parâmetros
    do construtor.
    """
    
    def __init__(self, nome, preco, estoque=0, desconto=0):
        """
        Inicializa um produto.
        
        Args:
            nome: Nome do produto (obrigatório)
            preco: Preço do produto (obrigatório)
            estoque: Quantidade em estoque (padrão: 0)
            desconto: Percentual de desconto (padrão: 0)
        """
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.desconto = desconto
    
    def aplicarDesconto(self):
        """Calcula o preço com desconto."""
        return self.preco * (1 - self.desconto / 100)
    
    def verificarDisponibilidade(self):
        """Verifica se o produto está disponível."""
        return self.estoque > 0
    
    def exibirInfo(self):
        """Exibe informações do produto."""
        preco_final = self.aplicarDesconto()
        disponivel = "Sim" if self.verificarDisponibilidade() else "Não"
        
        print(f"""
        Produto: {self.nome}
        Preço: R${self.preco:.2f}
        Desconto: {self.desconto}%
        Preço Final: R${preco_final:.2f}
        Estoque: {self.estoque}
        Disponível: {disponivel}
        """)


# Criando produtos de diferentes formas
produto1 = Produto("Notebook", 2500.00)  # Só nome e preço
produto2 = Produto("Mouse", 50.00, estoque=10)  # Com estoque
produto3 = Produto("Teclado", 150.00, estoque=5, desconto=10)  # Tudo

produto1.exibirInfo()
produto2.exibirInfo()
produto3.exibirInfo()


# ==========================================
# EXEMPLO 5: CONVENÇÕES DE NOMENCLATURA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 5: Convenções de Nomenclatura")
print("=" * 60)

print("""
CONVENÇÕES EM PYTHON:

Classes:
  ✓ PascalCase (primeira letra de cada palavra em maiúscula)
  ✓ Substantivos
  ✓ Exemplos: Pessoa, ContaBancaria, ProdutoLoja

Métodos e Atributos:
  ✓ snake_case (todas minúsculas, palavras separadas por _)
  ✓ Métodos: verbos (calcular_area, depositar_dinheiro)
  ✓ Atributos: substantivos/adjetivos (nome, idade, ativo)

Exemplos:
  class ContaBancaria:        # Classe: PascalCase
      def __init__(self):
          self.titular = ""    # Atributo: snake_case
          self.saldo = 0
    
      def depositar_dinheiro(self):  # Método: snake_case, verbo
          pass
""")


# ==========================================
# EXEMPLO 6: DOCUMENTAÇÃO COM DOCSTRINGS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 6: Documentação")
print("=" * 60)

class Funcionario:
    """
    Representa um funcionário da empresa.
    
    Esta classe gerencia informações básicas de um funcionário,
    incluindo nome, cargo e salário.
    
    Attributes:
        nome (str): Nome completo do funcionário
        cargo (str): Cargo ocupado na empresa
        salario (float): Salário mensal em reais
    
    Example:
        >>> func = Funcionario("João Silva", "Desenvolvedor", 5000.00)
        >>> func.exibir_info()
    """
    
    def __init__(self, nome, cargo, salario):
        """
        Inicializa um funcionário.
        
        Args:
            nome: Nome completo do funcionário
            cargo: Cargo na empresa
            salario: Salário mensal
        """
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def aumentarSalario(self, percentual):
        """
        Aumenta o salário do funcionário.
        
        Args:
            percentual: Percentual de aumento (ex: 10 para 10%)
        
        Returns:
            Novo valor do salário
        """
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        return self.salario
    
    def exibirInfo(self):
        """Exibe informações do funcionário."""
        print(f"{self.nome} - {self.cargo} - R${self.salario:.2f}")


# Testando
func = Funcionario("Maria Santos", "Analista", 4000.00)
func.exibirInfo()
func.aumentarSalario(15)
print("Após aumento de 15%:")
func.exibirInfo()


# ==========================================
# BOAS PRÁTICAS
# ==========================================

print("\n" + "=" * 60)
print("BOAS PRÁTICAS AO DEFINIR CLASSES")
print("=" * 60)

print("""
✓ SEMPRE use nomes descritivos para classes
✓ SEMPRE documente com docstrings
✓ Use __init__ para inicializar atributos
✓ Agrupe métodos relacionados
✓ Siga convenções de nomenclatura (PascalCase para classes)
✓ Mantenha classes focadas em uma única responsabilidade
✓ Use valores padrão quando apropriado
""")

