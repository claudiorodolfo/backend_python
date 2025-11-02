"""
03 - Funções Básicas

Este arquivo demonstra definição e chamada de funções.
"""

print("=" * 60)
print("FUNÇÕES - DEFINIÇÃO E CHAMADA")
print("=" * 60)

# ============================================
# FUNÇÃO SIMPLES
# ============================================
print("\n1. FUNÇÃO SIMPLES:")
print("-" * 60)

def cumprimentar():
    """Função que exibe cumprimento"""
    print("  Olá! Bem-vindo!")

print("Definindo função cumprimentar():")
print("Chamando função:")
cumprimentar()

# ============================================
# FUNÇÃO COM PARÂMETROS
# ============================================
print("\n2. FUNÇÃO COM PARÂMETROS:")
print("-" * 60)

def cumprimentar_nome(nome):
    """Cumprimenta uma pessoa pelo nome"""
    print(f"  Olá, {nome}!")

print("Chamando função:")
cumprimentar_nome("João")
cumprimentar_nome("Maria")

# ============================================
# FUNÇÃO COM MÚLTIPLOS PARÂMETROS
# ============================================
print("\n3. FUNÇÃO COM MÚLTIPLOS PARÂMETROS:")
print("-" * 60)

def apresentar(nome, idade):
    """Apresenta pessoa com nome e idade"""
    print(f"  {nome} tem {idade} anos")

print("Chamando função:")
apresentar("Carlos", 30)

# ============================================
# FUNÇÃO COM RETORNO
# ============================================
print("\n4. FUNÇÃO COM RETORNO:")
print("-" * 60)

def somar(a, b):
    """Soma dois números"""
    resultado = a + b
    return resultado

resultado = somar(10, 5)
print(f"somar(10, 5) = {resultado}")

# ============================================
# FUNÇÃO COM VALOR PADRÃO
# ============================================
print("\n5. FUNÇÃO COM VALOR PADRÃO:")
print("-" * 60)

def cumprimentar(nome, saudacao="Olá"):
    """Cumprimenta com saudação customizada"""
    print(f"  {saudacao}, {nome}!")

print("Chamando com parâmetro:")
cumprimentar("João", "Oi")

print("\nChamando sem parâmetro (usa padrão):")
cumprimentar("Maria")

# ============================================
# FUNÇÃO SEM RETORNO
# ============================================
print("\n6. FUNÇÃO SEM RETORNO:")
print("-" * 60)

def exibir_info(nome, idade):
    """Apenas exibe informações"""
    print(f"  Nome: {nome}, Idade: {idade}")

resultado = exibir_info("Ana", 25)
print(f"  Retorno da função: {resultado} (None)")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Calcular área
print("\nExemplo 1: Calcular área do retângulo")
print("-" * 60)

def calcular_area(largura, altura):
    """Calcula área de um retângulo"""
    return largura * altura

area = calcular_area(10, 5)
print(f"Área de 10 × 5 = {area}")

# Exemplo 2: Verificar maioridade
print("\nExemplo 2: Verificar maioridade")
print("-" * 60)

def eh_maior_idade(idade):
    """Verifica se é maior de idade"""
    return idade >= 18

print(f"Idade 20: {eh_maior_idade(20)}")
print(f"Idade 15: {eh_maior_idade(15)}")

