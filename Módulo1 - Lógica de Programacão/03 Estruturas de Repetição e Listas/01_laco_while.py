"""
01 - Laço While

Este arquivo demonstra o uso do laço while em Python.
"""

print("=" * 60)
print("LAÇO WHILE")
print("=" * 60)

# ============================================
# WHILE BÁSICO
# ============================================
print("\n1. WHILE BÁSICO:")
print("-" * 60)

print("Sintaxe:")
print("  while condicao:")
print("      # código que executa enquanto condição for True")

print("\nExemplo: Contador de 1 a 5")
contador = 1
while contador <= 5:
    print(f"  Contador: {contador}")
    contador += 1

print(f"\nApós o loop, contador = {contador}")

# ============================================
# CONTADOR CRESCENTE
# ============================================
print("\n2. CONTADOR CRESCENTE:")
print("-" * 60)

print("Contando de 0 a 10:")
numero = 0
while numero <= 10:
    print(f"  {numero}", end=" ")
    numero += 2  # Incrementa de 2 em 2
print()  # Nova linha

# ============================================
# CONTADOR DECRESCENTE
# ============================================
print("\n3. CONTADOR DECRESCENTE:")
print("-" * 60)

print("Contagem regressiva de 5 a 1:")
contador = 5
while contador > 0:
    print(f"  {contador}")
    contador -= 1
print("  Lançar!")

# ============================================
# WHILE COM CONDIÇÃO BOOLEANA
# ============================================
print("\n4. WHILE COM VARIÁVEL BOOLEANA:")
print("-" * 60)

continuar = True
tentativas = 0
max_tentativas = 3

print("Simulação de tentativas:")
while continuar and tentativas < max_tentativas:
    tentativas += 1
    print(f"  Tentativa {tentativas}/{max_tentativas}")
    
    # Simulando condição de parada
    if tentativas >= max_tentativas:
        continuar = False
        print("  Limite de tentativas atingido!")

# ============================================
# ACUMULADOR (SOMA)
# ============================================
print("\n5. ACUMULADOR:")
print("-" * 60)

print("Soma dos números de 1 a 10:")
soma = 0
numero = 1

while numero <= 10:
    soma += numero
    print(f"  Adicionando {numero}, soma parcial = {soma}")
    numero += 1

print(f"\nSoma total: {soma}")

# ============================================
# WHILE COM ENTRADA DO USUÁRIO (simulado)
# ============================================
print("\n6. WHILE ATÉ CONDIÇÃO SER ATENDIDA:")
print("-" * 60)

# Simulando entrada do usuário
senha_correta = "1234"
senha_digitada = "1234"  # Simulando que usuário digitou corretamente

print("Sistema de validação de senha (simulado):")
tentativas = 0
max_tentativas = 3

# Em código real seria:
# while senha_digitada != senha_correta and tentativas < max_tentativas:
#     senha_digitada = input("Digite a senha: ")
#     tentativas += 1

# Simulação
senha_valida = senha_digitada == senha_correta
if senha_valida:
    print("  ✓ Senha correta! Acesso liberado.")
else:
    print(f"  ✗ Senha incorreta após {max_tentativas} tentativas.")

# ============================================
# ⚠️ CUIDADO: LOOPS INFINITOS
# ============================================
print("\n" + "=" * 60)
print("⚠️  CUIDADO: LOOPS INFINITOS")
print("=" * 60)

print("\nExemplo de loop infinito (comentado para não executar):")
print()
print("  # ❌ ERRO: Loop infinito")
print("  # contador = 1")
print("  # while contador < 5:")
print("  #     print(contador)")
print("  #     # Esqueceu de incrementar contador!")
print()
print("Como evitar:")
print("  ✓ Sempre altere a variável da condição dentro do loop")
print("  ✓ Certifique-se de que a condição eventualmente será False")
print("  ✓ Use break se necessário")
print("  ✓ Teste com valores pequenos primeiro")

# Exemplo correto (com salvaguarda)
print("\nExemplo correto com salvaguarda:")
contador = 1
max_iteracoes = 1000  # Proteção contra loop infinito
iteracoes = 0

while contador < 5 and iteracoes < max_iteracoes:
    print(f"  Contador: {contador}, Iterações: {iteracoes}")
    contador += 1
    iteracoes += 1

if iteracoes >= max_iteracoes:
    print("  ⚠️  Loop interrompido por segurança!")

# ============================================
# WHILE-ELSE
# ============================================
print("\n7. WHILE-ELSE:")
print("-" * 60)

print("O bloco else executa quando o while termina normalmente")
print("(não por break):")

numero = 1
while numero <= 3:
    print(f"  Numero: {numero}")
    numero += 1
else:
    print("  Loop terminou normalmente!")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Menu interativo (simulado)
print("\nExemplo 1: Menu interativo")
print("-" * 60)
opcao = 0  # 0 = sair
while opcao != 0:
    print("  [1] Opção 1")
    print("  [2] Opção 2")
    print("  [0] Sair")
    opcao = 0  # Simulando que usuário escolheu sair
    print("  Saindo...")
    break  # Interrompe o loop

# Exemplo 2: Processar até encontrar valor
print("\nExemplo 2: Buscar número")
print("-" * 60)
numeros = [1, 3, 5, 7, 9, 11, 13]
valor_procurado = 7
indice = 0
encontrado = False

while indice < len(numeros) and not encontrado:
    if numeros[indice] == valor_procurado:
        encontrado = True
        print(f"  ✓ Número {valor_procurado} encontrado na posição {indice}")
    indice += 1

if not encontrado:
    print(f"  ✗ Número {valor_procurado} não encontrado")

# Exemplo 3: Validar entrada (simulado)
print("\nExemplo 3: Validar entrada numérica")
print("-" * 60)
valor = 25  # Simulando entrada válida
valor_valido = False
tentativas = 0

# Em código real seria:
# while not valor_valido:
#     try:
#         valor = int(input("Digite um número entre 1 e 100: "))
#         if 1 <= valor <= 100:
#             valor_valido = True
#         else:
#             print("Número fora do intervalo!")
#     except ValueError:
#         print("Digite um número válido!")

if valor_valido or (1 <= valor <= 100):
    print(f"  ✓ Valor válido: {valor}")

