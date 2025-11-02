"""
06 - Lançando Exceções (raise)

Este arquivo demonstra como lançar exceções.
"""

print("=" * 60)
print("LANÇANDO EXCEÇÕES COM RAISE")
print("=" * 60)

# ============================================
# RAISE SIMPLES
# ============================================
print("\n1. RAISE SIMPLES:")
print("-" * 60)

def verificar_idade(idade):
    """Valida idade"""
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade > 120:
        raise ValueError("Idade não pode ser maior que 120")
    return True

try:
    verificar_idade(25)
    print("  Idade válida!")
except ValueError as e:
    print(f"  Erro: {e}")

# ============================================
# VALIDAÇÃO DE DADOS
# ============================================
print("\n2. VALIDAÇÃO DE DADOS:")
print("-" * 60)

def processar_email(email):
    """Valida email"""
    if not "@" in email:
        raise ValueError("Email inválido: falta @")
    if not "." in email:
        raise ValueError("Email inválido: falta domínio")
    return email

try:
    email = processar_email("usuario@email.com")
    print(f"  Email válido: {email}")
except ValueError as e:
    print(f"  Erro: {e}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo: Divisão segura
print("\nExemplo: Divisão com validação")
print("-" * 60)

def dividir_seguro(a, b):
    """Divide dois números com validação"""
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return a / b

try:
    resultado = dividir_seguro(10, 2)
    print(f"10 / 2 = {resultado}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")

