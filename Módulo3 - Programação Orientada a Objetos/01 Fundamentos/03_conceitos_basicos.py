"""
Conceitos Básicos: Classe, Objeto, Atributo e Método

Este exemplo demonstra os quatro conceitos fundamentais da POO.
"""

# ==========================================
# CONCEITO 1: CLASSE
# ==========================================

print("=" * 60)
print("1. CLASSE - O Molde/Template")
print("=" * 60)

print("""
Uma CLASSE é como um molde que define:
  • Quais atributos (características) os objetos terão
  • Quais métodos (comportamentos) os objetos poderão executar

Pense em uma classe como:
  • Um projeto de arquitetura (a classe)
  • Uma casa construída (o objeto)
  • Uma receita de bolo (a classe)
  • Um bolo assado (o objeto)
""")

class Produto:
    """
    Esta é uma CLASSE.
    
    Ela define o que um objeto Produto terá:
    - Atributos (características)
    - Métodos (comportamentos)
    """
    pass  # Por enquanto vazia


# ==========================================
# CONCEITO 2: OBJETO (INSTÂNCIA)
# ==========================================

print("\n" + "=" * 60)
print("2. OBJETO - A Instância da Classe")
print("=" * 60)

print("""
Um OBJETO é uma instância específica de uma classe.
É como uma "casa construída" a partir do "projeto" (classe).
""")

# Criando objetos (instâncias) da classe Produto
produto1 = Produto()  # produto1 é um OBJETO
produto2 = Produto()  # produto2 é outro OBJETO
produto3 = Produto()  # produto3 é outro OBJETO

print(f"\nCriamos 3 objetos:")
print(f"produto1: {produto1}")
print(f"produto2: {produto2}")
print(f"produto3: {produto3}")
print("\nCada objeto é único, mesmo sendo da mesma classe!")


# ==========================================
# CONCEITO 3: ATRIBUTO
# ==========================================

print("\n" + "=" * 60)
print("3. ATRIBUTO - Características do Objeto")
print("=" * 60)

print("""
ATRIBUTOS são características ou propriedades do objeto.
Eles armazenam dados sobre o objeto.

Exemplos:
  • Uma pessoa tem: nome, idade, altura
  • Um carro tem: modelo, cor, ano
  • Um produto tem: nome, preço, quantidade
""")

class Pessoa:
    def __init__(self, nome, idade, altura):
        # ATRIBUTOS: definidos com self.xxxx
        self.nome = nome        # Atributo 'nome'
        self.idade = idade      # Atributo 'idade'
        self.altura = altura    # Atributo 'altura'


# Criando objetos com atributos
pessoa1 = Pessoa("Maria", 25, 1.65)
pessoa2 = Pessoa("João", 30, 1.80)

print(f"\nAtributos de pessoa1:")
print(f"  Nome: {pessoa1.nome}")
print(f"  Idade: {pessoa1.idade}")
print(f"  Altura: {pessoa1.altura}m")

print(f"\nAtributos de pessoa2:")
print(f"  Nome: {pessoa2.nome}")
print(f"  Idade: {pessoa2.idade}")
print(f"  Altura: {pessoa2.altura}m")

print("\nCada objeto tem seus próprios valores de atributos!")


# ==========================================
# CONCEITO 4: MÉTODO
# ==========================================

print("\n" + "=" * 60)
print("4. MÉTODO - Comportamentos do Objeto")
print("=" * 60)

print("""
MÉTODOS são funções definidas dentro de uma classe.
Eles definem comportamentos ou ações que o objeto pode realizar.

Diferença entre função e método:
  • Função: função_qualquer(pessoa, dados)
  • Método: pessoa.fazer_algo(dados)
""")

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # ATRIBUTOS
        self.titular = titular
        self.saldo = saldo_inicial
    
    # MÉTODOS - comportamentos do objeto
    def depositar(self, valor):
        """Método para depositar dinheiro."""
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado.")
    
    def sacar(self, valor):
        """Método para sacar dinheiro."""
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente!")
    
    def exibirSaldo(self):
        """Método para exibir o saldo."""
        print(f"Saldo: R${self.saldo:.2f}")


# Criando conta e usando métodos
print("\nCriando uma conta bancária:")
conta = ContaBancaria("Ana", 1000)

print("\nUsando os métodos:")
conta.depositar(500)      # Chama o método depositar
conta.exibirSaldo()      # Chama o método exibir_saldo
conta.sacar(200)          # Chama o método sacar
conta.exibirSaldo()


# ==========================================
# RESUMO VISUAL
# ==========================================

print("\n" + "=" * 60)
print("RESUMO DOS CONCEITOS")
print("=" * 60)

print("""
┌─────────────────────────────────────────────────┐
│ CLASSE                                          │
│ ─────────────────────────────────────────────  │
│ • Molde/template                                │
│ • Define atributos e métodos                    │
│ • Exemplo: class Carro:                         │
└─────────────────────────────────────────────────┘
                    │
                    │ instancia
                    ▼
┌─────────────────────────────────────────────────┐
│ OBJETO (INSTÂNCIA)                              │
│ ─────────────────────────────────────────────  │
│ • Instância específica da classe               │
│ • Exemplo: meu_carro = Carro()                  │
└─────────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌───────────────┐      ┌───────────────┐
│ ATRIBUTOS     │      │ MÉTODOS       │
│ ────────────  │      │ ────────────  │
│ • Características │  │ • Comportamentos │
│ • Dados       │      │ • Ações       │
│ • self.nome   │      │ • def fazer() │
│ • self.idade  │      │ • def calcular() │
└───────────────┘      └───────────────┘
""")


# ==========================================
# EXEMPLO COMPLETO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO COMPLETO")
print("=" * 60)

class Aluno:
    """Classe que representa um aluno."""
    
    # CONSTRUTOR: define os atributos
    def __init__(self, nome, matricula, nota1, nota2):
        # ATRIBUTOS
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
    
    # MÉTODOS: definem comportamentos
    def calcularMedia(self):
        """Calcula a média do aluno."""
        return (self.nota1 + self.nota2) / 2
    
    def verificarAprovacao(self):
        """Verifica se o aluno foi aprovado."""
        media = self.calcularMedia()
        return media >= 7.0
    
    def exibirInfo(self):
        """Exibe informações do aluno."""
        media = self.calcularMedia()
        status = "Aprovado" if self.verificarAprovacao() else "Reprovado"
        
        print(f"""
        Aluno: {self.nome}
        Matrícula: {self.matricula}
        Nota 1: {self.nota1}
        Nota 2: {self.nota2}
        Média: {media:.2f}
        Status: {status}
        """)


# Criando objetos (instâncias) da classe Aluno
print("\nCriando alunos:")
aluno1 = Aluno("Maria", "2024001", 8.5, 9.0)
aluno2 = Aluno("João", "2024002", 6.0, 5.5)
aluno3 = Aluno("Ana", "2024003", 7.5, 8.0)

# Usando os métodos dos objetos
aluno1.exibirInfo()
aluno2.exibirInfo()
aluno3.exibirInfo()

