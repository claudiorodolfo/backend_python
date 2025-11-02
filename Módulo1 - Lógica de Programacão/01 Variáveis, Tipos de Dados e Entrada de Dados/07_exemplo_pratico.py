"""
07 - Exemplo Prático Completo

Este arquivo combina todos os conceitos aprendidos em um exemplo prático:
um sistema simples de cadastro de aluno.
"""

print("=" * 70)
print("SISTEMA DE CADASTRO DE ALUNO")
print("Demonstração prática de todos os conceitos aprendidos")
print("=" * 70)

# ============================================
# CONSTANTES DO SISTEMA
# ============================================
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
IDADE_MINIMA = 16
IDADE_MAXIMA = 100
NOME_ESCOLA = "Escola Python Backend"

# ============================================
# VARIÁVEIS DO ALUNO
# ============================================
print("\n=== ENTRADA DE DADOS (Simulada) ===")
print("Em um programa real, usaria input() aqui.\n")

# Simulando entrada do usuário
aluno_nome = "João Silva"
aluno_idade = 20
aluno_email = "joao.silva@email.com"
aluno_matricula = "2024001"
aluno_ativo = True

# Notas do aluno
nota1 = 8.5
nota2 = 7.0
nota3 = 9.2

# ============================================
# PROCESSAMENTO DE DADOS
# ============================================

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação de aprovação (média >= 7.0)
aprovado = media >= 7.0

# Status do aluno
status_aluno = "Ativo" if aluno_ativo else "Inativo"

# Ano de nascimento estimado
ano_atual = 2024
ano_nascimento = ano_atual - aluno_idade

# ============================================
# SAÍDA DE DADOS FORMATADA
# ============================================
print("=" * 70)
print(f"CADASTRO DE ALUNO - {NOME_ESCOLA}")
print("=" * 70)

print("\n📋 DADOS PESSOAIS:")
print("-" * 70)
print(f"  Nome:           {aluno_nome}")
print(f"  Idade:          {aluno_idade} anos")
print(f"  Ano de nascimento: {ano_nascimento}")
print(f"  Email:          {aluno_email}")
print(f"  Matrícula:      {aluno_matricula}")
print(f"  Status:         {status_aluno}")

print("\n📊 NOTAS E MÉDIA:")
print("-" * 70)
print(f"  Nota 1:         {nota1:.2f}")
print(f"  Nota 2:         {nota2:.2f}")
print(f"  Nota 3:         {nota3:.2f}")
print(f"  ───────────────────────────────")
print(f"  MÉDIA:          {media:.2f}")

print("\n🎯 RESULTADO:")
print("-" * 70)
if aprovado:
    resultado = "APROVADO ✓"
    emoji = "🎉"
else:
    resultado = "REPROVADO ✗"
    emoji = "📚"
    
print(f"  Status: {resultado} {emoji}")
print(f"  Média mínima para aprovação: 7.0")

# ============================================
# VALIDAÇÃO DE DADOS (Demonstração)
# ============================================
print("\n" + "=" * 70)
print("VALIDAÇÃO DE DADOS")
print("=" * 70)

# Verificar se idade está no intervalo válido
idade_valida = IDADE_MINIMA <= aluno_idade <= IDADE_MAXIMA
print(f"\nValidação de idade:")
print(f"  Idade: {aluno_idade}")
print(f"  Faixa permitida: {IDADE_MINIMA} a {IDADE_MAXIMA} anos")
print(f"  Status: {'✓ Válida' if idade_valida else '✗ Inválida'}")

# Verificar se notas estão no intervalo válido
notas_validas = (
    NOTA_MINIMA <= nota1 <= NOTA_MAXIMA and
    NOTA_MINIMA <= nota2 <= NOTA_MAXIMA and
    NOTA_MINIMA <= nota3 <= NOTA_MAXIMA
)

print(f"\nValidação de notas:")
print(f"  Notas: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}")
print(f"  Faixa permitida: {NOTA_MINIMA} a {NOTA_MAXIMA}")
print(f"  Status: {'✓ Todas válidas' if notas_validas else '✗ Alguma inválida'}")

# ============================================
# EXEMPLO DE CASTING
# ============================================
print("\n" + "=" * 70)
print("EXEMPLO DE CASTING EM USO PRÁTICO")
print("=" * 70)

print("\nCenário: Recebendo dados como string (como seria com input())")
print("-" * 70)

# Simulando dados recebidos como string (input())
idade_str = "20"
nota_str = "8.5"

print(f"  Dados recebidos (strings):")
print(f"    idade_str = '{idade_str}' (tipo: {type(idade_str).__name__})")
print(f"    nota_str = '{nota_str}' (tipo: {type(nota_str).__name__})")

# Conversão necessária
idade_convertida = int(idade_str)
nota_convertida = float(nota_str)

print(f"\n  Após conversão (casting):")
print(f"    idade_convertida = {idade_convertida} (tipo: {type(idade_convertida).__name__})")
print(f"    nota_convertida = {nota_convertida} (tipo: {type(nota_convertida).__name__})")

# Agora podem ser usados em operações matemáticas
ano_nasc_calculado = 2024 - idade_convertida
print(f"\n  Operação matemática possível:")
print(f"    Ano de nascimento = 2024 - {idade_convertida} = {ano_nasc_calculado}")

# ============================================
# RESUMO DOS CONCEITOS UTILIZADOS
# ============================================
print("\n" + "=" * 70)
print("CONCEITOS UTILIZADOS NESTE EXEMPLO")
print("=" * 70)

print("\n✓ Constantes: NOTA_MINIMA, IDADE_MAXIMA, NOME_ESCOLA")
print("✓ Variáveis: aluno_nome, aluno_idade, notas, média, etc.")
print("✓ Tipos de dados: str, int, float, bool")
print("✓ Entrada de dados: input() (simulado)")
print("✓ Saída de dados: print() com f-strings")
print("✓ Casting: int(), float() para conversão de tipos")
print("✓ Operações matemáticas: +, -, *, /, >=, == ")
print("✓ Formatação: f-strings com formatação de números")

print("\n" + "=" * 70)
print("PRONTO PARA PROXIMOS MÓDULOS!")
print("=" * 70)
print("\nAgora você está preparado para aprender:")
print("  → Operadores e Estruturas Condicionais")
print("  → Estruturas de Repetição")
print("  → Listas, Tuplas e Dicionários")
print("  → Funções")
print("  → Tratamento de Exceções")

