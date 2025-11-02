"""
09 - Exemplo Prático Completo

Este arquivo combina todos os conceitos: laços, listas e métodos.
"""

print("=" * 70)
print("SISTEMA DE GERENCIAMENTO DE NOTAS")
print("Demonstração prática completa")
print("=" * 70)

# ============================================
# DADOS INICIAIS
# ============================================
alunos = []
notas_alunos = []

# Simular adição de alunos e notas
alunos.append("Ana")
notas_alunos.append([8.5, 7.0, 9.2])

alunos.append("Bruno")
notas_alunos.append([6.5, 7.5, 8.0])

alunos.append("Carlos")
notas_alunos.append([9.0, 9.5, 10.0])

# ============================================
# CALCULAR MÉDIAS
# ============================================
print("\n=== CALCULAR MÉDIAS ===")
medias = []

for i in range(len(alunos)):
    notas = notas_alunos[i]
    soma = 0
    
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)
    medias.append(media)
    print(f"{alunos[i]}: média {media:.2f}")

# ============================================
# ENCONTRAR MELHOR E PIOR DESEMPENHO
# ============================================
print("\n=== ANÁLISE DE DESEMPENHO ===")

# Encontrar melhor média
melhor_media = medias[0]
indice_melhor = 0

for i in range(1, len(medias)):
    if medias[i] > melhor_media:
        melhor_media = medias[i]
        indice_melhor = i

print(f"Melhor desempenho: {alunos[indice_melhor]} com média {melhor_media:.2f}")

# Encontrar pior média
pior_media = medias[0]
indice_pior = 0

for i in range(1, len(medias)):
    if medias[i] < pior_media:
        pior_media = medias[i]
        indice_pior = i

print(f"Pior desempenho: {alunos[indice_pior]} com média {pior_media:.2f}")

# ============================================
# CLASSIFICAR ALUNOS
# ============================================
print("\n=== CLASSIFICAÇÃO ===")
aprovados = []
reprovados = []

for i in range(len(alunos)):
    if medias[i] >= 7.0:
        aprovados.append(alunos[i])
    else:
        reprovados.append(alunos[i])

print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

# ============================================
# ESTATÍSTICAS
# ============================================
print("\n=== ESTATÍSTICAS ===")

# Média geral
soma_medias = 0
for media in medias:
    soma_medias += media
media_geral = soma_medias / len(medias)

print(f"Média geral da turma: {media_geral:.2f}")

# Contar aprovações
print(f"Taxa de aprovação: {len(aprovados)}/{len(alunos)}")

# ============================================
# RELATÓRIO FINAL
# ============================================
print("\n" + "=" * 70)
print("RELATÓRIO FINAL")
print("=" * 70)

for i in range(len(alunos)):
    print(f"\n{alunos[i]}:")
    print(f"  Notas: {notas_alunos[i]}")
    print(f"  Média: {medias[i]:.2f}")
    
    if medias[i] >= 7.0:
        print(f"  Status: APROVADO ✓")
    else:
        print(f"  Status: REPROVADO ✗")

print("\n" + "=" * 70)

