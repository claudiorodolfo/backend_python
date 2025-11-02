"""
08 - Boas Práticas na Escrita de Condicionais

Este arquivo demonstra boas práticas e padrões recomendados
para escrever código condicional limpo e legível.
"""

print("=" * 60)
print("BOAS PRÁTICAS NA ESCRITA DE CONDICIONAIS")
print("=" * 60)

# ============================================
# 1. USE VARIÁVEIS BOOLEANAS PARA CLAREZA
# ============================================
print("\n1. USE VARIÁVEIS BOOLEANAS PARA CLAREZA:")
print("-" * 60)

idade = 25
tem_cartao = True
compra = 150.00

# ❌ Evite: condição complexa diretamente no if
print("❌ Evite:")
print("  if idade >= 18 and tem_cartao and compra > 100:")

# ✅ Prefira: variáveis booleanas com nomes descritivos
print("\n✅ Prefira:")
maior_idade = idade >= 18
pode_desconto = maior_idade and tem_cartao and compra > 100

if pode_desconto:
    print("  Código mais legível e fácil de entender")

# ============================================
# 2. EVITE CONDICIONAIS ANINHADAS EXCESSIVAS
# ============================================
print("\n2. EVITE CONDICIONAIS ANINHADAS EXCESSIVAS:")
print("-" * 60)

# ❌ Evite: muitos níveis de aninhamento
print("❌ Evite (muitos níveis):")
print("  if condicao1:")
print("      if condicao2:")
print("          if condicao3:")
print("              if condicao4:")
print("                  # código muito aninhado")

# ✅ Prefira: early return ou múltiplas condições
print("\n✅ Prefira (early return):")

def verificar_acesso(idade, tem_cartao, ativo):
    """Exemplo de função com early return"""
    if not ativo:
        return False
    if idade < 18:
        return False
    if not tem_cartao:
        return False
    return True

print("  Usa early return para evitar aninhamento excessivo")

# ============================================
# 3. USE OPERADOR TERNÁRIO PARA VALORES SIMPLES
# ============================================
print("\n3. USE OPERADOR TERNÁRIO (PARA CASOS SIMPLES):")
print("-" * 60)

idade = 20

# ❌ Evite: if-else simples para atribuição
print("❌ Evite:")
print("  if idade >= 18:")
print("      status = 'Maior'")
print("  else:")
print("      status = 'Menor'")

# ✅ Prefira: operador ternário
print("\n✅ Prefira:")
status = "Maior" if idade >= 18 else "Menor"
print(f"  status = 'Maior' if idade >= 18 else 'Menor'")
print(f"  Resultado: {status}")

print("\n⚠️  Use apenas para expressões simples e legíveis!")

# ============================================
# 4. ORGANIZE CONDIÇÕES DE FORMA LÓGICA
# ============================================
print("\n4. ORGANIZE CONDIÇÕES DE FORMA LÓGICA:")
print("-" * 60)

nota = 8.5

# ✅ Ordem lógica: do mais específico ao mais genérico
print("✅ Ordem correta (específico → genérico):")
if nota >= 9.0:
    print("  Excelente")
elif nota >= 7.0:
    print("  Bom")
elif nota >= 5.0:
    print("  Regular")
else:
    print("  Insuficiente")

# ❌ Ordem incorreta causaria problemas
print("\n❌ Ordem incorreta (causaria problemas):")
print("  if nota >= 5.0:  # Muito genérico primeiro!")
print("      print('Regular')")
print("  elif nota >= 9.0:  # Nunca seria avaliado")
print("      print('Excelente')")

# ============================================
# 5. USE PARÊNTESES PARA CLAREZA
# ============================================
print("\n5. USE PARÊNTESES PARA CLAREZA:")
print("-" * 60)

idade = 25
tem_cartao = True
compra = 150.00

# ❌ Evite: dependência apenas da precedência
print("❌ Evite:")
print("  if idade >= 18 and tem_cartao or compra > 100:")
print("  (pode ser confuso qual operador tem precedência)")

# ✅ Prefira: parênteses explícitos
print("\n✅ Prefira:")
print("  if (idade >= 18 and tem_cartao) or compra > 100:")
print("  (intenção clara e explícita)")

# ============================================
# 6. NOMES DESCRITIVOS PARA VARIÁVEIS
# ============================================
print("\n6. NOMES DESCRITIVOS PARA VARIÁVEIS:")
print("-" * 60)

# ❌ Evite: nomes genéricos
print("❌ Evite:")
print("  x = 25")
print("  y = True")
print("  if x >= 18 and y:")

# ✅ Prefira: nomes descritivos
print("\n✅ Prefira:")
idade_usuario = 25
tem_autorizacao = True
if idade_usuario >= 18 and tem_autorizacao:
    print("  Código auto-explicativo!")

# ============================================
# 7. EVITE NEGAÇÕES DESNECESSÁRIAS
# ============================================
print("\n7. EVITE NEGAÇÕES DESNECESSÁRIAS:")
print("-" * 60)

usuario_ativo = True

# ❌ Evite: negação desnecessária
print("❌ Evite:")
print("  if not usuario_ativo == False:")
print("  if not usuario_ativo != True:")

# ✅ Prefira: forma positiva
print("\n✅ Prefira:")
if usuario_ativo:
    print("  if usuario_ativo:")
    print("  (mais direto e legível)")

# Ou se realmente precisa verificar False:
if not usuario_ativo:
    print("  if not usuario_ativo:")

# ============================================
# 8. SEPARE LÓGICA COMPLEXA EM FUNÇÕES
# ============================================
print("\n8. SEPARE LÓGICA COMPLEXA EM FUNÇÕES:")
print("-" * 60)

# ❌ Evite: lógica complexa no meio do código
print("❌ Evite:")
print("  if (idade >= 18 and idade <= 65 and")
print("      tem_cartao and not bloqueado and")
print("      (saldo > 100 or tem_credito)):")

# ✅ Prefira: extrair para função
print("\n✅ Prefira:")

def pode_fazer_saque(idade, tem_cartao, bloqueado, saldo, tem_credito):
    """Verifica se pode fazer saque"""
    idade_valida = 18 <= idade <= 65
    cartao_ok = tem_cartao and not bloqueado
    recursos_suficientes = saldo > 100 or tem_credito
    return idade_valida and cartao_ok and recursos_suficientes

print("  Função com nome descritivo e lógica separada")

# ============================================
# 9. CONSISTÊNCIA DE ESTILO
# ============================================
print("\n9. CONSISTÊNCIA DE ESTILO:")
print("-" * 60)

print("✅ Mantenha consistência em todo o código:")
print("  • Mesma indentação (4 espaços)")
print("  • Mesmo estilo de nomes (snake_case)")
print("  • Mesma estrutura de condições")
print("  • Mesmo padrão de comentários")

# ============================================
# 10. DOCUMENTE CONDIÇÕES COMPLEXAS
# ============================================
print("\n10. DOCUMENTE CONDIÇÕES COMPLEXAS:")
print("-" * 60)

# ✅ Use comentários para explicar "porquê", não "o quê"
print("✅ Boa documentação:")
print("  # Regra de negócio: desconto apenas para clientes VIP")
print("  # com compras acima de R$ 500 e cartão ativo")
if compra > 500 and tem_cartao:
    print("  Aplica desconto")

# ❌ Evite comentários óbvios
print("\n❌ Evite comentários óbvios:")
print("  # Verifica se compra é maior que 500")
print("  if compra > 500:")
print("  (o código já é claro)")

# ============================================
# RESUMO DAS BOAS PRÁTICAS
# ============================================
print("\n" + "=" * 60)
print("RESUMO DAS BOAS PRÁTICAS")
print("=" * 60)

praticas = [
    "Use variáveis booleanas com nomes descritivos",
    "Evite aninhamento excessivo (max 2-3 níveis)",
    "Use operador ternário para atribuições simples",
    "Organize condições do específico ao genérico",
    "Use parênteses para deixar precedência clara",
    "Prefira nomes descritivos (idade_usuario, não x)",
    "Evite negações desnecessárias",
    "Extraia lógica complexa para funções",
    "Mantenha consistência de estilo",
    "Documente o 'porquê', não o 'o quê'"
]

print("\nTop 10 boas práticas:")
for i, pratica in enumerate(praticas, 1):
    print(f"  {i:2}. {pratica}")

print("\n💡 Lembre-se: Código é lido muito mais vezes do que escrito!")
print("   Invista tempo em escrever código claro e legível.")

