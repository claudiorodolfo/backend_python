"""
07 - Métodos de Listas

Este arquivo demonstra métodos append(), insert() e remove() das listas.
"""

print("=" * 60)
print("MÉTODOS DE LISTAS")
print("=" * 60)

# ============================================
# APPEND() - Adicionar ao final
# ============================================
print("\n1. APPEND() - Adicionar ao final:")
print("-" * 60)

frutas = ["maçã", "banana"]
print(f"Antes: {frutas}")

frutas.append("laranja")
print(f"Após append('laranja'): {frutas}")

frutas.append("uva")
print(f"Após append('uva'): {frutas}")

# ============================================
# INSERT() - Inserir em posição específica
# ============================================
print("\n2. INSERT() - Inserir em posição:")
print("-" * 60)

frutas = ["maçã", "banana", "uva"]
print(f"Antes: {frutas}")

frutas.insert(1, "laranja")  # Insere na posição 1
print(f"Após insert(1, 'laranja'): {frutas}")

frutas.insert(0, "mamão")  # Insere no início
print(f"Após insert(0, 'mamão'): {frutas}")

# ============================================
# REMOVE() - Remover elemento
# ============================================
print("\n3. REMOVE() - Remover elemento:")
print("-" * 60)

frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Antes: {frutas}")

frutas.remove("banana")
print(f"Após remove('banana'): {frutas}")

# ============================================
# OUTROS MÉTODOS ÚTEIS
# ============================================
print("\n4. OUTROS MÉTODOS ÚTEIS:")
print("-" * 60)

# POP() - Remove e retorna último elemento
numeros = [10, 20, 30, 40]
print(f"Lista: {numeros}")
ultimo = numeros.pop()
print(f"pop(): removeu {ultimo}")
print(f"Lista após pop(): {numeros}")

# COUNT() - Contar ocorrências
lista = [1, 2, 2, 3, 2, 4]
print(f"\nLista: {lista}")
print(f"count(2): {lista.count(2)}")

# INDEX() - Encontrar índice
frutas = ["maçã", "banana", "laranja"]
print(f"\nLista: {frutas}")
print(f"index('banana'): {frutas.index('banana')}")

# REVERSE() - Inverter ordem
lista = [1, 2, 3, 4]
print(f"\nAntes reverse(): {lista}")
lista.reverse()
print(f"Depois reverse(): {lista}")

# SORT() - Ordenar
numeros = [30, 10, 40, 20]
print(f"\nAntes sort(): {numeros}")
numeros.sort()
print(f"Depois sort(): {numeros}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Construir lista dinamicamente
print("\nExemplo 1: Construir lista")
print("-" * 60)
notas = []
print(f"Lista inicial: {notas}")

notas.append(8.5)
notas.append(7.0)
notas.append(9.2)
print(f"Após adicionar notas: {notas}")

# Exemplo 2: Inserir em ordem
print("\nExemplo 2: Inserir em ordem")
print("-" * 60)
numeros = [10, 20, 40, 50]
print(f"Antes: {numeros}")

# Inserir 30 entre 20 e 40
numeros.insert(2, 30)
print(f"Depois: {numeros}")

# Exemplo 3: Remover duplicatas
print("\nExemplo 3: Remover elementos")
print("-" * 60)
lista = [1, 2, 2, 3, 2, 4]
print(f"Antes: {lista}")

# Remove primeira ocorrência de 2
lista.remove(2)
print(f"Depois remove(2): {lista}")

