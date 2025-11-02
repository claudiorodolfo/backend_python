"""
05 - Comandos break e continue

Este arquivo demonstra o uso de break e continue em laços.
"""

print("=" * 60)
print("COMANDOS BREAK E CONTINUE")
print("=" * 60)

# ============================================
# BREAK - SAIR DO LAÇO
# ============================================
print("\n1. BREAK - Interromper o laço:")
print("-" * 60)

print("Buscar número 7 e parar quando encontrar:")
for i in range(1, 11):
    print(f"  Verificando {i}...", end=" ")
    if i == 7:
        print(f"✓ Encontrado! Parando.")
        break
    print("não é 7")

# ============================================
# CONTINUE - PULAR ITERAÇÃO
# ============================================
print("\n2. CONTINUE - Pular iteração atual:")
print("-" * 60)

print("Imprimir apenas números pares:")
for i in range(1, 11):
    if i % 2 != 0:  # Se for ímpar
        continue  # Pula para próxima iteração
    print(f"  {i} é par")

# ============================================
# BREAK EM WHILE
# ============================================
print("\n3. BREAK EM WHILE:")
print("-" * 60)

print("Soma até encontrar número negativo:")
soma = 0
numeros = [10, 20, -5, 30, 40]
indice = 0

while indice < len(numeros):
    numero = numeros[indice]
    if numero < 0:
        print(f"  Número negativo encontrado: {numero}")
        print(f"  Parando...")
        break
    soma += numero
    print(f"  Adicionando {numero}, soma = {soma}")
    indice += 1

# ============================================
# CONTINUE COM VALIDAÇÃO
# ============================================
print("\n4. CONTINUE COM VALIDAÇÃO:")
print("-" * 60)

print("Processar apenas números positivos:")
numeros = [10, -5, 20, -3, 30, 0, 40]

for numero in numeros:
    if numero <= 0:
        continue  # Pula números não-positivos
    print(f"  Processando {numero}...")

# ============================================
# BREAK E CONTINUE JUNTOS
# ============================================
print("\n5. BREAK E CONTINUE JUNTOS:")
print("-" * 60)

print("Buscar primeiro número par maior que 10:")
for i in range(1, 20):
    if i <= 10:
        continue  # Pula números menores ou iguais a 10
    if i % 2 == 0:
        print(f"  ✓ Primeiro número par > 10: {i}")
        break  # Encontrou, para o loop

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Validar lista até encontrar inválido
print("\nExemplo 1: Validar lista")
print("-" * 60)
valores = [10, 20, 30, -5, 40, 50]
todos_validos = True

for valor in valores:
    if valor < 0:
        print(f"  ✗ Valor inválido encontrado: {valor}")
        todos_validos = False
        break
    print(f"  ✓ {valor} é válido")

if todos_validos:
    print("  Todos os valores são válidos!")

# Exemplo 2: Processar apenas números pares
print("\nExemplo 2: Soma apenas números pares")
print("-" * 60)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_pares = 0

for numero in numeros:
    if numero % 2 != 0:
        continue  # Pula ímpares
    soma_pares += numero
    print(f"  Adicionando {numero} (par), soma = {soma_pares}")

print(f"\nSoma total dos pares: {soma_pares}")

# Exemplo 3: Buscar e parar
print("\nExemplo 3: Buscar nome na lista")
print("-" * 60)
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
nome_procurado = "Carlos"

for nome in nomes:
    print(f"  Verificando: {nome}")
    if nome == nome_procurado:
        print(f"  ✓ {nome_procurado} encontrado!")
        break
else:
    print(f"  ✗ {nome_procurado} não encontrado")

