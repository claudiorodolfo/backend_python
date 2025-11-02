"""
03 - Formatação de Strings

Este arquivo demonstra formatação de strings.
"""

print("=" * 60)
print("FORMATAÇÃO DE STRINGS")
print("=" * 60)

# ============================================
# F-STRINGS (RECOMENDADO)
# ============================================
print("\n1. F-STRINGS (f'...'):")
print("-" * 60)

nome = "João"
idade = 25
print(f"Nome: {nome}, Idade: {idade}")

# Formatação de números
preco = 19.99
print(f"Preço: R$ {preco:.2f}")

# Expressões dentro de f-strings
print(f"Idade daqui 5 anos: {idade + 5}")

# ============================================
# .FORMAT()
# ============================================
print("\n2. .FORMAT():")
print("-" * 60)

print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))
print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))

# ============================================
# FORMATAÇÃO DE NÚMEROS
# ============================================
print("\n3. FORMATAÇÃO DE NÚMEROS:")
print("-" * 60)

numero = 1234.5678

print(f"Original: {numero}")
print(f".2f: {numero:.2f}")
print(f",.2f: {numero:,.2f}")
print(f":10.2f: {numero:10.2f}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo: Relatório formatado
print("\nExemplo: Relatório formatado")
print("-" * 60)
nome = "Maria"
salario = 5000.75
desconto = 750.50

print(f"Nome: {nome}")
print(f"Salário: R$ {salario:,.2f}")
print(f"Desconto: R$ {desconto:,.2f}")
print(f"Líquido: R$ {salario - desconto:,.2f}")

