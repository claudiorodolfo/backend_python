"""
Usando @property para Getters e Setters

O decorador @property permite criar getters e setters
com sintaxe mais elegante e "Pythonic".
"""

# ==========================================
# INTRODUÇÃO AO @property
# ==========================================

print("=" * 60)
print("USANDO @property")
print("=" * 60)

print("""
@property é um decorador que permite:
  • Criar getters com sintaxe natural
  • Criar setters com @atributo.setter
  • Usar como atributo normal (sem chamar como método)

Vantagens:
  ✓ Sintaxe mais elegante
  ✓ Mantém validação e controle
  ✓ Código mais "Pythonic"
""")


# ==========================================
# EXEMPLO 1: @property BÁSICO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: @property Básico")
print("=" * 60)

class Pessoa:
    """Classe usando @property para getters/setters."""
    
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = None
        self.idade = idade  # Usa o setter do @property
    
    @property
    def nome(self):
        """Getter para nome usando @property."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Setter para nome."""
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor.strip()
    
    @property
    def idade(self):
        """Getter para idade usando @property."""
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        """Setter para idade com validação."""
        if not isinstance(valor, int):
            raise TypeError("Idade deve ser um número inteiro")
        if valor < 0 or valor > 150:
            raise ValueError("Idade deve estar entre 0 e 150")
        self._idade = valor
    
    def exibirInfo(self):
        """Exibe informações."""
        print(f"{self.nome} tem {self.idade} anos")  # Usa como atributo


# Uso - sintaxe natural!
print("\nCriando pessoa:")
pessoa = Pessoa("Maria", 25)
pessoa.exibirInfo()

print("\nUsando como atributo normal:")
print(f"Nome: {pessoa.nome}")  # Chama o getter automaticamente
print(f"Idade: {pessoa.idade}")  # Chama o getter automaticamente

print("\nModificando como atributo normal:")
pessoa.nome = "João Silva"  # Chama o setter automaticamente
pessoa.idade = 30  # Chama o setter automaticamente
pessoa.exibirInfo()

print("\nTestando validação:")
try:
    pessoa.idade = -5  # Vai gerar erro
except ValueError as e:
    print(f"Erro: {e}")


# ==========================================
# EXEMPLO 2: PROPRIEDADE READ-ONLY
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Propriedade Read-Only (Somente Leitura)")
print("=" * 60)

class Produto:
    """Produto com propriedade calculada e read-only."""
    
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._dataCriacao = None
        self._inicializarData()
    
    def _inicializarData(self):
        """Inicializa data de criação (simulação)."""
        import datetime
        self._data_criacao = datetime.datetime.now()
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("Quantidade não pode ser negativa")
        self._quantidade = valor
    
    @property
    def valorTotal(self):
        """
        Propriedade calculada (read-only).
        
        Não tem setter, então é somente leitura.
        """
        return self._preco * self._quantidade
    
    @property
    def dataCriacao(self):
        """
        Propriedade read-only.
        
        Sem setter, não pode ser modificada.
        """
        return self._dataCriacao
    
    def exibirInfo(self):
        """Exibe informações do produto."""
        print(f"""
        Produto: {self.nome}
        Preço Unitário: R${self.preco:.2f}
        Quantidade: {self.quantidade}
        Valor Total: R${self.valorTotal:.2f}
        Data Criação: {self.dataCriacao}
        """)


# Testando
print("\nCriando produto:")
produto = Produto("Notebook", 2500.00, 2)
produto.exibirInfo()

print("\nModificando preço:")
produto.preco = 2300.00
produto.exibirInfo()

print("\nTentando modificar propriedade read-only:")
try:
    produto.valor_total = 5000  # Vai gerar erro - não tem setter!
except AttributeError as e:
    print(f"Erro esperado: {e}")

try:
    produto.data_criacao = "2024-01-01"  # Também vai gerar erro
except AttributeError as e:
    print(f"Erro esperado: {e}")


# ==========================================
# EXEMPLO 3: PROPRIEDADE COM VALIDAÇÃO COMPLEXA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Validação Complexa")
print("=" * 60)

class ContaBancaria:
    """Conta bancária com validações complexas."""
    
    def __init__(self, titular, saldoInicial=0):
        self._titular = None
        self.titular = titular  # Usa setter
        self._saldo = 0
        if saldoInicial > 0:
            self.depositar(saldoInicial)
    
    @property
    def titular(self):
        """Getter para titular."""
        return self._titular
    
    @titular.setter
    def titular(self, valor):
        """
        Setter com validação complexa.
        
        Args:
            valor: Nome do titular
        
        Raises:
            ValueError: Se nome for inválido
        """
        if not valor:
            raise ValueError("Titular não pode ser vazio")
        
        # Validação: nome deve ter pelo menos 2 palavras
        palavras = valor.strip().split()
        if len(palavras) < 2:
            raise ValueError("Titular deve ter nome e sobrenome")
        
        # Capitaliza corretamente
        valor_formatado = " ".join([p.capitalize() for p in palavras])
        self._titular = valor_formatado
    
    @property
    def saldo(self):
        """Getter para saldo (read-only via property)."""
        return self._saldo
    
    def depositar(self, valor):
        """Deposita dinheiro na conta."""
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado")
    
    def sacar(self, valor):
        """Saca dinheiro da conta."""
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado")
    
    def exibirExtrato(self):
        """Exibe informações da conta."""
        print(f"""
        Titular: {self.titular}
        Saldo: R${self.saldo:.2f}
        """)


# Testando
print("\nCriando conta:")
conta = ContaBancaria("maria silva", 1000)
conta.exibirExtrato()

print("\nTentando definir titular inválido:")
try:
    conta.titular = "Maria"  # Só um nome - vai gerar erro
except ValueError as e:
    print(f"Erro: {e}")

print("\nDefinindo titular válido:")
conta.titular = "joão santos oliveira"
conta.exibirExtrato()

print("\nNote: saldo não pode ser modificado diretamente")
print(f"Saldo: {conta.saldo}")
# conta.saldo = 5000  # Isso geraria erro se tivéssemos tentado


# ==========================================
# EXEMPLO 4: PROPRIEDADE COM LÓGICA CONDICIONAL
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Propriedade com Lógica Condicional")
print("=" * 60)

class Aluno:
    """Aluno com propriedades calculadas."""
    
    def __init__(self, nome):
        self._nome = nome
        self._notas = []
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def notas(self):
        """Retorna cópia da lista de notas (proteção)."""
        return self._notas.copy()
    
    def adicionarNota(self, nota):
        """Adiciona uma nota."""
        if not (0 <= nota <= 10):
            raise ValueError("Nota deve estar entre 0 e 10")
        self._notas.append(nota)
    
    @property
    def media(self):
        """Calcula a média das notas."""
        if len(self._notas) == 0:
            return 0
        return sum(self._notas) / len(self._notas)
    
    @property
    def status(self):
        """
        Retorna status do aluno baseado na média.
        
        Returns:
            'Aprovado', 'Recuperação' ou 'Reprovado'
        """
        media = self.media
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
    
    def exibirInfo(self):
        """Exibe informações do aluno."""
        print(f"""
        Aluno: {self.nome}
        Notas: {self.notas}
        Média: {self.media:.2f}
        Status: {self.status}
        """)


# Testando
print("\nCriando aluno:")
aluno = Aluno("Maria")
aluno.adicionarNota(8.5)
aluno.adicionarNota(9.0)
aluno.adicionarNota(7.5)

aluno.exibirInfo()

print("\nPropriedades calculadas se atualizam automaticamente:")
aluno.adicionarNota(6.0)
aluno.exibirInfo()


# ==========================================
# COMPARAÇÃO: TRADICIONAL vs @property
# ==========================================

print("\n" + "=" * 60)
print("COMPARAÇÃO: Tradicional vs @property")
print("=" * 60)

print("""
TRADICIONAL:
  pessoa.get_idade()
  pessoa.set_idade(30)

COM @property:
  pessoa.idade        # Mais natural
  pessoa.idade = 30   # Parece atributo, mas tem validação

VANTAGENS DO @property:
  ✓ Sintaxe mais elegante e Pythonic
  ✓ Mantém todos os benefícios de getters/setters
  ✓ Código mais legível
  ✓ Fácil de usar

QUANDO USAR:
  ✓ Sempre que precisar de validação ou controle
  ✓ Para propriedades calculadas
  ✓ Para propriedades read-only
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE @property")
print("=" * 60)

print("""
✓ @property cria getters com sintaxe natural
✓ @atributo.setter cria setters
✓ Uso: objeto.atributo (não precisa de parênteses)
✓ Mantém validação e controle
✓ Pode criar propriedades read-only (sem setter)
✓ Pode criar propriedades calculadas
✓ Sintaxe mais elegante que get_xxx()/set_xxx()
✓ Recomendado para código Python moderno
""")

