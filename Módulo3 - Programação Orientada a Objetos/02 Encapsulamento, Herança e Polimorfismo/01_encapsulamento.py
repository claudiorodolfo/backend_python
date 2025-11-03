"""
Encapsulamento

O encapsulamento agrupa dados e métodos relacionados em uma classe
e controla o acesso a esses dados.
"""

# ==========================================
# PROBLEMA: SEM ENCAPSULAMENTO
# ==========================================

print("=" * 60)
print("PROBLEMA: Sem Encapsulamento")
print("=" * 60)

class PessoaSemEncapsulamento:
    """Classe sem encapsulamento - NÃO RECOMENDADO."""
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade  # Pode ser modificado diretamente


# Problemas dessa abordagem:
pessoa1 = PessoaSemEncapsulamento("Maria", 25)
print(f"\nNome: {pessoa1.nome}, Idade: {pessoa1.idade}")

# ❌ Problema 1: Pode atribuir valores inválidos
pessoa1.idade = -5  # Idade negativa! Isso não faz sentido
print(f"Idade inválida: {pessoa1.idade}")

# ❌ Problema 2: Pode modificar sem controle
pessoa1.idade = 200  # Idade impossível
print(f"Idade impossível: {pessoa1.idade}")


# ==========================================
# SOLUÇÃO: COM ENCAPSULAMENTO
# ==========================================

print("\n" + "=" * 60)
print("SOLUÇÃO: Com Encapsulamento")
print("=" * 60)

class PessoaComEncapsulamento:
    """
    Classe com encapsulamento - RECOMENDADO.
    
    Controla o acesso aos dados através de métodos,
    permitindo validação e proteção.
    """
    
    def __init__(self, nome, idade):
        self._nome = nome  # Protegido (convenção _)
        self._idade = None  # Vamos usar setter para definir
        self.setIdade(idade)  # Usa o método setter para validar
    
    def getNome(self):
        """Getter: retorna o nome."""
        return self._nome
    
    def setNome(self, nome):
        """Setter: define o nome com validação."""
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        self._nome = nome
    
    def getIdade(self):
        """Getter: retorna a idade."""
        return self._idade
    
    def setIdade(self, idade):
        """
        Setter: define a idade com validação.
        
        Args:
            idade: Idade da pessoa (deve estar entre 0 e 150)
        
        Raises:
            ValueError: Se a idade for inválida
        """
        if not isinstance(idade, int):
            raise TypeError("Idade deve ser um número inteiro")
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        if idade > 150:
            raise ValueError("Idade não pode ser maior que 150")
        self._idade = idade
    
    def exibirInfo(self):
        """Exibe informações da pessoa."""
        print(f"{self._nome} tem {self._idade} anos")


# Uso com encapsulamento
print("\nCriando pessoa com encapsulamento:")
pessoa2 = PessoaComEncapsulamento("João", 30)
pessoa2.exibirInfo()

# ✅ Tentativa de atribuir idade inválida é bloqueada
print("\nTentando atribuir idade inválida:")
try:
    pessoa2.setIdade(-5)  # Isso vai gerar erro!
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    pessoa2.setIdade(200)  # Isso também vai gerar erro!
except ValueError as e:
    print(f"Erro capturado: {e}")

# ✅ Valores válidos funcionam
print("\nAtribuindo valores válidos:")
pessoa2.setIdade(35)
pessoa2.exibirInfo()


# ==========================================
# BENEFÍCIOS DO ENCAPSULAMENTO
# ==========================================

print("\n" + "=" * 60)
print("BENEFÍCIOS DO ENCAPSULAMENTO")
print("=" * 60)

print("""
1. PROTEÇÃO DE DADOS
   ✓ Previne valores inválidos
   ✓ Controla como os dados são modificados

2. VALIDAÇÃO
   ✓ Valida dados antes de atribuir
   ✓ Retorna erros claros

3. FLEXIBILIDADE
   ✓ Pode mudar implementação interna sem afetar código externo
   ✓ Pode adicionar lógica (ex: logging) sem quebrar código

4. MANUTENIBILIDADE
   ✓ Código mais fácil de manter
   ✓ Localiza problemas mais facilmente
""")


# ==========================================
# EXEMPLO PRÁTICO: CONTA BANCÁRIA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO PRÁTICO: Conta Bancária")
print("=" * 60)

class ContaBancaria:
    """
    Representa uma conta bancária com encapsulamento.
    
    Demonstra proteção de dados críticos (saldo).
    """
    
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = 0  # Inicializa como 0
        if saldo_inicial > 0:
            self.depositar(saldo_inicial)  # Usa método para validar
    
    def getTitular(self):
        """Retorna o titular da conta."""
        return self._titular
    
    def getSaldo(self):
        """Retorna o saldo atual."""
        return self._saldo
    
    def depositar(self, valor):
        """
        Deposita dinheiro na conta.
        
        Args:
            valor: Valor a depositar (deve ser positivo)
        
        Raises:
            ValueError: Se valor for inválido
        """
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo: R${self._saldo:.2f}")
    
    def sacar(self, valor):
        """
        Saca dinheiro da conta.
        
        Args:
            valor: Valor a sacar (deve ser positivo e <= saldo)
        
        Raises:
            ValueError: Se valor for inválido ou saldo insuficiente
        """
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado. Saldo: R${self._saldo:.2f}")
    
    def exibirExtrato(self):
        """Exibe informações da conta."""
        print(f"""
        Titular: {self._titular}
        Saldo: R${self._saldo:.2f}
        """)


# Testando a conta bancária
print("\nCriando conta:")
conta = ContaBancaria("Ana Silva", 1000)

print("\nTentando acessar saldo diretamente (não recomendado):")
# Note: Podemos acessar _saldo diretamente, mas não devemos
# O encapsulamento é uma convenção, não uma proteção rígida
print(f"Saldo (acesso direto): R${conta._saldo:.2f}")

print("\nUsando métodos (recomendado):")
conta.depositar(500)
conta.sacar(200)

print("\nTentando operações inválidas:")
try:
    conta.sacar(-100)  # Valor negativo
except ValueError as e:
    print(f"Erro: {e}")

try:
    conta.sacar(2000)  # Saldo insuficiente
except ValueError as e:
    print(f"Erro: {e}")

conta.exibirExtrato()


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE ENCAPSULAMENTO")
print("=" * 60)

print("""
✓ Encapsulamento agrupa dados e métodos relacionados
✓ Controla acesso aos dados através de métodos
✓ Permite validação e proteção de dados
✓ Facilita manutenção e mudanças futuras
✓ Use getters/setters ou @property (próximo exemplo)
✓ Convenções: _ protegido, __ privado
""")

