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
        self.set_idade(idade)  # Usa setter para validar
    
    # GETTERS
    def get_nome(self):
        """Getter para nome."""
        return self._nome
    
    def get_idade(self):
        """Getter para idade."""
        return self._idade
    
    # SETTERS
    def set_nome(self, nome):
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
    
    def set_idade(self, idade):
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
    
    def exibir_info(self):
        """Exibe informações usando getters."""
        print(f"{self.get_nome()} tem {self.get_idade()} anos")


# Uso
print("\nCriando pessoa:")
pessoa = Pessoa("Maria", 25)
pessoa.exibir_info()

print("\nUsando getters:")
print(f"Nome: {pessoa.get_nome()}")
print(f"Idade: {pessoa.get_idade()}")

print("\nUsando setters:")
pessoa.set_nome("João Silva")
pessoa.set_idade(30)
pessoa.exibir_info()

print("\nTestando validação:")
try:
    pessoa.set_idade(-5)
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    pessoa.set_nome("")
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
        self.set_preco(preco)  # Usa setter para validar
    
    # GETTERS
    def get_nome(self):
        """Retorna o nome do produto."""
        return self._nome
    
    def get_preco(self):
        """Retorna o preço original."""
        return self._preco
    
    def get_desconto(self):
        """Retorna o percentual de desconto."""
        return self._desconto
    
    def get_preco_final(self):
        """
        Calcula o preço final com desconto.
        
        Returns:
            Preço final após desconto
        """
        return self._preco * (1 - self._desconto / 100)
    
    # SETTERS
    def set_nome(self, nome):
        """Define o nome do produto."""
        if not nome:
            raise ValueError("Nome não pode ser vazio")
        self._nome = nome
    
    def set_preco(self, preco):
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
    
    def set_desconto(self, desconto):
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
    
    def exibir_info(self):
        """Exibe informações do produto."""
        preco_final = self.get_preco_final()
        print(f"""
        Produto: {self._nome}
        Preço Original: R${self._preco:.2f}
        Desconto: {self._desconto}%
        Preço Final: R${preco_final:.2f}
        """)


# Testando
print("\nCriando produto:")
produto = Produto("Notebook", 2500.00)
produto.exibir_info()

print("\nAplicando desconto:")
produto.set_desconto(15)
produto.exibir_info()

print("\nAlterando preço:")
produto.set_preco(2000.00)
produto.exibir_info()


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
    
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial
        self._historico_acessos = []
    
    def get_saldo(self):
        """
        Getter que registra o acesso.
        
        Returns:
            Saldo atual
        """
        import datetime
        self._historico_acessos.append(
            f"{datetime.datetime.now()}: Consulta de saldo"
        )
        return self._saldo
    
    def set_saldo(self, valor):
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
        
        valor_antigo = self._saldo
        self._saldo = valor
        
        self._historico_acessos.append(
            f"{datetime.datetime.now()}: Saldo alterado de R${valor_antigo:.2f} para R${valor:.2f}"
        )
    
    def get_historico(self):
        """Retorna o histórico de acessos."""
        return self._historico_acessos
    
    def exibir_extrato(self):
        """Exibe saldo e histórico."""
        print(f"\nTitular: {self._titular}")
        print(f"Saldo: R${self.get_saldo():.2f}")
        print("\nHistórico de acessos:")
        for registro in self._historico_acessos:
            print(f"  {registro}")


# Testando
print("\nCriando conta segura:")
conta = ContaSegura("Ana", 1000)
conta.exibir_extrato()

print("\nConsultando saldo várias vezes:")
saldo1 = conta.get_saldo()
saldo2 = conta.get_saldo()
conta.set_saldo(1500)

conta.exibir_extrato()


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

