"""
Exceções Customizadas

Criar exceções customizadas permite definir erros específicos
do seu domínio, tornando o código mais claro.
"""

# ==========================================
# POR QUE CRIAR EXCEÇÕES CUSTOMIZADAS?
# ==========================================

print("=" * 60)
print("POR QUE CRIAR EXCEÇÕES CUSTOMIZADAS?")
print("=" * 60)

print("""
Vantagens:
  ✓ Clareza: Erros mais específicos e descritivos
  ✓ Controle: Tratar diferentes erros de formas diferentes
  ✓ Depuração: Mais fácil identificar origem do problema
  ✓ Documentação: Indica claramente quais erros podem ocorrer
  ✓ Hierarquia: Pode criar hierarquia de exceções
""")


# ==========================================
# EXEMPLO 1: EXCEÇÃO CUSTOMIZADA BÁSICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Exceção Customizada Básica")
print("=" * 60)

class ValorInvalidoError(Exception):
    """
    Exceção customizada para valores inválidos.
    
    Herda de Exception (classe base para exceções).
    """
    pass


class ContaBancaria:
    """Classe que usa exceção customizada."""
    
    def __init__(self, titular, saldoInicial=0):
        self.titular = titular
        self.saldo = saldoInicial
    
    def depositar(self, valor):
        """Deposita dinheiro na conta."""
        if valor <= 0:
            # Lança exceção customizada
            raise ValorInvalidoError("Valor do depósito deve ser positivo")
        
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado")
    
    def sacar(self, valor):
        """Saca dinheiro da conta."""
        if valor <= 0:
            raise ValorInvalidoError("Valor do saque deve ser positivo")
        
        if valor > self.saldo:
            raise ValorInvalidoError("Saldo insuficiente")
        
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado")


# Testando exceção customizada
print("\nCriando conta:")
conta = ContaBancaria("Ana", 1000)

print("\nTestando validações:")
try:
    conta.depositar(-100)  # Vai lançar ValorInvalidoError
except ValorInvalidoError as e:
    print(f"Erro capturado: {e}")

try:
    conta.sacar(2000)  # Vai lançar ValorInvalidoError
except ValorInvalidoError as e:
    print(f"Erro capturado: {e}")


# ==========================================
# EXEMPLO 2: EXCEÇÃO COM ATRIBUTOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Exceção com Atributos")
print("=" * 60)

class IdadeInvalidaError(Exception):
    """
    Exceção customizada para idade inválida.
    
    Armazena o valor inválido e a mensagem.
    """
    
    def __init__(self, mensagem, valor):
        """
        Inicializa exceção com mensagem e valor.
        
        Args:
            mensagem: Mensagem de erro
            valor: Valor inválido que causou o erro
        """
        self.mensagem = mensagem
        self.valor = valor
        super().__init__(f"{mensagem}: {valor}")
    
    def __str__(self):
        """Representação legível da exceção."""
        return f"{self.mensagem}. Valor recebido: {self.valor}"


class Pessoa:
    """Classe que usa exceção customizada com atributos."""
    
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = None
        self.setIdade(idade)
    
    def setIdade(self, idade):
        """Define idade com validação."""
        if not isinstance(idade, int):
            raise IdadeInvalidaError("Idade deve ser um número inteiro", idade)
        
        if idade < 0:
            raise IdadeInvalidaError("Idade não pode ser negativa", idade)
        
        if idade > 150:
            raise IdadeInvalidaError("Idade não pode ser maior que 150", idade)
        
        self._idade = idade
    
    def getIdade(self):
        """Retorna idade."""
        return self._idade


# Testando exceção com atributos
print("\nCriando pessoa com idade válida:")
pessoa = Pessoa("Maria", 25)
print(f"Idade definida: {pessoa.getIdade()}")

print("\nTestando idades inválidas:")
try:
    pessoa.setIdade(-5)
except IdadeInvalidaError as e:
    print(f"Erro capturado: {e}")
    print(f"Valor inválido: {e.valor}")

try:
    pessoa.setIdade(200)
except IdadeInvalidaError as e:
    print(f"Erro capturado: {e}")
    print(f"Valor inválido: {e.valor}")


# ==========================================
# EXEMPLO 3: HIERARQUIA DE EXCEÇÕES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Hierarquia de Exceções")
print("=" * 60)

class ErroBanco(Exception):
    """Exceção base para erros de banco."""
    pass


class SaldoInsuficienteError(ErroBanco):
    """Erro específico: saldo insuficiente."""
    pass


class ContaNaoEncontradaError(ErroBanco):
    """Erro específico: conta não encontrada."""
    pass


class OperacaoInvalidaError(ErroBanco):
    """Erro específico: operação inválida."""
    pass


class SistemaBancario:
    """Sistema bancário com hierarquia de exceções."""
    
    def __init__(self):
        self.contas = {}
    
    def criarConta(self, numero, saldo_inicial=0):
        """Cria uma nova conta."""
        if numero in self.contas:
            raise OperacaoInvalidaError(f"Conta {numero} já existe")
        self.contas[numero] = saldo_inicial
    
    def depositar(self, numero, valor):
        """Deposita em uma conta."""
        if numero not in self.contas:
            raise ContaNaoEncontradaError(f"Conta {numero} não encontrada")
        
        if valor <= 0:
            raise OperacaoInvalidaError("Valor do depósito deve ser positivo")
        
        self.contas[numero] += valor
    
    def sacar(self, numero, valor):
        """Saca de uma conta."""
        if numero not in self.contas:
            raise ContaNaoEncontradaError(f"Conta {numero} não encontrada")
        
        if valor <= 0:
            raise OperacaoInvalidaError("Valor do saque deve ser positivo")
        
        if valor > self.contas[numero]:
            raise SaldoInsuficienteError(f"Saldo insuficiente. Saldo: R${self.contas[numero]:.2f}")
        
        self.contas[numero] -= valor


# Testando hierarquia
print("\nCriando sistema bancário:")
banco = SistemaBancario()
banco.criarConta("001", 1000)

print("\nTestando diferentes erros:")
try:
    banco.depositar("999", 100)  # Conta não existe
except ContaNaoEncontradaError as e:
    print(f"Erro específico capturado: {e}")

try:
    banco.sacar("001", 2000)  # Saldo insuficiente
except SaldoInsuficienteError as e:
    print(f"Erro específico capturado: {e}")

# Capturando exceção base (captura qualquer ErroBanco)
try:
    banco.depositar("001", -100)
except ErroBanco as e:
    print(f"Erro base capturado: {e}")


# ==========================================
# EXEMPLO 4: EXCEÇÕES ESPECÍFICAS DO DOMÍNIO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Exceções do Domínio")
print("=" * 60)

class ProdutoNaoEncontradoError(Exception):
    """Exceção para produto não encontrado."""
    pass


class EstoqueInsuficienteError(Exception):
    """Exceção para estoque insuficiente."""
    
    def __init__(self, produto, estoqueAtual, quantidadeSolicitada):
        self.produto = produto
        self.estoqueAtual = estoqueAtual
        self.quantidadeSolicitada = quantidadeSolicitada
        super().__init__(
            f"Estoque insuficiente de {produto}. "
            f"Disponível: {estoqueAtual}, Solicitado: {quantidadeSolicitada}"
        )


class PrecoInvalidoError(Exception):
    """Exceção para preço inválido."""
    pass


class Loja:
    """Loja com exceções específicas do domínio."""
    
    def __init__(self):
        self.produtos = {}
    
    def cadastrarProduto(self, nome, preco, estoque):
        """Cadastra um produto."""
        if preco <= 0:
            raise PrecoInvalidoError(f"Preço deve ser positivo. Recebido: {preco}")
        
        if nome in self.produtos:
            raise ValueError(f"Produto {nome} já cadastrado")
        
        self.produtos[nome] = {
            "preco": preco,
            "estoque": estoque
        }
        print(f"✓ Produto {nome} cadastrado")
    
    def buscarProduto(self, nome):
        """Busca um produto."""
        if nome not in self.produtos:
            raise ProdutoNaoEncontradoError(f"Produto '{nome}' não encontrado")
        return self.produtos[nome]
    
    def vender(self, nome, quantidade):
        """Vende um produto."""
        produto = self.buscarProduto(nome)  # Pode lançar ProdutoNaoEncontradoError
        
        if produto["estoque"] < quantidade:
            raise EstoqueInsuficienteError(
                nome,
                produto["estoque"],
                quantidade
            )
        
        produto["estoque"] -= quantidade
        total = produto["preco"] * quantidade
        print(f"✓ Venda: {quantidade}x {nome} = R${total:.2f}")


# Testando
print("\nCriando loja:")
loja = Loja()
loja.cadastrarProduto("Notebook", 2500.00, 5)
loja.cadastrarProduto("Mouse", 50.00, 10)

print("\nTestando exceções do domínio:")
try:
    loja.buscarProduto("Teclado")  # Não existe
except ProdutoNaoEncontradoError as e:
    print(f"Erro: {e}")

try:
    loja.vender("Notebook", 10)  # Estoque insuficiente
except EstoqueInsuficienteError as e:
    print(f"Erro: {e}")
    print(f"  Produto: {e.produto}")
    print(f"  Estoque atual: {e.estoqueAtual}")
    print(f"  Solicitado: {e.quantidadeSolicitada}")

try:
    loja.cadastrarProduto("Produto Inválido", -10, 5)
except PrecoInvalidoError as e:
    print(f"Erro: {e}")


# ==========================================
# BOAS PRÁTICAS
# ==========================================

print("\n" + "=" * 60)
print("BOAS PRÁTICAS PARA EXCEÇÕES CUSTOMIZADAS")
print("=" * 60)

print("""
✓ Use nomes descritivos terminados em "Error"
✓ Herde de Exception ou exceção específica
✓ Adicione atributos para contexto (valor inválido, etc.)
✓ Crie hierarquia quando apropriado
✓ Documente com docstrings
✓ Use mensagens claras e específicas
✓ Agrupe exceções relacionadas em hierarquia
✓ Evite exceções genéricas quando possível
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE EXCEÇÕES CUSTOMIZADAS")
print("=" * 60)

print("""
✓ Exceções customizadas tornam código mais claro
✓ Herdam de Exception
✓ Podem ter atributos para contexto
✓ Permitem hierarquia de exceções
✓ Facilita tratamento específico de erros
✓ Documenta erros que podem ocorrer
✓ Use para erros específicos do seu domínio
✓ Nome terminado em "Error" por convenção
""")

