"""
04 - Laços Aninhados

Este arquivo demonstra o uso de laços aninhados (laços dentro de laços).
"""

print("=" * 60)
print("LAÇOS ANINHADOS")
print("=" * 60)

# ============================================
# FOR DENTRO DE FOR
# ============================================
print("\n1. FOR DENTRO DE FOR:")
print("-" * 60)

print("Tabuada (1 a 3):")
for i in range(1, 4):
    for j in range(1, 4):
        resultado = i * j
        print(f"  {i} × {j} = {resultado}")

# ============================================
# TABUADA COMPLETA
# ============================================
print("\n2. TABUADA COMPLETA:")
print("-" * 60)

print("Tabuada de 1 a 5:")
for multiplicador in range(1, 6):
    print(f"\nTabuada do {multiplicador}:")
    for numero in range(1, 11):
        resultado = multiplicador * numero
        print(f"  {multiplicador} × {numero:2} = {resultado:3}")

# ============================================
# MATRIZ / TABELA
# ============================================
print("\n3. CRIANDO TABELA/MATRIZ:")
print("-" * 60)

print("Tabela de adição (1 a 3):")
print("   ", end="")
for j in range(1, 4):
    print(f"{j:4}", end="")
print()

for i in range(1, 4):
    print(f"{i:2} ", end="")
    for j in range(1, 4):
        print(f"{i+j:4}", end="")
    print()

# ============================================
# PADRÕES COM ASTERISCOS
# ============================================
print("\n4. PADRÕES COM ASTERISCOS:")
print("-" * 60)

print("Retângulo 4×5:")
for linha in range(4):
    for coluna in range(5):
        print("*", end=" ")
    print()

print("\nTriângulo:")
for linha in range(1, 6):
    for coluna in range(linha):
        print("*", end=" ")
    print()

# ============================================
# PROCESSAR LISTA DE LISTAS
# ============================================
print("\n5. PROCESSAR LISTA DE LISTAS:")
print("-" * 60)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:3}", end=" ")
    print()

print("\nSoma de cada linha:")
for i, linha in enumerate(matriz):
    soma = sum(linha)
    print(f"  Linha {i+1}: {soma}")

# ============================================
# WHILE DENTRO DE FOR
# ============================================
print("\n6. WHILE DENTRO DE FOR:")
print("-" * 60)

print("Contagem até encontrar número específico:")
numeros = [1, 3, 5, 7, 9, 11]
valor_procurado = 7

for lista_idx in range(len(numeros)):
    contador = 0
    while contador < 3 and numeros[lista_idx] != valor_procurado:
        contador += 1
        numeros[lista_idx] += 1  # Simulação
    if numeros[lista_idx] == valor_procurado:
        print(f"  Encontrado na posição {lista_idx}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Busca em matriz
print("\nExemplo 1: Buscar valor em matriz")
print("-" * 60)
matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
valor_busca = 50
encontrado = False

for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if valor == valor_busca:
            print(f"  ✓ Valor {valor_busca} encontrado em [{i}][{j}]")
            encontrado = True
            break
    if encontrado:
        break

# Exemplo 2: Produto cartesiano
print("\nExemplo 2: Produto cartesiano")
print("-" * 60)
cores = ["vermelho", "azul"]
tamanhos = ["P", "M", "G"]

print("Combinações de cor e tamanho:")
for cor in cores:
    for tamanho in tamanhos:
        print(f"  {cor} {tamanho}")

