"""
04 - Diferença entre Constantes e Variáveis

Este arquivo demonstra a diferença entre constantes e variáveis,
e as convenções de nomenclatura em Python.
"""

print("=" * 60)
print("CONSTANTES vs VARIÁVEIS")
print("=" * 60)

# ============================================
# VARIÁVEIS (podem mudar)
# ============================================
print("\n1. VARIÁVEIS - Valores podem ser alterados:")
print("-" * 60)

# Variáveis comuns usam snake_case em minúsculas
nome = "Ana"
idade = 25
salario = 3000.00

print(f"nome = '{nome}'")
print(f"idade = {idade}")
print(f"salario = R$ {salario:.2f}")

# Valores podem ser alterados
nome = "Maria"
idade = 30
salario = 5000.00

print(f"\nApós alteração:")
print(f"nome = '{nome}'")
print(f"idade = {idade}")
print(f"salario = R$ {salario:.2f}")

# ============================================
# CONSTANTES (não devem mudar)
# ============================================
print("\n2. CONSTANTES - Valores não devem ser alterados:")
print("-" * 60)

# Convenção: constantes em UPPER_CASE com underscores
PI = 3.14159
TAXA_JUROS = 0.05
VALOR_MAXIMO = 10000
NOME_APLICACAO = "Sistema Financeiro"

print(f"PI = {PI}")
print(f"TAXA_JUROS = {TAXA_JUROS}")
print(f"VALOR_MAXIMO = {VALOR_MAXIMO}")
print(f"NOME_APLICACAO = '{NOME_APLICACAO}'")

print("\n⚠️  IMPORTANTE:")
print("   Python não impede alteração de 'constantes'.")
print("   A convenção UPPER_CASE indica que o valor NÃO DEVE ser alterado.")
print("   É uma questão de boas práticas e convenção, não uma regra técnica.")

# ============================================
# EXEMPLO PRÁTICO: CONSTANTES DE CONFIGURAÇÃO
# ============================================
print("\n3. EXEMPLO: Constantes de Configuração:")
print("-" * 60)

# Configurações da aplicação (geralmente no topo do arquivo)
PORT_SERVIDOR = 8000
URL_BASE_API = "https://api.exemplo.com/v1"
TIMEOUT_REQUISICAO = 30  # segundos
LIMITE_TENTATIVAS = 3

print("Constantes de configuração:")
print(f"  PORT_SERVIDOR = {PORT_SERVIDOR}")
print(f"  URL_BASE_API = '{URL_BASE_API}'")
print(f"  TIMEOUT_REQUISICAO = {TIMEOUT_REQUISICAO}s")
print(f"  LIMITE_TENTATIVAS = {LIMITE_TENTATIVAS}")

# ============================================
# EXEMPLO PRÁTICO: CONSTANTES MATEMÁTICAS
# ============================================
print("\n4. EXEMPLO: Constantes Matemáticas:")
print("-" * 60)

# Constantes matemáticas
PI = 3.14159265359
EULER = 2.71828182846
GRAVIDADE_TERRA = 9.81  # m/s²
VELOCIDADE_LUZ = 299792458  # m/s

raio = 5
area_circulo = PI * (raio ** 2)
print(f"Raio = {raio}cm")
print(f"Área do círculo = π × r² = {PI:.2f} × {raio}² = {area_circulo:.2f}cm²")

# ============================================
# EXEMPLO PRÁTICO: CONSTANTES DE VALIDAÇÃO
# ============================================
print("\n5. EXEMPLO: Constantes de Validação:")
print("-" * 60)

# Limites e regras de validação
IDADE_MINIMA = 18
IDADE_MAXIMA = 120
EMAIL_MAX_LENGTH = 255
SENHA_MIN_LENGTH = 8

idade_teste = 25
print(f"Validação de idade:")
print(f"  Idade informada: {idade_teste}")
print(f"  Idade mínima permitida: {IDADE_MINIMA}")
print(f"  Idade máxima permitida: {IDADE_MAXIMA}")
print(f"  Status: {'Válida' if IDADE_MINIMA <= idade_teste <= IDADE_MAXIMA else 'Inválida'}")

# ============================================
# COMPARAÇÃO: VARIÁVEIS vs CONSTANTES
# ============================================
print("\n" + "=" * 60)
print("RESUMO: VARIÁVEIS vs CONSTANTES")
print("=" * 60)

print("\nVARIÁVEIS:")
print("  • Nomenclatura: snake_case (minúsculas)")
print("  • Exemplo: nome, idade, salario")
print("  • Propósito: armazenar valores que podem mudar")
print("  • Uso: dados dinâmicos durante a execução")

print("\nCONSTANTES:")
print("  • Nomenclatura: UPPER_CASE (maiúsculas)")
print("  • Exemplo: PI, TAXA_JUROS, VALOR_MAXIMO")
print("  • Propósito: armazenar valores fixos")
print("  • Uso: configurações, limites, valores matemáticos")

print("\n" + "=" * 60)
print("EXEMPLO COMPLETO: Sistema com Variáveis e Constantes")
print("=" * 60)

# Constantes do sistema
TAXA_DESCONTO = 0.10  # 10%
DESCONTO_MINIMO = 50.00
FRETE_GRATIS_LIMITE = 200.00

# Variáveis do usuário
valor_compra = 150.00
desconto_aplicado = valor_compra * TAXA_DESCONTO

print(f"\nCompra realizada:")
print(f"  Valor: R$ {valor_compra:.2f}")
print(f"  Taxa de desconto: {TAXA_DESCONTO * 100}%")
print(f"  Desconto: R$ {desconto_aplicado:.2f}")

valor_final = valor_compra - desconto_aplicado
print(f"  Valor final: R$ {valor_final:.2f}")

if valor_final >= FRETE_GRATIS_LIMITE:
    frete = 0.00
    print(f"  Frete: GRÁTIS (compras acima de R$ {FRETE_GRATIS_LIMITE:.2f})")
else:
    frete = 15.00
    print(f"  Frete: R$ {frete:.2f}")

total = valor_final + frete
print(f"  TOTAL A PAGAR: R$ {total:.2f}")

