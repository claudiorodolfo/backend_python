"""
02 - Métodos Úteis de Strings

Este arquivo demonstra métodos úteis de strings.
"""

print("=" * 60)
print("MÉTODOS ÚTEIS DE STRINGS")
print("=" * 60)

# ============================================
# LOWER() E UPPER()
# ============================================
print("\n1. LOWER() E UPPER():")
print("-" * 60)

texto = "Python é Fantástico"
print(f"Original: '{texto}'")
print(f"lower(): '{texto.lower()}'")
print(f"upper(): '{texto.upper()}'")

# ============================================
# STRIP()
# ============================================
print("\n2. STRIP():")
print("-" * 60)

texto_com_espacos = "  Python  "
print(f"Original: '{texto_com_espacos}'")
print(f"strip(): '{texto_com_espacos.strip()}'")
print(f"lstrip(): '{texto_com_espacos.lstrip()}'")
print(f"rstrip(): '{texto_com_espacos.rstrip()}'")

# ============================================
# SPLIT()
# ============================================
print("\n3. SPLIT():")
print("-" * 60)

frase = "Python é uma linguagem poderosa"
palavras = frase.split()
print(f"Frase: '{frase}'")
print(f"split(): {palavras}")

email = "usuario@email.com"
partes = email.split("@")
print(f"\nEmail: '{email}'")
print(f"split('@'): {partes}")

# ============================================
# JOIN()
# ============================================
print("\n4. JOIN():")
print("-" * 60)

palavras = ["Python", "é", "fantástico"]
frase = " ".join(palavras)
print(f"Lista: {palavras}")
print(f"' '.join(): '{frase}'")

numeros = ["1", "2", "3"]
sequencia = "-".join(numeros)
print(f"\nLista: {numeros}")
print(f"'-'.join(): '{sequencia}'")

# ============================================
# OUTROS MÉTODOS ÚTEIS
# ============================================
print("\n5. OUTROS MÉTODOS ÚTEIS:")
print("-" * 60)

texto = "Python"

print(f"texto.replace('P', 'J'): {texto.replace('P', 'J')}")
print(f"texto.startswith('P'): {texto.startswith('P')}")
print(f"texto.endswith('n'): {texto.endswith('n')}")
print(f"texto.count('t'): {texto.count('t')}")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'Python'.isalpha(): {'Python'.isalpha()}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Normalizar entrada
print("\nExemplo 1: Normalizar entrada")
print("-" * 60)
entrada = "  JOAO SILVA  "
nome_normalizado = entrada.strip().lower().title()
print(f"Original: '{entrada}'")
print(f"Normalizado: '{nome_normalizado}'")

# Exemplo 2: Processar CSV simples
print("\nExemplo 2: Processar dados separados")
print("-" * 60)
dados = "João,25,São Paulo"
partes = dados.split(",")
nome, idade, cidade = partes
print(f"Dados: '{dados}'")
print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

