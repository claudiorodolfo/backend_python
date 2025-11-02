"""
Validação com Exceções em Classes

Usar exceções para validação permite criar código robusto
que detecta e trata erros de forma elegante.
"""

# ==========================================
# VALIDAÇÃO COM EXCEÇÕES
# ==========================================

print("=" * 60)
print("VALIDAÇÃO COM EXCEÇÕES")
print("=" * 60)

print("""
Exceções são ideais para validação porque:
  ✓ Forçam tratamento de erros
  ✓ Não permitem ignorar problemas
  ✓ Fornecem mensagens claras
  ✓ Permitem propagação controlada
  ✓ Interrompem fluxo quando necessário
""")


# ==========================================
# EXEMPLO 1: VALIDAÇÃO NO CONSTRUTOR
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Validação no Construtor")
print("=" * 60)

class EmailInvalidoError(Exception):
    """Exceção para email inválido."""
    pass


class Pessoa:
    """Pessoa com validação no construtor."""
    
    def __init__(self, nome, email, idade):
        """
        Construtor com validações.
        
        Lança exceções se dados forem inválidos.
        
        Raises:
            ValueError: Se nome estiver vazio
            EmailInvalidoError: Se email for inválido
            ValueError: Se idade for inválida
        """
        # Valida nome
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        
        # Valida email
        if "@" not in email or "." not in email:
            raise EmailInvalidoError(f"Email inválido: {email}")
        
        # Valida idade
        if not isinstance(idade, int):
            raise TypeError("Idade deve ser um número inteiro")
        
        if idade < 0 or idade > 150:
            raise ValueError(f"Idade inválida: {idade} (deve estar entre 0 e 150)")
        
        # Se chegou aqui, dados são válidos
        self.nome = nome.strip()
        self.email = email
        self.idade = idade
        print(f"✓ Pessoa {self.nome} criada com sucesso")
    
    def exibir_info(self):
        """Exibe informações da pessoa."""
        print(f"{self.nome} ({self.idade} anos) - {self.email}")


# Testando validação no construtor
print("\nCriando pessoas válidas:")
try:
    pessoa1 = Pessoa("Maria Silva", "maria@email.com", 25)
    pessoa1.exibir_info()
except (ValueError, EmailInvalidoError, TypeError) as e:
    print(f"Erro: {e}")

print("\nTestando validações:")
try:
    pessoa2 = Pessoa("", "joao@email.com", 30)  # Nome vazio
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    pessoa3 = Pessoa("João", "email_invalido", 30)  # Email inválido
except EmailInvalidoError as e:
    print(f"Erro capturado: {e}")

try:
    pessoa4 = Pessoa("Ana", "ana@email.com", -5)  # Idade inválida
except ValueError as e:
    print(f"Erro capturado: {e}")


# ==========================================
# EXEMPLO 2: VALIDAÇÃO EM PROPRIEDADES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Validação em Propriedades (@property)")
print("=" * 60)

class Produto:
    """Produto com validação em propriedades."""
    
    def __init__(self, nome, preco, estoque):
        self._nome = None
        self._preco = None
        self._estoque = None
        
        # Usa setters para validar
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    @property
    def nome(self):
        """Getter para nome."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Setter com validação."""
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Nome do produto não pode ser vazio")
        self._nome = valor.strip()
    
    @property
    def preco(self):
        """Getter para preço."""
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        """Setter com validação."""
        if not isinstance(valor, (int, float)):
            raise TypeError("Preço deve ser numérico")
        
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        
        self._preco = float(valor)
    
    @property
    def estoque(self):
        """Getter para estoque."""
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor):
        """Setter com validação."""
        if not isinstance(valor, int):
            raise TypeError("Estoque deve ser um número inteiro")
        
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        
        self._estoque = valor
    
    def exibir_info(self):
        """Exibe informações do produto."""
        print(f"{self.nome} - R${self.preco:.2f} - Estoque: {self.estoque}")


# Testando validação em propriedades
print("\nCriando produto válido:")
produto = Produto("Notebook", 2500.00, 5)
produto.exibir_info()

print("\nTestando validações em setters:")
try:
    produto.nome = ""  # Nome vazio
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    produto.preco = -100  # Preço negativo
except ValueError as e:
    print(f"Erro capturado: {e}")

try:
    produto.estoque = "abc"  # Estoque não numérico
except TypeError as e:
    print(f"Erro capturado: {e}")


# ==========================================
# EXEMPLO 3: VALIDAÇÃO COMPLEXA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Validação Complexa")
print("=" * 60)

class CPFInvalidoError(Exception):
    """Exceção para CPF inválido."""
    pass


class Cliente:
    """Cliente com validação complexa de CPF."""
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = None
        self.cpf = cpf  # Usa setter para validar
    
    @property
    def cpf(self):
        """Getter para CPF."""
        return self._cpf
    
    @cpf.setter
    def cpf(self, valor):
        """
        Setter com validação complexa de CPF.
        
        Valida formato e tamanho.
        """
        # Remove caracteres não numéricos
        cpf_limpo = ''.join(filter(str.isdigit, str(valor)))
        
        # Valida tamanho
        if len(cpf_limpo) != 11:
            raise CPFInvalidoError(f"CPF deve ter 11 dígitos. Recebido: {len(cpf_limpo)}")
        
        # Valida se não são todos iguais (ex: 111.111.111-11)
        if len(set(cpf_limpo)) == 1:
            raise CPFInvalidoError("CPF inválido: todos os dígitos são iguais")
        
        # Formata CPF (XXX.XXX.XXX-XX)
        self._cpf = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    
    def exibir_info(self):
        """Exibe informações do cliente."""
        print(f"{self.nome} - CPF: {self.cpf}")


# Testando validação complexa
print("\nCriando cliente com CPF válido:")
try:
    cliente1 = Cliente("Ana Silva", "12345678901")
    cliente1.exibir_info()
except CPFInvalidoError as e:
    print(f"Erro: {e}")

print("\nTestando CPFs inválidos:")
try:
    cliente2 = Cliente("João", "123")  # CPF muito curto
except CPFInvalidoError as e:
    print(f"Erro capturado: {e}")

try:
    cliente3 = Cliente("Maria", "11111111111")  # Todos iguais
except CPFInvalidoError as e:
    print(f"Erro capturado: {e}")

try:
    cliente4 = Cliente("Pedro", "123.456.789-00")  # Com formatação (OK)
    cliente4.exibir_info()
except CPFInvalidoError as e:
    print(f"Erro: {e}")


# ==========================================
# EXEMPLO 4: VALIDAÇÃO COM MÚLTIPLAS REGRAS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Validação com Múltiplas Regras")
print("=" * 60)

class SenhaInvalidaError(Exception):
    """Exceção para senha inválida."""
    
    def __init__(self, motivo):
        self.motivo = motivo
        super().__init__(f"Senha inválida: {motivo}")


class Usuario:
    """Usuário com validação complexa de senha."""
    
    def __init__(self, nome, senha):
        self.nome = nome
        self._senha = None
        self.definir_senha(senha)
    
    def definir_senha(self, senha):
        """
        Define senha com múltiplas validações.
        
        Regras:
          - Mínimo 8 caracteres
          - Pelo menos uma letra maiúscula
          - Pelo menos uma letra minúscula
          - Pelo menos um número
          - Pelo menos um caractere especial
        """
        erros = []
        
        # Valida comprimento
        if len(senha) < 8:
            erros.append("mínimo 8 caracteres")
        
        # Valida maiúscula
        if not any(c.isupper() for c in senha):
            erros.append("pelo menos uma letra maiúscula")
        
        # Valida minúscula
        if not any(c.islower() for c in senha):
            erros.append("pelo menos uma letra minúscula")
        
        # Valida número
        if not any(c.isdigit() for c in senha):
            erros.append("pelo menos um número")
        
        # Valida caractere especial
        especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in especiais for c in senha):
            erros.append("pelo menos um caractere especial")
        
        # Se houver erros, lança exceção
        if erros:
            raise SenhaInvalidaError(", ".join(erros))
        
        # Senha válida
        self._senha = senha
        print(f"✓ Senha definida para {self.nome}")
    
    def verificar_senha(self, senha):
        """Verifica se a senha está correta."""
        return senha == self._senha


# Testando validação de senha
print("\nTestando senhas:")
senhas_teste = [
    "Senha123!",      # Válida
    "curta",          # Muito curta
    "SEMNUMERO!",     # Sem número
    "semmaiuscula1!", # Sem maiúscula
    "SENHASEMN1!",    # Sem minúscula
    "SenhaSemEspecial1", # Sem caractere especial
]

for senha in senhas_teste:
    try:
        usuario = Usuario("Teste", senha)
        print(f"✓ '{senha}': Válida")
    except SenhaInvalidaError as e:
        print(f"✗ '{senha}': {e.motivo}")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE VALIDAÇÃO COM EXCEÇÕES")
print("=" * 60)

print("""
✓ Use exceções para validação em classes
✓ Valide no construtor para garantir objeto válido
✓ Use @property para validação em setters
✓ Crie exceções customizadas para erros específicos
✓ Valide múltiplas regras e agregue erros
✓ Forneça mensagens de erro claras e específicas
✓ Não permita criação de objetos em estado inválido
✓ Validação impede dados inconsistentes
""")

