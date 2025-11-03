"""
Instanciação de Objetos

A instanciação é o processo de criar um objeto (instância)
a partir de uma classe.
"""

# ==========================================
# O QUE É INSTANCIAÇÃO?
# ==========================================

print("=" * 60)
print("O QUE É INSTANCIAÇÃO?")
print("=" * 60)

print("""
INSTANCIAÇÃO é o processo de criar um OBJETO (instância)
a partir de uma CLASSE.

Processo:
  1. Python chama automaticamente o método __init__
  2. Os parâmetros passados são atribuídos aos atributos
  3. O objeto criado é retornado e armazenado na variável

Sintaxe:
  objeto = NomeDaClasse(parametros)
""")


# ==========================================
# EXEMPLO 1: INSTANCIAÇÃO SIMPLES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Instanciação Básica")
print("=" * 60)

class Pessoa:
    """Classe simples para demonstração."""
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos")


# INSTANCIAÇÃO: criar um objeto
print("\nCriando objetos:")
pessoa1 = Pessoa("Maria", 25)  # Instanciação 1
pessoa2 = Pessoa("João", 30)   # Instanciação 2

# Cada objeto é independente
pessoa1.apresentar()
pessoa2.apresentar()


# ==========================================
# EXEMPLO 2: MÚLTIPLAS INSTÂNCIAS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Criando Múltiplas Instâncias")
print("=" * 60)

class Produto:
    """Representa um produto."""
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def exibir(self):
        print(f"Produto: {self.nome} - R${self.preco:.2f}")


# Criando vários objetos da mesma classe
print("\nCriando lista de produtos:")
produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Mouse", 50.00)
produto3 = Produto("Teclado", 150.00)
produto4 = Produto("Monitor", 800.00)

# Cada objeto é único
produtos = [produto1, produto2, produto3, produto4]
for produto in produtos:
    produto.exibir()


# ==========================================
# EXEMPLO 3: INSTÂNCIAS COM VALORES DIFERENTES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Instâncias Independentes")
print("=" * 60)

class ContaBancaria:
    """Representa uma conta bancária."""
    
    def __init__(self, titular, saldoInicial=0):
        self.titular = titular
        self.saldo = saldoInicial
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"{self.titular}: Depósito de R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"{self.titular}: Saque de R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")
        else:
            print(f"{self.titular}: Saldo insuficiente!")
    
    def exibirSaldo(self):
        print(f"{self.titular}: Saldo atual = R${self.saldo:.2f}")


# Criando múltiplas contas
print("\nCriando contas bancárias:")
conta1 = ContaBancaria("Ana", 1000)
conta2 = ContaBancaria("Bruno", 500)
conta3 = ContaBancaria("Carla")

print("\nDemonstrando independência entre objetos:")
conta1.depositar(200)
conta2.sacar(100)
conta3.depositar(300)

print("\nSaldo final de cada conta:")
conta1.exibirSaldo()
conta2.exibirSaldo()
conta3.exibirSaldo()


# ==========================================
# EXEMPLO 4: INSTANCIAÇÃO EM LISTA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Criando Objetos em Lista")
print("=" * 60)

class Aluno:
    """Representa um aluno."""
    
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def exibirInfo(self):
        status = "Aprovado" if self.nota >= 7 else "Reprovado"
        print(f"{self.nome}: {self.nota:.1f} - {status}")


# Criando lista de alunos de uma vez
print("\nCriando turma de alunos:")
alunos_dados = [
    ("Ana", 8.5),
    ("Bruno", 6.0),
    ("Carla", 9.0),
    ("Daniel", 7.5),
    ("Eduarda", 5.5)
]

# Instanciando em loop
alunos = []
for nome, nota in alunos_dados:
    aluno = Aluno(nome, nota)  # Instanciação dentro do loop
    alunos.append(aluno)

print("\nLista de alunos:")
for aluno in alunos:
    aluno.exibirInfo()


# ==========================================
# EXEMPLO 5: INSTANCIAÇÃO COM VALIDAÇÃO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 5: Instanciação com Validação")
print("=" * 60)

class IdadeInvalidaError(Exception):
    """Exceção para idade inválida."""
    pass


class PessoaValidada:
    """Pessoa com validação na instanciação."""
    
    def __init__(self, nome, idade):
        """
        Cria uma pessoa validando os dados.
        
        Args:
            nome: Nome da pessoa
            idade: Idade (deve estar entre 0 e 150)
        
        Raises:
            IdadeInvalidaError: Se idade for inválida
        """
        if not isinstance(idade, int) or idade < 0 or idade > 150:
            raise IdadeInvalidaError(f"Idade {idade} é inválida! Deve ser entre 0 e 150.")
        
        self.nome = nome
        self.idade = idade
        print(f"Pessoa {self.nome} criada com sucesso!")
    
    def exibirInfo(self):
        print(f"{self.nome} tem {self.idade} anos")


print("\nCriando pessoas válidas:")
p1 = PessoaValidada("Maria", 25)
p2 = PessoaValidada("João", 30)

print("\nTentando criar pessoa com idade inválida:")
try:
    p3 = PessoaValidada("Pedro", 200)  # Isso vai gerar erro
except IdadeInvalidaError as e:
    print(f"Erro: {e}")


# ==========================================
# EXEMPLO 6: INSTÂNCIAS COMO PARÂMETROS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 6: Objetos como Parâmetros")
print("=" * 60)

class Data:
    """Representa uma data."""
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


class Funcionario:
    """Representa um funcionário."""
    
    def __init__(self, nome, dataContratacao):
        """
        Cria funcionário com data de contratação.
        
        Args:
            nome: Nome do funcionário
            dataContratacao: Objeto Data
        """
        self.nome = nome
        self.dataContratacao = dataContratacao
    
    def exibirInfo(self):
        print(f"{self.nome} contratado em {self.dataContratacao}")


# Criando objeto Data
data1 = Data(15, 3, 2024)

# Passando objeto como parâmetro
func1 = Funcionario("Ana", data1)
func1.exibirInfo()

# Ou criando diretamente
func2 = Funcionario("Bruno", Data(20, 5, 2023))
func2.exibirInfo()


# ==========================================
# EXEMPLO 7: PROCESSO DE INSTANCIAÇÃO PASSO A PASSO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 7: Processo de Instanciação Detalhado")
print("=" * 60)

class ExemploDetalhado:
    """Classe para demonstrar o processo de instanciação."""
    
    def __init__(self, valor):
        print(f"  [1] __init__ chamado com valor = {valor}")
        self.valor = valor
        print(f"  [2] Atributo self.valor = {self.valor}")
        self.processar()
        print(f"  [3] __init__ finalizado")
    
    def processar(self):
        print(f"  [2.1] Método processar() executado")
        self.resultado = self.valor * 2
        print(f"  [2.2] Resultado calculado = {self.resultado}")


print("\nCriando objeto (veja cada etapa):")
print("[0] Chamando: obj = ExemploDetalhado(10)")
obj = ExemploDetalhado(10)
print("[4] Objeto criado e armazenado em 'obj'")
print(f"[5] Acessando atributos: obj.valor = {obj.valor}, obj.resultado = {obj.resultado}")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE INSTANCIAÇÃO")
print("=" * 60)

print("""
✓ Instanciação cria um objeto a partir de uma classe
✓ Sintaxe: objeto = NomeClasse(parametros)
✓ __init__ é chamado automaticamente
✓ Cada objeto é independente e único
✓ Pode criar múltiplas instâncias da mesma classe
✓ Objetos podem ser armazenados em listas, passados como parâmetros, etc.
✓ Validações podem ocorrer durante a instanciação
✓ Objetos mantêm seus próprios valores de atributos
""")

