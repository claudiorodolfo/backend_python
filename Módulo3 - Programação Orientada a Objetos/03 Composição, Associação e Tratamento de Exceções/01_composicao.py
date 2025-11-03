"""
Composição

Composição é um relacionamento forte onde uma classe CONTÉM outra
classe como parte essencial. O objeto composto não pode existir sem o componente.
"""

# ==========================================
# CONCEITO DE COMPOSIÇÃO
# ==========================================

print("=" * 60)
print("COMPOSIÇÃO")
print("=" * 60)

print("""
COMPOSIÇÃO:
  • Relacionamento "TEM-UM" FORTE
  • O objeto composto POSSUI o componente
  • Componente não existe independentemente
  • Ciclo de vida compartilhado

Características:
  ✓ Componente dependente é criado dentro do componente composto
  ✓ Componente dependente não faz sentido sozinho
  ✓ Quando o componente composto é destruído, o componente depend  ente também é
""")


# ==========================================
# EXEMPLO 1: COMPOSIÇÃO BÁSICA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Composição Básica - Carro e Motor")
print("=" * 60)

class Motor:
    """Componente - Motor de um carro."""
    
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"Motor {self.potencia}CV ligado")
        else:
            print("Motor já está ligado")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Motor desligado")
        else:
            print("Motor já está desligado")


class Carro:
    """
    Classe composta - Carro possui Motor.
    
    Composição: Carro TEM-UM Motor como parte essencial.
    Sem motor, não há carro.
    """
    
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        # COMPOSIÇÃO: Motor é criado dentro de Carro
        self.motor = Motor(potencia_motor)  # Motor não existe sem Carro
    
    def ligar(self):
        """Liga o carro (que liga o motor)."""
        print(f"{self.modelo}:")
        self.motor.ligar()
    
    def desligar(self):
        """Desliga o carro (que desliga o motor)."""
        print(f"{self.modelo}:")
        self.motor.desligar()
    
    def exibirInfo(self):
        """Exibe informações do carro."""
        print(f"""
        Modelo: {self.modelo}
        Motor: {self.motor.potencia}CV
        Motor Ligado: {self.motor.ligado}
        """)


# Testando composição
print("\nCriando carro (com motor):")
carro = Carro("Fusca", 40)
carro.exibirInfo()

print("\nLigando carro (liga o motor):")
carro.ligar()

print("\nDesligando carro:")
carro.desligar()

# Note: Motor não existe independentemente do carro
# Não faz sentido criar: motor = Motor(40) sem um carro


# ==========================================
# EXEMPLO 2: COMPOSIÇÃO COM MÚLTIPLOS COMPONENTES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Composição Múltipla - Computador")
print("=" * 60)

class CPU:
    """Componente: CPU do computador."""
    
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    
    def processar(self):
        print(f"CPU {self.modelo} processando...")


class Memoria:
    """Componente: Memória do computador."""
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
    
    def armazenar(self, dado):
        print(f"Armazenando {dado} em {self.capacidade}GB de memória")


class Disco:
    """Componente: Disco do computador."""
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
    
    def salvar(self, arquivo):
        print(f"Salvando {arquivo} no disco {self.capacidade}GB")


class Computador:
    """
    Classe composta - Computador possui CPU, Memória e Disco.
    
    Composição: Computador não pode existir sem esses componentes.
    """
    
    def __init__(self, modelo_cpu, velocidade_cpu, capacidade_memoria, capacidade_disco):
        self.modelo = "PC"
        # COMPOSIÇÃO: Componentes criados dentro de Computador
        self.cpu = CPU(modelo_cpu, velocidade_cpu)
        self.memoria = Memoria(capacidade_memoria)
        self.disco = Disco(capacidade_disco)
    
    def executarTarefa(self):
        """Usa os componentes para executar tarefa."""
        print(f"\n{self.modelo} executando tarefa:")
        self.cpu.processar()
        self.memoria.armazenar("dados")
        self.disco.salvar("arquivo.txt")
    
    def exibirEspecificacoes(self):
        """Exibe especificações do computador."""
        print(f"""
        {'=' * 50}
        Computador: {self.modelo}
        CPU: {self.cpu.modelo} ({self.cpu.velocidade}GHz)
        Memória: {self.memoria.capacidade}GB
        Disco: {self.disco.capacidade}GB
        {'=' * 50}
        """)


# Testando
print("\nCriando computador (com componentes):")
pc = Computador("Intel i7", 3.5, 16, 500)
pc.exibirEspecificacoes()
pc.executarTarefa()


# ==========================================
# EXEMPLO 3: COMPOSIÇÃO EM HIERARQUIA
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Composição em Hierarquia")
print("=" * 60)

class Endereco:
    """Componente: Endereço."""
    
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
    
    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"


class Contato:
    """Componente: Informações de contato."""
    
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email
    
    def __str__(self):
        return f"Tel: {self.telefone}, Email: {self.email}"


class Pessoa:
    """
    Classe composta - Pessoa possui Endereco e Contato.
    
    Composição: Pessoa não faz sentido sem endereço e contato.
    """
    
    def __init__(self, nome, rua, numero, cidade, telefone, email):
        self.nome = nome
        # COMPOSIÇÃO: Componentes criados dentro de Pessoa
        self.endereco = Endereco(rua, numero, cidade)
        self.contato = Contato(telefone, email)
    
    def exibirInfo(self):
        """Exibe informações da pessoa."""
        print(f"""
        {'=' * 50}
        Nome: {self.nome}
        Endereço: {self.endereco}
        Contato: {self.contato}
        {'=' * 50}
        """)


# Testando
print("\nCriando pessoa (com endereço e contato):")
pessoa = Pessoa(
    "Maria Silva",
    "Rua das Flores",
    123,
    "São Paulo",
    "(11) 99999-9999",
    "maria@email.com"
)
pessoa.exibirInfo()


# ==========================================
# EXEMPLO 4: COMPOSIÇÃO COM LISTA DE COMPONENTES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Composição com Lista")
print("=" * 60)

class Livro:
    """Componente: Livro."""
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Biblioteca:
    """
    Classe composta - Biblioteca possui lista de Livros.
    
    Composição: Os livros fazem parte da biblioteca.
    Quando biblioteca é destruída, os livros também são (neste exemplo).
    """
    
    def __init__(self, nome):
        self.nome = nome
        # COMPOSIÇÃO: Lista de componentes
        self.livros = []
    
    def adicionarLivro(self, titulo, autor):
        """Adiciona livro à biblioteca (cria o componente)."""
        livro = Livro(titulo, autor)  # Criado dentro da biblioteca
        self.livros.append(livro)
        print(f"✓ '{titulo}' adicionado à biblioteca")
    
    def listarLivros(self):
        """Lista todos os livros."""
        print(f"\nLivros na {self.nome}:")
        for i, livro in enumerate(self.livros, 1):
            print(f"  {i}. {livro}")
    
    def exibirInfo(self):
        """Exibe informações da biblioteca."""
        print(f"""
        {'=' * 50}
        Biblioteca: {self.nome}
        Total de Livros: {len(self.livros)}
        {'=' * 50}
        """)


# Testando
print("\nCriando biblioteca:")
biblioteca = Biblioteca("Biblioteca Central")

print("\nAdicionando livros (composição):")
biblioteca.adicionarLivro("1984", "George Orwell")
biblioteca.adicionarLivro("Dom Casmurro", "Machado de Assis")
biblioteca.adicionarLivro("O Senhor dos Anéis", "J.R.R. Tolkien")

biblioteca.exibirInfo()
biblioteca.listarLivros()


# ==========================================
# CARACTERÍSTICAS DA COMPOSIÇÃO
# ==========================================

print("\n" + "=" * 60)
print("CARACTERÍSTICAS DA COMPOSIÇÃO")
print("=" * 60)

print("""
✓ Componente é criado DENTRO da classe composta
✓ Componente não faz sentido existir sozinho
✓ Relacionamento FORTE - "possui" ou "tem"
✓ Ciclo de vida compartilhado
✓ Componente não é compartilhado entre objetos
✓ Exemplos: Carro TEM Motor, Computador TEM CPU

DIFERENÇA DE ASSOCIAÇÃO:
  • Composição: "TEM-UM" forte (não pode viver sem)
  • Associação: "TEM-UM" fraco ou "USA" (pode viver sem)
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE COMPOSIÇÃO")
print("=" * 60)

print("""
✓ Composição = relacionamento forte "TEM-UM"
✓ Componente criado dentro do composto
✓ Componente não existe independentemente
✓ Ciclo de vida compartilhado
✓ Use quando objeto não faz sentido sem o componente
✓ Exemplos: Carro-Motor, Computador-CPU, Pessoa-Endereço
""")

