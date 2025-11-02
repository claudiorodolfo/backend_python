"""
02 - Operadores Relacionais (Comparação)

Este arquivo demonstra todos os operadores relacionais disponíveis em Python.
"""

print("=" * 60)
print("OPERADORES RELACIONAIS (COMPARAÇÃO)")
print("=" * 60)

# Valores de exemplo
a = 10
b = 5
c = 10

print(f"\nValores de exemplo: a = {a}, b = {b}, c = {c}\n")

# ============================================
# 1. IGUAL (==)
# ============================================
print("1. IGUAL (==):")
print("-" * 60)
resultado1 = a == b
resultado2 = a == c
print(f"  {a} == {b} → {resultado1}")
print(f"  {a} == {c} → {resultado2}")

print("\n  Exemplos com strings:")
texto1 = "Python"
texto2 = "python"
texto3 = "Python"
print(f'  "{texto1}" == "{texto2}" → {texto1 == texto2}')
print(f'  "{texto1}" == "{texto3}" → {texto1 == texto3}')

# ============================================
# 2. DIFERENTE (!=)
# ============================================
print("\n2. DIFERENTE (!=):")
print("-" * 60)
resultado1 = a != b
resultado2 = a != c
print(f"  {a} != {b} → {resultado1}")
print(f"  {a} != {c} → {resultado2}")

# ============================================
# 3. MAIOR QUE (>)
# ============================================
print("\n3. MAIOR QUE (>):")
print("-" * 60)
resultado1 = a > b
resultado2 = a > c
resultado3 = b > a
print(f"  {a} > {b} → {resultado1}")
print(f"  {a} > {c} → {resultado2}")
print(f"  {b} > {a} → {resultado3}")

# ============================================
# 4. MENOR QUE (<)
# ============================================
print("\n4. MENOR QUE (<):")
print("-" * 60)
resultado1 = a < b
resultado2 = b < a
resultado3 = a < c
print(f"  {a} < {b} → {resultado1}")
print(f"  {b} < {a} → {resultado2}")
print(f"  {a} < {c} → {resultado3}")

# ============================================
# 5. MAIOR OU IGUAL (>=)
# ============================================
print("\n5. MAIOR OU IGUAL (>=):")
print("-" * 60)
resultado1 = a >= b
resultado2 = a >= c
resultado3 = b >= a
print(f"  {a} >= {b} → {resultado1}")
print(f"  {a} >= {c} → {resultado2}")
print(f"  {b} >= {a} → {resultado3}")

# ============================================
# 6. MENOR OU IGUAL (<=)
# ============================================
print("\n6. MENOR OU IGUAL (<=):")
print("-" * 60)
resultado1 = a <= b
resultado2 = a <= c
resultado3 = b <= a
print(f"  {a} <= {b} → {resultado1}")
print(f"  {a} <= {c} → {resultado2}")
print(f"  {b} <= {a} → {resultado3}")

# ============================================
# COMPARAÇÃO ENTRE DIFERENTES TIPOS
# ============================================
print("\n" + "=" * 60)
print("COMPARAÇÃO ENTRE DIFERENTES TIPOS")
print("=" * 60)

print("\nComparação numérica:")
print(f"  {a} == {float(a)} → {a == float(a)}")
print(f"  {a} == {a}.0 → {a == float(a)}")

print("\n⚠️  IMPORTANTE:")
print("  • == compara valores (5 == 5.0 é True)")
print("  • is compara identidade de objetos")
print("  • Use == para comparação de valores na maioria dos casos")

# ============================================
# OPERADORES CHAINED (ENCADEADOS)
# ============================================
print("\n" + "=" * 60)
print("COMPARAÇÕES ENCADEADAS")
print("=" * 60)

x = 5
y = 10
z = 15

print(f"\nValores: x = {x}, y = {y}, z = {z}")

# Python permite comparações encadeadas
resultado = x < y < z
print(f"\n  {x} < {y} < {z} → {resultado}")

resultado2 = x < y > x
print(f"  {x} < {y} > {x} → {resultado2}")

# Equivale a: (x < y) and (y < z)
print(f"\n  Equivale a: ({x} < {y}) and ({y} < {z}) = {(x < y) and (y < z)}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Validação de idade
print("\nExemplo 1: Validação de idade")
print("-" * 60)
idade = 20
idade_minima = 18
idade_maxima = 65

pode_votar = idade >= idade_minima
pode_aposentar = idade >= idade_maxima
esta_na_faixa = idade_minima <= idade <= idade_maxima

print(f"Idade: {idade} anos")
print(f"  Pode votar? ({idade} >= {idade_minima}) → {pode_votar}")
print(f"  Pode aposentar? ({idade} >= {idade_maxima}) → {pode_aposentar}")
print(f"  Está na faixa de trabalho? ({idade_minima} <= {idade} <= {idade_maxima}) → {esta_na_faixa}")

# Exemplo 2: Comparação de notas
print("\nExemplo 2: Comparação de notas")
print("-" * 60)
nota_aluno = 8.5
nota_minima_aprovacao = 7.0
nota_maxima = 10.0

aprovado = nota_aluno >= nota_minima_aprovacao
nota_valida = nota_minima_aprovacao <= nota_aluno <= nota_maxima

print(f"Nota do aluno: {nota_aluno}")
print(f"  Aprovado? ({nota_aluno} >= {nota_minima_aprovacao}) → {aprovado}")
print(f"  Nota válida? ({nota_minima_aprovacao} <= {nota_aluno} <= {nota_maxima}) → {nota_valida}")

# Exemplo 3: Comparação de strings
print("\nExemplo 3: Comparação de strings")
print("-" * 60)
nome1 = "Ana"
nome2 = "ana"
nome3 = "Bruno"

print(f"Nomes: '{nome1}', '{nome2}', '{nome3}'")
print(f"  '{nome1}' == '{nome2}' → {nome1 == nome2} (case-sensitive)")
print(f"  '{nome1}' != '{nome3}' → {nome1 != nome3}")
print(f"  '{nome1}' < '{nome3}' → {nome1 < nome3} (ordem alfabética)")

# ============================================
# RESUMO
# ============================================
print("\n" + "=" * 60)
print("RESUMO DOS OPERADORES RELACIONAIS")
print("=" * 60)

operadores = [
    ("==", "Igual", "Verifica se valores são iguais"),
    ("!=", "Diferente", "Verifica se valores são diferentes"),
    (">", "Maior que", "Verifica se primeiro valor é maior"),
    ("<", "Menor que", "Verifica se primeiro valor é menor"),
    (">=", "Maior ou igual", "Verifica se primeiro valor é maior ou igual"),
    ("<=", "Menor ou igual", "Verifica se primeiro valor é menor ou igual")
]

print("\nTodos os operadores retornam True ou False (bool):")
for op, nome, descricao in operadores:
    print(f"  {op:4} → {nome:15} → {descricao}")

print("\n💡 DICA: Use operadores relacionais para:")
print("   • Validar dados de entrada")
print("   • Comparar valores em condicionais")
print("   • Verificar limites e intervalos")
print("   • Ordenar e filtrar dados")

