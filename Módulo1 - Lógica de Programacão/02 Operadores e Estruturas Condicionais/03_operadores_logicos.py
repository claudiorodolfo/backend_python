"""
03 - Operadores Lógicos

Este arquivo demonstra os operadores lógicos (and, or, not) em Python.
"""

print("=" * 60)
print("OPERADORES LÓGICOS")
print("=" * 60)

# Valores booleanos de exemplo
a = True
b = False

print(f"\nValores de exemplo: a = {a}, b = {b}\n")

# ============================================
# 1. OPERADOR AND (E)
# ============================================
print("1. OPERADOR AND (E):")
print("-" * 60)
print("  Retorna True apenas quando AMBAS as condições são True")
print()

resultado1 = a and a
resultado2 = a and b
resultado3 = b and a
resultado4 = b and b

print(f"  {a} and {a} → {resultado1}")
print(f"  {a} and {b} → {resultado2}")
print(f"  {b} and {a} → {resultado3}")
print(f"  {b} and {b} → {resultado4}")

# ============================================
# 2. OPERADOR OR (OU)
# ============================================
print("\n2. OPERADOR OR (OU):")
print("-" * 60)
print("  Retorna True quando PELO MENOS UMA condição é True")
print()

resultado1 = a or a
resultado2 = a or b
resultado3 = b or a
resultado4 = b or b

print(f"  {a} or {a} → {resultado1}")
print(f"  {a} or {b} → {resultado2}")
print(f"  {b} or {a} → {resultado3}")
print(f"  {b} or {b} → {resultado4}")

# ============================================
# 3. OPERADOR NOT (NÃO)
# ============================================
print("\n3. OPERADOR NOT (NÃO):")
print("-" * 60)
print("  Inverte o valor booleano")
print()

resultado1 = not a
resultado2 = not b

print(f"  not {a} → {resultado1}")
print(f"  not {b} → {resultado2}")

# ============================================
# TABELA VERDADE COMPLETA
# ============================================
print("\n" + "=" * 60)
print("TABELA VERDADE COMPLETA")
print("=" * 60)

print("\nAND (E):")
print("  A     | B     | A and B")
print("  ------|-------|---------")
print(f"  {str(True):5} | {str(True):5} | {True and True}")
print(f"  {str(True):5} | {str(False):5} | {True and False}")
print(f"  {str(False):5} | {str(True):5} | {False and True}")
print(f"  {str(False):5} | {str(False):5} | {False and False}")

print("\nOR (OU):")
print("  A     | B     | A or B")
print("  ------|-------|---------")
print(f"  {str(True):5} | {str(True):5} | {True or True}")
print(f"  {str(True):5} | {str(False):5} | {True or False}")
print(f"  {str(False):5} | {str(True):5} | {False or True}")
print(f"  {str(False):5} | {str(False):5} | {False or False}")

print("\nNOT (NÃO):")
print("  A     | not A")
print("  ------|-------")
print(f"  {str(True):5} | {not True}")
print(f"  {str(False):5} | {not False}")

# ============================================
# COMBINAÇÕES DE OPERADORES
# ============================================
print("\n" + "=" * 60)
print("COMBINAÇÕES DE OPERADORES")
print("=" * 60)

# Combinações complexas
x = True
y = False
z = True

print(f"\nValores: x = {x}, y = {y}, z = {z}")

resultado1 = x and y or z
print(f"\n  {x} and {y} or {z} → {resultado1}")

resultado2 = x and (y or z)
print(f"  {x} and ({y} or {z}) → {resultado2}")

resultado3 = not x and y
print(f"  not {x} and {y} → {resultado3}")

resultado4 = not (x and y)
print(f"  not ({x} and {y}) → {resultado4}")

# ============================================
# OPERADORES LÓGICOS COM VALORES NÃO-BOOLEANOS
# ============================================
print("\n" + "=" * 60)
print("OPERADORES LÓGICOS COM VALORES NÃO-BOOLEANOS")
print("=" * 60)

print("\nPython trata valores como True ou False em contextos lógicos:")
print()

# Valores "truthy" (considerados True)
print("  Valores 'truthy' (True em contexto lógico):")
print(f"    {42} → {bool(42)}")
print(f"    {3.14} → {bool(3.14)}")
print(f"    'texto' → {bool('texto')}")
print(f"    [1, 2, 3] → {bool([1, 2, 3])}")

# Valores "falsy" (considerados False)
print("\n  Valores 'falsy' (False em contexto lógico):")
print(f"    {0} → {bool(0)}")
print(f"    {0.0} → {bool(0.0)}")
print(f"    '' → {bool('')}")
print(f"    [] → {bool([])}")
print(f"    None → {bool(None)}")

# Exemplo prático
print("\n  Exemplo com and/or e valores não-booleanos:")
valor = "Python" or "Default"
print(f"    'Python' or 'Default' → '{valor}'")

valor = "" or "Default"
print(f"    '' or 'Default' → '{valor}'")

numero = 0 and 100
print(f"    {0} and {100} → {numero}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Validação de múltiplas condições
print("\nExemplo 1: Validação de login")
print("-" * 60)
usuario_correto = True
senha_correta = False

pode_fazer_login = usuario_correto and senha_correta
print(f"Usuário correto: {usuario_correto}")
print(f"Senha correta: {senha_correta}")
print(f"  Pode fazer login? ({usuario_correto} and {senha_correta}) → {pode_fazer_login}")

# Exemplo 2: Verificação de condições complexas
print("\nExemplo 2: Verificação de desconto")
print("-" * 60)
tem_cartao_fidelidade = True
compra_acima_100 = True
primeira_compra = False

tem_desconto = (tem_cartao_fidelidade or primeira_compra) and compra_acima_100
print(f"Tem cartão fidelidade: {tem_cartao_fidelidade}")
print(f"Compra acima de R$ 100: {compra_acima_100}")
print(f"Primeira compra: {primeira_compra}")
print(f"  Tem desconto? (({tem_cartao_fidelidade} or {primeira_compra}) and {compra_acima_100}) → {tem_desconto}")

# Exemplo 3: Validação de idade e status
print("\nExemplo 3: Validação de acesso")
print("-" * 60)
idade = 20
maior_idade = idade >= 18
tem_autorizacao = False
ativo = True

pode_acessar = maior_idade and (tem_autorizacao or ativo)
print(f"Idade: {idade} anos")
print(f"Maior de idade: {maior_idade}")
print(f"Tem autorização: {tem_autorizacao}")
print(f"Está ativo: {ativo}")
print(f"  Pode acessar? ({maior_idade} and ({tem_autorizacao} or {ativo})) → {pode_acessar}")

# Exemplo 4: Negação de condições
print("\nExemplo 4: Verificação de status")
print("-" * 60)
usuario_bloqueado = False
conta_expirada = False

pode_usar_sistema = not (usuario_bloqueado or conta_expirada)
print(f"Usuário bloqueado: {usuario_bloqueado}")
print(f"Conta expirada: {conta_expirada}")
print(f"  Pode usar sistema? (not ({usuario_bloqueado} or {conta_expirada})) → {pode_usar_sistema}")

# ============================================
# PRECEDÊNCIA DOS OPERADORES LÓGICOS
# ============================================
print("\n" + "=" * 60)
print("PRECEDÊNCIA DOS OPERADORES LÓGICOS")
print("=" * 60)

print("\nOrdem de precedência:")
print("  1. not (maior precedência)")
print("  2. and")
print("  3. or (menor precedência)")

print("\nExemplo:")
x, y, z = True, False, True
print(f"  Valores: x = {x}, y = {y}, z = {z}")

resultado1 = not x and y or z
print(f"\n  not x and y or z")
print(f"  = (not x) and y) or z")
print(f"  = ((not {x}) and {y}) or {z}")
print(f"  = ({not x and y}) or {z}")
print(f"  = {resultado1}")

resultado2 = not (x and y) or z
print(f"\n  not (x and y) or z")
print(f"  = (not ({x} and {y})) or {z}")
print(f"  = ({not (x and y)}) or {z}")
print(f"  = {resultado2}")

print("\n💡 DICA: Use parênteses para deixar a precedência clara!")

