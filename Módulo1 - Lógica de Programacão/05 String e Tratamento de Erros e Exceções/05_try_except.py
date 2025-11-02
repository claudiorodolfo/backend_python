"""
05 - Bloco try-except

Este arquivo demonstra tratamento de exceções.
"""

print("=" * 60)
print("BLOCO TRY-EXCEPT")
print("=" * 60)

# ============================================
# TRY-EXCEPT BÁSICO
# ============================================
print("\n1. TRY-EXCEPT BÁSICO:")
print("-" * 60)

try:
    numero = int("123")
    print(f"  Conversão bem-sucedida: {numero}")
except ValueError:
    print("  Erro: não foi possível converter para inteiro")

# ============================================
# TRATAR EXCEÇÃO ESPECÍFICA
# ============================================
print("\n2. TRATAR EXCEÇÃO ESPECÍFICA:")
print("-" * 60)

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  Erro: divisão por zero não permitida!")

# ============================================
# MÚLTIPLAS EXCEÇÕES
# ============================================
print("\n3. MÚLTIPLAS EXCEÇÕES:")
print("-" * 60)

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except TypeError:
        return "Erro: tipo inválido"

print(f"dividir(10, 2) = {dividir(10, 2)}")
print(f"dividir(10, 0) = {dividir(10, 0)}")

# ============================================
# EXCEPT GENÉRICO
# ============================================
print("\n4. EXCEPT GENÉRICO:")
print("-" * 60)

try:
    valor = int("abc")
except Exception as e:
    print(f"  Erro ocorreu: {type(e).__name__}: {e}")

# ============================================
# TRY-EXCEPT-ELSE
# ============================================
print("\n5. TRY-EXCEPT-ELSE:")
print("-" * 60)

try:
    numero = int("42")
except ValueError:
    print("  Erro na conversão")
else:
    print(f"  Conversão bem-sucedida: {numero}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Validar entrada numérica
print("\nExemplo 1: Validar entrada")
print("-" * 60)
entrada = "25"  # Simulado

try:
    idade = int(entrada)
    print(f"Idade válida: {idade}")
except ValueError:
    print("Erro: digite um número válido")

# Exemplo 2: Acessar lista com índice
print("\nExemplo 2: Acessar lista")
print("-" * 60)
lista = [10, 20, 30]

try:
    valor = lista[5]
except IndexError:
    print("Erro: índice fora do range")

