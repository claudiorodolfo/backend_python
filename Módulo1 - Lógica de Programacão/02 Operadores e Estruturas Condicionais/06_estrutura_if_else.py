"""
06 - Estrutura Condicional if-else

Este arquivo demonstra a estrutura condicional if-else em Python.
"""

print("=" * 60)
print("ESTRUTURA CONDICIONAL IF-ELSE")
print("=" * 60)

# ============================================
# IF-ELSE BÁSICO
# ============================================
print("\n1. IF-ELSE BÁSICO:")
print("-" * 60)

print("Estrutura:")
print("  if condicao:")
print("      # Executa se condição for True")
print("  else:")
print("      # Executa se condição for False")
print()

# Exemplo prático
idade = 17
print(f"Idade: {idade} anos")

if idade >= 18:
    print("  ✓ Maior de idade")
    print("  ✓ Pode votar")
else:
    print("  ✗ Menor de idade")
    print("  ✗ Não pode votar")

# ============================================
# IF-ELSE COM DIFERENTES CASOS
# ============================================
print("\n2. DIFERENTES CASOS DE USO:")
print("-" * 60)

# Exemplo 1: Verificação de paridade
print("\nExemplo 1: Verificar se número é par ou ímpar")
numero = 7
if numero % 2 == 0:
    print(f"  O número {numero} é PAR")
else:
    print(f"  O número {numero} é ÍMPAR")

# Exemplo 2: Validação de acesso
print("\nExemplo 2: Validação de login")
usuario_correto = True
senha_correta = False

if usuario_correto and senha_correta:
    print("  ✓ Login realizado com sucesso!")
else:
    print("  ✗ Usuário ou senha incorretos")

# Exemplo 3: Verificação de saldo
print("\nExemplo 3: Verificação de saldo")
saldo = 100.00
valor_saque = 150.00

print(f"Saldo: R$ {saldo:.2f}")
print(f"Saque solicitado: R$ {valor_saque:.2f}")

if saldo >= valor_saque:
    novo_saldo = saldo - valor_saque
    print(f"  ✓ Saque aprovado!")
    print(f"  ✓ Novo saldo: R$ {novo_saldo:.2f}")
else:
    print(f"  ✗ Saldo insuficiente")
    print(f"  ✗ Faltam R$ {valor_saque - saldo:.2f}")

# ============================================
# IF-ELSE ANINHADOS
# ============================================
print("\n3. IF-ELSE ANINHADOS:")
print("-" * 60)

nota = 8.5
print(f"Nota: {nota}")

if nota >= 7.0:
    print("  ✓ Aprovado")
    if nota >= 9.0:
        print("  ✓ Excelente desempenho!")
    else:
        print("  ✓ Bom desempenho")
else:
    print("  ✗ Reprovado")
    if nota >= 5.0:
        print("  ⚠️  Pode fazer recuperação")
    else:
        print("  ✗ Precisa refazer o curso")

# ============================================
# IF-ELSE COM RETORNO DE VALOR
# ============================================
print("\n4. IF-ELSE PARA ATRIBUIR VALORES:")
print("-" * 60)

# Padrão: atribuir valor baseado em condição
idade = 25

# Forma tradicional
if idade >= 18:
    status = "Maior de idade"
else:
    status = "Menor de idade"

print(f"Idade: {idade} anos → Status: {status}")

# Forma com operador ternário (Python suporta)
status2 = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Usando operador ternário: {status2}")

# ============================================
# IF-ELSE COM MÚLTIPLAS CONDIÇÕES
# ============================================
print("\n5. IF-ELSE COM MÚLTIPLAS CONDIÇÕES:")
print("-" * 60)

temperatura = 25
tem_chuva = False

print(f"Temperatura: {temperatura}°C")
print(f"Tem chuva: {tem_chuva}")

if temperatura > 25 and not tem_chuva:
    print("  ☀️  Clima perfeito para praia!")
else:
    if temperatura <= 25:
        print("  🌡️  Está muito frio para praia")
    if tem_chuva:
        print("  🌧️  Está chovendo")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Sistema de desconto
print("\nExemplo 1: Sistema de desconto")
print("-" * 60)
valor_compra = 150.00
tem_cartao = True
LIMITE_DESCONTO = 100.00

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Tem cartão fidelidade: {tem_cartao}")

if valor_compra >= LIMITE_DESCONTO and tem_cartao:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"  ✓ Desconto aplicado: 10%")
    print(f"  ✓ Desconto: R$ {desconto:.2f}")
    print(f"  ✓ Valor final: R$ {valor_final:.2f}")
else:
    print(f"  ✗ Sem desconto")
    print(f"  ✗ Valor final: R$ {valor_compra:.2f}")

# Exemplo 2: Validação de senha
print("\nExemplo 2: Validação de senha")
print("-" * 60)
senha = "MinhaSenh@123"
TAMANHO_MINIMO = 8

print(f"Tamanho mínimo exigido: {TAMANHO_MINIMO} caracteres")
print(f"Tamanho da senha: {len(senha)} caracteres")

if len(senha) >= TAMANHO_MINIMO:
    print("  ✓ Senha tem tamanho adequado")
    if any(c.isupper() for c in senha) and any(c.islower() for c in senha):
        print("  ✓ Senha tem maiúsculas e minúsculas")
    else:
        print("  ⚠️  Senha deveria ter maiúsculas e minúsculas")
else:
    print("  ✗ Senha muito curta!")

# Exemplo 3: Classificação de IMC
print("\nExemplo 3: Classificação de IMC")
print("-" * 60)
peso = 70.0  # kg
altura = 1.75  # metros
imc = peso / (altura ** 2)

print(f"Peso: {peso}kg")
print(f"Altura: {altura}m")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"  Classificação: {classificacao}")

# ============================================
# BOAS PRÁTICAS
# ============================================
print("\n" + "=" * 60)
print("BOAS PRÁTICAS COM IF-ELSE")
print("=" * 60)

print("\n✓ Use else quando há apenas duas opções claras:")
print("  • Par/ímpar")
print("  • Aprovado/Reprovado")
print("  • Válido/Inválido")

print("\n✓ Evite else vazio:")
print("  ❌ Evite: if condicao: ... else: pass")
print("  ✅ Prefira: if condicao: ... (sem else)")

print("\n✓ Mantenha blocos if-else balanceados:")
print("  • Evite blocos muito diferentes em tamanho")
print("  • Considere usar elif para múltiplas condições")

