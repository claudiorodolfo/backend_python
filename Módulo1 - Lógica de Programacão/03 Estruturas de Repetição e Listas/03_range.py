"""
03 - Função range()

Este arquivo demonstra o uso da função range() em Python.
"""

print("=" * 60)
print("FUNÇÃO RANGE()")
print("=" * 60)

# ============================================
# RANGE(N) - DE 0 A N-1
# ============================================
print("\n1. RANGE(N) - De 0 até N-1:")
print("-" * 60)

print("range(5) gera: 0, 1, 2, 3, 4")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# Convertendo para lista para visualizar
print(f"\nLista: {list(range(5))}")

# ============================================
# RANGE(INICIO, FIM) - DE INICIO A FIM-1
# ============================================
print("\n2. RANGE(INICIO, FIM):")
print("-" * 60)

print("range(1, 6) gera: 1, 2, 3, 4, 5")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

print(f"\nLista: {list(range(1, 6))}")

# Exemplo prático
print("\nContando de 10 a 20:")
for i in range(10, 21):
    print(f"  {i}", end=" ")
print()

# ============================================
# RANGE(INICIO, FIM, PASSO)
# ============================================
print("\n3. RANGE(INICIO, FIM, PASSO):")
print("-" * 60)

print("range(0, 10, 2) - de 0 a 9, pulando de 2 em 2:")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print()

print(f"\nLista: {list(range(0, 10, 2))}")

print("\nrange(10, 0, -1) - contagem regressiva:")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print()

print(f"\nLista: {list(range(10, 0, -1))}")

# ============================================
# CASOS DE USO COMUNS
# ============================================
print("\n4. CASOS DE USO COMUNS:")
print("-" * 60)

# Contar de 1 a 10
print("Contar de 1 a 10:")
for i in range(1, 11):
    print(f"  {i}", end=" ")
print()

# Números pares de 0 a 10
print("\nNúmeros pares de 0 a 10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()

# Contagem regressiva de 5 a 1
print("\nContagem regressiva 5, 4, 3, 2, 1:")
for i in range(5, 0, -1):
    print(f"  {i}", end=" ")
print()

# Múltiplos de 3
print("\nMúltiplos de 3 até 30:")
for i in range(3, 31, 3):
    print(f"  {i}", end=" ")
print()

# ============================================
# RANGE COM FOR - ACESSANDO ÍNDICES
# ============================================
print("\n5. RANGE PARA ACESSAR ÍNDICES:")
print("-" * 60)

frutas = ["maçã", "banana", "laranja", "uva"]

print("Acessando elementos por índice:")
for i in range(len(frutas)):
    print(f"  [{i}] {frutas[i]}")

# Alternativa melhor: enumerate()
print("\nUsando enumerate() (mais pythônico):")
for i, fruta in enumerate(frutas):
    print(f"  [{i}] {fruta}")

# ============================================
# RANGE EM OPERAÇÕES MATEMÁTICAS
# ============================================
print("\n6. RANGE EM OPERAÇÕES MATEMÁTICAS:")
print("-" * 60)

# Soma dos números de 1 a 100
print("Soma dos números de 1 a 100:")
soma = 0
for i in range(1, 101):
    soma += i
print(f"  Soma = {soma}")

# Fatorial de 5
print("\nFatorial de 5 (5!):")
fatorial = 1
for i in range(1, 6):
    fatorial *= i
    print(f"  {i}! = {fatorial}")

# Potências de 2
print("\nPrimeiras 5 potências de 2:")
for i in range(5):
    potencia = 2 ** i
    print(f"  2^{i} = {potencia}")

# ============================================
# RANGE COM LISTAS
# ============================================
print("\n7. USANDO RANGE PARA MODIFICAR LISTAS:")
print("-" * 60)

numeros = [10, 20, 30, 40, 50]
print(f"Lista original: {numeros}")

print("Multiplicando cada elemento por 2:")
for i in range(len(numeros)):
    numeros[i] *= 2

print(f"Lista modificada: {numeros}")

# ============================================
# RANGE NEGATIVO (PASSO NEGATIVO)
# ============================================
print("\n8. RANGE COM PASSO NEGATIVO:")
print("-" * 60)

print("Contagem regressiva de 10 a 1:")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print()

print("\nDe 20 a 0, de 5 em 5:")
for i in range(20, -1, -5):
    print(f"  {i}", end=" ")
print()

# ============================================
# CONVERSÃO DE RANGE PARA LISTA
# ============================================
print("\n9. CONVERTENDO RANGE PARA LISTA:")
print("-" * 60)

print("range(5):")
print(f"  Tipo: {type(range(5))}")
print(f"  Como lista: {list(range(5))}")

print("\nrange(1, 11, 2):")
print(f"  Como lista: {list(range(1, 11, 2))}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Tabuada
print("\nExemplo 1: Tabuada do 5")
print("-" * 60)
numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"  {numero} × {i} = {resultado}")

# Exemplo 2: Progressão aritmética
print("\nExemplo 2: Progressão aritmética (3, 6, 9, ..., 30)")
print("-" * 60)
for i in range(3, 31, 3):
    print(f"  {i}", end=" ")
print()

# Exemplo 3: Tabela de conversão
print("\nExemplo 3: Conversão Celsius para Fahrenheit (0 a 40°C)")
print("-" * 60)
print("  °C  |  °F")
print("  ----|-----")
for celsius in range(0, 41, 5):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"  {celsius:3} | {fahrenheit:5.1f}")

