"""
06 - Casting de Dados (Conversão de Tipos)

Este arquivo demonstra como converter dados entre diferentes tipos em Python.
"""

print("=" * 60)
print("CASTING DE DADOS - CONVERSÃO DE TIPOS")
print("=" * 60)

# ============================================
# CONVERSÃO PARA INT (int())
# ============================================
print("\n1. CONVERSÃO PARA INT (int()):")
print("-" * 60)

# String numérica para int
numero_string = "42"
numero_int = int(numero_string)
print(f'"42" (string) → int("42") = {numero_int} → tipo: {type(numero_int).__name__}')

# Float para int (trunca a parte decimal)
numero_float = 3.99
numero_int_do_float = int(numero_float)
print(f'{numero_float} (float) → int({numero_float}) = {numero_int_do_float}')
print(f'⚠️  ATENÇÃO: A parte decimal é descartada, não arredondada!')

# Bool para int
print(f'\nTrue → int(True) = {int(True)}')
print(f'False → int(False) = {int(False)}')

# ============================================
# CONVERSÃO PARA FLOAT (float())
# ============================================
print("\n2. CONVERSÃO PARA FLOAT (float()):")
print("-" * 60)

# String numérica para float
numero_string = "3.14"
numero_float = float(numero_string)
print(f'"3.14" (string) → float("3.14") = {numero_float} → tipo: {type(numero_float).__name__}')

# Int para float
numero_int = 42
numero_float_do_int = float(numero_int)
print(f'{numero_int} (int) → float({numero_int}) = {numero_float_do_int}')

# String com número inteiro para float
numero_string_int = "100"
numero_float_int = float(numero_string_int)
print(f'"100" (string) → float("100") = {numero_float_int}')

# ============================================
# CONVERSÃO PARA STR (str())
# ============================================
print("\n3. CONVERSÃO PARA STR (str()):")
print("-" * 60)

# Int para string
numero_int = 123
numero_string = str(numero_int)
print(f'{numero_int} (int) → str({numero_int}) = "{numero_string}" → tipo: {type(numero_string).__name__}')

# Float para string
numero_float = 45.67
numero_string_float = str(numero_float)
print(f'{numero_float} (float) → str({numero_float}) = "{numero_string_float}"')

# Bool para string
valor_bool = True
valor_string_bool = str(valor_bool)
print(f'{valor_bool} (bool) → str({valor_bool}) = "{valor_string_bool}"')

# None para string
valor_none = None
valor_string_none = str(valor_none)
print(f'{valor_none} (None) → str({valor_none}) = "{valor_string_none}"')

# ============================================
# CONVERSÃO PARA BOOL (bool())
# ============================================
print("\n4. CONVERSÃO PARA BOOL (bool()):")
print("-" * 60)

# Números para bool (0 é False, qualquer outro é True)
print(f'int(0) → bool(0) = {bool(0)}')
print(f'int(1) → bool(1) = {bool(1)}')
print(f'int(-5) → bool(-5) = {bool(-5)}')
print(f'float(0.0) → bool(0.0) = {bool(0.0)}')
print(f'float(3.14) → bool(3.14) = {bool(3.14)}')

# Strings para bool (string vazia é False, qualquer outra é True)
print(f'\nstr("") → bool("") = {bool("")}')
print(f'str("texto") → bool("texto") = {bool("texto")}')
print(f'str("False") → bool("False") = {bool("False")}  ⚠️  "False" é uma string não-vazia!')

# None para bool
print(f'\nNone → bool(None) = {bool(None)}')

# ============================================
# CASTING COM INPUT() - CASO COMUM
# ============================================
print("\n5. CASTING COM input() - CASO IMPORTANTE:")
print("-" * 60)

print('input() sempre retorna STRING, então precisa de conversão:')
print()
print('# Exemplo 1: Entrada numérica')
print('  idade_str = input("Digite sua idade: ")  # Recebe "25" (string)')
print('  idade = int(idade_str)  # Converte para int')
print('  print(f"Você tem {idade} anos")')
print()
print('# Exemplo 2: Entrada numérica direta (mais comum)')
print('  idade = int(input("Digite sua idade: "))  # Conversão direta')
print('  preco = float(input("Digite o preço: "))  # Para decimais')
print()
print('⚠️  ATENÇÃO: Se o usuário digitar algo que não possa ser convertido,')
print('   ocorrerá um erro (ValueError). Veremos tratamento de erros depois!')

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n6. EXEMPLOS PRÁTICOS:")
print("-" * 60)

# Exemplo 1: Calculadora com entrada do usuário (simulado)
print("\nExemplo 1: Conversão em operações matemáticas")
print("-" * 50)

# Simulando entrada do usuário (seria input() em uso real)
numero1_str = "15"  # Simulando input()
numero2_str = "7"   # Simulando input()

# Conversão necessária para operações matemáticas
numero1 = int(numero1_str)
numero2 = int(numero2_str)

soma = numero1 + numero2
print(f'{numero1_str} + {numero2_str} = {soma}')
print(f'  → Sem conversão: "15" + "7" = "{numero1_str + numero2_str}" (concatenação)')
print(f'  → Com conversão: {numero1} + {numero2} = {soma} (adição)')

# Exemplo 2: Formatação de saída
print("\nExemplo 2: Formatação de números")
print("-" * 50)

valor = 1234.5678
print(f'Valor original: {valor}')
print(f'Formatado como string: R$ {valor:.2f}')
print(f'Convertido para int (perde decimais): {int(valor)}')

# Exemplo 3: Validação de entrada
print("\nExemplo 3: Validação com conversão")
print("-" * 50)

idade_str = "25"  # Simulando input()
try:
    idade = int(idade_str)
    print(f'Idade válida: {idade} anos')
except ValueError:
    print('Erro: Idade deve ser um número!')

# ============================================
# RESUMO E DICAS
# ============================================
print("\n" + "=" * 60)
print("RESUMO DE CONVERSÕES")
print("=" * 60)

conversoes = [
    ("Para INT", "int()", "string numérica, float (trunca), bool"),
    ("Para FLOAT", "float()", "string numérica, int"),
    ("Para STR", "str()", "qualquer tipo (converte tudo para texto)"),
    ("Para BOOL", "bool()", "qualquer tipo (0/None/'' são False, resto True)")
]

print("\nTipos de conversão disponíveis:")
for tipo, funcao, aceita in conversoes:
    print(f"  {tipo:12} → {funcao:10} → Aceita: {aceita}")

print("\n" + "=" * 60)
print("DICAS IMPORTANTES")
print("=" * 60)
print("✓ input() sempre retorna string → use int() ou float() para números")
print("✓ Verifique se a conversão é possível antes de tentar")
print("✓ int() de float descarta decimais (não arredonda)")
print("✓ bool() de string: '' é False, qualquer outro texto é True")
print("✓ str() converte qualquer coisa para texto (útil para print)")

