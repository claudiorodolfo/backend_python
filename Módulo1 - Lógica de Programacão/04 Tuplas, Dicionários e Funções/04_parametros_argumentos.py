"""
04 - Parâmetros e Argumentos

Este arquivo demonstra diferentes tipos de parâmetros e argumentos.
"""

print("=" * 60)
print("PARÂMETROS E ARGUMENTOS")
print("=" * 60)

# ============================================
# ARGUMENTOS POSICIONAIS
# ============================================
print("\n1. ARGUMENTOS POSICIONAIS:")
print("-" * 60)

def apresentar(nome, idade, cidade):
    """Apresenta pessoa"""
    print(f"  {nome}, {idade} anos, de {cidade}")

print("Chamada com argumentos posicionais:")
apresentar("João", 25, "São Paulo")

# ============================================
# ARGUMENTOS NOMEADOS
# ============================================
print("\n2. ARGUMENTOS NOMEADOS:")
print("-" * 60)

print("Chamada com argumentos nomeados:")
apresentar(nome="Maria", idade=30, cidade="Rio de Janeiro")

# Misturado (posicionais primeiro, depois nomeados)
print("\nMisturando posicionais e nomeados:")
apresentar("Carlos", idade=28, cidade="Belo Horizonte")

# ============================================
# VALORES PADRÃO
# ============================================
print("\n3. VALORES PADRÃO:")
print("-" * 60)

def cumprimentar(nome, saudacao="Olá", pontuacao="!"):
    """Cumprimenta com parâmetros opcionais"""
    print(f"  {saudacao}, {nome}{pontuacao}")

print("Todos os parâmetros:")
cumprimentar("João", "Oi", "!!!")

print("\nApenas nome (usa padrões):")
cumprimentar("Maria")

print("\nNome e saudação:")
cumprimentar("Carlos", "Bom dia")

# ============================================
# MÚLTIPLOS ARGUMENTOS
# ============================================
print("\n4. ARGUMENTOS VARIÁVEIS (*args):")
print("-" * 60)

def somar(*numeros):
    """Soma números variáveis"""
    total = 0
    for num in numeros:
        total += num
    return total

print(f"somar(1, 2, 3) = {somar(1, 2, 3)}")
print(f"somar(10, 20, 30, 40) = {somar(10, 20, 30, 40)}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo: Calcular desconto
print("\nExemplo: Função com parâmetros opcionais")
print("-" * 60)

def calcular_preco_final(valor, desconto=0, taxa=0):
    """Calcula preço final com desconto e taxa"""
    valor_com_desconto = valor * (1 - desconto)
    valor_final = valor_com_desconto * (1 + taxa)
    return valor_final

preco = 100.00
print(f"Preço: R$ {preco:.2f}")
print(f"Sem desconto/taxa: R$ {calcular_preco_final(preco):.2f}")
print(f"Com 10% desconto: R$ {calcular_preco_final(preco, desconto=0.10):.2f}")
print(f"Com 5% taxa: R$ {calcular_preco_final(preco, taxa=0.05):.2f}")

