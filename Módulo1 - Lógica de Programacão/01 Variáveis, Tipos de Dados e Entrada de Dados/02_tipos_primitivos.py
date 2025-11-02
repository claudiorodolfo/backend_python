"""
02 - Tipos de Dados Primitivos

Este arquivo demonstra todos os tipos primitivos disponíveis em Python.
"""

print("=" * 60)
print("TIPOS DE DADOS PRIMITIVOS EM PYTHON")
print("=" * 60)

# ============================================
# 1. INT - Números Inteiros
# ============================================
print("\n1. INT (Números Inteiros):")
print("-" * 60)

idade = 25
ano_nascimento = 1999
temperatura = -5
numero_alunos = 0

print(f"idade = {idade} → tipo: {type(idade)}")
print(f"ano_nascimento = {ano_nascimento} → tipo: {type(ano_nascimento)}")
print(f"temperatura = {temperatura} → tipo: {type(temperatura)}")
print(f"numero_alunos = {numero_alunos} → tipo: {type(numero_alunos)}")

# Operações com inteiros
soma = idade + ano_nascimento
print(f"\nOperação: {idade} + {ano_nascimento} = {soma}")

# ============================================
# 2. FLOAT - Números Decimais
# ============================================
print("\n2. FLOAT (Números Decimais):")
print("-" * 60)

altura = 1.75
peso = 68.5
pi = 3.14159
preco = 19.99

print(f"altura = {altura} → tipo: {type(altura)}")
print(f"peso = {peso} → tipo: {type(peso)}")
print(f"pi = {pi} → tipo: {type(pi)}")
print(f"preco = {preco} → tipo: {type(preco)}")

# Operações com floats
imc = peso / (altura ** 2)
print(f"\nOperação: IMC = {peso} / ({altura}²) = {imc:.2f}")

# ============================================
# 3. STR - Strings (Texto)
# ============================================
print("\n3. STR (Strings - Texto):")
print("-" * 60)

nome = "Maria"
sobrenome = 'Silva'
mensagem = "Olá, mundo!"
texto_multilinha = """Este é um texto
que pode ocupar
várias linhas"""

print(f'nome = "{nome}" → tipo: {type(nome)}')
print(f'sobrenome = "{sobrenome}" → tipo: {type(sobrenome)}')
print(f'mensagem = "{mensagem}" → tipo: {type(mensagem)}')
print(f'\ntexto_multilinha:')
print(texto_multilinha)

# Concatenação de strings
nome_completo = nome + " " + sobrenome
print(f"\nConcatenação: {nome} + ' ' + {sobrenome} = {nome_completo}")

# ============================================
# 4. BOOL - Booleanos
# ============================================
print("\n4. BOOL (Booleanos):")
print("-" * 60)

is_estudante = True
tem_carteira = False
maior_idade = idade >= 18

print(f"is_estudante = {is_estudante} → tipo: {type(is_estudante)}")
print(f"tem_carteira = {tem_carteira} → tipo: {type(tem_carteira)}")
print(f"maior_idade (idade >= 18) = {maior_idade} → tipo: {type(maior_idade)}")

# Operações booleanas
print(f"\nOperações booleanas:")
print(f"  True and False = {True and False}")
print(f"  True or False = {True or False}")
print(f"  not True = {not True}")

# ============================================
# 5. NONE - Ausência de Valor
# ============================================
print("\n5. NONE (Ausência de Valor):")
print("-" * 60)

valor_pendente = None
resultado = None

print(f"valor_pendente = {valor_pendente} → tipo: {type(valor_pendente)}")
print(f"resultado = {resultado} → tipo: {type(resultado)}")

# None é útil para inicializar variáveis que serão preenchidas depois
dados_usuario = None
print(f"\ndados_usuario inicializado como: {dados_usuario}")

# ============================================
# RESUMO E VERIFICAÇÃO DE TIPOS
# ============================================
print("\n" + "=" * 60)
print("RESUMO - VERIFICAÇÃO DE TIPOS")
print("=" * 60)

variaveis = [
    ("idade", idade, int),
    ("altura", altura, float),
    ("nome", nome, str),
    ("is_estudante", is_estudante, bool),
    ("valor_pendente", valor_pendente, type(None))
]

print("\nVerificação de tipos usando type():")
for nome_var, valor, tipo_esperado in variaveis:
    tipo_real = type(valor)
    print(f"  {nome_var:20} = {str(valor):15} → {tipo_real.__name__}")

print("\n" + "=" * 60)
print("IMPORTANTE:")
print("=" * 60)
print("• Python é uma linguagem de tipagem dinâmica")
print("• O tipo é inferido automaticamente pelo valor atribuído")
print("• Você não precisa declarar o tipo explicitamente")
print("• Mas pode verificar o tipo usando type() quando necessário")

