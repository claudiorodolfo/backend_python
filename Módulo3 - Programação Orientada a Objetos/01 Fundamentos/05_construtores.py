"""
Métodos Construtores (__init__)

O método __init__ é o construtor da classe e é chamado
automaticamente quando um objeto é criado.
"""

# ==========================================
# O QUE É __init__?
# ==========================================

print("=" * 60)
print("O QUE É __init__?")
print("=" * 60)

print("""
__init__ é o MÉTODO CONSTRUTOR da classe.

Características:
  • Sempre se chama __init__ (com dois underscores)
  • Recebe 'self' como primeiro parâmetro
  • É executado AUTOMATICAMENTE quando o objeto é criado
  • Usado para INICIALIZAR os atributos do objeto
  • Pode receber parâmetros para definir valores iniciais
""")


# ==========================================
# EXEMPLO 1: __init__ BÁSICO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Construtor Básico")
print("=" * 60)

class Pessoa:
    """Representa uma pessoa."""
    
    def __init__(self, nome, idade):
        """
        Construtor: inicializa uma pessoa.
        
        Este método é chamado automaticamente quando fazemos:
        pessoa = Pessoa("Maria", 25)
        
        Args:
            nome: Nome da pessoa
            idade: Idade da pessoa
        """
        self.nome = nome
        self.idade = idade
        print(f"Objeto {self.nome} criado!")  # Executado automaticamente


# Ao criar o objeto, __init__ é chamado automaticamente
print("\nCriando objetos:")
pessoa1 = Pessoa("Maria", 25)
pessoa2 = Pessoa("João", 30)

print(f"\n{pessoa1.nome} tem {pessoa1.idade} anos")
print(f"{pessoa2.nome} tem {pessoa2.idade} anos")


# ==========================================
# EXEMPLO 2: __init__ SEM PARÂMETROS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Construtor sem Parâmetros")
print("=" * 60)

class Configuracao:
    """
    Representa configurações do sistema.
    
    Demonstra __init__ que inicializa com valores padrão.
    """
    
    def __init__(self):
        """Construtor sem parâmetros - usa valores padrão."""
        self.idioma = "pt-BR"
        self.tema = "claro"
        self.notificacoes = True
        print("Configuração inicializada com valores padrão")
    
    def exibir(self):
        """Exibe as configurações."""
        print(f"Idioma: {self.idioma}, Tema: {self.tema}, Notificações: {self.notificacoes}")


# Criando sem parâmetros
config = Configuracao()
config.exibir()


# ==========================================
# EXEMPLO 3: __init__ COM PARÂMETROS OPCIONAIS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Parâmetros Opcionais")
print("=" * 60)

class Carro:
    """
    Representa um carro.
    
    Demonstra __init__ com parâmetros opcionais (valores padrão).
    """
    
    def __init__(self, modelo, ano, cor="Branco", quilometragem=0):
        """
        Construtor com parâmetros obrigatórios e opcionais.
        
        Args:
            modelo: Modelo do carro (obrigatório)
            ano: Ano do carro (obrigatório)
            cor: Cor do carro (padrão: "Branco")
            quilometragem: Quilometragem inicial (padrão: 0)
        """
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
    
    def exibirInfo(self):
        """Exibe informações do carro."""
        print(f"{self.modelo} {self.ano} - Cor: {self.cor} - KM: {self.quilometragem}")


print("\nDiferentes formas de criar carros:")
carro1 = Carro("Fusca", 1975)  # Usa valores padrão para cor e km
carro2 = Carro("Gol", 2020, "Vermelho")  # Especifica cor
carro3 = Carro("Civic", 2018, "Preto", 50000)  # Especifica tudo

carro1.exibirInfo()
carro2.exibirInfo()
carro3.exibirInfo()


# ==========================================
# EXEMPLO 4: __init__ COM LÓGICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Lógica no Construtor")
print("=" * 60)

class ContaBancaria:
    """
    Representa uma conta bancária.
    
    Demonstra __init__ que pode fazer cálculos e validações.
    """
    
    def __init__(self, titular, saldo_inicial=0):
        """
        Construtor com validação e inicialização.
        
        Args:
            titular: Nome do titular
            saldo_inicial: Saldo inicial (padrão: 0)
        """
        self.titular = titular
        # Validação: não permite saldo negativo
        if saldo_inicial < 0:
            print("Aviso: Saldo inicial negativo convertido para 0")
            self.saldo = 0
        else:
            self.saldo = saldo_inicial
        
        self.numeroTransacoes = 0
        self.ativa = True
    
    def exibirInfo(self):
        """Exibe informações da conta."""
        status = "Ativa" if self.ativa else "Inativa"
        print(f"""
        Titular: {self.titular}
        Saldo: R${self.saldo:.2f}
        Transações: {self.numeroTransacoes}
        Status: {status}
        """)


print("\nCriando contas:")
conta1 = ContaBancaria("Ana", 1000)
conta2 = ContaBancaria("Bruno", -500)  # Será convertido para 0
conta3 = ContaBancaria("Carla")  # Usa valor padrão 0

conta1.exibirInfo()
conta2.exibirInfo()
conta3.exibirInfo()


# ==========================================
# EXEMPLO 5: MÚLTIPLOS ATRIBUTOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 5: Inicializando Múltiplos Atributos")
print("=" * 60)

class Estudante:
    """
    Representa um estudante.
    
    Demonstra inicialização de vários atributos.
    """
    
    def __init__(self, nome, matricula, curso, ano_ingresso):
        """
        Construtor com múltiplos atributos.
        
        Args:
            nome: Nome do estudante
            matricula: Número de matrícula
            curso: Curso que está fazendo
            ano_ingresso: Ano de ingresso
        """
        # Atributos básicos
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.anoIngresso = ano_ingresso
        
        # Atributos calculados/inicializados
        self.notas = []  # Lista de notas
        self.ativo = True  # Status do estudante
    
    def adicionarNota(self, nota):
        """Adiciona uma nota."""
        self.notas.append(nota)
    
    def calcularMedia(self):
        """Calcula a média das notas."""
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def exibirInfo(self):
        """Exibe informações do estudante."""
        media = self.calcularMedia()
        print(f"""
        Nome: {self.nome}
        Matrícula: {self.matricula}
        Curso: {self.curso}
        Ano de Ingresso: {self.anoIngresso}
        Notas: {self.notas}
        Média: {media:.2f}
        """)


# Testando
estudante = Estudante("Maria", "2024001", "Ciência da Computação", 2024)
estudante.adicionarNota(8.5)
estudante.adicionarNota(9.0)
estudante.adicionarNota(7.5)
estudante.exibirInfo()


# ==========================================
# EXEMPLO 6: ORDEM DE EXECUÇÃO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 6: Ordem de Execução do __init__")
print("=" * 60)

class ExemploOrdem:
    """Demonstra a ordem de execução no __init__."""
    
    def __init__(self, valor):
        print("1. Início do __init__")
        self.valor = valor
        print(f"2. Atribuindo valor: {self.valor}")
        self.processar()
        print("3. Fim do __init__")
    
    def processar(self):
        """Método chamado durante a inicialização."""
        print(f"   Processando valor: {self.valor * 2}")


print("\nCriando objeto (veja a ordem de execução):")
obj = ExemploOrdem(10)


# ==========================================
# IMPORTANTE SOBRE SELF
# ==========================================

print("\n" + "=" * 60)
print("IMPORTANTE: Sobre o 'self'")
print("=" * 60)

print("""
SELF:
  • 'self' é uma referência ao objeto que está sendo criado
  • É SEMPRE o primeiro parâmetro de métodos de instância
  • Usamos 'self.xxxx' para acessar atributos do objeto
  • Python passa 'self' automaticamente, você não precisa passar

Exemplo:
  def __init__(self, nome):    # self é automático
      self.nome = nome         # self.nome é o atributo do objeto

  pessoa = Pessoa("Maria")     # self é passado automaticamente
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE __init__")
print("=" * 60)

print("""
✓ __init__ é o CONSTRUTOR da classe
✓ É chamado AUTOMATICAMENTE ao criar um objeto
✓ Use para INICIALIZAR atributos do objeto
✓ 'self' é sempre o primeiro parâmetro
✓ Pode ter parâmetros obrigatórios e opcionais
✓ Pode conter lógica de validação e cálculo
✓ Não retorna nada (ou retorna None implicitamente)
✓ Pode chamar outros métodos durante a inicialização
""")

