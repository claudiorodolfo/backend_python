"""
Tratamento de Exceções em Classes

Tratar exceções dentro de classes permite validar dados,
lançar exceções apropriadas e manter estado consistente.
"""

# ==========================================
# TRATAMENTO DE EXCEÇÕES EM MÉTODOS
# ==========================================

print("=" * 60)
print("TRATAMENTO DE EXCEÇÕES EM CLASSES")
print("=" * 60)

print("""
Por que tratar exceções em classes?
  ✓ Validar dados de entrada
  ✓ Manter estado consistente
  ✓ Fornecer mensagens de erro claras
  ✓ Prevenir corrupção de dados
  ✓ Tratar erros de forma elegante
""")


# ==========================================
# EXEMPLO 1: VALIDAÇÃO COM TRY-EXCEPT
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Validação em Métodos")
print("=" * 60)

class ContaBancaria:
    """Conta bancária com tratamento de exceções."""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = 0
        if saldo_inicial > 0:
            self.depositar(saldo_inicial)
    
    def depositar(self, valor):
        """
        Deposita dinheiro na conta.
        
        Trata exceções e valida entrada.
        
        Args:
            valor: Valor a depositar
        
        Raises:
            ValueError: Se valor for inválido
        """
        try:
            # Validação
            if not isinstance(valor, (int, float)):
                raise TypeError("Valor deve ser numérico")
            
            if valor <= 0:
                raise ValueError("Valor do depósito deve ser positivo")
            
            # Operação segura
            self.saldo += valor
            print(f"✓ Depósito de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}")
            
        except (TypeError, ValueError) as e:
            print(f"✗ Erro ao depositar: {e}")
            raise  # Propaga a exceção
    
    def sacar(self, valor):
        """
        Saca dinheiro da conta.
        
        Trata exceções e valida entrada.
        """
        try:
            if not isinstance(valor, (int, float)):
                raise TypeError("Valor deve ser numérico")
            
            if valor <= 0:
                raise ValueError("Valor do saque deve ser positivo")
            
            if valor > self.saldo:
                raise ValueError(f"Saldo insuficiente. Saldo atual: R${self.saldo:.2f}")
            
            self.saldo -= valor
            print(f"✓ Saque de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}")
            
        except (TypeError, ValueError) as e:
            print(f"✗ Erro ao sacar: {e}")
            raise
    
    def transferir(self, conta_destino, valor):
        """
        Transfere dinheiro para outra conta.
        
        Demonstra tratamento de exceções complexo.
        """
        try:
            # Validações
            if not isinstance(conta_destino, ContaBancaria):
                raise TypeError("Conta de destino inválida")
            
            if valor <= 0:
                raise ValueError("Valor da transferência deve ser positivo")
            
            if valor > self.saldo:
                raise ValueError(f"Saldo insuficiente para transferência")
            
            # Operação atômica (ou ambas funcionam ou nenhuma)
            self.saldo -= valor
            conta_destino.saldo += valor
            
            print(f"✓ Transferência de R${valor:.2f} realizada")
            print(f"  De: {self.titular} (Saldo: R${self.saldo:.2f})")
            print(f"  Para: {conta_destino.titular} (Saldo: R${conta_destino.saldo:.2f})")
            
        except (TypeError, ValueError) as e:
            print(f"✗ Erro na transferência: {e}")
            raise


# Testando
print("\nCriando contas:")
conta1 = ContaBancaria("Ana", 1000)
conta2 = ContaBancaria("Bruno", 500)

print("\nTestando validações:")
try:
    conta1.depositar(-100)
except ValueError:
    print("Erro tratado corretamente")

try:
    conta1.depositar("abc")
except TypeError:
    print("Erro tratado corretamente")

print("\nTransferindo:")
conta1.transferir(conta2, 200)


# ==========================================
# EXEMPLO 2: MANTER ESTADO CONSISTENTE
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Manter Estado Consistente")
print("=" * 60)

class CarrinhoCompras:
    """Carrinho que mantém estado consistente mesmo com erros."""
    
    def __init__(self):
        self.itens = {}  # {produto: quantidade}
        self.total = 0.0
    
    def adicionarItem(self, produto, quantidade, preco_unitario):
        """
        Adiciona item ao carrinho.
        
        Garante que o carrinho permanece consistente mesmo se houver erro.
        """
        try:
            if quantidade <= 0:
                raise ValueError("Quantidade deve ser positiva")
            
            if preco_unitario <= 0:
                raise ValueError("Preço deve ser positivo")
            
            # Calcula total antes de modificar
            novo_total = self.total + (quantidade * preco_unitario)
            
            # Atualiza estado de forma atômica
            if produto in self.itens:
                self.itens[produto] += quantidade
            else:
                self.itens[produto] = quantidade
            
            self.total = novo_total
            
            print(f"✓ {quantidade}x {produto} adicionado. Total: R${self.total:.2f}")
            
        except ValueError as e:
            print(f"✗ Erro ao adicionar item: {e}")
            # Estado permanece consistente (não foi modificado)
            raise
    
    def removerItem(self, produto, quantidade):
        """Remove item do carrinho com validação."""
        try:
            if produto not in self.itens:
                raise ValueError(f"Produto '{produto}' não está no carrinho")
            
            if quantidade > self.itens[produto]:
                raise ValueError(f"Quantidade maior que disponível no carrinho")
            
            # Operação segura
            self.itens[produto] -= quantidade
            if self.itens[produto] == 0:
                del self.itens[produto]
            
            print(f"✓ {quantidade}x {produto} removido")
            
        except ValueError as e:
            print(f"✗ Erro ao remover item: {e}")
            raise


# Testando
print("\nCriando carrinho:")
carrinho = CarrinhoCompras()

print("\nAdicionando itens:")
carrinho.adicionarItem("Notebook", 1, 2500.00)
carrinho.adicionarItem("Mouse", 2, 50.00)

print("\nTentando adicionar item inválido (estado mantém-se consistente):")
try:
    carrinho.adicionarItem("Teclado", -1, 100.00)
except ValueError:
    print("Estado do carrinho permaneceu consistente")
    print(f"Itens: {carrinho.itens}")


# ==========================================
# EXEMPLO 3: TRATAMENTO COM ROLLBACK
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Tratamento com Rollback")
print("=" * 60)

class BancoDadosSimulado:
    """Simula operações de banco de dados."""
    
    def __init__(self):
        self.registros = {}
        self._backup = None
    
    def iniciarTransacao(self):
        """Inicia transação (faz backup)."""
        self._backup = self.registros.copy()
        print("Transação iniciada")
    
    def inserir(self, chave, valor):
        """Insere registro."""
        self.registros[chave] = valor
        print(f"Registro inserido: {chave} = {valor}")
    
    def commit(self):
        """Confirma transação."""
        self._backup = None
        print("Transação confirmada")
    
    def rollback(self):
        """Desfaz transação."""
        if self._backup:
            self.registros = self._backup.copy()
            self._backup = None
            print("Transação revertida")


class Sistema:
    """Sistema que usa transações."""
    
    def processarDados(self, dados):
        """
        Processa dados com tratamento de exceções e rollback.
        
        Se houver erro, desfaz todas as operações.
        """
        db = BancoDadosSimulado()
        
        try:
            db.iniciarTransacao()
            
            # Processa múltiplos dados
            for chave, valor in dados.items():
                if not chave or not valor:
                    raise ValueError(f"Dado inválido: {chave}={valor}")
                
                db.inserir(chave, valor)
            
            db.commit()
            print("\n✓ Processamento concluído com sucesso")
            return db.registros
            
        except ValueError as e:
            print(f"\n✗ Erro no processamento: {e}")
            db.rollback()
            raise
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
            db.rollback()
            raise


# Testando
print("\nProcessando dados válidos:")
dados_validos = {"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
resultado = Sistema().processar_dados(dados_validos)
print(f"Registros: {resultado}")

print("\nProcessando dados inválidos (rollback automático):")
dados_invalidos = {"nome": "Bruno", "idade": "", "cidade": "Rio"}
try:
    Sistema().processar_dados(dados_invalidos)
except ValueError:
    print("Erro tratado e transação revertida")


# ==========================================
# EXEMPLO 4: TRATAMENTO COM LOGGING
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Tratamento com Logging")
print("=" * 60)

class SistemaLogging:
    """Sistema com tratamento de exceções e logging."""
    
    def __init__(self):
        self.log = []
    
    def registrarLog(self, mensagem):
        """Registra log."""
        self.log.append(mensagem)
        print(f"LOG: {mensagem}")
    
    def processarOperacao(self, operacao, dados):
        """
        Processa operação com tratamento completo.
        
        Registra sucessos e falhas.
        """
        try:
            self.registrarLog(f"Iniciando operação: {operacao}")
            
            # Validação
            if not dados:
                raise ValueError("Dados não podem ser vazios")
            
            # Processamento
            resultado = f"Processado: {operacao} com {len(dados)} itens"
            
            self.registrarLog(f"Operação {operacao} concluída com sucesso")
            return resultado
            
        except ValueError as e:
            self.registrarLog(f"Erro na operação {operacao}: {e}")
            raise
        except Exception as e:
            self.registrarLog(f"Erro inesperado em {operacao}: {e}")
            raise
        finally:
            self.registrarLog(f"Finalizando operação: {operacao}")


# Testando
print("\nCriando sistema com logging:")
sistema = SistemaLogging()

print("\nProcessando operação válida:")
resultado = sistema.processarOperacao("importar", {"a": 1, "b": 2})
print(f"Resultado: {resultado}")

print("\nProcessando operação inválida:")
try:
    sistema.processarOperacao("importar", {})
except ValueError:
    print("Erro tratado e logado")


# ==========================================
# BOAS PRÁTICAS
# ==========================================

print("\n" + "=" * 60)
print("BOAS PRÁTICAS PARA TRATAMENTO EM CLASSES")
print("=" * 60)

print("""
✓ Valide dados de entrada nos métodos
✓ Use exceções específicas quando possível
✓ Mantenha estado consistente mesmo com erros
✓ Use try-except-finally quando necessário
✓ Documente quais exceções cada método pode lançar
✓ Não ignore exceções sem razão
✓ Propague exceções quando apropriado
✓ Use finally para limpeza (fechar arquivos, etc.)
✓ Considere rollback para operações complexas
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE TRATAMENTO EM CLASSES")
print("=" * 60)

print("""
✓ Trate exceções dentro de métodos para validação
✓ Mantenha estado consistente mesmo com erros
✓ Use try-except para operações que podem falhar
✓ Documente exceções que métodos podem lançar
✓ Use finally para limpeza quando necessário
✓ Considere rollback para operações atômicas
✓ Propague exceções quando não puder tratar adequadamente
✓ Valide entrada antes de modificar estado
""")

