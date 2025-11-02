"""
01 - Tuplas

Este arquivo demonstra o uso de tuplas em Python.
"""

print("=" * 60)
print("TUPLAS")
print("=" * 60)

# ============================================
# CRIAR TUPLAS
# ============================================
print("\n1. CRIAR TUPLAS:")
print("-" * 60)

# Tupla com parênteses
tupla1 = (1, 2, 3, 4, 5)
print(f"Tupla com parênteses: {tupla1}")

# Tupla sem parênteses (vírgulas definem tupla)
tupla2 = 10, 20, 30
print(f"Tupla sem parênteses: {tupla2}")

# Tupla de um elemento (precisa vírgula)
tupla3 = (42,)
print(f"Tupla de um elemento: {tupla3}, tipo: {type(tupla3)}")

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")

# ============================================
# ACESSAR ELEMENTOS
# ============================================
print("\n2. ACESSAR ELEMENTOS:")
print("-" * 60)

coordenadas = (10, 20, 30)
print(f"Tupla: {coordenadas}")

print(f"coordenadas[0]: {coordenadas[0]}")
print(f"coordenadas[1]: {coordenadas[1]}")
print(f"coordenadas[-1]: {coordenadas[-1]}")

# ============================================
# TUPLAS SÃO IMUTÁVEIS
# ============================================
print("\n3. TUPLAS SÃO IMUTÁVEIS:")
print("-" * 60)

tupla = (1, 2, 3)
print(f"Tupla original: {tupla}")

print("\n⚠️  Não é possível modificar tupla:")
print("  tupla[0] = 10  # ❌ TypeError!")

print("\nMas podemos criar nova tupla:")
nova_tupla = (10, 2, 3)
print(f"  Nova tupla: {nova_tupla}")

# ============================================
# DESEMPACOTAMENTO
# ============================================
print("\n4. DESEMPACOTAMENTO:")
print("-" * 60)

ponto = (5, 10)
x, y = ponto
print(f"Tupla: {ponto}")
print(f"x = {x}, y = {y}")

# Múltiplos valores
dados = ("João", 25, "São Paulo")
nome, idade, cidade = dados
print(f"\nDados: {dados}")
print(f"nome = {nome}, idade = {idade}, cidade = {cidade}")

# ============================================
# TUPLA vs LISTA
# ============================================
print("\n5. DIFERENÇA: TUPLA vs LISTA:")
print("-" * 60)

lista = [1, 2, 3]
tupla = (1, 2, 3)

print(f"Lista: {lista}, tipo: {type(lista)}")
print(f"Tupla: {tupla}, tipo: {type(tupla)}")

print("\n✓ Tupla: imutável, mais rápida, menos memória")
print("✓ Lista: mutável, mais métodos, mais flexível")

# ============================================
# QUANDO USAR TUPLAS
# ============================================
print("\n6. QUANDO USAR TUPLAS:")
print("-" * 60)

print("✓ Coordenadas (x, y)")
print("✓ Retornar múltiplos valores de função")
print("✓ Chaves de dicionário")
print("✓ Valores que não devem mudar")

# Exemplo: coordenadas
ponto_a = (10, 20)
ponto_b = (30, 40)
print(f"\nCoordenadas: A{ponto_a}, B{ponto_b}")

# ============================================
# OPERAÇÕES COM TUPLAS
# ============================================
print("\n7. OPERAÇÕES COM TUPLAS:")
print("-" * 60)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação
tupla3 = tupla1 + tupla2
print(f"{tupla1} + {tupla2} = {tupla3}")

# Repetição
tupla4 = tupla1 * 2
print(f"{tupla1} * 2 = {tupla4}")

# Tamanho
print(f"len({tupla1}) = {len(tupla1)}")

# Verificar se elemento existe
print(f"2 in {tupla1}? {2 in tupla1}")

