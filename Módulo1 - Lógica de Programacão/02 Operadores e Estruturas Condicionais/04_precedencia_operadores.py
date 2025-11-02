"""
04 - Precedência e Associação de Operadores

Este arquivo demonstra a ordem de avaliação dos operadores em Python.
"""

print("=" * 60)
print("PRECEDÊNCIA E ASSOCIAÇÃO DE OPERADORES")
print("=" * 60)

# ============================================
# TABELA DE PRECEDÊNCIA (DO MAIOR PARA O MENOR)
# ============================================
print("\nTABELA DE PRECEDÊNCIA DOS OPERADORES")
print("=" * 60)
print("(Do maior para o menor - primeiro avaliado para último)")

precedencias = [
    ("**", "Exponenciação"),
    ("+x, -x", "Positivo, Negativo unário"),
    ("*, /, //, %", "Multiplicação, Divisão, Divisão inteira, Módulo"),
    ("+, -", "Adição, Subtração"),
    ("<, <=, >, >=", "Comparações"),
    ("==, !=", "Igualdade"),
    ("not", "NOT lógico"),
    ("and", "AND lógico"),
    ("or", "OR lógico")
]

print("\nOrdem de precedência:")
for i, (operador, descricao) in enumerate(precedencias, 1):
    print(f"  {i:2}. {operador:20} → {descricao}")

# ============================================
# EXEMPLOS DE PRECEDÊNCIA
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS DE PRECEDÊNCIA")
print("=" * 60)

a = 10
b = 5
c = 2

print(f"\nValores: a = {a}, b = {b}, c = {c}\n")

# Exemplo 1: Aritméticos
print("1. Operadores Aritméticos:")
print("-" * 60)
resultado1 = a + b * c
print(f"  {a} + {b} * {c}")
print(f"  = {a} + ({b} * {c})  → Multiplicação primeiro")
print(f"  = {a} + {b * c}")
print(f"  = {resultado1}")

resultado2 = a * b ** c
print(f"\n  {a} * {b} ** {c}")
print(f"  = {a} * ({b} ** {c})  → Exponenciação primeiro")
print(f"  = {a} * {b ** c}")
print(f"  = {resultado2}")

# Exemplo 2: Misturando aritméticos e relacionais
print("\n2. Misturando Aritméticos e Relacionais:")
print("-" * 60)
resultado3 = a + b > c * 2
print(f"  {a} + {b} > {c} * 2")
print(f"  = ({a} + {b}) > ({c} * 2)  → Aritméticos primeiro, depois comparação")
print(f"  = {a + b} > {c * 2}")
print(f"  = {resultado3}")

# Exemplo 3: Operadores lógicos
print("\n3. Operadores Lógicos:")
print("-" * 60)
x = True
y = False
z = True

resultado4 = x and y or z
print(f"  {x} and {y} or {z}")
print(f"  = (({x} and {y}) or {z})  → AND antes de OR")
print(f"  = ({x and y} or {z})")
print(f"  = {resultado4}")

resultado5 = not x and y
print(f"\n  not {x} and {y}")
print(f"  = (not {x}) and {y}  → NOT antes de AND")
print(f"  = {not x} and {y}")
print(f"  = {resultado5}")

# ============================================
# USO DE PARÊNTESES PARA CONTROLAR PRECEDÊNCIA
# ============================================
print("\n" + "=" * 60)
print("USO DE PARÊNTESES PARA CONTROLAR PRECEDÊNCIA")
print("=" * 60)

print("\nOs parênteses alteram a ordem de avaliação:")
print("-" * 60)

# Sem parênteses
resultado1 = 2 + 3 * 4
print(f"\nSem parênteses:")
print(f"  2 + 3 * 4 = {resultado1}")
print(f"  (multiplicação primeiro: 2 + (3 * 4) = {2 + (3 * 4)})")

# Com parênteses
resultado2 = (2 + 3) * 4
print(f"\nCom parênteses:")
print(f"  (2 + 3) * 4 = {resultado2}")
print(f"  (adição primeiro: (2 + 3) * 4 = {(2 + 3) * 4})")

# Exemplo mais complexo
print("\nExemplo complexo:")
print("-" * 60)
print(f"  Sem parênteses: 10 - 2 * 3 + 1 = {10 - 2 * 3 + 1}")
print(f"    Ordem: 10 - (2 * 3) + 1 = {10 - (2 * 3) + 1}")

print(f"\n  Com parênteses diferentes:")
print(f"    (10 - 2) * (3 + 1) = {(10 - 2) * (3 + 1)}")
print(f"    10 - (2 * (3 + 1)) = {10 - (2 * (3 + 1))}")

# ============================================
# ASSOCIAÇÃO (ASSOCIATIVIDADE)
# ============================================
print("\n" + "=" * 60)
print("ASSOCIAÇÃO (ASSOCIATIVIDADE)")
print("=" * 60)

print("\nQuando operadores têm a mesma precedência, a ordem é:")
print("-" * 60)

# Associatividade à esquerda (esquerda → direita)
print("\n1. Associatividade à esquerda (esquerda → direita):")
resultado = 10 - 5 - 2
print(f"  10 - 5 - 2")
print(f"  = (10 - 5) - 2  → Avalia da esquerda para direita")
print(f"  = {10 - 5} - 2")
print(f"  = {resultado}")

resultado = 16 / 4 / 2
print(f"\n  16 / 4 / 2")
print(f"  = (16 / 4) / 2  → Avalia da esquerda para direita")
print(f"  = {16 / 4} / 2")
print(f"  = {resultado}")

# Associatividade à direita (direita → esquerda)
print("\n2. Associatividade à direita (direita → esquerda):")
resultado = 2 ** 3 ** 2
print(f"  2 ** 3 ** 2")
print(f"  = 2 ** (3 ** 2)  → Exponenciação avalia da direita para esquerda")
print(f"  = 2 ** {3 ** 2}")
print(f"  = {resultado}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Cálculo de média ponderada
print("\nExemplo 1: Cálculo de média ponderada")
print("-" * 60)
nota1 = 8.0
peso1 = 2
nota2 = 7.5
peso2 = 3

# Sem parênteses (ERRADO)
media_errada = nota1 * peso1 + nota2 * peso2 / peso1 + peso2
print(f"  Sem parênteses (ERRADO):")
print(f"    {nota1} * {peso1} + {nota2} * {peso2} / {peso1} + {peso2} = {media_errada}")

# Com parênteses (CORRETO)
media_correta = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print(f"\n  Com parênteses (CORRETO):")
print(f"    ({nota1} * {peso1} + {nota2} * {peso2}) / ({peso1} + {peso2}) = {media_correta:.2f}")

# Exemplo 2: Validação complexa
print("\nExemplo 2: Validação de condições")
print("-" * 60)
idade = 25
tem_cartao = True
compra = 150.00

# Sem parênteses (pode ser confuso)
resultado1 = idade >= 18 and tem_cartao or compra > 100
print(f"  Sem parênteses:")
print(f"    {idade} >= 18 and {tem_cartao} or {compra} > 100")
print(f"    = (({idade} >= 18) and {tem_cartao}) or ({compra} > 100)")
print(f"    = {resultado1}")

# Com parênteses (mais claro)
resultado2 = (idade >= 18 and tem_cartao) or compra > 100
print(f"\n  Com parênteses (mais claro):")
print(f"    ({idade} >= 18 and {tem_cartao}) or {compra} > 100")
print(f"    = {resultado2}")

# ============================================
# BOAS PRÁTICAS
# ============================================
print("\n" + "=" * 60)
print("BOAS PRÁTICAS")
print("=" * 60)

print("\n✓ Use parênteses mesmo quando não são necessários para:")
print("  • Deixar a intenção clara")
print("  • Facilitar a leitura do código")
print("  • Evitar erros de interpretação")

print("\n✓ Prefira clareza sobre concisão:")
print("  • Código claro é melhor que código curto")
print("  • Outros desenvolvedores (e você no futuro) agradecem")

print("\n✓ Quando em dúvida, use parênteses:")
print("  • É melhor usar parênteses desnecessários")
print("  • Do que depender apenas da precedência")

# Exemplo de boa prática
print("\nExemplo de boa prática:")
print("-" * 60)
print("  ❌ Evite: resultado = a + b * c - d / e")
print("  ✅ Prefira: resultado = a + (b * c) - (d / e)")
print("\n  Mesmo resultado, mas muito mais claro!")

