"""
01 - Operações Básicas com Strings

Este arquivo demonstra operações básicas com strings.
"""

print("=" * 60)
print("OPERAÇÕES BÁSICAS COM STRINGS")
print("=" * 60)

# ============================================
# CONCATENAÇÃO
# ============================================
print("\n1. CONCATENAÇÃO:")
print("-" * 60)

nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(f"'{nome}' + ' ' + '{sobrenome}' = '{nome_completo}'")

# ============================================
# REPETIÇÃO
# ============================================
print("\n2. REPETIÇÃO:")
print("-" * 60)

texto = "Python "
print(f"'{texto}' * 3 = '{texto * 3}'")

# ============================================
# INDEXAÇÃO
# ============================================
print("\n3. INDEXAÇÃO:")
print("-" * 60)

palavra = "Python"
print(f"String: '{palavra}'")
print(f"  palavra[0] = '{palavra[0]}'")
print(f"  palavra[1] = '{palavra[1]}'")
print(f"  palavra[-1] = '{palavra[-1]}'")
print(f"  palavra[-2] = '{palavra[-2]}'")

# ============================================
# FATIAMENTO
# ============================================
print("\n4. FATIAMENTO:")
print("-" * 60)

texto = "Programação"
print(f"Texto: '{texto}'")
print(f"  texto[0:7] = '{texto[0:7]}'")
print(f"  texto[:4] = '{texto[:4]}'")
print(f"  texto[4:] = '{texto[4:]}'")
print(f"  texto[::-1] = '{texto[::-1]}'")

# ============================================
# VERIFICAÇÃO
# ============================================
print("\n5. VERIFICAÇÃO:")
print("-" * 60)

texto = "Python é fantástico"
print(f"Texto: '{texto}'")
print(f"  'Python' in texto? {'Python' in texto}")
print(f"  'Java' in texto? {'Java' in texto}")
print(f"  len(texto) = {len(texto)}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Construir string
print("\nExemplo 1: Construir string")
print("-" * 60)
nome = "Maria"
idade = 25
mensagem = nome + " tem " + str(idade) + " anos"
print(f"Mensagem: '{mensagem}'")

# Exemplo 2: Extrair partes
print("\nExemplo 2: Extrair partes")
print("-" * 60)
email = "usuario@email.com"
usuario = email[:email.index("@")]
dominio = email[email.index("@")+1:]
print(f"Email: {email}")
print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")

