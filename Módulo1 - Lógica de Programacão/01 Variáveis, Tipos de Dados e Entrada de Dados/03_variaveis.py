"""
03 - Declaração e Uso de Variáveis

Este arquivo demonstra como declarar e usar variáveis em Python.
"""

print("=" * 60)
print("DECLARAÇÃO E USO DE VARIÁVEIS")
print("=" * 60)

# ============================================
# DECLARAÇÃO DE VARIÁVEIS
# ============================================
print("\n1. DECLARAÇÃO SIMPLES:")
print("-" * 60)

# Python não exige declaração explícita de tipo
nome = "Ana"
idade = 30
salario = 5000.00

print(f"nome = '{nome}'")
print(f"idade = {idade}")
print(f"salario = {salario}")

# ============================================
# REATRIBUIÇÃO DE VALORES
# ============================================
print("\n2. REATRIBUIÇÃO DE VALORES:")
print("-" * 60)

contador = 0
print(f"contador inicial = {contador}")

contador = 10
print(f"contador após reatribuição = {contador}")

contador = contador + 5
print(f"contador após incremento = {contador}")

# Forma abreviada de incremento
contador += 3
print(f"contador após contador += 3 = {contador}")

# ============================================
# MÚLTIPLAS ATRIBUIÇÕES
# ============================================
print("\n3. MÚLTIPLAS ATRIBUIÇÕES:")
print("-" * 60)

# Atribuir mesmo valor a múltiplas variáveis
x = y = z = 0
print(f"x = y = z = 0")
print(f"x = {x}, y = {y}, z = {z}")

# Atribuir valores diferentes em uma linha
nome, idade, cidade = "Pedro", 28, "São Paulo"
print(f"\nnome, idade, cidade = 'Pedro', 28, 'São Paulo'")
print(f"nome = {nome}, idade = {idade}, cidade = {cidade}")

# Trocar valores entre variáveis
print("\n4. TROCAR VALORES ENTRE VARIÁVEIS:")
print("-" * 60)
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")

a, b = b, a  # Troca elegante em Python
print(f"Depois (a, b = b, a): a = {a}, b = {b}")

# ============================================
# BOAS PRÁTICAS DE NOMENCLATURA
# ============================================
print("\n5. BOAS PRÁTICAS DE NOMENCLATURA:")
print("-" * 60)

# ✓ Use snake_case (recomendado em Python)
nome_usuario = "João"
idade_usuario = 25
email_usuario = "joao@email.com"

print("✓ Correto (snake_case):")
print(f"  nome_usuario = '{nome_usuario}'")
print(f"  idade_usuario = {idade_usuario}")
print(f"  email_usuario = '{email_usuario}'")

# ✗ Evite estilos inconsistentes
print("\n✗ Evite:")
print("  NomeUsuario = 'João'  # PascalCase (para classes)")
print("  nomeUsuario = 'João'  # camelCase (outras linguagens)")
print("  nome-usuario = 'João' # hífens (não funciona)")

# ============================================
# REGRAS DE NOMENCLATURA
# ============================================
print("\n6. REGRAS DE NOMENCLATURA:")
print("-" * 60)

print("✓ Pode começar com letra ou underscore: _variavel")
print("✓ Pode conter letras, números e underscores: var_123")
print("✓ Case-sensitive: nome ≠ Nome ≠ NOME")
print("✗ Não pode começar com número: 123var (inválido)")
print("✗ Não pode usar palavras reservadas: if, for, def, etc.")

# Exemplos válidos
_variavel = "válido"
variavel123 = "válido"
VARIAVEL_CONSTANTE = "válido"

print(f"\nExemplos válidos:")
print(f"  _variavel = '{_variavel}'")
print(f"  variavel123 = '{variavel123}'")
print(f"  VARIAVEL_CONSTANTE = '{VARIAVEL_CONSTANTE}'")

# ============================================
# VARIÁVEIS COM TIPOS DIFERENTES
# ============================================
print("\n7. VARIÁVEIS PODEM MUDAR DE TIPO:")
print("-" * 60)

variavel = 10
print(f"variavel = {variavel} → tipo: {type(variavel).__name__}")

variavel = "agora é uma string"
print(f"variavel = '{variavel}' → tipo: {type(variavel).__name__}")

variavel = 3.14
print(f"variavel = {variavel} → tipo: {type(variavel).__name__}")

print("\n⚠️  ATENÇÃO: Embora seja possível, não é recomendado")
print("   mudar o tipo de uma variável durante a execução.")
print("   Mantenha consistência de tipo para facilitar a leitura do código.")

# ============================================
# EXEMPLO PRÁTICO COMPLETO
# ============================================
print("\n" + "=" * 60)
print("EXEMPLO PRÁTICO: Sistema de Usuário")
print("=" * 60)

# Dados do usuário
usuario_nome = "Carlos"
usuario_idade = 32
usuario_email = "carlos@exemplo.com"
usuario_ativo = True
usuario_saldo = 1500.75

# Exibir informações
print(f"\nDados do usuário:")
print(f"  Nome: {usuario_nome}")
print(f"  Idade: {usuario_ativo}")
print(f"  Email: {usuario_email}")
print(f"  Status: {'Ativo' if usuario_ativo else 'Inativo'}")
print(f"  Saldo: R$ {usuario_saldo:.2f}")

# Atualizar saldo (simulando uma transação)
deposito = 500.00
usuario_saldo += deposito
print(f"\nApós depósito de R$ {deposito:.2f}:")
print(f"  Novo saldo: R$ {usuario_saldo:.2f}")

