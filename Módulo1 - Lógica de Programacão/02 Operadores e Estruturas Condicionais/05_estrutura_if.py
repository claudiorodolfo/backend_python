"""
05 - Estrutura Condicional Básica (if)

Este arquivo demonstra a estrutura condicional if em Python.
"""

print("=" * 60)
print("ESTRUTURA CONDICIONAL IF")
print("=" * 60)

# ============================================
# IF BÁSICO
# ============================================
print("\n1. IF BÁSICO:")
print("-" * 60)

idade = 18

print(f"Idade: {idade} anos")
if idade >= 18:
    print("  ✓ Você é maior de idade!")
    print("  ✓ Pode votar nas eleições")

print("\nFluxo: Se a condição for True, executa o bloco.")
print("       Se for False, pula o bloco.")

# ============================================
# IF COM INDENTAÇÃO
# ============================================
print("\n2. IMPORTÂNCIA DA INDENTAÇÃO:")
print("-" * 60)

print("Em Python, a indentação define os blocos de código:")
print()

print("Código:")
print('  if condicao:')
print('      print("Dentro do if")  # 4 espaços (ou 1 tab)')
print('  print("Fora do if")       # Sem indentação')
print()

# Exemplo prático
temperatura = 25
print(f"Temperatura: {temperatura}°C")

if temperatura > 30:
    print("  Está muito quente!")
    print("  Use protetor solar")

print("  (Esta linha sempre executa - está fora do if)")

# ============================================
# IF COM DIFERENTES CONDIÇÕES
# ============================================
print("\n3. DIFERENTES TIPOS DE CONDIÇÕES:")
print("-" * 60)

# Condição numérica
print("\nCondição numérica:")
nota = 8.5
if nota >= 7.0:
    print(f"  Nota {nota}: Aprovado!")

# Condição booleana
print("\nCondição booleana:")
usuario_ativo = True
if usuario_ativo:
    print("  Usuário está ativo no sistema")

# Condição com string
print("\nCondição com string:")
nome = "Python"
if nome == "Python":
    print(f"  O nome '{nome}' foi reconhecido!")

# Condição com operador lógico
print("\nCondição com operador lógico:")
idade = 25
tem_cartao = True
if idade >= 18 and tem_cartao:
    print("  Pode fazer compras com desconto!")

# ============================================
# IF COM EXPRESSÕES COMPLEXAS
# ============================================
print("\n4. IF COM EXPRESSÕES COMPLEXAS:")
print("-" * 60)

email = "usuario@email.com"
senha_correta = True

print(f"Email: {email}")
print(f"Senha correta: {senha_correta}")

# Condição composta
if "@" in email and senha_correta:
    print("  ✓ Login válido!")
    print("  ✓ Acesso permitido ao sistema")

# ============================================
# IF COM VARIÁVEIS BOOLEANAS EXPLÍCITAS
# ============================================
print("\n5. IF COM VARIÁVEIS BOOLEANAS:")
print("-" * 60)

# Boa prática: usar variáveis booleanas para clareza
idade = 20
maior_idade = idade >= 18
tem_autorizacao = True

print(f"Idade: {idade}")
print(f"Maior de idade: {maior_idade}")
print(f"Tem autorização: {tem_autorizacao}")

# Mais legível do que: if idade >= 18 and tem_autorizacao:
pode_acessar = maior_idade and tem_autorizacao
if pode_acessar:
    print("  ✓ Acesso permitido!")

# ============================================
# IF ANINHADOS (NESTED IF)
# ============================================
print("\n6. IF ANINHADOS:")
print("-" * 60)

saldo = 1000.00
limite_saque = 500.00
valor_saque = 300.00

print(f"Saldo: R$ {saldo:.2f}")
print(f"Limite de saque: R$ {limite_saque:.2f}")
print(f"Valor solicitado: R$ {valor_saque:.2f}")

if valor_saque <= limite_saque:
    print("\n  ✓ Valor dentro do limite")
    if valor_saque <= saldo:
        print("  ✓ Saldo suficiente")
        novo_saldo = saldo - valor_saque
        print(f"  ✓ Saque aprovado! Novo saldo: R$ {novo_saldo:.2f}")
    else:
        print("  ✗ Saldo insuficiente")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Verificação de número positivo
print("\nExemplo 1: Verificar se número é positivo")
print("-" * 60)
numero = 15
if numero > 0:
    print(f"  O número {numero} é positivo")

# Exemplo 2: Validação de email
print("\nExemplo 2: Validação básica de email")
print("-" * 60)
email = "teste@exemplo.com"
if "@" in email and "." in email:
    print(f"  O email '{email}' parece válido")

# Exemplo 3: Verificação de acesso
print("\nExemplo 3: Sistema de acesso")
print("-" * 60)
is_admin = True
is_autenticado = True

if is_admin and is_autenticado:
    print("  ✓ Acesso de administrador concedido")
    print("  ✓ Permissões completas ativadas")

# ============================================
# IMPORTANTE: INDENTAÇÃO EM PYTHON
# ============================================
print("\n" + "=" * 60)
print("IMPORTANTE: INDENTAÇÃO EM PYTHON")
print("=" * 60)

print("\n⚠️  REGRAS DE INDENTAÇÃO:")
print("  • Python usa indentação para definir blocos (não chaves {})")
print("  • Recomendado: 4 espaços por nível (padrão PEP 8)")
print("  • Pode usar TAB, mas mantenha consistência")
print("  • Não misture espaços e tabs!")

print("\nExemplo de indentação correta:")
print('  if condicao:')
print('      print("Dentro do if")  # 4 espaços')
print('      print("Ainda dentro")  # 4 espaços')
print('  print("Fora do if")        # 0 espaços')

print("\n💡 DICA: A maioria dos editores configura TAB como 4 espaços automaticamente")

