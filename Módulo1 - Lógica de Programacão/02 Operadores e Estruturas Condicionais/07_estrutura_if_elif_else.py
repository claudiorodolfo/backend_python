"""
07 - Estrutura Condicional if-elif-else

Este arquivo demonstra a estrutura condicional if-elif-else em Python,
usada para múltiplas condições.
"""

print("=" * 60)
print("ESTRUTURA CONDICIONAL IF-ELIF-ELSE")
print("=" * 60)

# ============================================
# IF-ELIF-ELSE BÁSICO
# ============================================
print("\n1. IF-ELIF-ELSE BÁSICO:")
print("-" * 60)

print("Estrutura:")
print("  if condicao1:")
print("      # Executa se condicao1 for True")
print("  elif condicao2:")
print("      # Executa se condicao1 for False e condicao2 for True")
print("  elif condicao3:")
print("      # Executa se anteriores forem False e condicao3 for True")
print("  else:")
print("      # Executa se todas forem False")
print()

# Exemplo prático
nota = 8.5
print(f"Nota: {nota}")

if nota >= 9.0:
    print("  ✓ Conceito A - Excelente!")
elif nota >= 7.0:
    print("  ✓ Conceito B - Bom")
elif nota >= 5.0:
    print("  ⚠️  Conceito C - Regular (Recuperação)")
else:
    print("  ✗ Conceito D - Reprovado")

# ============================================
# MÚLTIPLOS ELIF
# ============================================
print("\n2. MÚLTIPLOS ELIF:")
print("-" * 60)

idade = 25
print(f"Idade: {idade} anos")

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
elif idade < 75:
    categoria = "Idoso"
else:
    categoria = "Terceira idade"

print(f"  Categoria: {categoria}")

# ============================================
# IF-ELIF SEM ELSE
# ============================================
print("\n3. IF-ELIF SEM ELSE:")
print("-" * 60)

temperatura = 22
print(f"Temperatura: {temperatura}°C")

if temperatura > 30:
    print("  ☀️  Muito quente!")
elif temperatura > 20:
    print("  🌤️  Temperatura agradável")
elif temperatura > 10:
    print("  🌡️  Frio moderado")
elif temperatura > 0:
    print("  ❄️  Frio")
# Sem else: se nenhuma condição for atendida, nada acontece

# ============================================
# ELIF COM CONDIÇÕES COMPLEXAS
# ============================================
print("\n4. ELIF COM CONDIÇÕES COMPLEXAS:")
print("-" * 60)

saldo = 500.00
tem_cartao_premium = False
tem_cartao_basico = True

print(f"Saldo: R$ {saldo:.2f}")
print(f"Cartão Premium: {tem_cartao_premium}")
print(f"Cartão Básico: {tem_cartao_basico}")

if saldo >= 10000 and tem_cartao_premium:
    limite_saque = 5000.00
    print(f"  ✓ Limite VIP: R$ {limite_saque:.2f}")
elif saldo >= 5000 and (tem_cartao_premium or tem_cartao_basico):
    limite_saque = 2000.00
    print(f"  ✓ Limite Intermediário: R$ {limite_saque:.2f}")
elif saldo >= 1000 and tem_cartao_basico:
    limite_saque = 500.00
    print(f"  ✓ Limite Básico: R$ {limite_saque:.2f}")
else:
    limite_saque = 100.00
    print(f"  Limite Padrão: R$ {limite_saque:.2f}")

# ============================================
# ELIF COM OPERADORES LÓGICOS
# ============================================
print("\n5. ELIF COM OPERADORES LÓGICOS:")
print("-" * 60)

hora = 14
dia_semana = "segunda"
feriado = False

print(f"Hora: {hora}h")
print(f"Dia da semana: {dia_semana}")
print(f"É feriado: {feriado}")

if feriado:
    status_loja = "Fechada - Feriado"
elif dia_semana == "domingo":
    status_loja = "Fechada - Domingo"
elif dia_semana == "sabado" and hora < 14:
    status_loja = "Aberta - Sábado (até 14h)"
elif (dia_semana != "sabado" and dia_semana != "domingo") and (hora >= 9 and hora < 18):
    status_loja = "Aberta - Horário comercial"
else:
    status_loja = "Fechada - Fora do horário"

print(f"  Status da loja: {status_loja}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Sistema de desconto por faixa
print("\nExemplo 1: Sistema de desconto por valor")
print("-" * 60)
valor_compra = 850.00
print(f"Valor da compra: R$ {valor_compra:.2f}")

if valor_compra >= 1000:
    desconto = 0.20  # 20%
    categoria = "Desconto Premium"
elif valor_compra >= 500:
    desconto = 0.15  # 15%
    categoria = "Desconto Intermediário"
elif valor_compra >= 200:
    desconto = 0.10  # 10%
    categoria = "Desconto Básico"
else:
    desconto = 0.0  # 0%
    categoria = "Sem desconto"

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"  {categoria}: {desconto * 100:.0f}%")
print(f"  Desconto: R$ {valor_desconto:.2f}")
print(f"  Valor final: R$ {valor_final:.2f}")

# Exemplo 2: Classificação de notas
print("\nExemplo 2: Sistema de notas")
print("-" * 60)
nota = 7.5
print(f"Nota: {nota}")

if nota >= 9.0:
    conceito = "A"
    status = "Excelente"
elif nota >= 8.0:
    conceito = "B"
    status = "Muito Bom"
elif nota >= 7.0:
    conceito = "C"
    status = "Bom"
elif nota >= 6.0:
    conceito = "D"
    status = "Regular"
elif nota >= 5.0:
    conceito = "E"
    status = "Suficiente"
else:
    conceito = "F"
    status = "Insuficiente"

print(f"  Conceito: {conceito}")
print(f"  Status: {status}")

# Exemplo 3: Sistema de mensalidade por idade
print("\nExemplo 3: Mensalidade por faixa etária")
print("-" * 60)
idade = 35
print(f"Idade: {idade} anos")

if idade < 18:
    mensalidade = 50.00
    categoria = "Júnior"
elif idade < 30:
    mensalidade = 80.00
    categoria = "Adulto Jovem"
elif idade < 50:
    mensalidade = 100.00
    categoria = "Adulto"
elif idade < 65:
    mensalidade = 90.00
    categoria = "Maturidade"
else:
    mensalidade = 70.00
    categoria = "Senior"

print(f"  Categoria: {categoria}")
print(f"  Mensalidade: R$ {mensalidade:.2f}")

# ============================================
# COMPARAÇÃO: MÚLTIPLOS IF vs ELIF
# ============================================
print("\n" + "=" * 60)
print("MÚLTIPLOS IF vs ELIF")
print("=" * 60)

print("\n⚠️  IMPORTANTE: Diferença entre múltiplos IF e ELIF:")
print()

print("MÚLTIPLOS IF (avalia TODOS):")
print("-" * 60)
numero = 15
if numero > 10:
    print(f"  IF 1: {numero} > 10 → True")
if numero > 20:
    print(f"  IF 2: {numero} > 20 → False (não executa)")
if numero > 5:
    print(f"  IF 3: {numero} > 5 → True")

print("\nELIF (para na PRIMEIRA condição verdadeira):")
print("-" * 60)
numero = 15
if numero > 10:
    print(f"  ELIF 1: {numero} > 10 → True (executa e PARA)")
elif numero > 20:
    print(f"  ELIF 2: {numero} > 20 → Não avalia (anterior foi True)")
elif numero > 5:
    print(f"  ELIF 3: {numero} > 5 → Não avalia (anterior foi True)")

# ============================================
# BOAS PRÁTICAS
# ============================================
print("\n" + "=" * 60)
print("BOAS PRÁTICAS COM IF-ELIF-ELSE")
print("=" * 60)

print("\n✓ Use elif para condições mutuamente exclusivas:")
print("  • Quando apenas UMA condição deve ser verdadeira")
print("  • Classificações e categorizações")

print("\n✓ Use múltiplos if quando todas podem ser verdadeiras:")
print("  • Quando múltiplas condições podem acontecer ao mesmo tempo")

print("\n✓ Coloque a condição mais específica primeiro:")
print("  • if numero > 100:  (mais específico)")
print("  • elif numero > 10: (menos específico)")

print("\n✓ Use else como padrão:")
print("  • Captura todos os casos não previstos")
print("  • Evita bugs silenciosos")

