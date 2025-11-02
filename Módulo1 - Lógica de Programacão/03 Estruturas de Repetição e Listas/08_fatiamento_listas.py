"""
08 - Fatiamento de Listas (Slicing)

Este arquivo demonstra o uso de fatiamento (slicing) em listas.
"""

print("=" * 60)
print("FATIAMENTO DE LISTAS (SLICING)")
print("=" * 60)

# ============================================
# FATIAMENTO BÁSICO
# ============================================
print("\n1. FATIAMENTO BÁSICO [inicio:fim]:")
print("-" * 60)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista completa: {numeros}")

print(f"\n[0:5]: {numeros[0:5]}")  # Elementos de 0 a 4
print(f"[2:7]: {numeros[2:7]}")  # Elementos de 2 a 6
print(f"[1:4]: {numeros[1:4]}")  # Elementos de 1 a 3

# ============================================
# FATIAMENTO COM OMISSÃO
# ============================================
print("\n2. FATIAMENTO COM OMISSÃO:")
print("-" * 60)

numeros = [0, 1, 2, 3, 4, 5]
print(f"Lista: {numeros}")

print(f"\n[:3]: {numeros[:3]}")      # Do início até índice 2
print(f"[3:]: {numeros[3:]}")      # Do índice 3 até o final
print(f"[:]: {numeros[:]}")        # Lista completa (cópia)

# ============================================
# FATIAMENTO COM PASSO
# ============================================
print("\n3. FATIAMENTO COM PASSO [inicio:fim:passo]:")
print("-" * 60)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista: {numeros}")

print(f"\n[::2]: {numeros[::2]}")      # Do início ao fim, passo 2
print(f"[1::2]: {numeros[1::2]}")     # Do índice 1, passo 2
print(f"[::3]: {numeros[::3]}")       # Passo 3

# ============================================
# FATIAMENTO REVERSO
# ============================================
print("\n4. FATIAMENTO REVERSO:")
print("-" * 60)

numeros = [0, 1, 2, 3, 4, 5]
print(f"Lista: {numeros}")

print(f"\n[::-1]: {numeros[::-1]}")    # Lista invertida
print(f"[::-2]: {numeros[::-2]}")     # Invertido, passo 2

# ============================================
# ÍNDICES NEGATIVOS NO FATIAMENTO
# ============================================
print("\n5. ÍNDICES NEGATIVOS:")
print("-" * 60)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista: {numeros}")

print(f"\n[-5:]: {numeros[-5:]}")      # Últimos 5 elementos
print(f"[:-3]: {numeros[:-3]}")       # Todos exceto últimos 3
print(f"[-5:-2]: {numeros[-5:-2]}")   # Do -5 ao -3

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Primeiros e últimos elementos
print("\nExemplo 1: Primeiros e últimos")
print("-" * 60)
lista = [10, 20, 30, 40, 50, 60]
print(f"Lista: {lista}")

print(f"Primeiros 3: {lista[:3]}")
print(f"Últimos 3: {lista[-3:]}")

# Exemplo 2: Elementos do meio
print("\nExemplo 2: Elementos do meio")
print("-" * 60)
lista = [10, 20, 30, 40, 50, 60, 70]
print(f"Lista: {lista}")
print(f"Elementos do meio [2:5]: {lista[2:5]}")

# Exemplo 3: Extrair todos os pares
print("\nExemplo 3: Elementos em posições pares")
print("-" * 60)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista: {lista}")
print(f"Posições pares [::2]: {lista[::2]}")

# Exemplo 4: Inverter lista
print("\nExemplo 4: Inverter lista")
print("-" * 60)
original = [1, 2, 3, 4, 5]
print(f"Original: {original}")
invertida = original[::-1]
print(f"Invertida: {invertida}")

