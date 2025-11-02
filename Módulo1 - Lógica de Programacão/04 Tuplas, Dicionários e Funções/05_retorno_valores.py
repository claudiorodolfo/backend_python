"""
05 - Retorno de Valores

Este arquivo demonstra retorno de valores em funções.
"""

print("=" * 60)
print("RETORNO DE VALORES")
print("=" * 60)

# ============================================
# RETORNO SIMPLES
# ============================================
print("\n1. RETORNO SIMPLES:")
print("-" * 60)

def dobrar(numero):
    """Dobra um número"""
    return numero * 2

resultado = dobrar(5)
print(f"dobrar(5) = {resultado}")

# ============================================
# RETORNO MÚLTIPLO (TUPLA)
# ============================================
print("\n2. RETORNO MÚLTIPLO:")
print("-" * 60)

def calcular_stats(numeros):
    """Calcula soma e média"""
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media  # Retorna tupla

valores = [10, 20, 30, 40]
total, media = calcular_stats(valores)

print(f"Números: {valores}")
print(f"Soma: {total}")
print(f"Média: {media:.2f}")

# ============================================
# RETORNO CONDICIONAL
# ============================================
print("\n3. RETORNO CONDICIONAL:")
print("-" * 60)

def maior_numero(a, b):
    """Retorna maior número"""
    if a > b:
        return a
    else:
        return b

print(f"maior_numero(10, 5) = {maior_numero(10, 5)}")
print(f"maior_numero(3, 8) = {maior_numero(3, 8)}")

# ============================================
# FUNÇÃO SEM RETORNO EXPLÍCITO
# ============================================
print("\n4. FUNÇÃO SEM RETORNO:")
print("-" * 60)

def exibir_mensagem(texto):
    """Apenas exibe mensagem"""
    print(f"  {texto}")
    # Sem return - retorna None implicitamente

resultado = exibir_mensagem("Olá!")
print(f"  Retorno: {resultado}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo: Validar e processar
print("\nExemplo: Função que valida e retorna")
print("-" * 60)

def processar_idade(idade):
    """Valida e classifica idade"""
    if idade < 0:
        return None, "Idade inválida"
    elif idade < 18:
        return "menor", "Menor de idade"
    elif idade < 65:
        return "adulto", "Adulto"
    else:
        return "idoso", "Idoso"

categoria, mensagem = processar_idade(25)
print(f"Idade 25: {categoria} - {mensagem}")

categoria, mensagem = processar_idade(70)
print(f"Idade 70: {categoria} - {mensagem}")

