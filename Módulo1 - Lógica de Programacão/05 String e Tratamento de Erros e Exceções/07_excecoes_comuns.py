"""
07 - Tratamento de Exceções Comuns

Este arquivo demonstra tratamento de exceções comuns.
"""

print("=" * 60)
print("TRATAMENTO DE EXCEÇÕES COMUNS")
print("=" * 60)

# ============================================
# ValueError
# ============================================
print("\n1. ValueError:")
print("-" * 60)

try:
    numero = int("abc")
except ValueError:
    print("  Erro: valor não pode ser convertido para int")

# ============================================
# TypeError
# ============================================
print("\n2. TypeError:")
print("-" * 60)

try:
    resultado = "10" + 5
except TypeError:
    print("  Erro: tipos incompatíveis para operação")

# ============================================
# IndexError
# ============================================
print("\n3. IndexError:")
print("-" * 60)

lista = [1, 2, 3]
try:
    valor = lista[10]
except IndexError:
    print("  Erro: índice fora do range da lista")

# ============================================
# KeyError
# ============================================
print("\n4. KeyError:")
print("-" * 60)

dic = {"nome": "João"}
try:
    idade = dic["idade"]
except KeyError:
    print("  Erro: chave não existe no dicionário")

# ============================================
# ZeroDivisionError
# ============================================
print("\n5. ZeroDivisionError:")
print("-" * 60)

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  Erro: divisão por zero não permitida")

# ============================================
# TRATAR MÚLTIPLAS EXCEÇÕES
# ============================================
print("\n6. TRATAR MÚLTIPLAS EXCEÇÕES:")
print("-" * 60)

def processar_numero(entrada):
    """Processa entrada numérica"""
    try:
        numero = int(entrada)
        resultado = 100 / numero
        return resultado
    except ValueError:
        return "Erro: não é um número"
    except ZeroDivisionError:
        return "Erro: não pode dividir por zero"

print(f"processar_numero('50'): {processar_numero('50')}")
print(f"processar_numero('abc'): {processar_numero('abc')}")
print(f"processar_numero('0'): {processar_numero('0')}")

