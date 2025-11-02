"""
04 - Exceções Básicas

Este arquivo demonstra o que são exceções.
"""

print("=" * 60)
print("O QUE SÃO EXCEÇÕES")
print("=" * 60)

print("\nExceções são erros que ocorrem durante a execução:")
print("-" * 60)

print("\nExemplos comuns de exceções:")
print("  • ValueError: valor inválido")
print("  • TypeError: tipo incorreto")
print("  • IndexError: índice fora do range")
print("  • KeyError: chave não existe no dicionário")
print("  • ZeroDivisionError: divisão por zero")

print("\nSem tratamento, exceções interrompem o programa:")
print("-" * 60)

# Exemplos que causariam exceção (comentados)
print("\nExemplos (comentados para não interromper):")
print("  # ValueError:")
print("  # int('abc')  # ValueError: invalid literal")

print("  # ZeroDivisionError:")
print("  # 10 / 0  # ZeroDivisionError: division by zero")

print("  # IndexError:")
print("  # lista = [1, 2, 3]")
print("  # lista[10]  # IndexError: list index out of range")

print("\n💡 Solução: usar try-except para tratar exceções!")

