"""
02 - Laço For

Este arquivo demonstra o uso do laço for em Python.
"""

print("=" * 60)
print("LAÇO FOR")
print("=" * 60)

# ============================================
# FOR BÁSICO COM LISTA
# ============================================
print("\n1. FOR BÁSICO COM LISTA:")
print("-" * 60)

frutas = ["maçã", "banana", "laranja", "uva"]

print("Iterando sobre lista de frutas:")
for fruta in frutas:
    print(f"  {fruta}")

# ============================================
# FOR COM STRING
# ============================================
print("\n2. FOR COM STRING:")
print("-" * 60)

palavra = "Python"

print("Iterando sobre cada caractere:")
for letra in palavra:
    print(f"  {letra}")

# Contando caracteres
print("\nContando caracteres:")
contador = 0
for letra in palavra:
    contador += 1
print(f"  A palavra '{palavra}' tem {contador} letras")

# ============================================
# FOR COM RANGE()
# ============================================
print("\n3. FOR COM RANGE():")
print("-" * 60)

print("Contando de 0 a 4:")
for i in range(5):
    print(f"  {i}")

print("\nContando de 1 a 5:")
for i in range(1, 6):
    print(f"  {i}")

# ============================================
# FOR COM ENUMERATE()
# ============================================
print("\n4. FOR COM ENUMERATE() (índice e valor):")
print("-" * 60)

frutas = ["maçã", "banana", "laranja"]

print("Iterando com índice e valor:")
for indice, fruta in enumerate(frutas):
    print(f"  [{indice}] {fruta}")

# ============================================
# ACUMULADOR COM FOR
# ============================================
print("\n5. ACUMULADOR COM FOR:")
print("-" * 60)

print("Soma dos números de 1 a 10:")
soma = 0
for numero in range(1, 11):
    soma += numero
    print(f"  Adicionando {numero}, soma parcial = {soma}")

print(f"\nSoma total: {soma}")

# ============================================
# FOR COM CONDIÇÃO
# ============================================
print("\n6. FOR COM CONDIÇÃO (dentro do loop):")
print("-" * 60)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(f"  {numero} é par")

# ============================================
# FOR-ELSE
# ============================================
print("\n7. FOR-ELSE:")
print("-" * 60)

print("O bloco else executa quando o for termina normalmente")
print("(não por break):")

for i in range(3):
    print(f"  Iteração {i}")
else:
    print("  Loop terminou normalmente!")

# ============================================
# ITERAÇÃO SOBRE MÚLTIPLAS LISTAS
# ============================================
print("\n8. ITERAÇÃO SOBRE MÚLTIPLAS LISTAS (zip):")
print("-" * 60)

nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 28]

print("Iterando sobre duas listas simultaneamente:")
for nome, idade in zip(nomes, idades):
    print(f"  {nome} tem {idade} anos")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Calcular média
print("\nExemplo 1: Calcular média de notas")
print("-" * 60)
notas = [8.5, 7.0, 9.2, 6.5, 8.0]
soma = 0

print("Notas:", notas)
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.2f}")

# Exemplo 2: Encontrar maior valor
print("\nExemplo 2: Encontrar maior número")
print("-" * 60)
numeros = [45, 23, 67, 12, 89, 34]
maior = numeros[0]

print("Números:", numeros)
for numero in numeros:
    if numero > maior:
        maior = numero

print(f"Maior número: {maior}")

# Exemplo 3: Contar ocorrências
print("\nExemplo 3: Contar ocorrências de letra")
print("-" * 60)
texto = "programação"
letra_procurada = "a"
contador = 0

print(f"Texto: '{texto}'")
print(f"Letra procurada: '{letra_procurada}'")

for letra in texto:
    if letra == letra_procurada:
        contador += 1

print(f"Ocorrências: {contador}")

# Exemplo 4: Processar lista de produtos
print("\nExemplo 4: Processar lista de produtos")
print("-" * 60)
produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
precos = [2500.00, 50.00, 150.00, 800.00]

print("Produtos e preços:")
for i, (produto, preco) in enumerate(zip(produtos, precos), 1):
    print(f"  {i}. {produto}: R$ {preco:.2f}")

# ============================================
# FOR vs WHILE
# ============================================
print("\n" + "=" * 60)
print("FOR vs WHILE")
print("=" * 60)

print("\nUse FOR quando:")
print("  ✓ Você sabe quantas vezes vai iterar")
print("  ✓ Está iterando sobre uma coleção")
print("  ✓ Não precisa modificar a coleção durante iteração")

print("\nUse WHILE quando:")
print("  ✓ Não sabe quantas iterações serão necessárias")
print("  ✓ Condição de parada é complexa")
print("  ✓ Precisa de controle mais fino do loop")

print("\nExemplo comparativo:")
print("-" * 60)

# Mesma tarefa com for e while
print("Com FOR (mais simples):")
for i in range(1, 6):
    print(f"  {i}")

print("\nCom WHILE (mais verboso):")
i = 1
while i <= 5:
    print(f"  {i}")
    i += 1

