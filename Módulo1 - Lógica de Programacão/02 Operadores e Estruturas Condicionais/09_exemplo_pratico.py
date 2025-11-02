"""
09 - Exemplo Prático Completo

Este arquivo combina todos os conceitos aprendidos em um exemplo prático:
um sistema completo de validação e processamento de pedidos.
"""

print("=" * 70)
print("SISTEMA DE VALIDAÇÃO E PROCESSAMENTO DE PEDIDOS")
print("Demonstração prática de todos os conceitos aprendidos")
print("=" * 70)

# ============================================
# CONSTANTES DO SISTEMA
# ============================================
VALOR_MINIMO_PEDIDO = 50.00
VALOR_FRETE_GRATIS = 200.00
DESCONTO_VIP = 0.15  # 15%
DESCONTO_BASICO = 0.10  # 10%
IDADE_MINIMA = 18
IDADE_MAXIMA = 120

# ============================================
# DADOS DO CLIENTE (simulados)
# ============================================
print("\n=== DADOS DO CLIENTE ===")
cliente_nome = "Maria Silva"
cliente_idade = 25
cliente_email = "maria@email.com"
cliente_eh_vip = True
cliente_tem_cartao = True
cliente_conta_ativa = True

print(f"Nome: {cliente_nome}")
print(f"Idade: {cliente_idade} anos")
print(f"Email: {cliente_email}")
print(f"Cliente VIP: {cliente_eh_vip}")
print(f"Tem cartão: {cliente_tem_cartao}")
print(f"Conta ativa: {cliente_conta_ativa}")

# ============================================
# DADOS DO PEDIDO (simulados)
# ============================================
print("\n=== DADOS DO PEDIDO ===")
valor_pedido = 250.00
quantidade_itens = 3
codigo_promocional = "DESC10"

print(f"Valor do pedido: R$ {valor_pedido:.2f}")
print(f"Quantidade de itens: {quantidade_itens}")
print(f"Código promocional: {codigo_promocional}")

# ============================================
# VALIDAÇÃO DO CLIENTE
# ============================================
print("\n" + "=" * 70)
print("ETAPA 1: VALIDAÇÃO DO CLIENTE")
print("=" * 70)

# Verificações usando operadores relacionais e lógicos
idade_valida = IDADE_MINIMA <= cliente_idade <= IDADE_MAXIMA
email_valido = "@" in cliente_email and "." in cliente_email

pode_fazer_pedido = (
    idade_valida and
    email_valido and
    cliente_conta_ativa
)

print(f"\nVerificações:")
print(f"  Idade válida ({IDADE_MINIMA}-{IDADE_MAXIMA}): {idade_valida}")
print(f"  Email válido: {email_valido}")
print(f"  Conta ativa: {cliente_conta_ativa}")
print(f"\n  → Cliente pode fazer pedido? {pode_fazer_pedido}")

# ============================================
# VALIDAÇÃO DO PEDIDO
# ============================================
print("\n" + "=" * 70)
print("ETAPA 2: VALIDAÇÃO DO PEDIDO")
print("=" * 70)

# Operadores relacionais e lógicos
valor_valido = valor_pedido >= VALOR_MINIMO_PEDIDO
quantidade_valida = quantidade_itens > 0

pedido_valido = valor_valido and quantidade_valida

print(f"\nVerificações:")
print(f"  Valor acima do mínimo (R$ {VALOR_MINIMO_PEDIDO:.2f}): {valor_valido}")
print(f"  Quantidade válida: {quantidade_valida}")
print(f"\n  → Pedido válido? {pedido_valido}")

# ============================================
# CÁLCULO DE DESCONTO (usando if-elif-else)
# ============================================
print("\n" + "=" * 70)
print("ETAPA 3: CÁLCULO DE DESCONTO")
print("=" * 70)

desconto_aplicado = 0.0
tipo_desconto = "Sem desconto"

# Estrutura if-elif-else
if cliente_eh_vip and valor_pedido >= 200:
    desconto_aplicado = valor_pedido * DESCONTO_VIP
    tipo_desconto = "VIP (15%)"
elif cliente_tem_cartao and valor_pedido >= 100:
    desconto_aplicado = valor_pedido * DESCONTO_BASICO
    tipo_desconto = "Básico (10%)"
elif codigo_promocional == "DESC10" and valor_pedido >= 100:
    desconto_aplicado = valor_pedido * 0.10
    tipo_desconto = "Promocional (10%)"
else:
    desconto_aplicado = 0.0
    tipo_desconto = "Sem desconto"

valor_com_desconto = valor_pedido - desconto_aplicado

print(f"\nDesconto aplicado:")
print(f"  Tipo: {tipo_desconto}")
print(f"  Valor do desconto: R$ {desconto_aplicado:.2f}")
print(f"  Valor após desconto: R$ {valor_com_desconto:.2f}")

# ============================================
# CÁLCULO DE FRETE (usando if-else)
# ============================================
print("\n" + "=" * 70)
print("ETAPA 4: CÁLCULO DE FRETE")
print("=" * 70)

# Estrutura if-else simples
if valor_com_desconto >= VALOR_FRETE_GRATIS:
    valor_frete = 0.00
    frete_gratis = True
else:
    # Frete calculado: R$ 0.50 por item
    valor_frete = quantidade_itens * 0.50
    frete_gratis = False

print(f"\nCálculo de frete:")
if frete_gratis:
    print(f"  ✓ FRETE GRÁTIS (pedido acima de R$ {VALOR_FRETE_GRATIS:.2f})")
else:
    print(f"  Frete: R$ 0.50 por item")
    print(f"  Quantidade de itens: {quantidade_itens}")
    print(f"  Valor do frete: R$ {valor_frete:.2f}")

# ============================================
# VALOR FINAL
# ============================================
print("\n" + "=" * 70)
print("ETAPA 5: RESUMO FINAL")
print("=" * 70)

valor_final = valor_com_desconto + valor_frete

print(f"\n{'RESUMO DO PEDIDO':^70}")
print("-" * 70)
print(f"  Valor do pedido:        R$ {valor_pedido:>10.2f}")
print(f"  Desconto ({tipo_desconto}):  R$ {desconto_aplicado:>10.2f}")
print(f"  Subtotal:                R$ {valor_com_desconto:>10.2f}")
print(f"  Frete:                   R$ {valor_frete:>10.2f}")
print("-" * 70)
print(f"  VALOR FINAL:             R$ {valor_final:>10.2f}")

# ============================================
# VALIDAÇÃO FINAL E STATUS
# ============================================
print("\n" + "=" * 70)
print("ETAPA 6: VALIDAÇÃO FINAL")
print("=" * 70)

# Usando operadores lógicos para validação final
pedido_aprovado = (
    pode_fazer_pedido and
    pedido_valido and
    valor_final > 0
)

if pedido_aprovado:
    print("\n  ✓✓✓ PEDIDO APROVADO ✓✓✓")
    print(f"\n  Cliente: {cliente_nome}")
    print(f"  Email: {cliente_email}")
    print(f"  Valor a pagar: R$ {valor_final:.2f}")
    if frete_gratis:
        print(f"  🎁 Bônus: Frete grátis incluído!")
else:
    print("\n  ✗✗✗ PEDIDO REJEITADO ✗✗✗")
    print("\n  Motivos possíveis:")
    if not pode_fazer_pedido:
        print("    • Cliente não atende aos requisitos")
    if not pedido_valido:
        print("    • Pedido não atende aos requisitos")
    if valor_final <= 0:
        print("    • Valor final inválido")

# ============================================
# CONCEITOS UTILIZADOS
# ============================================
print("\n" + "=" * 70)
print("CONCEITOS UTILIZADOS NESTE EXEMPLO")
print("=" * 70)

print("\n✓ Operadores Aritméticos:")
print("  • +, -, *, / para cálculos")
print("  • Comparações numéricas")

print("\n✓ Operadores Relacionais:")
print("  • >=, <=, >, <, == para comparações")
print("  • Verificação de intervalos")

print("\n✓ Operadores Lógicos:")
print("  • and, or para combinar condições")
print("  • Validações complexas")

print("\n✓ Estrutura if:")
print("  • Validações simples")

print("\n✓ Estrutura if-else:")
print("  • Decisões binárias (frete grátis ou não)")

print("\n✓ Estrutura if-elif-else:")
print("  • Múltiplas condições (tipos de desconto)")

print("\n✓ Boas Práticas:")
print("  • Variáveis com nomes descritivos")
print("  • Constantes em UPPER_CASE")
print("  • Código organizado e legível")
print("  • Comentários quando necessário")

