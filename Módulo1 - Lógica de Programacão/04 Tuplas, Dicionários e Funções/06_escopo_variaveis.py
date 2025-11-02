"""
06 - Escopo de Variáveis

Este arquivo demonstra escopo de variáveis em funções.
"""

print("=" * 60)
print("ESCOPO DE VARIÁVEIS")
print("=" * 60)

# ============================================
# VARIÁVEIS LOCAIS
# ============================================
print("\n1. VARIÁVEIS LOCAIS:")
print("-" * 60)

def minha_funcao():
    """Função com variável local"""
    x = 10  # Variável local
    print(f"  Dentro da função: x = {x}")

x = 5  # Variável global (fora da função)
print(f"Fora da função: x = {x}")
minha_funcao()
print(f"Fora da função (após chamada): x = {x}")

# ============================================
# VARIÁVEIS GLOBAIS
# ============================================
print("\n2. VARIÁVEIS GLOBAIS:")
print("-" * 60)

contador = 0  # Variável global

def incrementar():
    """Incrementa variável global"""
    global contador
    contador += 1
    print(f"  Contador dentro: {contador}")

print(f"Contador antes: {contador}")
incrementar()
print(f"Contador depois: {contador}")

# ============================================
# VARIÁVEL LOCAL vs GLOBAL
# ============================================
print("\n3. VARIÁVEL LOCAL vs GLOBAL:")
print("-" * 60)

numero = 100  # Global

def teste():
    numero = 50  # Local (não afeta global)
    print(f"  Dentro (local): {numero}")

print(f"Fora (global): {numero}")
teste()
print(f"Fora (global, inalterado): {numero}")

# ============================================
# BOAS PRÁTICAS
# ============================================
print("\n" + "=" * 60)
print("BOAS PRÁTICAS")
print("=" * 60)

print("\n✓ Evite variáveis globais quando possível")
print("✓ Use parâmetros e retorno")
print("✓ Variáveis locais são mais seguras")
print("✓ Use 'global' apenas quando necessário")

# Exemplo melhor: usar parâmetros
print("\nExemplo melhor (sem global):")
print("-" * 60)

def somar(a, b):
    """Soma dois números"""
    resultado = a + b  # Local
    return resultado

total = somar(10, 5)
print(f"somar(10, 5) = {total}")

