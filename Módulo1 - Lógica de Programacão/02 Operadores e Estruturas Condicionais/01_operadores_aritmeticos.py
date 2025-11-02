"""
01 - Operadores Aritméticos

Este arquivo demonstra todos os operadores aritméticos disponíveis em Python.
"""

print("=" * 60)
print("OPERADORES ARITMÉTICOS EM PYTHON")
print("=" * 60)

# Valores de exemplo
a = 15
b = 4

print(f"\nValores de exemplo: a = {a}, b = {b}\n")

# ============================================
# 1. ADIÇÃO (+)
# ============================================
print("1. ADIÇÃO (+):")
print("-" * 60)
soma = a + b
print(f"  {a} + {b} = {soma}")

# Concatenação de strings (também usa +)
texto1 = "Olá"
texto2 = "Mundo"
texto_completo = texto1 + " " + texto2
print(f"  '{texto1}' + ' ' + '{texto2}' = '{texto_completo}'")

# ============================================
# 2. SUBTRAÇÃO (-)
# ============================================
print("\n2. SUBTRAÇÃO (-):")
print("-" * 60)
subtracao = a - b
print(f"  {a} - {b} = {subtracao}")

# Resultado negativo
print(f"  {b} - {a} = {b - a}")

# ============================================
# 3. MULTIPLICAÇÃO (*)
# ============================================
print("\n3. MULTIPLICAÇÃO (*):")
print("-" * 60)
multiplicacao = a * b
print(f"  {a} × {b} = {multiplicacao}")

# Repetição de strings (também usa *)
texto = "Python "
texto_repetido = texto * 3
print(f"  '{texto}' * 3 = '{texto_repetido}'")

# ============================================
# 4. DIVISÃO (/)
# ============================================
print("\n4. DIVISÃO (/):")
print("-" * 60)
divisao = a / b
print(f"  {a} ÷ {b} = {divisao}")

# Divisão sempre retorna float
print(f"  Tipo do resultado: {type(divisao).__name__}")
print(f"  Mesmo com inteiros: 10 / 2 = {10 / 2} (tipo: {type(10 / 2).__name__})")

# ============================================
# 5. DIVISÃO INTEIRA (//)
# ============================================
print("\n5. DIVISÃO INTEIRA (//):")
print("-" * 60)
divisao_inteira = a // b
print(f"  {a} // {b} = {divisao_inteira} (descarta a parte decimal)")

# Exemplo com resto
print(f"  {a} ÷ {b} = {a // b} com resto {a % b}")
print(f"  {17} // {3} = {17 // 3} (descarta .666...)")

# ============================================
# 6. MÓDULO/RESTO (%)
# ============================================
print("\n6. MÓDULO/RESTO (%):")
print("-" * 60)
resto = a % b
print(f"  {a} % {b} = {resto} (resto da divisão)")

# Verificar se número é par ou ímpar
numero = 7
eh_par = (numero % 2) == 0
print(f"\n  Verificar se {numero} é par:")
print(f"  {numero} % 2 = {numero % 2}")
print(f"  É par? {eh_par}")

# Exemplo com múltiplos de 3
numero2 = 15
eh_multiplo_de_3 = (numero2 % 3) == 0
print(f"\n  Verificar se {numero2} é múltiplo de 3:")
print(f"  {numero2} % 3 = {numero2 % 3}")
print(f"  É múltiplo de 3? {eh_multiplo_de_3}")

# ============================================
# 7. EXPONENCIAÇÃO (**)
# ============================================
print("\n7. EXPONENCIAÇÃO (**):")
print("-" * 60)
potencia = a ** b
print(f"  {a} ** {b} = {a ** b} (15 elevado a 4)")

print(f"\n  Outros exemplos:")
print(f"  2 ** 3 = {2 ** 3} (2 elevado a 3)")
print(f"  10 ** 2 = {10 ** 2} (10 elevado a 2)")
print(f"  2 ** 0.5 = {2 ** 0.5:.4f} (raiz quadrada de 2)")

# ============================================
# OPERADORES DE ATRIBUIÇÃO ABREVIADA
# ============================================
print("\n" + "=" * 60)
print("OPERADORES DE ATRIBUIÇÃO ABREVIADA")
print("=" * 60)

x = 10
print(f"\nValor inicial: x = {x}")

x += 5  # Equivale a: x = x + 5
print(f"x += 5  → x = {x}")

x -= 3  # Equivale a: x = x - 3
print(f"x -= 3  → x = {x}")

x *= 2  # Equivale a: x = x * 2
print(f"x *= 2  → x = {x}")

x /= 4  # Equivale a: x = x / 4
print(f"x /= 4  → x = {x}")

x //= 2  # Equivale a: x = x // 2
print(f"x //= 2 → x = {x}")

x **= 3  # Equivale a: x = x ** 3
print(f"x **= 3 → x = {x}")

x %= 5   # Equivale a: x = x % 5
print(f"x %= 5  → x = {x}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Cálculo de média
print("\nExemplo 1: Cálculo de média")
print("-" * 60)
nota1 = 8.5
nota2 = 7.0
nota3 = 9.2
media = (nota1 + nota2 + nota3) / 3
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média = ({nota1} + {nota2} + {nota3}) / 3 = {media:.2f}")

# Exemplo 2: Conversão de unidades
print("\nExemplo 2: Conversão de temperatura")
print("-" * 60)
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = ({celsius} × 9/5) + 32 = {fahrenheit}°F")

# Exemplo 3: Cálculo de área e perímetro
print("\nExemplo 3: Cálculo de área e perímetro")
print("-" * 60)
largura = 10
altura = 5
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"Retângulo: {largura}m × {altura}m")
print(f"Área = {largura} × {altura} = {area}m²")
print(f"Perímetro = 2 × ({largura} + {altura}) = {perimetro}m")

# Exemplo 4: Operações com tempo
print("\nExemplo 4: Conversão de segundos")
print("-" * 60)
total_segundos = 3665
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"{total_segundos} segundos = {horas}h {minutos}min {segundos}s")

