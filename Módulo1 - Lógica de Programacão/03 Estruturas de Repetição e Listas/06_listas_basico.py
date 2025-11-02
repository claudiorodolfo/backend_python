"""
06 - Listas Básicas

Este arquivo demonstra criação e acesso a listas em Python.
"""

print("=" * 60)
print("LISTAS - CRIAÇÃO E ACESSO")
print("=" * 60)

# ============================================
# CRIAR LISTAS
# ============================================
print("\n1. CRIAR LISTAS:")
print("-" * 60)

# Lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Lista com elementos
frutas = ["maçã", "banana", "laranja"]
print(f"Frutas: {frutas}")

# Lista com diferentes tipos
misturada = [1, "texto", 3.14, True]
print(f"Lista mista: {misturada}")

# ============================================
# ACESSAR ELEMENTOS (ÍNDICES)
# ============================================
print("\n2. ACESSAR ELEMENTOS POR ÍNDICE:")
print("-" * 60)

numeros = [10, 20, 30, 40, 50]
print(f"Lista: {numeros}")

# Índices começam em 0
print(f"\nÍndice 0: {numeros[0]}")
print(f"Índice 1: {numeros[1]}")
print(f"Índice 2: {numeros[2]}")

# Índices negativos (do final)
print(f"\nÍndice -1 (último): {numeros[-1]}")
print(f"Índice -2 (penúltimo): {numeros[-2]}")
print(f"Índice -3: {numeros[-3]}")

# ============================================
# MODIFICAR ELEMENTOS
# ============================================
print("\n3. MODIFICAR ELEMENTOS:")
print("-" * 60)

numeros = [10, 20, 30, 40, 50]
print(f"Antes: {numeros}")

numeros[1] = 25
numeros[-1] = 55

print(f"Depois: {numeros}")

# ============================================
# TAMANHO DA LISTA
# ============================================
print("\n4. TAMANHO DA LISTA (len()):")
print("-" * 60)

lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")
print(f"Tamanho: {len(lista)} elementos")

# ============================================
# ITERAR SOBRE LISTA
# ============================================
print("\n5. ITERAR SOBRE LISTA:")
print("-" * 60)

frutas = ["maçã", "banana", "laranja"]

print("Método 1 - Direto:")
for fruta in frutas:
    print(f"  {fruta}")

print("\nMétodo 2 - Com índice:")
for i in range(len(frutas)):
    print(f"  [{i}] {frutas[i]}")

print("\nMétodo 3 - Com enumerate:")
for i, fruta in enumerate(frutas):
    print(f"  [{i}] {fruta}")

# ============================================
# VERIFICAR SE ELEMENTO EXISTE
# ============================================
print("\n6. VERIFICAR SE ELEMENTO EXISTE:")
print("-" * 60)

frutas = ["maçã", "banana", "laranja"]
print(f"Lista: {frutas}")

print(f"\n'banana' está na lista? {'banana' in frutas}")
print(f"'uva' está na lista? {'uva' in frutas}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Lista de notas
print("\nExemplo 1: Lista de notas")
print("-" * 60)
notas = [8.5, 7.0, 9.2, 6.5, 8.0]
print(f"Notas: {notas}")

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.2f}")

# Exemplo 2: Acessar primeiro e último
print("\nExemplo 2: Primeiro e último elemento")
print("-" * 60)
lista = ["primeiro", "segundo", "terceiro", "último"]
print(f"Lista: {lista}")
print(f"Primeiro: {lista[0]}")
print(f"Último: {lista[-1]}")

# Exemplo 3: Modificar múltiplos elementos
print("\nExemplo 3: Modificar elementos")
print("-" * 60)
valores = [1, 2, 3, 4, 5]
print(f"Antes: {valores}")

valores[0] = 10
valores[2] = 30
valores[-1] = 50

print(f"Depois: {valores}")

