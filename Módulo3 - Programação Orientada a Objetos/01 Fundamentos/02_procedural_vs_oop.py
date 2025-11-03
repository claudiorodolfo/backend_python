"""
Comparação: Programação Procedural vs Orientada a Objetos

Este exemplo mostra o mesmo problema resolvido de duas formas:
1. Programação Procedural (baseada em funções)
2. Programação Orientada a Objetos (baseada em classes)
"""

# ==========================================
# PROBLEMA: Gerenciar informações de carros
# ==========================================

print("=" * 60)
print("PROBLEMA: Gerenciar um sistema de carros")
print("=" * 60)

# ==========================================
# SOLUÇÃO 1: PROGRAMACAO PROCEDURAL
# ==========================================

print("\n" + "=" * 60)
print("ABORDAGEM PROCEDURAL")
print("=" * 60)


# Funções que operam sobre dados separados
def criar_carro(modelo, ano, cor, quilometragem=0):
    """Cria um dicionário representando um carro."""
    return {
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "quilometragem": quilometragem
    }


def dirigir_carro(carro, km):
    """Aumenta a quilometragem do carro."""
    carro["quilometragem"] += km
    print(f"{carro['modelo']} rodou {km} km. Total: {carro['quilometragem']} km")


def calcular_idade_carro(carro, ano_atual):
    """Calcula a idade do carro."""
    idade = ano_atual - carro["ano"]
    print(f"{carro['modelo']} tem {idade} anos")
    return idade


def exibir_info_carro(carro):
    """Exibe informações do carro."""
    print(f"""
    Modelo: {carro['modelo']}
    Ano: {carro['ano']}
    Cor: {carro['cor']}
    Quilometragem: {carro['quilometragem']} km
    """)


# Uso da abordagem procedural
carro1_procedural = criar_carro("Fusca", 1975, "Azul")
dirigir_carro(carro1_procedural, 100)
calcular_idade_carro(carro1_procedural, 2024)
exibir_info_carro(carro1_procedural)


# ==========================================
# SOLUÇÃO 2: PROGRAMACAO ORIENTADA A OBJETOS
# ==========================================

print("\n" + "=" * 60)
print("ABORDAGEM ORIENTADA A OBJETOS")
print("=" * 60)


class Carro:
    """
    Representa um carro no sistema.
    
    Agrupa dados (atributos) e comportamentos (métodos)
    relacionados em uma única unidade.
    """
    
    def __init__(self, modelo, ano, cor, quilometragem=0):
        """
        Construtor: inicializa os atributos do carro.
        
        Args:
            modelo: Modelo do carro (ex: "Fusca")
            ano: Ano de fabricação
            cor: Cor do carro
            quilometragem: Quilometragem inicial (padrão: 0)
        """
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
    
    def dirigir(self, km):
        """
        Simula o carro dirigindo, aumentando a quilometragem.
        
        Args:
            km: Quantidade de quilômetros percorridos
        """
        self.quilometragem += km
        print(f"{self.modelo} rodou {km} km. Total: {self.quilometragem} km")
    
    def calcularIdade(self, ano_atual):
        """
        Calcula a idade do carro.
        
        Args:
            ano_atual: Ano atual para cálculo
        
        Returns:
            Idade do carro em anos
        """
        idade = ano_atual - self.ano
        print(f"{self.modelo} tem {idade} anos")
        return idade
    
    def exibirInfo(self):
        """Exibe todas as informações do carro."""
        print(f"""
    Modelo: {self.modelo}
    Ano: {self.ano}
    Cor: {self.cor}
    Quilometragem: {self.quilometragem} km
    """)


# Uso da abordagem orientada a objetos
carro1_oop = Carro("Fusca", 1975, "Azul")
carro1_oop.dirigir(100)
carro1_oop.calcularIdade(2024)
carro1_oop.exibirInfo()


# ==========================================
# COMPARAÇÃO DETALHADA
# ==========================================

print("\n" + "=" * 60)
print("COMPARAÇÃO: PROCEDURAL vs OOP")
print("=" * 60)

print("""
┌─────────────────────────────────────────────────┐
│ PROCEDURAL                                      │
├─────────────────────────────────────────────────┤
│ • Dados e funções separados                     │
│ • Precisa passar dados como parâmetros          │
│ • Dificulta organização em projetos grandes     │
│ • Exemplo:                                       │
│   dirigir_carro(carro1, 100)                    │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ ORIENTADO A OBJETOS                             │
├─────────────────────────────────────────────────┤
│ • Dados e métodos agrupados na classe           │
│ • Dados já estão no objeto (self)               │
│ • Melhor organização e escalabilidade           │
│ • Exemplo:                                       │
│   carro1.dirigir(100)                           │
└─────────────────────────────────────────────────┘
""")


# ==========================================
# EXEMPLO: MÚLTIPLOS CARROS
# ==========================================

print("\n" + "=" * 60)
print("VANTAGEM: MÚLTIPLOS OBJETOS")
print("=" * 60)

# Criando múltiplos carros facilmente
carro2 = Carro("Gol", 2020, "Vermelho")
carro3 = Carro("Civic", 2018, "Preto", 50000)

print("\nFrota de carros:")
carro2.exibirInfo()
carro3.exibirInfo()

print("\nCada carro pode realizar ações independentes:")
carro2.dirigir(50)
carro3.dirigir(200)

print("\nEstado atual:")
carro2.exibirInfo()
carro3.exibirInfo()


# ==========================================
# CONCLUSÃO
# ==========================================

print("\n" + "=" * 60)
print("QUANDO USAR CADA ABORDAGEM")
print("=" * 60)

print("""
PROCEDURAL:
✓ Programas simples e lineares
✓ Scripts pequenos
✓ Quando não há necessidade de organização complexa

ORIENTADO A OBJETOS:
✓ Projetos grandes e complexos
✓ Quando precisa modelar entidades do mundo real
✓ Quando há necessidade de reutilização de código
✓ Quando múltiplos objetos compartilham comportamentos
✓ Backend, APIs, sistemas empresariais
""")

