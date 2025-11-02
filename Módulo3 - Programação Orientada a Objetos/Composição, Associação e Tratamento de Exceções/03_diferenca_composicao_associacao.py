"""
Diferença entre Composição e Associação

Este exemplo demonstra claramente a diferença entre
composição (relacionamento forte) e associação (relacionamento fraco).
"""

# ==========================================
# COMPARAÇÃO LADO A LADO
# ==========================================

print("=" * 60)
print("COMPOSIÇÃO vs ASSOCIAÇÃO")
print("=" * 60)

# ==========================================
# COMPOSIÇÃO: Carro e Motor
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: COMPOSIÇÃO - Carro TEM-UM Motor")
print("=" * 60)

class Motor:
    """Componente - Motor não existe sem carro."""
    
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"Motor {potencia}CV criado (dentro de um carro)")


class Carro:
    """
    COMPOSIÇÃO: Carro cria Motor dentro dele.
    
    Motor não faz sentido existir sem carro.
    """
    
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        # COMPOSIÇÃO: Motor criado DENTRO de Carro
        self.motor = Motor(potencia)
        print(f"Carro {modelo} criado com motor")


# Testando composição
print("\nCriando carro (motor é criado automaticamente):")
carro = Carro("Fusca", 40)

print(f"\nCarro: {carro.modelo}")
print(f"Motor: {carro.motor.potencia}CV")

print("\n❌ Motor não deveria existir sem carro:")
print("   motor = Motor(40)  # Não faz sentido!")


# ==========================================
# ASSOCIAÇÃO: Pessoa e Biblioteca
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: ASSOCIAÇÃO - Pessoa USA Biblioteca")
print("=" * 60)

class Pessoa:
    """Classe independente - pode existir sem biblioteca."""
    
    def __init__(self, nome):
        self.nome = nome
        print(f"Pessoa {nome} criada (independente)")


class Biblioteca:
    """Classe independente - pode existir sem pessoas."""
    
    def __init__(self, nome):
        self.nome = nome
        self.visitantes = []  # ASSOCIAÇÃO: lista de pessoas
        print(f"Biblioteca {nome} criada (independente)")
    
    def registrar_visitante(self, pessoa):
        """Associação: Biblioteca referencia Pessoa."""
        if pessoa not in self.visitantes:
            self.visitantes.append(pessoa)
            print(f"✓ {pessoa.nome} registrado(a)")


# Criando objetos independentes
print("\nCriando objetos independentemente:")
pessoa1 = Pessoa("Maria")
pessoa2 = Pessoa("João")
biblioteca = Biblioteca("Central")

print("\n✅ Pessoas existem sem biblioteca:")
print(f"   {pessoa1.nome} existe")
print(f"   {pessoa2.nome} existe")

print("\n✅ Biblioteca existe sem pessoas:")
print(f"   {biblioteca.nome} existe")

print("\nAssociação: Registrando pessoas na biblioteca")
biblioteca.registrar_visitante(pessoa1)
biblioteca.registrar_visitante(pessoa2)


# ==========================================
# TABELA COMPARATIVA
# ==========================================

print("\n" + "=" * 60)
print("TABELA COMPARATIVA")
print("=" * 60)

print("""
┌──────────────────────────────────────────────────────────┐
│ COMPOSIÇÃO                        │ ASSOCIAÇÃO            │
├──────────────────────────────────────────────────────────┤
│ Relacionamento FORTE             │ Relacionamento FRACO   │
│ "TEM-UM" obrigatório             │ "TEM-UM" opcional       │
│ Componente criado DENTRO         │ Objeto referenciado   │
│ Componente não existe sozinho    │ Objeto existe sozinho  │
│ Ciclo de vida compartilhado       │ Ciclo de vida separado│
│ Carro TEM Motor                  │ Pessoa USA Biblioteca  │
│ Computador TEM CPU                │ Professor TEM Alunos   │
│ Pessoa TEM Endereço               │ Departamento TEM Func  │
└──────────────────────────────────────────────────────────┘
""")


# ==========================================
# EXEMPLO 3: QUANDO USAR CADA UMA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Decisão: Composição ou Associação?")
print("=" * 60)

# Pergunta: Pessoa TEM Endereço ou USA Endereço?

print("""
Pergunta: Pessoa e Endereço - Composição ou Associação?

ANÁLISE:
  • Uma pessoa sempre tem um endereço? SIM → Composição
  • Endereço faz sentido sem pessoa? NÃO → Composição
  • Endereço é parte essencial de Pessoa? SIM → Composição

DECISÃO: COMPOSIÇÃO
""")


class Endereco:
    """Componente - Endereço não faz sentido sem pessoa."""
    
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade


class PessoaComEndereco:
    """
    COMPOSIÇÃO: Pessoa TEM-UM Endereço.
    
    Endereço é criado dentro de Pessoa.
    """
    
    def __init__(self, nome, rua, cidade):
        self.nome = nome
        # COMPOSIÇÃO: Endereço criado dentro
        self.endereco = Endereco(rua, cidade)
    
    def exibir_info(self):
        print(f"{self.nome} mora em {self.endereco.rua}, {self.endereco.cidade}")


print("\nCriando pessoa com endereço (composição):")
pessoa_end = PessoaComEndereco("Ana", "Rua A", "São Paulo")
pessoa_end.exibir_info()


# Pergunta: Funcionário e Empresa - Composição ou Associação?

print("""
Pergunta: Funcionário e Empresa - Composição ou Associação?

ANÁLISE:
  • Funcionário sempre tem empresa? NÃO → Associação
  • Funcionário pode existir sem empresa? SIM → Associação
  • Empresa é parte essencial de Funcionário? NÃO → Associação

DECISÃO: ASSOCIAÇÃO
""")


class Empresa:
    """Classe independente."""
    
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []


class Funcionario:
    """
    ASSOCIAÇÃO: Funcionário USA Empresa.
    
    Funcionário pode existir sem empresa (desempregado).
    """
    
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
        self.empresa = None  # Pode ser None (associação)
    
    def contratar_empresa(self, empresa):
        """Associação: Funcionário referencia Empresa."""
        self.empresa = empresa
        empresa.funcionarios.append(self)
    
    def exibir_info(self):
        emp_nome = self.empresa.nome if self.empresa else "Desempregado"
        print(f"{self.nome} ({self.cargo}) - Empresa: {emp_nome}")


print("\nCriando funcionário sem empresa (associação):")
func = Funcionario("Bruno", "Desenvolvedor")
func.exibir_info()

empresa = Empresa("Tech Corp")
func.contratar_empresa(empresa)
func.exibir_info()


# ==========================================
# REGRA PRÁTICA
# ==========================================

print("\n" + "=" * 60)
print("REGRA PRÁTICA PARA DECIDIR")
print("=" * 60)

print("""
Faça a pergunta:

"O objeto B pode existir sem o objeto A?"

  • NÃO → COMPOSIÇÃO (A cria B dentro dele)
  • SIM → ASSOCIAÇÃO (A referencia B)

EXEMPLOS:

  Carro e Motor:
    Motor pode existir sem Carro? NÃO → Composição ✓

  Pessoa e Biblioteca:
    Pessoa pode existir sem Biblioteca? SIM → Associação ✓
    Biblioteca pode existir sem Pessoa? SIM → Associação ✓

  Computador e CPU:
    CPU pode existir sem Computador? NÃO → Composição ✓

  Professor e Aluno:
    Professor pode existir sem Aluno? SIM → Associação ✓
    Aluno pode existir sem Professor? SIM → Associação ✓
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO: COMPOSIÇÃO vs ASSOCIAÇÃO")
print("=" * 60)

print("""
COMPOSIÇÃO:
  ✓ "TEM-UM" obrigatório e forte
  ✓ Componente criado dentro
  ✓ Não pode existir separadamente
  ✓ Ciclo de vida compartilhado
  ✓ Use: Carro-Motor, Pessoa-Endereço, Computador-CPU

ASSOCIAÇÃO:
  ✓ "TEM-UM" opcional ou "USA"
  ✓ Objeto referenciado
  ✓ Pode existir separadamente
  ✓ Ciclo de vida independente
  ✓ Use: Pessoa-Biblioteca, Professor-Aluno, Funcionário-Empresa

PERGUNTA-CHAVE:
  "O objeto B pode existir sem A?"
  NÃO → Composição | SIM → Associação
""")

