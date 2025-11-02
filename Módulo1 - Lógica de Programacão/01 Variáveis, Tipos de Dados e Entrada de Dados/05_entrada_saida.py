"""
05 - Entrada e Saída de Dados

Este arquivo demonstra como receber dados do usuário (input)
e exibir informações (print) em Python.
"""

print("=" * 60)
print("ENTRADA E SAÍDA DE DADOS")
print("=" * 60)

# ============================================
# SAÍDA DE DADOS - print()
# ============================================
print("\n1. SAÍDA DE DADOS - print():")
print("-" * 60)

# print() básico
print("Olá, mundo!")
print("Esta é uma mensagem simples.")

# print() com múltiplos argumentos
print("\nPrint com múltiplos valores:")
print("Nome:", "João", "Idade:", 25)
print("Valores:", 10, 20, 30)

# print() com separador customizado
print("\nPrint com separador customizado:")
print("Python", "é", "fantástico", sep="-")
print("2024", "01", "15", sep="/")

# print() com final customizado
print("\nPrint com final customizado:")
print("Linha 1", end=" | ")
print("Linha 2", end=" | ")
print("Linha 3")

# print() vazio para linha em branco
print()  # Imprime uma linha vazia

# ============================================
# FORMATAÇÃO DE SAÍDA - f-strings (recomendado)
# ============================================
print("\n2. FORMATAÇÃO DE SAÍDA - f-strings:")
print("-" * 60)

nome = "Maria"
idade = 30
salario = 5000.75

# f-string (Python 3.6+)
print(f"Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}")

# f-string com expressões
print(f"Ano de nascimento aproximado: {2024 - idade}")

# f-string com formatação de números
numero = 1234.5678
print(f"Número formatado: {numero:.2f}")
print(f"Número com separador de milhar: {numero:,.2f}")

# ============================================
# OUTRAS FORMAS DE FORMATAÇÃO
# ============================================
print("\n3. OUTRAS FORMAS DE FORMATAÇÃO:")
print("-" * 60)

# .format() (Python 3.5 e anteriores)
print("Método .format():")
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {0}, Idade: {1}, Salário: R$ {2:.2f}".format(nome, idade, salario))

# % (formatação estilo C - legado)
print("\nFormatação estilo C (%):")
print("Nome: %s, Idade: %d" % (nome, idade))

# ============================================
# ENTRADA DE DADOS - input()
# ============================================
print("\n4. ENTRADA DE DADOS - input():")
print("-" * 60)

print("\n⚠️  NOTA: Os exemplos abaixo estão comentados porque")
print("   input() requer interação do usuário em tempo de execução.")
print("   Descomente para testar interativamente.")

# Exemplo básico de input()
# nome_usuario = input("Digite seu nome: ")
# print(f"Olá, {nome_usuario}!")

# Exemplo com input() numérico (necessita conversão)
# idade_usuario = input("Digite sua idade: ")
# idade_usuario = int(idade_usuario)  # Conversão para int
# print(f"Você tem {idade_usuario} anos.")

# Demonstração simulada
print("\nDemonstração simulada:")
print('  nome = input("Digite seu nome: ")')
print('  → usuário digita: "Carlos"')
print('  → nome = "Carlos"')
print('  print(f"Olá, {nome}!")')
print('  → Saída: Olá, Carlos!')

# ============================================
# INPUT() RETORNA SEMPRE STRING
# ============================================
print("\n5. IMPORTANTE: input() sempre retorna STRING:")
print("-" * 60)

print('  entrada = input("Digite um número: ")')
print('  → Se usuário digita: 25')
print('  → entrada = "25" (string, não número!)')
print('  → type(entrada) = <class "str">')
print('\n  Para converter:')
print('  numero = int(entrada)')
print('  → numero = 25 (número inteiro)')
print('  → type(numero) = <class "int">')

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n6. EXEMPLOS PRÁTICOS:")
print("-" * 60)

# Exemplo 1: Formulário simples (simulado)
print("\nExemplo 1: Formulário de Cadastro")
print("-" * 40)
# Simulando entrada
nome_simulado = "Ana Silva"
email_simulado = "ana@email.com"
idade_simulada = 28

print("Formulário de cadastro:")
print(f"  Nome: {nome_simulado}")
print(f"  Email: {email_simulado}")
print(f"  Idade: {idade_simulada}")
print("\n✓ Cadastro realizado com sucesso!")

# Exemplo 2: Calculadora simples (simulado)
print("\nExemplo 2: Calculadora Simples")
print("-" * 40)
# Simulando entrada
num1_simulado = 15
num2_simulado = 7

soma = num1_simulado + num2_simulado
subtracao = num1_simulado - num2_simulado
multiplicacao = num1_simulado * num2_simulado
divisao = num1_simulado / num2_simulado

print(f"Operações com {num1_simulado} e {num2_simulado}:")
print(f"  Soma: {num1_simulado} + {num2_simulado} = {soma}")
print(f"  Subtração: {num1_simulado} - {num2_simulado} = {subtracao}")
print(f"  Multiplicação: {num1_simulado} × {num2_simulado} = {multiplicacao}")
print(f"  Divisão: {num1_simulado} ÷ {num2_simulado} = {divisao:.2f}")

# ============================================
# TEMPLATE PARA INTERAÇÃO COM USUÁRIO
# ============================================
print("\n" + "=" * 60)
print("TEMPLATE PARA USO COM input():")
print("=" * 60)

template = '''
# Template básico de interação
print("=== Sistema de Cadastro ===")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

print(f"\\nDados cadastrados:")
print(f"  Nome: {nome}")
print(f"  Idade: {idade}")
print(f"  Email: {email}")
'''

print(template)
print("\n💡 DICA: Copie este template e teste em um arquivo .py separado!")

