"""
Getters e Setters

Métodos para acessar e modificar atributos de forma controlada.
"""

# ==========================================
# POR QUE USAR GETTERS E SETTERS?
# ==========================================

print("=" * 60)
print("POR QUE USAR GETTERS E SETTERS?")
print("=" * 60)

print("""
1. VALIDAÇÃO: Validar dados antes de atribuir
2. CONTROLE: Controlar como os dados são acessados
3. COMPUTAÇÃO: Calcular valores derivados
4. LOGGING: Registrar acessos e modificações
5. FLEXIBILIDADE: Mudar implementação sem afetar código externo
""")


# ==========================================
# MÉTODO TRADICIONAL
# ==========================================

print("\n" + "=" * 60)
print("MÉTODO TRADICIONAL: get_xxx() e set_xxx()")
print("=" * 60)

class Pessoa:
    """Classe usando getters e setters tradicionais."""
    
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido
        self._idade = None
        self.setIdade(idade)  # Usa setter para validar
    
    # GETTERS
    def getNome(self):
        """Getter para nome."""
        return self._nome
    
    def getIdade(self):
        """Getter para idade."""
        return self._idade
    
    # SETTERS
    def setNome(self, nome):
        """
        Setter para nome com validação.
        
        Args:
            nome: Nome da pessoa (não pode ser vazio)
        
        Raises:
            ValueError: Se nome for inválido
        """
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        self._nome = nome.strip()
    
    def setIdade(self, idade):
        """
        Setter para idade com validação.
        
        Args:
            idade: Idade da pessoa (0-150)
        
        Raises:
            TypeError: Se idade não for inteiro
            ValueError: Se idade for inválida
        """
        if not isinstance(idade, int):
            raise TypeError("Idade deve ser um número inteiro")
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        if idade > 150:
            raise ValueError("Idade não pode ser maior que 150")
        self._idade = idade
    
    def exibirInfo(self):
        """Exibe informações usando getters."""
        print(f"{self.getNome()} tem {self.getIdade()} anos")


# Uso
print("\nCriando pessoa:")
pessoa = Pessoa("Maria", 25)
pessoa.exibirInfo()

print("\nUsando getters:")
print(f"Nome: {pessoa.getNome()}")
print(f"Idade: {pessoa.getIdade()}")

print("\nUsando setters:")
pessoa.setNome("João Silva")
pessoa.setIdade(30)
pessoa.exibirInfo()

print("\nTestando validação:")
try:
    pessoa.setIdade(-5)
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    pessoa.setNome("")
except ValueError as e:
    print(f"Erro capturado: {e}")


# ==========================================
# EXEMPLO PRÁTICO: PRODUTO COM DESCONTO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO PRÁTICO: Produto com Desconto")
print("=" * 60)

class Produto:
    """
    Produto com getters/setters para preço e desconto.
    
    Demonstra cálculo de valores derivados.
    """
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = None
        self._desconto = 0
        self.setPreco(preco)  # Usa setter para validar
    
    # GETTERS
    def getNome(self):
        """Retorna o nome do produto."""
        return self._nome
    
    def getPreco(self):
        """Retorna o preço original."""
        return self._preco
    
    def getDesconto(self):
        """Retorna o percentual de desconto."""
        return self._desconto
    
    def getPrecoFinal(self):
        """
        Calcula o preço final com desconto.
        
        Returns:
            Preço final após desconto
        """
        return self._preco * (1 - self._desconto / 100)
    
    # SETTERS
    def setNome(self, nome):
        """Define o nome do produto."""
        if not nome:
            raise ValueError("Nome não pode ser vazio")
        self._nome = nome
    
    def setPreco(self, preco):
        """
        Define o preço do produto.
        
        Args:
            preco: Preço (deve ser positivo)
        
        Raises:
            ValueError: Se preço for inválido
        """
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = preco
    
    def setDesconto(self, desconto):
        """
        Define o desconto (percentual).
        
        Args:
            desconto: Percentual de desconto (0-100)
        
        Raises:
            ValueError: Se desconto for inválido
        """
        if not (0 <= desconto <= 100):
            raise ValueError("Desconto deve estar entre 0 e 100")
        self._desconto = desconto
    
    def exibirInfo(self):
        """Exibe informações do produto."""
        precoFinal = self.getPrecoFinal()
        print(f"""
        Produto: {self._nome}
        Preço Original: R${self._preco:.2f}
        Desconto: {self._desconto}%
        Preço Final: R${precoFinal:.2f}
        """)


# Testando
print("\nCriando produto:")
produto = Produto("Notebook", 2500.00)
produto.exibirInfo()

print("\nAplicando desconto:")
produto.setDesconto(15)
produto.exibirInfo()

print("\nAlterando preço:")
produto.setPreco(2000.00)
produto.exibirInfo()


# ==========================================
# EXEMPLO: LOGGING DE ACESSOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO: Getter/Setter com Logging")
print("=" * 60)

class ContaSegura:
    """
    Conta bancária que registra acessos.
    
    Demonstra uso de getters/setters para logging.
    """
    
    def __init__(self, titular, saldoInicial=0):
        self._titular = titular
        self._saldo = saldoInicial
        self._historicoAcessos = []
    
    def getSaldo(self):
        """
        Getter que registra o acesso.
        
        Returns:
            Saldo atual
        """
        import datetime
        self._historicoAcessos.append(
            f"{datetime.datetime.now()}: Consulta de saldo"
        )
        return self._saldo
    
    def setSaldo(self, valor):
        """
        Setter que registra a modificação.
        
        Args:
            valor: Novo valor de saldo
        
        Raises:
            ValueError: Se valor for negativo
        """
        import datetime
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        
        valorAntigo = self._saldo
        self._saldo = valor
        
        self._historicoAcessos.append(
            f"{datetime.datetime.now()}: Saldo alterado de R${valorAntigo:.2f} para R${valor:.2f}"
        )
    
    def getHistorico(self):
        """Retorna o histórico de acessos."""
        return self._historicoAcessos
    
    def exibirExtrato(self):
        """Exibe saldo e histórico."""
        print(f"\nTitular: {self._titular}")
        print(f"Saldo: R${self.getSaldo():.2f}")
        print("\nHistórico de acessos:")
        for registro in self._historicoAcessos:
            print(f"  {registro}")


# Testando
print("\nCriando conta segura:")
conta = ContaSegura("Ana", 1000)
conta.exibirExtrato()

print("\nConsultando saldo várias vezes:")
saldo1 = conta.getSaldo()
saldo2 = conta.getSaldo()
conta.setSaldo(1500)

conta.exibirExtrato()


# ==========================================
# VANTAGENS E DESVANTAGENS
# ==========================================

print("\n" + "=" * 60)
print("VANTAGENS E DESVANTAGENS")
print("=" * 60)

print("""
VANTAGENS:
  ✓ Validação de dados
  ✓ Controle de acesso
  ✓ Flexibilidade para mudanças futuras
  ✓ Possibilidade de adicionar lógica (logging, cálculo)

DESVANTAGENS:
  ✗ Sintaxe mais verbosa (get_xxx(), set_xxx())
  ✗ Menos "Pythonic"

SOLUÇÃO: Usar @property (próximo exemplo)
  → Mantém validação e controle
  → Sintaxe mais elegante e natural
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE GETTERS E SETTERS")
print("=" * 60)

print("""
✓ GETTERS: Métodos para ler valores (get_xxx())
✓ SETTERS: Métodos para modificar valores (set_xxx())
✓ Permitem validação e controle
✓ Podem adicionar lógica adicional
✓ Sintaxe: objeto.get_atributo(), objeto.set_atributo(valor)
✓ Próximo passo: @property para sintaxe mais elegante
""")

